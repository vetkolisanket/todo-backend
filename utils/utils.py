from flask import Response

headers_mapping = {'csv': {'content-type': 'application/csv'},
                   'json': {'content-type': 'application/json'}}


# def ok_response(response, status=False, message="OK", headers='json', code=200):
#     return status, response, code, message, headers_mapping[headers]


def ok_response(response, status=True, message="OK", headers='json', code=200):
    return {
        'responseData': response,
        'status': status,
        'message': message
    }


def error_response(code, message, response=None, status=False , headers='json'):
    res = {
        'responseData': response,
        'status': status,
        'message': message
    }
    return Response(res, status, mimetype='application/json')