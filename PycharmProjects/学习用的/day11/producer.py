#Author：Alex.Zhang
import pika

connection = pika.BlockingConnection( pika.ConnectionParameters(
    'localhost' ) )
channel = connection.channel()

# 声明queue
channel.queue_declare( queue='hello2',durable=True)#队列持久化，即使Rabbitmq服务关闭也可以让队列存在，但并不是消息持久化

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
t=['asdasd','asdasdfdf']
for i in t:
    channel.basic_publish( exchange='' ,
                           routing_key='hello2' ,
                           body=i ,
                           properties=pika.BasicProperties(
                               delivery_mode=2 ,  # make message persistent，这个属性PROPERTIES是让消息持久化的命令
                           )
                           )

print( " [x] Sent 'Hello World!'" )
connection.close()