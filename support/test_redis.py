#!/usr/bin/env python
import redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)
print("Sending")
out = redis_client.publish('test_channel', 'some data')

print(out)
'''
p = redis_client.pubsub()
p.subscribe('my-channel')
p.get_message()
'''
