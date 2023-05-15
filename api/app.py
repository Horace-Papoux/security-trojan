from flask import Flask, request
from flask_cors import CORS
import sys, os

from src.models.account import Account

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    # Return todos as json
    return [account.to_json() for account in Account.all()]

# Add a todo via post request
@app.route('/add', methods=['POST'])
def add():
    print(request.get_json(), file=sys.stderr)
    account = Account.from_json(request.get_json())
    
    account.save()
    
    return [account.to_json() for account in Account.all()]

port = int(os.environ.get('PORT', 5000))

app.run(debug=True, host='0.0.0.0', port=port)