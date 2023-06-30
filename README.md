# OpenCV-Automatic-Attendance
This repository contains the code and resources for implementing an automatic attendance system using OpenCV and the Face Recognition library. The system utilizes facial recognition techniques to recognize and track individuals in real-time, allowing for automatic attendance marking.

## Introduction
The automatic attendance system implemented in this repository leverages the power of OpenCV and the Face Recognition library to detect and recognize faces. The system is designed to streamline the attendance process in various settings, such as classrooms, conferences, or office environments.

## Key Features 
* Real-time face detection and tracking using Haar cascades.
* Face recognition using the Face Recognition library.
* Automatic marking of attendance based on recognized faces.
* Exporting attendance records to a CSV file for further analysis.

## Installation
1. Clone this repository to your local machine
2. Install the required dependencies. You can use pip to install them:
    ```shell
    pip install -r requirements.txt

3. Ensure that you have a compatible webcam connected to your machine.

## Usage
1. Navigate to the project directory
2. Add images of individuals whose attendance you want to track into the Train Images directory. Create a subdirectory for each individual and place their images inside.
3. Run the `Attendance.py` script:
4. The system will start capturing video from your webcam and detect faces in real-time. It will compare the detected faces with the images in the dataset to recognize individuals.
5. As faces are recognized, the system will mark their attendance and display their names on the screen.
6. The final attendance record will be saved in a CSV file named attendance.csv




