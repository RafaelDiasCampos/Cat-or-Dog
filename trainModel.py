from imageai.Prediction.Custom import ModelTraining
from os import listdir

generations = 200

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("data")

#Searches for trained models
models = listdir("data/models")

#If a model exists, start training from it
if len(models) > 1: #(1 because .gitignore always exists at the folder)
    models.sort(reverse=True)
    bestModel = models[0]
    print("Continuing from existing model")
    model_trainer.trainModel(continue_from_model=f"data/models/{bestModel}", num_objects=2, num_experiments=generations, enhance_data=True, batch_size=16, show_network_summary=True)
#If no model exists, create a new one and train it
else:    
    model_trainer.trainModel(num_objects=2, num_experiments=generations, enhance_data=True, batch_size=16, show_network_summary=True)