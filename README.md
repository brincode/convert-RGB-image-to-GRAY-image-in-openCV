
## Introduction

This repository contains a Jupyter Notebook (`convert_RGB_to_GRAY_in_OpenCV.ipynb`) that demonstrates basic image processing using the OpenCV library. The notebook reads an RGB image, displays the original image, converts it to grayscale, and optionally saves the grayscale version. This README provides information on how to use the notebook and the prerequisites for running it.

## Prerequisites

- **Python:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- **OpenCV:** Install the OpenCV library using the following command:

  ```bash
  pip install opencv-python
  ```

- **Jupyter Notebook:** If you don't have Jupyter Notebook installed, you can install it using:

  ```bash
  pip install notebook
  ```

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/image-processing-opencv.git
   cd image-processing-opencv
   ```

2. **Open the Jupyter Notebook:**

   ```bash
   jupyter notebook convert_RGB_to_GRAY_in_OpenCV.ipynb
   ```

   This will open the Jupyter Notebook in your default web browser.

3. **Execute the Code:**

   - Inside the Jupyter Notebook, run each cell in sequence to execute the code.
   - Follow the on-screen instructions to interact with the script.

## Notebook Explanation

The notebook uses the OpenCV library to perform the following actions:

1. Read an RGB image (`lite.jpeg`) from the specified file path.

2. Display the original image and wait for a key event.

3. If the `ESC` key is pressed, close the window.

4. Convert the original RGB image to grayscale.

5. Display the grayscale image and wait for a key event.

6. If the `ESC` key is pressed, close the window. If the `s` key is pressed, save the grayscale image as "lite_gray.png" in the notebook directory.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.

## Issues

If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/brincode/convert-RGB-image-to-GRAY-image-in-openCV/issues).

Happy Coding!
