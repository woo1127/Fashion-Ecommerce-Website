from flask import current_app, jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code=400, message=None):
    current_app.logger.error(f'Status code: {status_code}, message: {message}')

    if message is None:
        message = HTTP_STATUS_CODES.get(status_code, 'Unknown error')
    
    return jsonify({
        'code': status_code,
        'message': message,
        'data': None
    }), status_code
    

def render_response(status_code=200, message='Success', data=None):
    return jsonify({
        'code': status_code,
        'message': message,
        'data': data
    }), status_code