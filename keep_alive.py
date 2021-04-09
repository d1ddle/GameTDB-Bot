from flask import Flask, request
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Hi. This, isn't a website yet. It just pings my discord bot repl so that it stays active. I might figure out how to change it into a website in the future though. Do me a favour, visit: https://d1ddle.com"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()