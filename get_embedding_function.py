from langchain_openai import AzureOpenAIEmbeddings
from azure_config import *

def get_embedding_function():
    embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
        azure_deployment=AZURE_EMBEDDING_DEPLOYMENT,
        openai_api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
    )
    return embeddings
