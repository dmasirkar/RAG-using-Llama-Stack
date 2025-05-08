# import required library
from llama_stack_client import LlamaStackClient
from llama_stack_client import Agent, AgentEventLogger
from llama_stack_client.types import Document
from llama_stack_client import RAGDocument
import uuid
from termcolor import cprint
from rich.pretty import pprint

# connect to llama stack server
client = LlamaStackClient(base_url="http://localhost:8321")

# Create a vector database instance
embed_lm = next(m for m in client.models.list() if m.model_type == "embedding")
embedding_model = embed_lm.identifier
vector_db_id = f"v{uuid.uuid4().hex}"
client.vector_dbs.register(
    vector_db_id=vector_db_id,
    embedding_model=embedding_model,
)

source = "https://llama-stack.readthedocs.io/en/latest/index.html"

print("rag_tool> Ingesting document:", source)

document = RAGDocument(
    document_id="document_1",
    content=source,
    mime_type="text/html",
    metadata={},
)


# Insert documents
client.tool_runtime.rag_tool.insert(
    documents= [document],
    vector_db_id=vector_db_id,
    chunk_size_in_tokens=500,
)

# Get the model being served
llm = next(m for m in client.models.list() if m.model_type == "llm")
model = llm.identifier

# Create the RAG agent
rag_agent = Agent(
    client,
    model=model,
    instructions="You are a helpful assistant. Use the RAG tool to answer questions as needed.",
    tools=[
        {
            "name": "builtin::rag/knowledge_search",
            "args": {"vector_db_ids": [vector_db_id]},
        }
    ],
)

session_id = rag_agent.create_session(session_name=f"s{uuid.uuid4().hex}")

prompt = "What does llama stack provides?"
#prompt = "What are client-side SDKs available for different languages?"

# Non-streaming API
response = rag_agent.create_turn(
    session_id=session_id,
    messages=[{"role": "user", "content": prompt}],
    stream=False,
)
print("Inputs:")
pprint(response.input_messages)
print("Output:")
pprint(response.output_message.content)
#print("Steps:")
#pprint(response.steps)
