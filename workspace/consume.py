from confluent_kafka import Consumer
import time

conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "0",
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

### USed single compute
consumer.subscribe(['SomeTopic'])
while True:
    msg = consumer.poll(1.0)
    
    if msg is None:
        print(msg)
        continue
        
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue
    print("Connected to Topic: {} and Partition : {}".format(msg.topic(), msg.partition() ))
    print("Received Message : {} with Offset : {}".format(msg.value().decode('utf-8'), msg.offset() ))
    time.sleep(2.5)


### Used thread
# from confluent_kafka import KafkaError, KafkaException

# def consume(consumer, topics):    
#     try:
#         consumer.subscribe(topics)
#         # use this as a way to stop the loop
#         t = threading.currentThread()
#         while getattr(t, "run", True):
#             msg = consumer.poll(timeout=5.0)
#             print(msg)
#             if msg is None: 
#                 print('123')
#                 continue

#             if msg.error():
#                 if msg.error().code() == KafkaError._PARTITION_EOF:
#                     # End of partition event
#                     sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
#                                      (msg.topic(), msg.partition(), msg.offset()))

#                 elif msg.error():
#                     raise KafkaException(msg.error())

#             else:
#                 key = msg.key().decode("utf-8")
#                 data = msg.value().decode("utf-8")
#                 print(key, data)
#     finally:
#         # Close down consumer to commit final offsets.
#         consumer.close()


# import threading
# thread = threading.Thread(target=consume, 
#                           args=(consumer, ["SomeTopic"]))
# thread.start()
# print('end')

# thread.run = False ### if want to end