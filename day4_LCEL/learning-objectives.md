# 향후 확장

|주제|설명|
|---|---|
|LangServe|LangChain 기반 서버화, REST API 또는 FastAPI 연동|
|LangGraph|LangChain 기반 비동기/병렬/상태머신형 체인 (후속 진행 예정)|
|Guardrails|응답 안전성 검증 및 필터링|
|Tools 연동|Google Search, File I/O, Terminal, Database 등|

### 🔧 환경 유지 관리 팁

- Python 3.9.x에서 대부분의 LangChain 기능은 무리 없이 동작합니다.  
- LangChain은 빠르게 업데이트되므로, 버전 호환성이 안 맞을 경우 `pip install langchain==0.3.25` 등 고정 버전을 유지하세요.  
- Ollama 모델 성능 문제 발생 시 `deepseek-coder` 또는 `llama3` 모델을 활용해 보세요.  

### 다음 추천 실습  
- 원하는 주제로 간단한 RAG 시스템 구축  
- Chat 형식 PromptTemplate 및 메시지 흐름 이해  
- 간단한 에이전트와 툴 연동 실습  
