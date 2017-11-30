import pika


credentials = pika.PlainCredentials("rabbit","rabbit")

# 没有指定虚拟主机，使用默认的 "/"
conn_params = pika.ConnectionParameters("192.168.199.198",credentials=credentials,port=9002)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

# passive=False 表示要声明交换器，而非仅仅获得它的信息
# durable=True 持久化交换器 hello-exchange
# auto_delete=True 当最后一个绑定的队列从交互器中删除时，自动删除此交换器
channel.exchange_declare(exchange="hello-exchange",exchange_type="direct",passive=False,durable=True,auto_delete=False)

# 设置镜像参数
# 当设置成 all 时，ha-mode 告诉 Rabbit 你想让队列被镜像到集群所有的节点上
# 这意味着如果在该队列声明之后，集群又新增节点的话，那么该节点就会自动托管一份队列的从拷贝
queue_args = {"ha-mode":"all"}

# 声明队列
channel.queue_declare(queue="hello-queue",arguments=queue_args)

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


