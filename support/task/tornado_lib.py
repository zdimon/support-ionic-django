import redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)
import json

def ws_update_list():
    data = {"action": "update_list", "message": "ok"}
    redis_client.publish("support-channel", json.dumps(data))

def ws_update_task(task_id):
    data = {"action": "update_task", "message": task_id}
    redis_client.publish("support-channel", json.dumps(data))