from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def list_all_booked_trades():
    return render_template('list-trades.html')


@app.route("/book-trade", methods=['GET'])
def book_new_trade():
    return render_template('book-trade.html')


if __name__ == "__main__":
    app.run(port=8081, debug=True)
