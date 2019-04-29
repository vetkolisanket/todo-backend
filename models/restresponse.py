import json

class RestResponse:

    def __init__(self, status, message="", data=None):
        self.status = status
        self.message = message
        self.data = data

    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__,
        #                   sort_keys=True, indent=4)

        return {
            'responseData': json.dumps(self.data),
            'message': self.message,
            'status': self.status
        }