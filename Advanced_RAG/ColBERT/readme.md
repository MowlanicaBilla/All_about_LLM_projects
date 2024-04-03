## Identifying the Issue with Dense Embeddings
The dense embedding that you're using in your rack pipelines have a critical flaw which probably is impacting the accuracy of your retrieval. 
Wwe will look at what this potential issue is and what is the potential solution.

### Explaining the Issue
In order to explain this, let's look at a very simple example. 
Here, I have three documents, each one of them contains a single sentence. 

On the right-hand side, we have a query. We compute the embedding of our documents or chunks, and depending on the embedding model that we choose, we will get a vector for each of these chunks. 
Similarly, for the query, we will also get a vector. Then we do similarity search. So basically, we compare this embedding vector with each of the document's embedding vector and figure out which one is the closest and that is returned as a result of our retrieval step.

### Dimensionality of Embedding Models
img
If you look here, there are different embedding models and each one of them has a different dimension. One of the most widely used open-source embedding models is this BGE small which has only 384 dimensions. And more recently, we have started seeing much larger dimensional embeddings when it comes to open-source embedding models.

### Understanding the Issue
Now you might be thinking, what is the issue with embeddings? Let's assume instead of this single sentence, your chunk contains multiple paragraphs because you have a much larger chunk size. In that case, if you're computing embeddings for your chunk, you're going to be compressing all that information into a single vector. That vector may not be able to represent everything that is present in a given chunk. 
In this case, the compression is basically a loss of a lot of information.

### Solution: Colbert v2 for Efficient Retrieval
So what's the solution? A potential solution is in this paper "Colbert v2 for Efficient Retrieval" via Lightweight Late Interaction. And we're going to look at a practical code example later in the video.

### Exploring Colbert v2 Concept
Now, this is a dense paper, but let me try to explain the concepts with a very simple example. Coming back to this, with dense embeddings that we usually use, we are representing a whole chunk with a single embedding vector. But Colbert or Colbert suggests a different technique. In this case, the "C" is contextualized late interaction.

### Implementing the Solution
Let me explain what it means. The first step in this case is that both for our documents and chunks as well as for a query, we tokenize it. That means depending on the tokenizer that we use, we are going to get individual tokens from our documents. So, for each token, we compute embeddings. Every token is going to be represented by a different embedding vector.

### Computing Similarity Scores
Next, for each token in the query, we will compute a similarity score with each token in your documents. Based on these individual similarity scores, we compute an overall score for each document or each chunk. These are called late interactions.

### Conclusion and Recommendation
In this case, each token individually is contributing to the overall score rather than everything being compressed into a single vector. The embeddings that you get for each of these tokens are actually contextualized, so depending on the overall context in which this token is present, that is taken into account when the embeddings are computed.

