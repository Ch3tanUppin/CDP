from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Index documentation
def index_docs(docs):
    embeddings = model.encode(docs)
    return docs, embeddings

# Perform search
def search(query, docs, embeddings):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    top_indices = np.argsort(similarities[0])[::-1][:3]
    return [docs[i] for i in top_indices]
