from langchain_ollama import OllamaLLM  # 최신 기준으로 community 모듈 사용

llm = OllamaLLM(model="mistral")  # 또는 설치된 모델 이름 사용

response = llm.invoke("What is the LangChain Python library used for?")
print("mistral's answer:" + response)