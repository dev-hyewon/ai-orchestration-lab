from langchain_ollama.llms import OllamaLLM  # 최신 기준으로 community 모듈 사용

#Ollama 모델 초기화
llm = OllamaLLM(model="mistral")

response = llm.invoke("What is langChain?")
print("mistral's answer:" + response)