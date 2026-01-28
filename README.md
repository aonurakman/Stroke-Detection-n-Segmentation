# Detection, Classification and Segmentation of Stroke Regions in Brain CT Images

Bachelor's Thesis - 2021 - Yildiz Technical University

**Team members:** AKMAN, Onur; AYDIN, Ahmet; SINAR, Emine Betul

**Full report:** [View PDF](https://github.com/aonurakman/Stroke-Detection-n-Segmentation/blob/d046383654f4e6b97ad4dbb893ce0f26149a3cd9/Doc/Report.pdf)

## Overview

This project presents a comprehensive deep learning pipeline for automated stroke analysis in non-contrast computed tomography (CT) images. The system performs three primary tasks:

1. **Detection:** Binary classification to determine the presence or absence of stroke
2. **Classification:** Multi-class classification to identify stroke type (hemorrhagic or ischemic)
3. **Segmentation:** Pixel-wise localization of stroke regions within CT images

The pipeline employs a two-phase approach combining multiple state-of-the-art deep learning architectures to achieve robust performance across all tasks.

## Methodology

### Phase 1: Stroke Detection

The detection phase employs an ensemble approach using transfer learning with the following architectures:
- VGG16
- Inception
- MobileNet
- ResNet
- EfficientNet
- DenseNet

The final prediction is obtained through soft-voting across all models, improving overall robustness and accuracy.

![Fusion of models in Phase 1](https://i.hizliresim.com/59zgai2.PNG)

### Phase 2: Classification and Segmentation

The classification and segmentation phase utilizes instance segmentation models to simultaneously identify stroke type and generate pixel-wise masks:

**Primary Approach:** Mask R-CNN with transfer learning provides both stroke classification (hemorrhagic/ischemic) and precise segmentation masks.

**Alternative Approaches:** U-Net and YOLOv3 were also trained and evaluated for comparison. While these models demonstrated competitive performance in classification, they produce bounding boxes rather than pixel-wise segmentation masks.

![Segmentation in Phase 2](https://i.hizliresim.com/derossa.PNG)

## Dataset

The dataset consists of 6,650 CT images in various formats (PNG, DICOM, MASK, and OVERLAY):
- **Hemorrhagic stroke:** 1,093 images
- **Ischemic stroke:** 1,130 images
- **No stroke:** 4,427 images

*Note: The dataset cannot be publicly shared due to privacy regulations.*

## Prerequisites

- Python 3.x
- Google Colab (for Jupyter notebook execution) or local Jupyter environment
- Google Drive account (for cloud-based training)
- Required Python packages (varies by model, see individual sections below)
- For Mask R-CNN: [Matterport Mask R-CNN implementation](https://github.com/matterport/Mask_RCNN)

## General Setup Instructions

1. **Environment Setup:**
   - Clone or download this repository
   - Prepare your Python environment with necessary dependencies
   - Ensure sufficient storage space (~250 MB per epoch for model checkpoints)

2. **Data Preparation:**
   - Organize CT images and corresponding mask files according to model-specific requirements
   - Ensure all images are in PNG format
   - Maintain consistent naming conventions between images and their masks

3. **Path Configuration:**
   - Update file path variables in scripts to match your directory structure
   - Configure ROOT_DIR or equivalent path variables as specified in each section



## Model Training and Testing

### Mask R-CNN

#### Training

1. **Setup Dependencies:**
   - Download the Mask R-CNN implementation from [Matterport's repository](https://github.com/matterport/Mask_RCNN)
   - Copy the `mrcnn` folder, `setup.py`, and `requirements.txt` to your working directory
   - Download pre-trained COCO weights `mask_rcnn_coco.h5` from the [releases page](https://github.com/matterport/Mask_RCNN/releases)

2. **Directory Structure:**
   ```
   ROOT_DIR/
   ├── mrcnn/
   ├── setup.py
   ├── requirements.txt
   ├── mask_rcnn_coco.h5
   └── Dataset/
       ├── train/
       │   ├── images (PNG format)
       │   └── annotations.json
       └── val/
           ├── images (PNG format)
           └── annotations.json
   ```

3. **Configuration:**
   - Set the `ROOT_DIR` variable in the training script to your working directory path
   - Update all file path variables to match your directory structure
   - Ensure at least 250 MB of free storage per training epoch for model checkpoints

4. **Data Format:**
   - All CT images must be in PNG format
   - Annotation files should be in JSON format containing mask information
   - Place training images and annotations in `Dataset/train/`
   - Place validation images and annotations in `Dataset/val/`

5. **Execution:**
   - Run the training script from `Code/Phase 2/Mask R-CNN/MaskRCNN_training.py`
   - Model weights are automatically saved after each epoch

#### Testing

1. **Setup:**
   - Use the same Mask R-CNN dependencies as training
   - Create two directories: `test_imgs/` and `test_masks/`

2. **Directory Structure:**
   ```
   ROOT_DIR/
   ├── mrcnn/
   ├── model_weights.h5
   ├── test_imgs/
   └── test_masks/
   ```

3. **Data Preparation:**
   - Place test CT images in `test_imgs/`
   - Place corresponding ground truth masks in `test_masks/` with matching filenames
   - For mask images: non-zero pixel values indicate stroke regions, zero values indicate background

4. **Configuration:**
   - Set `ROOT_DIR` to your working directory
   - Specify the path to your trained model weights
   - Update file path variables in the testing script

5. **Execution:**
   - Run the testing script to perform inference on test images

#### IoU (Intersection over Union) Measurement

1. **Setup:**
   - Follow the same dependency setup as training/testing
   - Create `img/` and `mask/` directories

2. **Directory Structure:**
   ```
   ROOT_DIR/
   ├── mrcnn/
   ├── model_weights.h5
   ├── img/
   └── mask/
   ```

3. **Data Preparation:**
   - Place original CT images in `img/`
   - Place corresponding ground truth masks in `mask/` with matching filenames

4. **Execution:**
   - Run the IoU measurement script to evaluate segmentation accuracy


### U-Net

#### Training

1. **Environment:**
   - Open the U-Net training Jupyter notebook in Google Colab or local Jupyter environment
   - Mount Google Drive if using Colab

2. **Data Preparation:**
   - Organize dataset with images and masks in the same directory
   - Ensure each image and its corresponding mask have identical filenames
   - Split data into training and validation sets
   - Upload to Google Drive or local directory

3. **Execution:**
   - Mount your Drive (if using Colab)
   - Execute notebook cells sequentially
   - Model checkpoints and training logs will be saved automatically

#### IoU Measurement

1. **Environment Setup:**
   - Open `U-net_Test.py` in an IDE (e.g., Spyder, PyCharm, or VS Code)
   - Place the trained model file `model.h5` in the same directory as the script

2. **Configuration:**
   - Set the stroke type for testing in the script:
     - `1` for hemorrhagic stroke
     - `0` for ischemic stroke
   - Specify input image path
   - All images must be in PNG format

3. **Execution:**
   - Run the script to generate segmentation predictions
   - Output images will be saved in the script directory


### YOLOv3

#### Training

1. **Environment:**
   - Open the YOLOv3 training Jupyter notebook in Google Colab or local Jupyter environment
   - Mount Google Drive if using Colab

2. **Data Preparation:**
   - Prepare bounding box annotations for each training image
   - Each annotation should include: x and y coordinates, width, height, and class labels
   - Generate YOLO-format annotation files (`.txt`) using one of these methods:
     - Use [LabelImg](https://github.com/tzutalin/labelImg) annotation tool
     - Use provided scripts to convert existing annotations to YOLO format

3. **Configuration Files:**
   - Adapt configuration files from YOLOv3 sample files:
     - `train.cfg`: Training configuration
     - `test.cfg`: Testing configuration  
     - `train.names`: Class names file
   - Upload configuration files along with dataset to Google Drive or local directory

4. **Execution:**
   - Mount your Drive (if using Colab)
   - Execute notebook cells sequentially
   - Training progress and model weights will be saved automatically

## Repository Structure

```
├── Code/
│   ├── Phase 1/              # Stroke detection models
│   └── Phase 2/              # Classification and segmentation models
│       ├── Mask R-CNN/
│       ├── U-NET/
│       └── YoloV3/
├── Database/                 # Dataset information
├── Doc/                      # Project documentation and report
├── Run/                      # Detailed run instructions
└── README.md
```

## Citation

If you use this work in your research, please cite:

```
AKMAN, O., AYDIN, A., & SINAR, E. B. (2021). Detection, Classification and Segmentation of 
Stroke Regions in Brain CT Images. Bachelor's Thesis, Yildiz Technical University.
```

## License

This project is part of a Bachelor's Thesis submitted to Yildiz Technical University in 2021.

## Contact

For questions or collaboration inquiries, please contact the team members or open an issue in this repository.
