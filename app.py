import docker
from elasticsearch import Elasticsearch
import json
import time

# Configure Elasticsearch connection
es = Elasticsearch(hosts=['http://elk:9200'])

# Connect to Docker daemon
client = docker.from_env()

def send_to_elastic(event):
    try:
        es.index(
            index='docker-events',
            document=event
        )
    except Exception as e:
        print(f"Error sending event: {str(e)}")

def sanitize_keys(obj):
    if isinstance(obj, dict):
        return {k.replace('.', '_'): sanitize_keys(v) for k, v in obj.items()}
    return obj

# Listen for Docker events
for event in client.events(decode=True):
    if event['Type'] in ('container', 'image'):
        if event['status'].startswith(('start', 'die')):
            send_to_elastic(sanitize_keys(event))