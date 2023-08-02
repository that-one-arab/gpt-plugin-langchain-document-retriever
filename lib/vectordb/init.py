from lib.vectordb.index import vectordb
from lib.vectordb.load_docs import load_documents

documents = load_documents()

print("Initializing and loading documents to vector database...")
vectordb.init(documents)
print("Successfully initialized vector database.")