# from langchain.document_loaders import TextLoader
# from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import pinecone
from langchain import VectorDBQA,OpenAI
import pinecone

pinecone.init(api_key="df229a77-4e4f-4c31-8a39-ceba51e11858")

if __name__ == "__main__":
    load_dotenv()
    print("Hello VectorStore")
    loader = TextLoader(
        "D:/pr/backend/newc/documentation/intro-to-vector-db/mediumblogs/mediumblog1.txt"
    )
    document = loader.load()
    text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
    texts=text_splitter.split_documents(document)
    
    print(len(texts))
    embeddings=OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    docsearch=Pinecone.from_documents(text.embeddings,index_name="medium-blogs-embedding-index")
    
    qa=VectorDBQA.from_chain_type(llm=OpenAI(),chain_type="stuff",vectorstore=docsearch,return_source_documents=True)
    query="what is the vector DB? Give me a 15 word answer from a beginner"
    result=qa({"query":query})
    print(result)
