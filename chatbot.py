from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("gsk_api_key"),
    base_url="https://api.groq.com/openai/v1"
)

# chat history list
chat_history = []

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

def get_response(user_input, chat_history):
    chain = template | model

    result = chain.invoke({
        "query": user_input,
        "chat_history": chat_history
    })

    # update history
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=result.content))

    return result.content, chat_history


