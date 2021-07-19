
from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sign_up():
    return render_template("shop_list.html")

@app.route('/items', methods=['POST', 'GET'])
def items():
    results = request.form
    return render_template('items.html', result=results)

if __name__ == '__main__':
    app.run(debug=True)
