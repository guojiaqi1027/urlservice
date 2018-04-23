from flask import Flask
from api.restore import restore
app = Flask(__name__)
app.register_blueprint(restore)
if __name__ == "__main__":
    app.run()
