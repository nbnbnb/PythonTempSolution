import pika
import json
import time

# 建立到服务器的连接
creds_broker = pika.PlainCredentials("rabbit","rabbit")
conn_params = pika.ConnectionParameters("192.168.199.198",virtual_host="/",credentials=creds_broker)

conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

msg = json.dumps({"client_name":"RPC Client 1.0","time":time.time()})

# 创建应答队列
# exclusive=True 表示队列名称是唯一的
# auto_delete=True 表示当接收完应答消息后断开和队列的连接时，Rabbit 会自动将队列删除
# 当指定没有名字的 queue 时，RabbitMQ 会自动为你分配一个唯一的名称
result = channel.queue_declare(exclusive=True,auto_delete=True)
msg_props = pika.BasicProperties()
# 唯一的名称通过 result.method.queue 读取
# 并将消息的 reply_to 头设置唯一的队列名称
msg_props.reply_to = result.method.queue

channel.basic_publish(body=msg,exchange="rpc",properties=msg_props,routing_key="ping")

print("Send 'ping' RPC call. Waiting for reply...")

def reply_callbaack(channel,method,header,body):
    print("RPC Reply --- " + body.decode())
    channel.stop_consuming()

channel.basic_consume(reply_callbaack,queue=result.method.queue,consumer_tag=result.method.queue)

channel.start_consuming()

# 先启动 Client 端