from flask import Response, jsonify

headers_mapping = {'csv': {'content-type': 'application/csv'},
                   'json': {'content-type': 'application/json'}}


# def ok_response(response, status=False, message="OK", headers='json', code=200):
#     return status, response, code, message, headers_mapping[headers]


def ok_response(response, status=True, message="OK", headers='json', code=200):
    res = {
        'responseData': response,
        'status': status,
        'message': message
    }
    r = jsonify(res)
    r.status_code = code
    return r


def error_response(code, message, response=None, status=False , headers='json'):
    res = {
        'responseData': response,
        'status': status,
        'message': message
    }
    # return Response(res, status=code, mimetype='application/json')
    r = jsonify(res)
    r.status_code = code
    return r


# Check if some built-in class which contains these already and use it instead
class StatusCodes():
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
