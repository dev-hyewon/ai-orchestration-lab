"""
2단계: 문서 기반 질문 응답 (RAG: Retrieval-Augmented Generation)
📌 학습 목표
    - TextLoader / PyPDFLoader / UnstructuredLoader
    - TextSplitter (RecursiveCharacterTextSplitter 등)
    - FAISS 벡터DB 사용
    - RetrievalQA 체인 구성
"""

# Load PDF
# PyPDFLoader는 PyMuPDF(fitz) 또는 pdfminer와 같은 백엔드를 사용하므로 pypdf 패키지를 추가 install 해야함
from langchain_community.document_loaders import PyPDFLoader
PDF_PATH = "/home/hub/dev.lab/Notes/python_leehyewon/sample.pdf"
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

"""
#Check - Load PDF
for i, doc in enumerate(documents):
    print(f"\n--- Page {i+1} ---\n")
    print(doc.page_content)

print(f"\n--- End ---\n")
"""


# Split Document
## 조각 내 중복 최소화 및 맥락 유지를 목적으로 함
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, # 한 조각 당 최대 문자 수
    chunk_overlap=200 # 이전 조각과 겹치는 문자 수 (맥락 유지)
)
docs = text_splitter.split_documents(documents)

"""
#Check - Split Document
for i, doc in enumerate(docs):
    print(f"\n--- Page {i+1} ---\n")
    print(doc.page_content)

print(f"\n--- End ---\n")
"""

# Vectorize
## 문서 -> 벡터로 변환해서 검색 가능하게 함
## FAISS가 빠른 검색용 인덱스를 생성함
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
embedding = OllamaEmbeddings(model="mistral")
vectorstore = FAISS.from_documents(docs, embedding)

"""
#Check - Split Document
print(f"Indexed {vectorstore.index.ntotal} vectors.")  # 저장된 벡터 개수 출력 (FAISS 내부 index 크기 확인)
"""

# QA
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
retriever = vectorstore.as_retriever() # 벡터스토어로부터 retriever 생성
llm = OllamaLLM(model="mistral") # 최신 LLM 객체로 교체
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever) # RetrievalQA 체인 구성

# 질문과 응답 실행 (invoke 방식 사용)
#print(qa_chain.run("What is the main topic of this document?"))
query = "What is the main topic of this document?"
response = qa_chain.invoke({"query": query})
print(response["result"])  # invoke 결과는 딕셔너리로 반환됨

"""
Q: "What is the main topic of this document?"
A: "The main topic of this document is Joe Biden's prostate cancer diagnosis."
"""
