## About
This is a chat gpt plugin quickstarter that supports vector database document retrieval out of the box.

Essentially, it is a preconfigured server that allows you to load documents into a vector database and query them over an API endpoint that is exposed to the chat gpt plugin.

It supports 2 embedding functions and 2 vector databases, allowing you to choose the option that suits you best.


## Setup
- **RECOMMENDED** Create a python virtual environment
- Run `pip install -r requirements.txt`
- Copy `.env.example` and rename to `.env`
- Set up one Embedding function and one Vector database. Refer to the steps inside **Embedding Functions** and **Vector Databases**
- Run `python vectordb.py init` to initialize your vector database

## Usage
For development:
- Run `python main.py`

For production:
- Run `export PRODUCTION="True" && gunicorn -k uvicorn.workers.UvicornWorker main:app`


## Embedding Functions
#### Open AI Embeddings:
- * Run `pip install openai tiktoken`
- * Edit the `.env` file and modify the following fields:
  ```python
  export EMBEDDINGS=openai
  export OPENAI_API_KEY="YOUR_OPENAI_KEY"
  ```

#### Sentence Transformer Embeddings:
- Install the Sentence Transformers library:
  ```sh
  pip install sentence_transformers
  ```
- No need to edit the `.env` file since **Sentence Transformer** is the default embedding function.

## Vector Databases
#### Pinecone DB:
- Run `pip install pinecone-client`
- Create an index named **sahih-ai** with the following properties:
  - Dimensions: Set it to 768 if you chose **Sentence Transformer Embeddings**, or set it to 1536 if you chose **Open AI Embeddings**.
  - Metric: cosine.
- Edit the `.env` file and place the appropriate values
```python
# Vector Database configuration. Default is pinecone
export PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
export PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
```

#### Chroma DB:
- Run `pip install chromadb` to install chroma db client
- Run `git clone git@github.com:chroma-core/chroma.git` to clone the chroma db server, which we will spin up in a docker container
- `cd` into the `chroma` directory.
- Edit the `docker-compose.yml` file and add `ALLOW_RESET=TRUE` under `environment`:
```yaml
...
    command: uvicorn chromadb.app:app --reload --workers 1 --host 0.0.0.0 --port 8000 --log-config log_config.yml
    environment:
      - IS_PERSISTENT=TRUE
      - ALLOW_RESET=TRUE
    ports:
      - 8000:8000
...
```
- Run the following command to run the Chroma server Docker container:
```sh
docker compose up -d --build
```