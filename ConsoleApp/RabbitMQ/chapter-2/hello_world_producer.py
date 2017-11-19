import pika


credentials = pika.PlainCredentials("rabbit","rabbit")

# 没有指定虚拟主机，使用默认的 "/"
conn_params = pika.ConnectionParameters("192.168.199.198",credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

# passive=False 表示要声明交互器，而非仅仅获得它的信息
channel.exchange_declare(exchange="hello-exchange",exchange_type="direct",passive=False,durable=True,auto_delete=False)

msg = 'quit'

msg_props = pika.BasicProperties()

msg_props.content_type = "text/plain"

channel.basic_publish(body=msg,exchange="hello-exchange",properties=msg_props,routing_key="hola")

