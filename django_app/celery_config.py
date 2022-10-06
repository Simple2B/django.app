import os

REDIS_URI = os.environ.get("REDIS_URI", "redis://127.0.0.1:5656")

broker_url = REDIS_URI
result_backend = REDIS_URI

# task_annotations = {"tasks.add": {"rate_limit": "3/m"}}
