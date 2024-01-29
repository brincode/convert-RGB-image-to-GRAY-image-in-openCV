**README for Image Processing with OpenCV**

## Introduction

This repository contains a simple Python script that demonstrates basic image processing using the OpenCV library. The script reads an image, displays it in its original form, converts it to grayscale, and optionally saves the grayscale version. This README provides information on how to use the script and the prerequisites for running it.

## Prerequisites

- Python: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- OpenCV: Install the OpenCV library using the following command:

  ```bash
  pip install opencv-python
  ```

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/image-processing-opencv.git
   cd image-processing-opencv
   ```

2. **Run the Script:**

   ```bash
   python image_processing_script.py
   ```

   This will execute the script with the provided image (lite.jpeg) and display the original image.

3. **Follow On-Screen Instructions:**

   - Press `ESC` key to close the displayed window.
   - Press `ESC` key again or `s` key to save the grayscale version of the image as "lite_gray.png".

## Script Explanation

The script uses the OpenCV library to perform the following actions:

1. Read an image (`lite.jpeg`) from the specified file path.

2. Display the original image and wait for a key event.

3. If the `ESC` key is pressed, close the window.

4. Convert the original RGB image to grayscale.

5. Display the grayscale image and wait for a key event.

6. If the `ESC` key is pressed, close the window. If the `s` key is pressed, save the grayscale image as "lite_gray.png" in the script directory.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.

## Issues

If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/your-username/image-processing-opencv/issues).

Happy Coding!
