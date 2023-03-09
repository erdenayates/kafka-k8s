from kafka import KafkaConsumer

consumer = KafkaConsumer('mks101', bootstrap_servers=['b-2.erdenaymks.dibkfn.c13.kafka.us-east-1.amazonaws.com:9092','b-1.erdenaymks.dibkfn.c13.kafka.us-east-1.amazonaws.com:9092'])

for message in consumer:
    print(message)
