from src.controllers.rest_controller import RestController
from src.domains.request import Request
from src.models.zebra_print import print_zebra


class PrintController(RestController):
    def __init__(self):
        super().__init__()

    def print(self, req: Request):
        try:
            print_zebra(req.zpl, req.driver)
            return self.build_ok_response_with_data("Yes")
        except Exception as e:
            return self.build_error_response(str(e))
