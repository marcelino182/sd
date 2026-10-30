<?php

$connection = new AMQPConnection();
$connection->setHost('192.168.204.140');
#$connection->setHost('10.0.0.30');
$connection->setVhost('/my_vhost');
$connection->setLogin('aluno');
$connection->setPassword('aluno');
$connection->connect();

$channel = new AMQPChannel($connection);
$exchange = new AMQPExchange($channel);

$callback_func = function(AMQPEnvelope $message, AMQPQueue $q) use (&$max_consume) {
    echo " [x] Received ", $message->getBody(), PHP_EOL;
    $q->nack($message->getDeliveryTag());
    sleep(1);
};

try {
    $routing_key = 'Hello_World';
    $queue = new AMQPQueue($channel);
    $queue->setName($routing_key);
    $queue->setFlags(AMQP_NOPARAM);
    $queue->declareQueue();
    echo ' [*] Waiting for messages. To exit press CTRL+C ', PHP_EOL;
    $queue->consume($callback_func);
}
catch(AMQPQueueException $ex) {
    print_r($ex);
}
catch(Exception $ex){
    print_r($ex);
}

echo 'Close connection...', PHP_EOL;
$queue->cancel();
$connection->disconnect();

?>
