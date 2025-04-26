from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Try to read a dummy key from Redis
    message = r.get('message')
    if not message:
        r.set('message', 'Hello, World!')
        message = 'Hello, World!'
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

