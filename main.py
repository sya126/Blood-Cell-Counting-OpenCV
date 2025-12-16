import cv2
import numpy as np
import os
import pandas as pd

# --- CONFIGURATION ---
INPUT_FOLDER = "images"       
OUTPUT_FOLDER = "output"      
REPORT_FILE = "Cell_Counting_Report.csv"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def count_all_cells(image_path, filename):
    img = cv2.imread(image_path)
    if img is None:
        return 0, None

    # 1. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Gaussian Blur (Noise reduction)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. ADAPTIVE THRESHOLDING (The Key Change!)
    # Instead of global threshold, this looks at neighbors to find edges.
    # Perfect for separating Red Blood Cells (RBC) from background.
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # 4. Morphological Operations
    # Separate touching cells slightly
    kernel = np.ones((3,3), np.uint8)
    # Erode helps to separate connected cells
    processed = cv2.erode(thresh, kernel, iterations=1)
    processed = cv2.dilate(processed, kernel, iterations=1)

    # 5. Contour Detection
    contours, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count = 0
    result_img = img.copy()

    for c in contours:
        area = cv2.contourArea(c)
        
        # --- SENSITIVITY SETTINGS ---
        # Lower limit is now 30 pixels. This captures even small RBCs.
        if 30 < area < 10000:
            cv2.drawContours(result_img, [c], -1, (0, 255, 0), 1) # Thin green line
            count += 1

    # Add text
    cv2.putText(result_img, f"Total Cells: {count}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Save image
    cv2.imwrite(os.path.join(OUTPUT_FOLDER, "counted_" + filename), result_img)

    return count

def main():
    print("--- STARTING SENSITIVE CELL COUNTING ---")
    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    
    data = []

    for filename in files:
        file_path = os.path.join(INPUT_FOLDER, filename)
        
        count = count_all_cells(file_path, filename)
        
        print(f"Image: {filename} -> Count: {count}")
        
        data.append({
            "Image_Name": filename,
            "Total_Cell_Count": count
        })

    # Save CSV
    df = pd.DataFrame(data)
    df.to_csv(REPORT_FILE, index=False)
    
    print("\n--- PROCESSING DONE ---")
    print(f"Check the '{OUTPUT_FOLDER}' for green contours.")

if __name__ == "__main__":
    main()