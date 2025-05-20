from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Chat 모델 사용 (대부분의 Ollama 모델은 이 방식 선호)
model = ChatOllama(model="mistral")

# 메시지 기반 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that always starts answers with 'I'll explain it step by step.'"),
    ("human", "Q: {question}")
])

chain = prompt | model

response = chain.invoke({"question": "What is LangChain?"})
print(response.content)