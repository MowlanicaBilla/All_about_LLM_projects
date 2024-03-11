# Langchain-FastAPI Integration

## Overview
This project integrates Langchain with FastAPI, providing a framework for document indexing and retrieval, as well as chat functionality, using PostgreSQL and pgvector. It is designed to support both synchronous and asynchronous operations.

## Features
- **Document Management**: Methods for adding, retrieving, and deleting documents.
- **Vector Store**: Utilizes Langchain's vector store for efficient document retrieval.
- **Chat Functionality**: Includes a chat endpoint that leverages Langchain for response generation.
- **Asynchronous Support**: Offers async operations for enhanced performance.

## Configuration
Ensure to set environment variables such as `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `DB_HOST`, `DB_PORT`, and `OPENAI_API_KEY`. Configure the database connection string appropriately and initialize Langchain and OpenAI embeddings according to project needs. Set all the variables in an `.env` file like below:
```
OPENAI_API_KEY = YOUR_API_KEY
POSTGRES_DB = DB_NAME
POSTGRES_USER = USERNAME
POSTGRES_PASSWORD = PASSWORD
DB_HOST = localhost
DB_PORT = 5433 # Default
USE_ASYNC = True # True for ASYNC and False for Synchronous calls
```


### Steps to configure
1. Install Postgres DB in your local if you do not have one
2. Create a password, host and port
3. Install Docker and make sure it is running.
4. `pip install -r requirements.txt`
5. Once all the requirements are set.
6. Run `docker-compose up`
7. Run `docker ps` - You will see an image created and running
8. Run `uvicorn main:app --port 8000`
9. Open `http://127.0.0.1:8000/docs`
10. In the FastAPI UI - To check for Sync and Async requests - change the env accordingly as mentioned above
   * Write the text you want to search in the POST method- Click execute
   * This creates an ID and copy-paste that in the GET method - Click execute
   * Open a new terminal and run `python myrequest.py`
   * You will see a response like so- `Response from get-all-ids/: ['d7db3c1e-def5-11ee-801c-eec107e38d71']`.
   * For Synchronous call:
       * Since we repeated the calls thrice in `myrequest.py`, all calls will be done simultaneously one after the other - text, ID, text, ID, and so on.
   * For Asynchrounous call:
       *  Since we repeated the calls thrice in `myrequest.py`, all calls will be executed which ever gets executed first. 




#### References
* https://youtu.be/Arf7UwWjGyc?si=kJYOqhDt3QAvrKO9
