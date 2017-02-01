import threading

from flask import *

from bot import bot_server

from bot.logger import get_log

app = Flask(__name__)

other_thread = threading.Lock()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log')
def log_html():
    return render_template('log.html', log = get_log())

def start_bot():
    with other_thread:
        bot_server.start()

def main():
    t1 = threading.Thread(target=start_bot)
    t1.start()
    app.run(host = '0.0.0.0')
