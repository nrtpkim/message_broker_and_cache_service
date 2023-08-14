from src.providers import KafkaConsumeService
from confluent_kafka import Consumer
import time
from PIL import Image
import numpy as np
import io

KCS = KafkaConsumeService.KafkaService()

while True:
    msg = KCS.consume()
    if msg is None:
        print(msg)
        continue
            
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue
    
    if msg is not None:


        # print(type(msg.value()))
        # print(msg.value())

        image_data = msg.value()
        image = Image.open(io.BytesIO(image_data))
        image_np = np.array(image)
        # print(image_np)

        # cv2.imshow("image", image_np)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    time.sleep(2.5)