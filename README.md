# Cat or Dog?
## An AI based solution to categorize images as containing either cats or dogs

## Description:
This project can be used to categorize images as being either cats or dogs. Train the AI model (or use the one already trained which achieves 81.88%) and test its predictions.

## Installation
The first step needed is to install Python 3.7 (version 3.8 is not supported) and make sure pip is on PATH.  

After that, run the following commands to install the dependencies:
```python
pip install requests
pip install tensorflow-gpu==1.15
pip install opencv-python
pip install keras==2.2.4
pip install numpy==1.16.1
pip install imageai --upgrade
pip install h5py==2.10.0
```

If you're interested in training the model, using a GPU with CUDA capabilities is higly recommended. For that you will need to configure tensorflow-gpu to use CUDA. Follow the instructions at https://www.tensorflow.org/install/gpu for information on how to do that (Reminder: tensorflow-gpu 1.15 supports Cuda Toolkit 10.0).

## Acquiring data
This app is configured to use The Cat API (https://thecatapi.com) for acquiring cat images and Dog API (https://dog.ceo/dog-api/) for dog images.  
Run the script `getImages.py` to start the acquisiton. By default 1000 training images and 200 test images of each animal will be downloaded. This number can be changed by editing the variables `nImagesTrain` and `nImagesTest` before running the script.

## Training the model
To start training the model, just run the `trainModel.py` script. All necessary files will be created and the module will be save at `/data/models`. If the script detects a model already created, it will try to continue from it. To start a new model, simply delete all existing ones in the models folder.  
By default, the training will happen during 200 Epochs. To change that, alter the `generations` variable in the training script.

## Test the model
To test the model, place the test images in the folder `predictFiles` and run the script `predict.py`. All images inside the folder will be passed through the model and the results will be printed at the console output.