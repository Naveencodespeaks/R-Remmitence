from fastapi.responses import JSONResponse
import uuid


class Utility:
    @staticmethod
    def json_response(status, message, error, data,code=''):
        return JSONResponse({
            'status': status,
            'message': message,
            'error': error,
            'result': data,
            "code": code if code else''
        })

    @staticmethod
    def dict_response(status, message, error, data,code=''):
        return ({
            'status': status,
            'message': message,
            'error': error,
            'result': data,
            "code": code if code else''
        })

    @staticmethod
    def uuid():
        return str(uuid.uuid4())


#print(Utility.uuid())
