"""
1단계: LangChain 핵심 컴포넌트 실습

LangChain의 기반 구조에 익숙해지는 것이 중요합니다.

📌 학습 목표
    - PromptTemplate
    - LLMChain
    - ConversationChain
    - ChatPromptTemplate & ChatOpenAI-like 인터페이스 사용법
"""
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_community.llms.ollama import Ollama

llm = Ollama(model="mistral")
prompt = PromptTemplate(
    input_variables=["product"],
    template="Write a creative ad for the following product: {product}",
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("AI-powered coffee machine"))