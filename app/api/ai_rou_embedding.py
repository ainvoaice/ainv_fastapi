from fastapi import APIRouter, Depends

from app.core.dependency_injection import ZMeDataClass, get_zme
from app.schemas.sch_ai_embedding import (
    RagAnswerResponse,
    RagQueryRequest,
    RagQueryResponse,
    RagRerankAnswerResponse,
)
from app.service.ser_ai_embedding import rag_answer as rag_answer_service
from app.service.ser_ai_embedding import rag_answer_rerank as rag_answer_rerank_service
from app.service.ser_ai_embedding import rag_query as rag_query_service


embRou = APIRouter()


@embRou.post("/build-chunks")
async def build_chunks(zme: ZMeDataClass = Depends(get_zme)):
    chunks = "await WageEmbeddingRepository.build_chunks(zme)"
    return {"count": len(chunks), "sample": chunks[:3]}

@embRou.post("/rag_query", response_model=RagQueryResponse)
async def rag_query(
    payload: RagQueryRequest,
    zme: ZMeDataClass = Depends(get_zme),
):
    return await rag_query_service(payload, zme)


@embRou.post("/rag_answer", response_model=RagAnswerResponse)
async def rag_answer(
    payload: RagQueryRequest,
    zme: ZMeDataClass = Depends(get_zme),
):
    return await rag_answer_service(payload, zme)


@embRou.post("/rag_answer_rerank", response_model=RagRerankAnswerResponse)
async def rag_answer_rerank(
    payload: RagQueryRequest,
    zme: ZMeDataClass = Depends(get_zme),
):
    return await rag_answer_rerank_service(payload, zme)
