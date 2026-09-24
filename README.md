# Real-Time Face Recognition System

A Python prototype that uses a webcam to detect faces and compare them with a known face image. It uses OpenCV to capture and display video, and the `face_recognition` library to locate faces and compare face encodings.

> **Project status:** This repository is an early prototype. The current code needs fixes before it will run successfully; see [Known issues](#known-issues) below.

## How it works

1. The program loads a reference image and creates a face encoding from it.
2. It reads frames from the computer's default webcam.
3. It scales each frame down and searches it for faces.
4. It compares detected face encodings with the reference encoding.
5. It displays a name for a match or `Unknown` otherwise. Press **Q** to close the camera window.

## Requirements

- Python 3
- A webcam
- The Python packages `opencv-python`, `face_recognition`, and `numpy`

`face_recognition` depends on native libraries, so installation steps can vary by operating system. Follow its installation guidance if `pip` reports a build or dependency error.

## Setup

Clone the repository and open its folder:

```bash
git clone https://github.com/shivasaibadha/Real-Time-Face-Recognition-System-.git
cd Real-Time-Face-Recognition-System-
```

Install the dependencies:

```bash
python -m pip install opencv-python face_recognition numpy
```

Place a clear image of the person to recognize in the project folder and name it `Shiva.jpeg`. Keep personal face images private; do not commit them to a public repository.

## Run

The intended entry point is `main.py`:

```bash
python main.py
```

Allow the application to access the webcam if prompted. Press **Q** in the video window to exit.

## Repository files

- `main.py` — primary webcam recognition prototype
- `projeck.py` — additional experimental script; currently incomplete
- `__init__.py` — Python package marker
- `face_recognition.iml` — IDE project configuration

## Known issues

The code on the repository's `main` branch currently has issues that prevent the documented workflow from running as-is:

- `main.py` loads `Shiva.jpeg`, but that image is not included in the repository. Add your own reference image locally.
- `main.py` uses `image_Shiva` after assigning `image_shiva`; Python treats these as different names. Fix the capitalization in the code before running it.
- `projeck.py` contains unfinished code and should not be treated as a working entry point.
- There is no dependency lock or requirements file yet. A `requirements.txt` would make setup easier to reproduce.

## Privacy and responsible use

Face images and face encodings are biometric information. Use this project only with the knowledge and consent of the people whose faces are enrolled. Store face data securely, limit access, and delete it when it is no longer needed. Do not use this prototype for consequential decisions or covert identification.

## License

This project is licensed under the terms of the MIT License.
