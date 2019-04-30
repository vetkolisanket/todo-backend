from flask_restful import Resource
from models.restresponse import RestResponse
from utils.utils import ok_response


class Ping(Resource):

    # def get(self):
    #     return RestResponse(status=True, message="Okay", data="Okay").to_json()

    def get(self):
        return {
            'responseData': 'Okay',
            'message': 'Okay',
            'status': True
        }

    # def get(self):
    #     ok_response("Okay")