from .classes import State
from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI

SECRET_KEY = config('OPENAI_API_KEY')

llm:ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(api_key=SECRET_KEY, model="gemini-1.5-flash")

def node_1(state:State):
    result = llm.invoke(state["prompt"])
    return {"output": result.content}
