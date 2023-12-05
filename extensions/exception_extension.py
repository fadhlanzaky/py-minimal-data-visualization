from core.exception import BadRequestException, EntityTooLargeException, ItemNotFound
from werkzeug.exceptions import HTTPException

def error_handler(error: HTTPException):
    response = {
        'message': error.description
    }

    return response, error.code

def register_exception_handler(app):
    app.register_error_handler(HTTPException, error_handler)
    app.register_error_handler(BadRequestException, error_handler)
    app.register_error_handler(EntityTooLargeException, error_handler)
    app.register_error_handler(ItemNotFound, error_handler)