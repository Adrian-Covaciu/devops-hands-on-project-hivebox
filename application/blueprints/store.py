from flask import Blueprint


store = Blueprint('store', __name__)

@store.route('/store')
def store():
    print('')