#Author：Alex.Zhang
import pika
import uuid,time,random


class FibonacciRpcClient( object ):
    def __init__(self):
        self.connection = pika.BlockingConnection( pika.ConnectionParameters(
            host='localhost') )

        self.channel = self.connection.channel()

        result = self.channel.queue_declare( exclusive=True ,queue=str(random.random()))
        self.callback_queue = result.method.queue

        self.channel.basic_consume( self.callback_queue,self.on_response
                                     )

    def on_response(self , ch , method , props , body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self , n):
        self.response = None
        self.corr_id = str( uuid.uuid4() )
        self.channel.basic_publish( exchange='' ,
                                    routing_key='rpc_queue' ,
                                    properties=pika.BasicProperties(
                                        reply_to=self.callback_queue ,
                                        correlation_id=self.corr_id ,
                                    ),
                                    body=str( n ) )
        while self.response is None:
            self.connection.process_data_events()#非阻塞版的consumer。start
            print('no message....')
            time.sleep(0.5)
        return int( self.response )

while True:

    fibonacci_rpc = FibonacciRpcClient()
    num=input('put your number:')

    print( " [x] Requesting fib(%s)"%num )
    response = fibonacci_rpc.call(num)
    if response is None:
        print('hehe')
    else:
        print( " [.] Got %r" % response )
