from fastapi import APIRouter

from src.domains.request import Request
from src.domains.response import ResponseDictionary
from src.controllers.print_controller import PrintController

controller = PrintController()

router = APIRouter(
    prefix="/print",
    responses={
        404: {"Description": "Not found"}
    }
)


@router.post("")
async def list_files(req: Request) -> ResponseDictionary:
    return controller.print(req)
