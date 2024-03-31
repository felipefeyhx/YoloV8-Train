from ultralytics import YOLO

model = YOLO('C:/Users/U170021/OneDrive - GRUPO EQUATORIAL ENERGIA/Projetos/Treinamento_Modelo_QAS/runs/detect/train5/weights/best.pt')
model.export(format='onnx')