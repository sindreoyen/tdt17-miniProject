# Road-Pole/Stick Detection on Edge Devices

This project focuses on detecting road poles (commonly referred to as "brøytestikker" in Norwegian) using modern Visual Intelligence (VI) techniques. The goal is to develop a model that can perform real-time inference on hardware-restricted edge devices, such as smartphones.

## Table of Contents
- [Introduction](#introduction)
- [Data Preparation](#data-preparation)
- [Model Selection](#model-selection)
- [Training](#training)
- [Testing and Evaluation](#testing-and-evaluation)
- [Deployment Feasibility](#deployment-feasibility)
- [Discussion and Conclusion](#discussion-and-conclusion)
- [References](#references)

## Introduction
Road poles are essential for navigation guidance during winter, especially for indicating road edges on snowy roads. This project aims to leverage VI technology to detect road poles, enhancing navigation for self-driving vehicles and other applications.

## Data Preparation
The dataset used in this project consists of LiDAR images of poles, collected and annotated by NAPLab. The dataset is divided into training, validation, and test splits. The original validation dataset is used for final evaluation, while a new train/validation split is created from the training dataset. The dataset is not available for redistribution.

## Model Selection
The project explores various lightweight Object Detection (OD) models, with a focus on the YOLO11 series. YOLO11s is chosen for its balance between precision and computational efficiency, making it suitable for edge-device deployment.

## Training
The model is trained using the Ultralytics YOLO package. Data augmentation techniques such as rotation, scaling, translation, and photometric transformations are applied to improve model robustness. The training process is documented in `src/train_model.py`.

## Testing and Evaluation
The trained model is evaluated on the original validation dataset. Performance metrics such as mAP, precision, and recall are calculated. The results are visualized through confusion matrices and other performance graphs.

## Deployment Feasibility
The feasibility of deploying the trained model on edge devices is discussed, considering factors such as computational requirements and inference speed.

## Discussion and Conclusion
The project concludes with a discussion on the sustainability of the model training and inference processes, as well as potential future improvements.

## References
- Bavirisetti, Durga Prasad, Gabriel Hanssen Kiss, and Frank Lindseth. “A Pole Detection and Geospatial Localization Framework Using LiDAR-GNSS Data Fusion.” FUSION 2024 - 27th International Conference on Information Fusion, 2024. https://doi.org/10.23919/FUSION59988.2024.10706275.
- Ultralytics YOLO documentation: https://docs.ultralytics.com/

## How to Run
1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Train the model:
    ```sh
    make train
    ```
3. Run the notebook for detailed analysis:
    ```sh
    jupyter notebook src/pole_detection.ipynb
    ```