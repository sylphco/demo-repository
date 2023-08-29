from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["testing"])


@router.get("/endpoint")
async def return_endpoint_msg():
    return {
        "status": "successful",
    }
