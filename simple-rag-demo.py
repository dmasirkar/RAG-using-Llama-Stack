from llama_stack_client import Agent, AgentEventLogger, RAGDocument, LlamaStackClient
from rich.pretty import pprint

vector_db_id = "my_demo_vector_db"
client = LlamaStackClient(base_url="http://localhost:8321")

models = client.models.list()

# Select the first LLM and first embedding models
model_id = next(m for m in models if m.model_type == "llm").identifier
embedding_model_id = (
    em := next(m for m in models if m.model_type == "embedding")
).identifier
embedding_dimension = em.metadata["embedding_dimension"]

_ = client.vector_dbs.register(
    vector_db_id=vector_db_id,
    embedding_model=embedding_model_id,
    embedding_dimension=embedding_dimension,
    provider_id="faiss",
)

#source = "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_ai/1.4/html-single/building_and_maintaining_your_rhel_ai_environment/index.html"

source = "https://llama-stack.readthedocs.io/en/latest/index.html"

print("rag_tool> Ingesting document:", source)

document = RAGDocument(
    document_id="document_1",
    content=source,
    mime_type="text/html",
    metadata={},
)
client.tool_runtime.rag_tool.insert(
    documents=[document],
    vector_db_id=vector_db_id,
    chunk_size_in_tokens=400,
)
agent = Agent(
    client,
    model=model_id,
    instructions="You are a helpful assistant",
    tools=[
        {
            "name": "builtin::rag/knowledge_search",
            "args": {"vector_db_ids": [vector_db_id]},
        }
    ],
)

prompt = "What client-side SDKs available for different languages in llama stack?"
print("prompt>", prompt)


# Non-streaming API
response = agent.create_turn(
    session_id=agent.create_session("rag_session"),
    messages=[{"role": "user", "content": prompt}],
    stream=False,
)
print("Inputs:")
pprint(response.input_messages)
print("Output:")
pprint(response.output_message.content)
#print("Steps:")
#pprint(response.steps)
