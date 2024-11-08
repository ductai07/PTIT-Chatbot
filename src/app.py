import os
from pydantic import BaseModel, Field
from fastapi import FastAPI
from langserve import add_routes
from src.model.llm_model import llm_model
from src.rag_code.RAG_chains import read_vectors_db, create_qa_chain, creat_prompt

 
llm = llm_model()

#  Load db and create chatbot
db = read_vectors_db()

template = """<|im_start|>system\nSử dụng thông tin sau đây để trả lời câu hỏi. Hãy trả lời chính xác nhất có thể \n
    {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""

prompt = creat_prompt(template)
chatbot = create_qa_chain(prompt, llm, db)

#   FastAPI
app = FastAPI(title="PTIT Chatbot",
              description="A simple chatbot for PTIT students built by DucTaiTran.")

#  Pydantic models
class InputData(BaseModel):
    question: str = Field(..., title="Xin chào, tôi có thể giúp gì cho bạn?")

class OutputData(BaseModel):
    answer: str = Field(..., title="Câu trả lời: ")
#  Routes 
@app.get("/check")
async def check():
    return {"message": "Hello Chatbot PTIT is running!!!!"}

@app.post("/chatbot", response_model=OutputData)
async def chatbot_api(input_data: InputData):
    output = chatbot.invoke(input_data.question)
    return {"answer": output}

#  routes Langserve
add_routes(app, chatbot, playground_type="default", path="/chatbot")

 
# run: python -m uvicorn src.app:app --host "0.0.0.0" --port 5000  
# http://127.0.0.1:5000/docs