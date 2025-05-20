import os
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_ollama.llms import OllamaLLM

# Tavily API 키 설정 (https://app.tavily.com/home)
os.environ["TAVILY_API_KEY"] = "자신의 API KEY 붙여넣기"

# LLM 설정 (Ollama - mistral)
llm = OllamaLLM(model="mistral")

# Tavily 검색 툴 로드
search_tool = TavilySearchResults()

# 에이전트 초기화
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# 실행
query = "What are the latest developments in generative AI in 2025?"
result = agent.run(query)
print(result)