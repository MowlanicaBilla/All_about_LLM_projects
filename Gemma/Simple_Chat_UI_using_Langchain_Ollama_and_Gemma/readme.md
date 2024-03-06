# Langchain, Gemma, Ollama and Chainlit
Simple Chat UI using the Gemma model via Ollama, LangChain, and Chainlit

### Open Source in Action 🚀
- [Gemma](https://ai.google.dev/gemma/docs/model_card) as Large Language model via [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/) as a Framework for LLM
- [LangSmith](https://smith.langchain.com/) for developing, collaborating, testing, deploying, and monitoring LLM applications.
- [Chainlit](https://docs.chainlit.io/langchain) for deploying.

## System Requirements

You must have Python 3.10 or later installed. Earlier versions of Python may not compile.

## Steps to Replicate 

1. Fork this repository and create a codespace in GitHub OR Clone it locally.
   ```
   https://github.com/MowlanicaBilla/All_about_LLM_projects.git
   ```
2. OPTIONAL - To extract only this specific folder: Install `git-filter-repo` (if not already installed):
   ```
   # For Linux/macOS:
   sudo apt install git-filter-repo

   # For Windows:
   # Download and install from https://github.com/newt/git-filter-repo
   ```
3. OPTIONAL - Filter the repository to keep only the desired subfolder:
   ```
    cd Gemma/Simple_Chat_UI_using_Langchain_Ollama_and_Gemma  # Change directory to the cloned repository
    git filter-branch --subdirectory-filter Simple_Chat_UI_using_Langchain_Ollama_and_Gemma --all

   ```

4. Create a virtualenv and activate it
   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```

5. OPTIONAL - Rename example.env to .env with `cp example.env .env`and input the environment variables from [LangSmith](https://smith.langchain.com/). You need to create an account on the LangSmith website if you haven't already.
   ``` 
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY="your-api-key"
   LANGCHAIN_PROJECT="your-project"
   ```

4. Run the following command in the terminal to install the necessary Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the following command in your terminal to start the chat UI:
   ```
   chainlit run langchain_gemma_ollama.py
   ```

## Disclaimer
This test project is an attempt to learn new stuff using the available open-source projects and models. It is not meant to be used in production as it's not production-ready. You can modify the code and use it for your use cases ✌️

