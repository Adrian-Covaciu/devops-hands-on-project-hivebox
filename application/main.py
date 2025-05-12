
from flask import Flask
from blueprints import temperature, version

app = Flask(__name__)
app.register_blueprint(temperature, url_prefix='')
app.register_blueprint(version, url_prefix='')

if __name__ == "__main__":
    app.run()
