## Qdrant


### Installation
1. Install docker on your system. Make sure it's running.
2. Open your favorite editor - I'm using VScode, open a terminal and type `docker pull qdrant/qdrant`
3. Then type `docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant`
* This step runs a server at `http://localhost:6333/dashboard`
* While this is running, run the steps in the notebook
