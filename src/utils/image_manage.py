from PIL import Image
import numpy as np
import base64
import cv2
import io


def convert_np_2_base64(frame: np.array, encoding='utf-8', format='.png') -> str:
    _, buffer = cv2.imencode(format, frame)
    frame_base64 = base64.b64encode(buffer).decode(encoding)
    return frame_base64

def convert_base64_2_np(b64):
    base64_decoded = base64.b64decode(b64)
    image = Image.open(io.BytesIO(base64_decoded))
    image_np = np.array(image)

    return image_np