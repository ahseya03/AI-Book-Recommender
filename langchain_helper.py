# langchain_helper.py
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
from langchain.llms import OpenAI

import os
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize the LLM with appropriate settings
llm = OpenAI(temperature=0.7)

def recommend_books(genre):
    # Chain 1: Generate Book Titles
    prompt_template_titles = PromptTemplate(
        input_variables=['genre'],
        template="Suggest three intriguing book titles in the {genre} genre."
    )

    titles_chain = LLMChain(llm=llm, prompt=prompt_template_titles, output_key="book_titles")

    # Chain 2: Generate Brief Descriptions
    prompt_template_descriptions = PromptTemplate(
        input_variables=['book_titles'],
        template="Provide a brief description for each of the following book titles: {book_titles}. Return it as a list."
    )

    descriptions_chain = LLMChain(llm=llm, prompt=prompt_template_descriptions, output_key="book_descriptions")

    # Combine the chains
    chain = SequentialChain(
        chains=[titles_chain, descriptions_chain],
        input_variables=['genre'],
        output_variables=['book_titles', "book_descriptions"]
    )

    response = chain({'genre': genre})

    return response

if __name__ == "__main__":
    genre = "Science Fiction"  # Example genre
    response = recommend_books(genre)
    print(response)
