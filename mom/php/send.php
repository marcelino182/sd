<?php

$connection = new AMQPConnection();
$connection->setHost('127.0.0.1');
#$connection->setHost('192.168.204.140');
$connection->setVhost('/my_vhost');
$connection->setLogin('aluno');
$connection->setPassword('aluno');
$connection->connect();

$channel = new AMQPChannel($connection);
$exchange = new AMQPExchange($channel);

try {
    $routing_key = 'Hello_World';
    $queue = new AMQPQueue($channel);
    $queue->setName($routing_key);
    $queue->setFlags(AMQP_NOPARAM);
    $queue->declareQueue();

    $message = 'Hello RabbitMQ World!';
    $exchange->publish($message, $routing_key);
    echo " [x] Sent 'Hello_World'\n";
    $connection->disconnect();
}
catch (Exception $ex) {
    print_r($ex);
}

?>