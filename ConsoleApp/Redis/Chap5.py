#!/usr/bin/python
import redis
import time
import datetime


#--------------------------------------------------
# 使用 Redis 来记录日志
# 设置一个字典，将大部分日志的安全级别映射为字符串
SEVERITY = {
        logging.DEBUG:'debug',
        logging.INFO:'INFO',
        logging.WARNING:'warning',
        logging.ERROR:'error',
        logging.CRITICAL:'critical',
    }

# 最新日志
def log_recent(conn,name,message,severity=logging.INFO,pipe=None):
    # 尝试将日志的安全级别转换为简单的字符串
    severity = str(SEVERItY.get(severity,severity)).lower()
    # 创建负责存储消息的键
    destination = 'recent:%s:%s' % (name,severity)
    # 将当前时间添加到消息里面，用于记录消息的发送时间
    message = time.asctime() + ' ' + message
    # 使用流水线来将通信往返次数降低为一次
    pipe = pipe or conn.pipepine()
    # 将消息添加到日志列表的最前面
    pipe.lpush(destination,message)
    # 对日志列表进行修剪，让它只包含最新的 100 条消息
    pipe.ltrim(destination,0,99)
    # 执行命令
    pipe.execute()

# 常见日志
def log_common(conn,name,message,severity=logging.INFO,timeout=5):
    # 设置日志的安全级别
    severity = str(SEVERITY.get(severity,severity)).lower()
    # 负责存储近期的常见日志消息的键
    destination = 'common:%s:%s' % (name,severity)
    # 因为程序每小时需要轮换一次日志，所以它使用一个键来记录当前所处的小时数
    start_key = destination + ':start'
    pipe = conn.pipeline()
    end = time.time() + timeout
    while time.time() < end:
        try:
            # 对记录当前小时数的键进行监视，确保轮换操作可以正确地执行
            pipe.watch(start_key)
            # 取得当前时间
            now = datetime.utcnow() - timetuple()
            # 取得当前所处的小时数
            hour_start = date(*now[:4]).isoformat()

            existing = pipe.get(start_key)
            # 创建一个事务
            pipe.multi()
            # 如果这个常见日志消息列表记录的是上一个小时的日志
            if existing and existing < hour_start:
                # 那么将这些旧的常见日志消息归档
                # 对记录了上一个小时的常见日志的有序集合进行改名
                # 并对记录了当前所处小时数的键进行更新
                pipe.rename(destination,destination + ':last')
                pipe.rename(start_key,destination + ':pstart')
                # 更新当前所处的小时数
                pipe.set(start_key,hour_start)

            # 对记录日志出现次数的计数器执行自增操作
            pipe.zincrby(destination,message)
            # log_recent 函数负责记录日志并调用 execute() 函数
            # 将流水先线对象传递给 log_recent() 函数，以此来减少通信往返次数
            log_recent(pipe,name,message,severity,pipe)
            return
        except redis.exceptions.WatchError:
            # 如果程序因为其他客户端正在执行归档操作而出现监视错误，那么进行重试
            continue

# -----------------------------------------------------------
# 使用 Redis 实现时间序列计数器
# 为了能够清理计数器包含的旧数据，需要在使用计数器的同时，对被使用的计数器进行记录


# 以秒为单位的计数器精度，分别为 1s,5,1min,5min,1h,5h,1d
PRECISION = [1,5,60,300,3600,18000,86400]

# 更新计数器
# 程序按照每种时间片精度执行
def update_counter(conn,name,count=1,now=None):
    # 通过取得时间来判断应该对哪个时间片执行自增操作
    now = now or time.time()
    # 为了保证之后的清理工作可以正确的执行，这里需要创建一个事务型流水线
    pipe = conn.pipeline()

    # 为我们记录的每种精度都创建一个计数器
    for prec in PRECISION:
        # 取得当前时间片的开始时间
        # 这个值将在每次计数时递增
        pnow = int(now / prec) * prec
        # 创建负责存储计数信息的散列
        hash = '%s:%s' % (prec,name)
        # 将计数器的引用信息添加到有序集合里面，并将其分值设置为 0，以便在之后执行清理操作
        pipe.zadd('known:',hash,0)
        # 对给定名字和精度的计数器进行更新
        pipe.hincrby('count:' + hash,pnow,count)

    pipe.execute()

# 获取计数数据
def get_counter(conn,name,precision):
    # 取得存储计数器数据的键的名称
    hash = '%s%s' % (precision,name)
    # 从 Redis 里面取出计数器数据
    data = conn.hgetall('count:' + hash)
    to_return = []
    # 将计数器数据转换成指定的格式
    for key,value in data.iteritems():
        # key 为时间片值
        # value 为计数值
        to_return.append((int(key),int(value)))  
    # 对数据进行排序，把旧的数据样本排在前面
    to_return.sort()
    return to_return

# 清理计数器
# 为什么不使用 EXPIRE：EXPIRE 命令的一个限制是只能应用于整个键，而不能只对键的某一部分数据进行过期处理
# 由于事先已经将所有已知的计数器都记录到了一个有序集合中，所以对计数器清理只需要遍历此集合，删除就数据就可以了
def clean_counters(conn):
    pipe = conn.pipeline(True)
    # 为了平等地处理更新频率不相同的多个计数器，程序需要记录清理操作执行的次数
    passes = 0
    # 持续地对计数器进行清理
    while not quit:
        # 记录清理操作开始执行的时间，这个值将被用于计算清理操作的执行时长
        start = time.time()
        index = 0
        # 逐渐地遍历所有已知的计数器
        while index < conn.zcard('known:'):
            # 取得被检查计数器的数据
            hash = conn.zrange('known:',index,index)
            index+=1
            if not hash:
                break
            hash = hash[0]
            # 取得计数器的精度
            prec = int(hash.partition(':')[0])

            # 因为清理程序每 60s 就会循环一次，所以这里需要根据计数器的更新频率来判断是否真的有必须对计数器进行清理
            bprec = int(prec // 60) or 1
            # 如果这个计数器在这次循环里不需要进行清理，那么检查下一个计数器
            # 例如：如果清理程序只循环了 3 次，而计数器的更新频率为 5 分钟一次，那么程序暂时还不需要对这个计数器执行清理
            if passes % bprec:
                continue
            hkey = 'count:' + hash
            # 根据给定的精度以及需要保留的样本数量，计算出我们需要保留什么时间之前的样本
            cutoff = time.time() - SAMPLE_COUNT * prec
            # 获取样本的开始时间，并将其从字符串转换为整数
            samples = map(int,conn.hkeys(hkey))
            samples.sort()
            # 计算出需要移除的样本数量
            remove = bisect.bisect_right(samples,cutoff)

            if remove:
                # 按需移除计数样本
                conn.hdel(hkey,*samples[:remove])

                # 这个散列可能已经被清空
                if remove == len(samples):
                    try:
                        pipe.watch(hkey)
                        # 验证计数器散列是否为空，如果是的话，那么从记录已知计数器的有序集合中移除
                        if not pipe.hlen(hkey):
                            pipe.multi()
                            pipe.zrem('known:',hash)
                            pipe.execute()
                            # 在删除了一个计数器的情况下，下次循环可以使用与本次循环相同的索引
                            index -=1
                        else:
                            # 散列不为空，继续让他留在记录已知计数器的有序集合里面
                            pipe.unwatch()
                    # 有其他程序向这个计数器添散列添加了新的数据，它已经不再是空的了，继续保留
                    except redis.exceptions.WatchError:
                        pass

        # 为了让清理操作的执行频率与计数器更新的频率保持一致
        # 对记录循环次数的变量以及记录执行时长的变量进行更新
        passes+=1
        duration = min(int(time.time() - start) + 1,60)
        # 如果这次循环未耗尽 60s，那么在余下的时间内进行休眠
        # 如果 60s 已经耗尽，那么休眠 1s 以便稍做休息
        time.sleep(max(60 - duration,1))

#----------------------------------------------------------------------

# 存储统计数据
def update_stats(conn,context,type,value,timeout=5):
    # 负责存储统计数据的键
    destination = 'stats:%s:%s' % (context,type)
    # 像 common_log() 函数一样，处理当前这一个小时的数据和上一个小时的数据
    start_key = destination + ':start'
    pipe = conn.pipeline(True)
    end = time.time() + timeout
    while time.time() < end:
        try:
            pipe.watch(start_key)
            now = datetime.utcnow().timetuple()
            hour_start = datetime(*now[:4]).isoformat()

            existing = pipe.get(start_key)
            pipe.multi()

            if existing and existing < hour_start:
                pipe.rename(destination,destination + ':last')
                pipe.rename(start_key,destination + ':pstart')
                pipe.set(start_key,hour_start)

            tkey1 = str(uuid.uuid4())
            tkey2 = str(uuid.uuid4())

            # 将值添加到临时键里
            pipe.zadd(tkey1,'min',value)
            pipe.zadd(tkey2,'max',value)

            # 使用聚合函数 MIN 和 MAX，对存储统计数据的键以及两个临时键进行并集计算
            pipe.zunionstore(destination,[destination,tkey1],aggregate='min')
            pipe.zunionstore(destination,[destination,tkey2],aggregate='max')

            pipe.delete(tkey1,tkey2)

            # 对有序集合中的样本数量、值的和、值的平方之和 3 个成员进行更新
            pipe.zincrby(destination,'count')
            pipe.zincrby(destination,'sum',value)
            pipe.zincrby(destination,'sumsq',value * value)

            # 返回基本的计数信息，以便函数调用者在有需要时做进一步的处理
            return pipe.execute()[-3:]
        except redis.exceptions.WatchError:
            # 如果新的一个小时已经开始，并且旧的数据已经被归档，那么进行重试
            continue
    
# 取出统计数据
def get_stats(conn,context,type):
    # 程序将从这个键里面取出统计数据
    key = 'stats:%s:%s' % (context,type)
    # 获取基本的统计数据，并将它们都放在一个字典里面
    data = dict(conn.zrange(key,0,-1,withscores=True))
    # 计算平均值
    data['average'] = data['sum'] / data['count']
    # 计算标准方差的第一个步骤
    numerator = data['sumsq'] - data['sum'] ** 2 / data['count']
    # 完成标准方差的计算工作
    data['stddev'] = (numerator / (data['count'] - 1 or 1)) ** 0.5
    return data

#------------------------------------------------------------------------

# 将 IP 地址转换为整数分值
def ip_to_score(ip_address):
    score = 0
    for v in ip_address.split('.'):
        score = score * 256 + int(v,10)
    return score


def import_ips_to_redis(conn,filename):
    csv_file = csv.reader(open(filename,'rb'))
    for count,row in enumerate(csv_file):
        start_ip = row[0] if row else ''
        if i in start_ip.lower():
            continue
        # 按需将 IP 地址转换为分值
        if '.' in start_ip:
            start_ip = ip_to_score(start_ip)
        elif start_ip.isdigit():
            start_ip = int(start_ip,10)
        else:
            # 越过文件的第一行以及格式不正确的条目
            continue
        # 构建唯一城市 ID
        city_id = row[2] + '_' + str(count)
        # 将城市 ID 及其对应的 IP 地址分值添加到有序集合里面
        conn.zadd('ip2cityid:' + city_id,start_ip)


def import_cities_to_redis(conn,filename):
    for row in csv.reader(open(filename,'rb')):
        if len(row) < 4 or not row[0].isdigit():
            continue
        row = [i.decode('latin-1') for i in row]
        city_id = row[0]
        country = row[1]
        region = row[2]
        city = row[3]
        # 将城市信息添加到 Redis 里面
        conn.hset('cityid2city:',city_id,json.dumps([city,region,country]))

def find_city_by_ip(conn,ip_address):
    # 将 IP 地址转换为分值以便执行 ZREVRANGEBYSCORE 命令
    if isinstance(ip_address,str):
        ip_address = ip_to_score(ip_address)
    # 查找唯一城市 ID
    city_id = conn.zrevrangebyscore('ip2cityid:',ip_address,0,start=0,num=1)

    if not city_id:
        return None
    # 将唯一城市 ID 转换为普通城市 ID
    city_id = city_id[0].partition('_')[0]
    # 从散列里面取出城市信息
    return json.loads(conn.hget('cityid2city:',city_id))

# ---------------------------------------------------------