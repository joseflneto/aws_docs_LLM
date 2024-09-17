import pickle
import faiss
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from variables import variables


def get_retriever():

    faiss_index = faiss.read_index(variables.faiss_index_path)

    with open(variables.metadata_path, 'rb') as f:
        docs_after_split = pickle.load(f)


    huggingface_embeddings = HuggingFaceBgeEmbeddings(
        model_name="BAAI/bge-small-en-v1.5", 
        model_kwargs={'device':'cpu'}, 
        encode_kwargs={'normalize_embeddings': True}
    )

    vectorstore = FAISS.from_documents(docs_after_split, huggingface_embeddings)

    vectorstore.index = faiss_index


    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    
    return retriever


def build_LLM(retriever):
    llm = HuggingFacePipeline.from_model_id(
        model_id="distilbert/distilgpt2",
        task="text-generation",
        pipeline_kwargs={"temperature": 0.7, "max_new_tokens": 300},
        model_kwargs={"use_auth_token": variables.token}
    )


    prompt_template = """Use the following pieces of context to answer the question at the end. Please follow the following rules:
    1. If you don't know the answer, don't try to make up an answer. Just say "I can't find the final answer but you may want to check the following links".
    2. If you find the answer, write the answer in a concise way with five sentences maximum.

    {context}

    Question: {question}

    Helpful Answer:
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    retrievalQA = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return retrievalQA


def get_LLM():

    retriever = get_retriever()
    retrievalQA = build_LLM(retriever)
    
    return retrievalQA
