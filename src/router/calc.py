from fastapi import APIRouter

from src.schemas.calc import CalcInput

router = APIRouter()


@router.post("/add_numbers", tags=["Math"])
def add_numbers(data: CalcInput):
    """
    Adds two numbers and returns the result.
    """
    return {"result": data.a + data.b}


@router.get("/subtract_numbers/{a}/{b}", tags=["Math"])
def subtract_numbers(data: CalcInput):
    """
    Subtracts the second number from the first and returns the result.
    """
    return {"result": data.a - data.b}
