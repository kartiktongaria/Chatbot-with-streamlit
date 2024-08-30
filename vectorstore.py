from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

class CustomEmbeddingModel:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
    
    def embed_documents(self, texts):
        return self.model.encode(texts)

    def embed_query(self, query):
        return self.model.encode([query])[0]

    def __call__(self, texts):
        # This makes the class callable
        return self.embed_documents(texts)

class CustomFAISS:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.embedding_model = CustomEmbeddingModel(model_name)
    
    def create_faiss(self, text, faiss_index_path="faiss_index"):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )
        texts = text_splitter.create_documents([text])
        docs = text_splitter.split_documents(texts)

        db = FAISS.from_documents(docs, self.embedding_model)
        db.save_local(faiss_index_path)

        print(f"FAISS index saved to {faiss_index_path} successfully!")

        return db

    def return_vectorstore(self):
        new_db = FAISS.load_local("faiss_index", self.embedding_model, allow_dangerous_deserialization=True)
        return new_db



