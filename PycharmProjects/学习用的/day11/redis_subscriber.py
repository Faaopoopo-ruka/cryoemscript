#Author：Alex.Zhang
from RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()
print('hehe')
while True:
    msg = redis_sub.parse_response()
    print(msg)