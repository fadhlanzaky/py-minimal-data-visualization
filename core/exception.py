from werkzeug.exceptions import HTTPException

class BadRequestException(HTTPException):
    code = 400

class EntityTooLargeException(HTTPException):
    code = 413

class ItemNotFound(HTTPException):
    code = 404