from confluent_kafka import Producer
import cv2
import socket
from PIL import Image
import numpy as np
import io

conf = {
    'bootstrap.servers': "localhost:9092",
    'client.id': socket.gethostname()
}

producer = Producer(conf)


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


# producer.produce("SomeTopic", key="key3", value="33333", callback=acked)     
# producer.poll(1)   # Maximum time (1s) to block while waiting for events


# producer.produce("SomeTopic", key="key4", value="444", callback=acked)     
# producer.poll(1)


image_path = "assets/123.jpg"
# img = cv2.imread("assets/123.jpg", cv2.IMREAD_COLOR)

with open(image_path, 'rb') as image_file:
    image_data = image_file.read()




producer.produce("SomeTopic", key="key4", value=image_data, callback=acked)     
producer.poll(1)

# producer.produce("SomeTopic", key="key4", value=str('123456'), callback=acked)     
# producer.poll(1)

## // Ref docker: https://medium.com/tech-inno/kafka-x-docker-%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A-101-42bf66b52bbd
## // Ref produce, consume : https://towardsdatascience.com/using-kafka-with-python-54dc20717cf7
## // localhost:9000 for ui
