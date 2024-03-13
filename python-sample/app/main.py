from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def main():
  return "hello world!"

if __name__ == '__main__':
  port = 8080
  app.run(port=port,host='0.0.0.0') 
