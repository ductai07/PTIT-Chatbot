# PTIT CHATBOT BY DUCTAI
## Description:
Famework : Langchain  
API : FastAPI
Model: *gemini-1.5-flash* của Google , *all-MiniLM-L6-v2* của HuggingFace  


PTIT CHATBOT :.  
├───data  
├───img  
├───src  
│   ├───model  
│   │   └───__pycache__  
│   ├───rag_code  
│   │   └───__pycache__  
│   └───__pycache__  
└───vectorstores  
    └───db_faiss  

## Install and setup :  
1.Setup môi trường:  
```pip install -r requirements.txt``` 

2.Sử dụng API Key của Google với model *gemini 1.5 flash* và model Embedding *all-MiniLM-L6-v2* ở HuggingFace  

3.Chạy code ở local với đoạn code:   
```python -m uvicorn src.app:app --host "0.0.0.0" --port 5000```


## API  
![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/Chatbot_gui.png)    
*Một số kết quả*  

> Câu hỏi về điều kiện đạt học bổng:  

![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/result.png)  
> Câu hỏi về địa chỉ của trường PTIT:  

![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/result3.png)  

> Câu hỏi giới thiệu về trường PTIT:  

![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/result2.png)  



