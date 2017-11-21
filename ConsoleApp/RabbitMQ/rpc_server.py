import pika
import json

# 建立到服务器的连接
creds_broker = pika.PlainCredentials("rabbit","rabbit")
conn_params = pika.ConnectionParameters("192.168.199.198",virtual_host="/",credentials=creds_broker)

conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

# 声明交换器和 ping 调用队列
channel.exchange_declare(exchange="rpc",exchange_type="direct",auto_delete=False)
channel.queue_declare(queue="ping",auto_delete=False)
# 为了实现 API 服务器，你遵循着一种模式：将 RPC 函数调用名称作为路由键（同时作为队列名称）
channel.queue_bind(queue="ping",exchange="rpc",routing_key="ping")

# 等待 RPC 调用和应答
def api_ping(channel,method,header,body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    msg_dict = json.loads(body)
    print("Received API call...replying...")
    channel.basic_publish(body="Pong!" + str(msg_dict["time"]),exchange="",routing_key=header.reply_to)


channel.basic_consume(api_ping,queue="ping",consumer_tag="ping")

print("Waiting for RPC calls...")
channel.start_consuming()

