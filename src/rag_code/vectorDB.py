from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader 
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

vector_db_path = "C:/Users/ASUS/Desktop/PTIT Chatbot/vectorstores/db_faiss"
pdf_path = "C:/Users/ASUS/Desktop/PTIT Chatbot/data/so-tay-sinh-vien.pdf"

def create_db(pdf_file):
    # Load PDF file and split text
    loader = PyPDFLoader(pdf_file)
    pages = loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50))
    
    # Use HuggingFaceEmbeddings to embed text
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create FAISS vector store from documents and embeddings
    db = FAISS.from_documents(pages, embedding=embedding_model)
    db.save_local(vector_db_path)
    print("Success")
    return db

create_db(pdf_path) # Create db 
