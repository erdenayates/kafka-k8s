var kafka = require('kafka-node'),
    Consumer = kafka.Consumer,
    client = new kafka.KafkaClient({kafkaHost: 'b-2.erdenaymks.dibkfn.c13.kafka.us-east-1.amazonaws.com:9092,b-1.erdenaymks.dibkfn.c13.kafka.us-east-1.amazonaws.com:9092'}),
    consumer = new Consumer(
        client,
        [
            { topic: 'mks101', partition: 0 }
        ],
        {
            autoCommit: false
        }
    );
    
consumer.on('message', function (message) {
    console.log(message.value);
});
