from fastapi import APIRouter, Depends, HTTPException, Response, Request
from schemas.ae_msg import MsgCreate, Out

import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(
    prefix="/api/ae",
    tags=["ae"],
)

# AE表达式
@router.post('/expressions/', response_model=Out)
async def ae_expressions(msg: MsgCreate):
    user_question = msg.content

    # 获取提示词

    # 等待LLM回答问题

    # 结构化输出

    # 使用JSON结构

    # 返回结果

    return {"res":"this is from fastpi","your_qa":user_question}