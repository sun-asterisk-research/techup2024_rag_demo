# RAG Demo for Sun* TechUp 2024 

## Introduction
This is a demo for the Retrieval Augmented Generation (RAG) model. The RAG model is a combination of a retriever and a generator. The retriever is responsible for finding relevant documents from a large corpus, and the generator is responsible for generating the answer based on the retrieved documents.

## Installation
To install the required libraries, run the following command:
```bash
pip install -r requirements.txt
```

## Usage

### Config the OpenAI Azure 
You need to config the Azure OpenAI API key in the azure_config.py file. 

### Indexing the documents
First you need push the documents into the /data folder. Then you can index the documents by running the following command:
```bash
python populate_database.py
```
After this step the database will be save into /chroma folder 

### Running the RAG model
After indexing the documents, you can run the RAG model by running the following command:
```bash
python query_data.py "Why did Mr. Kobayashi Taihei come to Vietnam?"
```

### Run with GUI interface 
```bash 
python ui.py
```