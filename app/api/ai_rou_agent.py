from fastapi import APIRouter, Depends

from app.core.dependency_injection import ZMeDataClass, get_zme
from app.schemas.sch_agent import AgentRequest, AgentResponse
from app.agent.executor import agent_answer


agentRou = APIRouter()


@agentRou.post("/ask", response_model=AgentResponse)
async def ask_agent(payload: AgentRequest, zme: ZMeDataClass = Depends(get_zme)):
    return await agent_answer(payload, zme)
