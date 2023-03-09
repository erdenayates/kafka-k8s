from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['b-2.erdenaymks.dibkfn.c13.kafka.us-east-1.amazonaws.com:9092','b-1.erdenaymks.dibkfn.c13.kafka.us-east-1.amazonaws.com:9092'])

producer.send('mks101', b'Hello, World!')
