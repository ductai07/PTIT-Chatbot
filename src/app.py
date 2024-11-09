import os
from pydantic import BaseModel, Field
from fastapi import FastAPI,  HTTPException
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
    question: str 

class Output(BaseModel):
    answer: str
    
def clean_response(response: str) -> str:
    # Loại bỏ các thẻ không cần thiết
    response = response.replace("assistant\n", "")
    response = response.replace("", "")
    response = response.strip()
    # Loại bỏ các dòng trống
    lines = response.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    cleaned_response = ' '.join(cleaned_lines)
    return cleaned_response

#  Routes 
@app.get("/check")
async def check():
    return {"message": "Hello Chatbot PTIT is running!!!!"}

@app.post("/answer/", response_model=Output)
async def chatbot_api(input_data: InputData):
    try:
        output = chatbot.invoke(input_data.question)
         
        # Trích xuất chuỗi văn bản từ output
        output_text = output["result"]
        # clean an xơ 
        cleaned_output = clean_response(output_text)
        return {"answer": cleaned_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

 
# run: python -m uvicorn src.app:app --host "0.0.0.0" --port 6060  
# http://127.0.0.1:6060/docs (máy local)