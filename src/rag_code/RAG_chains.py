from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

vector_db_path = "C:/Users/ASUS/Desktop/PTIT Chatbot/vectorstores/db_faiss"


def creat_prompt(template):
    prompt = PromptTemplate(template=template, input_variables=[
                            "context", "question"])
    return prompt

def create_qa_chain(prompt, llm, db):
    llm_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 10}, max_tokens_limit=500),
        return_source_documents=False,
        chain_type_kwargs={'prompt': prompt}
    )
    return llm_chain


def read_vectors_db():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(vector_db_path, embedding_model,
                          allow_dangerous_deserialization=True)
    return db




    