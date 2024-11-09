# PTIT CHATBOT
## Description:
Famework : Langchain  
API : FastAPI 
FRONT END : Streamlit  
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

2.Sử dụng API Google Key(của bạn) với model *gemini 1.5 flash* và model Embedding *all-MiniLM-L6-v2* ở HuggingFace  

3.Chạy code ở local với đoạn code:   
-Đối với API :   
```python -m uvicorn src.app:app --host "0.0.0.0" --port 5000 ```

-Chạy để hiển thị giao diện:  
```python -m streamlit run frontend.py```


## API  
![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/Chatbot_gui.png)    
*Một số kết quả*  

> Câu hỏi về địa chỉ PTIT:  

![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/result.png)  

> Câu hỏi về học bổng ở PTIT:  

![](https://github.com/ductai07/PTIT-Chatbot/blob/dev/img/result2.png)  



