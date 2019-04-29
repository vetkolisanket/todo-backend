from flask_restful import Resource
from models.restresponse import RestResponse


class Ping(Resource):

    def get(self):
        return RestResponse(status=True, message="Okay").toJSON()

    # def get(self):
    #     return {
    #         'responseData': 'Okay',
    #         'message': 'Okay',
    #         'status': True
    #     }