from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_ollama.llms import OllamaLLM

# 1. LLM 구성
llm = OllamaLLM(model="mistral")

# 2. 필요한 툴 불러오기 (계산기 포함)
tools = load_tools(["llm-math"], llm=llm)

# 3. 에이전트 초기화
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4. 실행
result = agent.invoke("What is 57.5% of 12345?")
print(result)
