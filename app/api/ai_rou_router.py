from fastapi import APIRouter, Depends

from app.core.dependency_injection import ZMeDataClass, get_zme
from app.schemas.sch_ai_embedding import RagRerankAnswerResponse
from app.schemas.sch_ai_router import RouterQueryRequest
from app.service.ser_ai_router import route_and_answer as route_and_answer_service


routerRou = APIRouter()


@routerRou.post("/route_answer", response_model=RagRerankAnswerResponse)
async def route_answer(
    payload: RouterQueryRequest,
    zme: ZMeDataClass = Depends(get_zme),
):
    return await route_and_answer_service(payload, zme)
