from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")
prompt = PromptTemplate.from_template("What is the capital of {country}?")
chain = prompt | llm
print(chain.invoke({"country": "South Korea"}))
