from confluent_kafka import Consumer
from src.utils.app_settings import get_settings
import logging
import time

class KafkaService:
    def __init__(self) -> None:
        conf = {
                'bootstrap.servers': get_settings().KAFKA_URL,
                'group.id': "0",
                'auto.offset.reset': "earliest" 
        }
        
        self.consumer = Consumer(conf)
        self.consumer.subscribe(['SomeTopic'])
        self.timeout_consume = get_settings().KAFKA_TIMEOUT_CONSUME


    def consume(self,):
        msg = self.consumer.poll(self.timeout_consume) # Poll for messages with a timeout of 1 second
        current_time = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))
        print("Current time:", current_time)

        return msg


    



# conf = {
#     'bootstrap.servers': "localhost:9092",
#     'group.id': "0",
#     'auto.offset.reset': 'earliest'
# }

# consumer = Consumer(conf)

# ### USed single compute
# consumer.subscribe(['SomeTopic'])
# while True:
#     msg = consumer.poll(1.0)
    
#     if msg is None:
#         print(msg)
#         continue
        
#     if msg.error():
#         print("Consumer error happened: {}".format(msg.error()))
#         continue


#     print("Connected to Topic: {} and Partition : {}".format(msg.topic(), msg.partition() ))
#     print("Received Message : {} with Offset : {}".format(msg.value().decode('utf-8'), msg.offset() ))
#     time.sleep(2.5)