# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
# https://smith.langchain.com/hub/rlm/rag-prompt
template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {summaries} 
Answer:
"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
