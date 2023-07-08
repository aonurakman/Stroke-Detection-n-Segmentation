# Detection, Classification and Segmentation of Stroke Regions in Brain CT Images

Bachelor's Thesis - 2021 - Yildiz Technical University

Team members: **AKMAN, Onur**; **AYDIN, Ahmet**; **SINAR, Emine Betul**

Full report ![HERE](https://github.com/aonurakman/Stroke-Detection-n-Segmentation/blob/d046383654f4e6b97ad4dbb893ce0f26149a3cd9/Doc/Report.pdf)

### Description:
Analyze the non-contrast computed tomography with the deep learning model to be created, classify it for the presence or absence of stroke, classify the type of the stroke (Hemorrhagic or Ischemic), and pixel-wise segmentation of the stroke region in the tomography image.

* **Detection of the stroke**: Transfer learning of VGG16, Inception, MobileNet, ResNet, EfficientNet, DenseNet. Output is obtained by soft-voting all the models obtained.

[Fusion of models in P1](https://i.hizliresim.com/59zgai2.PNG)

* **Classification and segmentation of stroke region**: Transfer learning of Mask-R-CNN. Output is the stroke type and the mask for the stroke region. In addition to Mask-R-CNN, also U-Net and YOLOv3 are trained for the same task and evaluated. They seem to perform better but they yield bounding boxes instead of a mask.

![Segmentation in P2](https://i.hizliresim.com/derossa.PNG)



## Mask R-CNN Training

* A folder must be opened in the mounted Google Drive and the path of this folder must be given to the "ROOT_DIR" variable.
* The mrcnn folder in the "https://github.com/matterport/Mask_RCNN" rep, setup.py file, requirements.txt file
	should be taken and placed inside this folder.
* Get "mask_rcnn_coco.h5" file from "https://github.com/matterport/Mask_RCNN/releases" link and place it in this directory. 
	should be added.
* A folder named "Dataset" and two folders named "train" and "val" should be opened inside this folder.
* The original versions of the CT images to be used as Train and Validation Data, the .JSON where the mask images are kept
	files should be placed in the relevant directories.
* File path dependent variables in the script should be aligned with the paths of these provided items in Drive.
* Model weights are saved at the end of each epoch while the script is running. Since there is ~250 MB of space available per epoch
	must be made sure.
* All image files must be in .png format.


## Mask R-CNN Testing

* A folder must be opened in the mounted Google Drive and the path of this folder must be given to the "ROOT_DIR" variable.
* The mrcnn folder in the "https://github.com/matterport/Mask_RCNN" rep, setup.py file, requirements.txt file
	should be taken and placed in this folder.
* Open two folders, "test_imgs" and "test_masks". test_imgs contains the BT images to be tested.
	and the mask images of these images (with the same name) should be placed in test_masks.
	For mask images, only the pixel values of the coordinates where the mask is located in the image should be different from 0.
* The model to be used in the experiment should be placed in the main directory of the folder.
* File path dependent variables in the code should be aligned with the paths of these provided items in Drive.
* All image files must be in .png format.


## Mask R-CNN IoU Measurement

* A folder must be opened in the mounted Google Drive and the path of this folder must be given to the "ROOT_DIR" variable.
* The mrcnn folder in the "https://github.com/matterport/Mask_RCNN" rep, setup.py file, requirements.txt file
	should be taken and placed in this folder.
* Two folders, "img" and "mask", should be opened.
	original images and mask images of these images (with the same name) should be placed in the mask.
* The model to be tested must be placed in the main directory of the folder.
* File path dependent variables in the code should be aligned with the paths of these provided items in Drive.
* All image files must be in .png format.


## U-Net Training
* The relevant jupyter code file should be opened under Google Colab.
* The database should be set up and the images should be organized so that the image and mask are under the same folder and have the same name.
* Training and validation images should be uploaded to Drive.
* After the images are uploaded, the drive should be mounted and the code lines should be executed one by one in order.


## U-Net IoU Measurement

* U-net_Test.py code should be opened with spyder or pycharm. Model.h5 file should be under the same folder as the script. 
* The type of the image selected for the test should be set in the script as 1 bleeding 0 ischemia class.
* The output image will be visible under the same folder.
* The format of all images should be .png.


## Yolov3 Training

* The relevant jupyter code file should be opened under Google Colab.
* Images for training, x and y coordinates, width and height information and classes of the masks in the image should be known.
* In order to obtain the .txt files containing these operations, either the LabelImg tool should be used or the necessary operations should be done with the code and edited in accordance with the Yolo format.
* Training and validation images and necessary files such as train.cfg test.cfg and train.names should be edited and uploaded to the drive by selecting them from yolo's sample files.
* After the images are uploaded, the drive should be mounted and the code lines should be executed one by one in order.
