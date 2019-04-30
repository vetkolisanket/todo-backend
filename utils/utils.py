headers_mapping = {'csv': {'content-type': 'application/csv'},
                   'json': {'content-type': 'application/json'}}


def ok_response(response, status=False, message="OK", headers='json', code=200):
    return status, response, code, message, headers_mapping[headers]
