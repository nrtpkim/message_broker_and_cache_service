from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Consumer, KafkaError

def clear_topic_messages(admin_client, topic_name):
    admin_client.delete_topics([topic_name])
    print(f"Topic '{topic_name}' cleared.")

def consume_all_messages(consumer, topic):
    consumer.subscribe([topic])

    while True:
        message = consumer.poll(1.0)
        
        if message is None:
            print("No message received.")
            break
        elif not message.error():
            print('Received message: {}'.format(message.value().decode('utf-8')))
        elif message.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached.')
            break
        else:
            print('Error: {}'.format(message.error()))
            break


def create_new_topic(admin_client, topic_name):
    new_topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)
    admin_client.create_topics([new_topic])


def main():
    # Kafka configuration
    kafka_config = {
        'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
    }

    # Topic to be cleared
    topic_to_clear = 'SomeTopic'

    # Create an AdminClient instance
    admin_client = AdminClient(kafka_config)

    topic_to_prune = 'SomeTopic'
    # retention_duration_ms = 5000


    # PRUNE TOPIC
    create_new_topic(admin_client, topic_to_prune)

    # Clear the topic's messages
    clear_topic_messages(admin_client, topic_to_clear)

    # Create a Kafka consumer instance
    consumer = Consumer({
                'bootstrap.servers': '0.0.0.0:9092',
                'group.id': "0",
                'auto.offset.reset': "earliest" 
    })

    # Consume all messages from the cleared topic
    consume_all_messages(consumer, topic_to_clear)

if __name__ == '__main__':
    main()