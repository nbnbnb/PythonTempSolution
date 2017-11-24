import pika


credentials = pika.PlainCredentials("rabbit","rabbit")

# 没有指定虚拟主机，使用默认的 "/"
conn_params = pika.ConnectionParameters("192.168.199.198",credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

# passive=False 表示要声明交互器，而非仅仅获得它的信息
channel.exchange_declare(exchange="hello-exchange",exchange_type="direct",passive=False,durable=True,auto_delete=False)

# 声明队列
channel.queue_declare(queue="hello-queue")

# 通过键 "hola" 将队列和交换器绑定起来
channel.queue_bind(queue="hello-queue",exchange="hello-exchange",routing_key="hola")

# 用于处理传入的消息的函数
def msg_consumer(channel,method,header,body):
    # 消息确认
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == b"quit":
        # 停止消费并退出
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print("接收消息：" + body.decode())
    return

# 订阅消费者
channel.basic_consume(msg_consumer,queue="hello-queue",consumer_tag="hello-consumer")

print("启动消费者")

# 开始消费
channel.start_consuming()


