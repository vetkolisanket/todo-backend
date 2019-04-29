from flask import Flask
from flask_restful import Api  # Should I specify these things in requirements.txt? Ask Kasim

from service_apis.ping import Ping

app = Flask(__name__)

todo_api = Api(app, prefix='/todoservice/v1')

todo_api.add_resource(Ping, '/ping')

if __name__ == '__main__':
    print("app {} started..".format(app.name))
    app.run(host="0.0.0.0", debug=True, port=8510)
