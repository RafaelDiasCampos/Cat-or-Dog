#Code derived from https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba
from imageai.Prediction.Custom import CustomImagePrediction
from os import listdir, getcwd

#Searches for trained models
models = listdir("data/models")

#If no model exists, raise an error 
if len(models) < 2: #(2 because .gitignore always exists at the folder)
    raise Exception("No trained model found")

models.sort(reverse=True)
bestModel = models[0]

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(f"data/models/{bestModel}")
prediction.setJsonPath("data/json/model_class.json")
prediction.loadModel(num_objects=2)

#Searches for files to predict
filenames = listdir("predictFiles")
filenames.remove(".gitignore")
filepaths = ["predictFiles/" + filename for filename in filenames]

results = prediction.predictMultipleImages(filepaths)
for filename, result in zip(filenames, results):
    print(f"{filename}: {result['predictions'][0]} ({result['percentage_probabilities'][0]}% certainty)")