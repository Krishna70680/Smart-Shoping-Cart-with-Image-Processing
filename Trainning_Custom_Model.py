from ultralytics import YOLO

#Load a model 
model = YOLO("yolov5s.yaml") #building a new model from scratch

#use the model 
results = model.train(data='dataset.yaml.yaml', epochs =9) 