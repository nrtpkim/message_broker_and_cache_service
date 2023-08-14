from src.providers import KafkaConsumeService
from src.providers import RedisService
from src.utils import image_manage
from PIL import Image
import numpy as np
import time
import cv2
import io

KCS = KafkaConsumeService.KafkaService()
RS = RedisService.CacheService()

while True:
    msg = KCS.consume()
    if msg is None:
        print(msg)
        continue
            
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue
    
    if msg is not None:

        image_data = msg.value()
        image = Image.open(io.BytesIO(image_data))
        image_np = np.array(image)

        base64_img = image_manage.convert_np_2_base64(image_np)

        ### Insert byte img
        RS.set_hash(field = 'img1',value=base64_img)

        ### Query 
        base64_img = RS.get_hash(field = 'img1')

        ### Decode
        image_np = image_manage.convert_base64_2_np(base64_img)
        print(image_np.shape)

        # cv2.imshow("image", image_np)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    

    current_time = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))
    print("Current time out:", current_time)


    time.sleep(5) ### Consume 1 meg : every ... sec