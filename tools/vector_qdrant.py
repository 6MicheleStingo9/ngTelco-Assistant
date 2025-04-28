from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from models.cohere import embeddings
from uuid import uuid4
from data.docs import offers_docs

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="demo_collection",
    vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="demo_collection",
    embedding=embeddings,
)

uuids = [str(uuid4()) for _ in range(len(offers_docs))]
vector_store.add_documents(documents=offers_docs, ids=uuids)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2})


def get_vector_info(query):
    return retriever.invoke(query)
