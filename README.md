# Automated Blood Cell Counting & Segmentation

## 📌 Project Overview
This project is a computer vision application designed to automatically count Red Blood Cells (RBC) and White Blood Cells (WBC) from microscopic blood smear images.

Unlike standard Deep Learning approaches, this project utilizes **Traditional Image Processing** techniques (OpenCV) to achieve fast and accurate segmentation without the need for extensive model training.

## 🚀 Key Features
* **Adaptive Thresholding:** Capable of detecting faint cells under varying lighting conditions.
* **Noise Reduction:** Uses Gaussian Blur and Morphological Operations to filter out artifacts.
* **Batch Processing:** Automatically processes hundreds of images in a directory.
* **Data Reporting:** Exports counting results to a CSV file for further analysis.

## 🛠 Technologies Used
* **Python 3.x**
* **OpenCV (cv2):** For image processing algorithms.
* **Pandas:** For data structuring and CSV export.
* **NumPy:** For numerical matrix operations.

## 📊 Methodology (Pipeline)
The image processing pipeline consists of the following steps:
1.  **Grayscale Conversion:** Simplifying the image data.
2.  **Gaussian Blurring:** Reducing high-frequency noise.
3.  **Adaptive Thresholding:** Unlike global thresholding, this method calculates thresholds for smaller regions, allowing the detection of RBCs that have low contrast with the background.
4.  **Morphological Operations (Erosion & Dilation):** Separating touching cells and removing small noise dots.
5.  **Contour Detection:** Identifying and counting valid cell boundaries based on area filters.

## 📷 Results
Below is an example of the segmentation output where cells are detected and outlined in green:

<img width="256" height="256" alt="counted_image-44" src="https://github.com/user-attachments/assets/48ffc267-e126-41dc-a02a-560f6fd221c0" />


## 💻 How to Run
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Place your images in the `images/` folder.
4.  Run the script:
    ```bash
    python main.py
    ```
5.  Check the `output/` folder for processed images and `Cell_Counting_Report.csv` for the data.

---
**Author:** Şeyma Adanalı
