from ultralytics import YOLO

model = YOLO('../ultralytics/runs/detect/train23/weights/best.pt')
# model = YOLO('/root/autodl-tmp/HUST.AIA.CV/Fog.pt')
# 评估模型在验证集上的性能
results = model.val()