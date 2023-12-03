from ultralytics import YOLO


model = YOLO('yolov8n.yaml').load('yolov8n.pt')
result = model.train(data='../datasets/data_pretrain/data.yaml', epochs=250,  imgsz=640, resume=True)