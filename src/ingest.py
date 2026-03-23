from langchain_community.document_loaders import PyPDFLoader
def load_pdf(path="data/raw/spark_definitive_guide.pdf"):
    loader = PyPDFLoader(path)
    documents = loader.load()
    return documents