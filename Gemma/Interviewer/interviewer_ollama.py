from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    
    # Sending an image with the local file path
    elements = [
    cl.Image(name="image1", display="inline", path="interviewer.jpeg")
    ]
    await cl.Message(content="Hello there, I am  Gemma Interviewer. How can I help you ?", elements=elements).send()
    model = Ollama(model="gemma:2b")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You're a very knowledgeable Generative AI Data Science interviewer who asks in-depth questions about the all the latest advanced AI topics and provides answers if asked.
                Help me prepare for the data science interview. Ask all the possible questions on LLMs, Langchain, Machine Learning algorithms, Llamaindex, vector dbs, statistics and other related topics. keep going until I ask you to stop.
                Ask questions one by one. Wait for my answer and correct my answer if its wrong if I ask you to you answer, then go to the next question""",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()