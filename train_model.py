from ultralytics import YOLO
from multiprocessing import freeze_support
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

if __name__ == '__main__':
    freeze_support()
    # Load a model
    #model = YOLO("yolov8x-seg.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    #model = YOLO('runs/detect/train10/weights/best.pt')
    #model.to('cuda')

    results = model.train(data="config.yaml", epochs=10)  # train the model 