from flask import Flask, render_template

from .domain.config import Config

config = Config().get()

app = Flask(__name__)


@app.route("/", methods=['GET'])
def list_all_booked_trades():
    return render_template('list-trades.html')


@app.route("/book-trade", methods=['GET'])
def book_new_trade():
    return render_template('book-trade.html')


# Expose the Flask App so WSGI server can access it
flask_app = app

if __name__ == 'main':
    # If just running manually outside of WSGI server, run the app
    app.run(port=config.getint('app', 'port'))
