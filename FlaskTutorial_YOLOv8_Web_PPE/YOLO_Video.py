from flask import render_template
from ultralytics import YOLO
import cv2
import math
import requests
from io import BytesIO
from PIL import Image
from datetime import datetime, timedelta
import os

def fetch_qr_code(product_names, backend_url='http://127.0.0.1:8000/api/generate-qr/'):
    try:
        payload = {'items': product_names}
        response = requests.get(backend_url, params=payload)
        if response.status_code == 200:
            with open('static/qr_code.png', 'wb') as f:
                f.write(response.content)
            print("QR code saved")
            qr_image_bytes = BytesIO(response.content)
            qr_image = Image.open(qr_image_bytes)
            return qr_image
        else:
            print(f"Failed to fetch QR code. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching QR code from backend: {e}")
        return None

def video_detection(path_x):
    video_capture = path_x
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    model = YOLO("YOLO-Weights/best.pt")
    classNames = ['Cheese_ObourLand', 'Dina_Milk', 'Dina_Orange_Juice', 'Halawa_ElBawadi', 'Juhayna_Guava', 'Red_egg', 'Yosfy']

    detected_items = ['Dina_Orange_Juice', 'Dina_Milk']

    taken_time = datetime.now()
    while True:
        if datetime.now() - taken_time >= timedelta(seconds=30):
            break
        success, img = cap.read()
        if not success:
            break
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                color = (85, 45, 255)
                if class_name == 'Dina_Milk':
                    color = (0, 204, 255)
                elif class_name == "Dina_Orange_Juice":
                    color = (222, 82, 175)
                elif class_name == "Cheese_ObourLand":
                    color = (0, 149, 255)
                if conf > 0.5:
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        yield img

    fetch_qr_code(detected_items)
    cv2.destroyAllWindows()
