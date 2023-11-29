from src.domains.response import ResponseDictionary


class RestController:

    @staticmethod
    def build_ok_response() -> ResponseDictionary:
        return ResponseDictionary(ok=True, message='Process Finished')

    @staticmethod
    def build_ok_response_with_data(data) -> ResponseDictionary:
        return ResponseDictionary(ok=True, message='Process Finished', data=data)

    @staticmethod
    def build_error_response(error: str) -> ResponseDictionary:
        return ResponseDictionary(ok=False, error=error)
