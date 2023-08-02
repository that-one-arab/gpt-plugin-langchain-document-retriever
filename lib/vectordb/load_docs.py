from langchain.docstore.document import Document

def load_documents() -> list[Document]:
    """
    Here you can load your own documents, the only requirement is that it must return
    a Langchain documents list.
    Example:
        # load the document and split it into chunks
        loader = TextLoader("PATH_TO_YOUR_TXT")
        documents = loader.load()

        # split it into chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
    
    Langchain supports many other loaders which can be found here: https://python.langchain.com/docs/integrations/document_loaders/
    """
    docs = []

    return docs