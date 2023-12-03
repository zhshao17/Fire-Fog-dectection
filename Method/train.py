from ultralytics import YOLO

# Load a model

# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights


# Train the model
results = model.train(data='../datasets/data/data.yaml', epochs=250, imgsz=640)

# 评估模型在验证集上的性能
# results = model.val()

# 使用模型对图片进行目标检测-推理
# results = model('https://ultralytics.com/images/bus.jpg')

# YOLOv8/ultralytics/cfg/default.yaml