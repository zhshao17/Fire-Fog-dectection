from ultralytics import YOLO

model = YOLO('../weight.pt')

results = model(source='../images', stream=True)

for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        masks = r.masks  # Masks object for segment masks outputs
        probs = r.probs  # Class probabilities for classification outputs