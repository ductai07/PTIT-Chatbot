from langchain_google_genai import GoogleGenerativeAI

def llm_model():
    llm = GoogleGenerativeAI(model ="gemini-1.5-flash",
        temperature=0,
        verbose=True,
        google_api_key="da che"
    )
    return llm
