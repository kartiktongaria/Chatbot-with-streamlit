import os
from groq import Groq
import configparser
from langchain_community.vectorstores import FAISS
from vectorstore import *
from document_processing import clean_text, extract_text_from_pdf_directory
import warnings
warnings.filterwarnings("ignore")



config = configparser.ConfigParser()
config.read('config.ini')

client = Groq(
    api_key=config['model_config']['api_key'],
)

prompt = config['model_config']['prompt']

def get_result(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=config['model_config']['model'],
    )
    return chat_completion.choices[0].message.content

faiss_handler = CustomFAISS()

def handle_user_query(question):
    if os.path.exists('faiss_index'):
        print("Using existing FAISS")
        vectorstore = faiss_handler.return_vectorstore()

    else:
        print("FAISS Index Not Found!, Creating New FAISS Index")
        text = extract_text_from_pdf_directory()
        cleaned_text = clean_text(text)
        vectorstore = faiss_handler.create_faiss(cleaned_text)

    retriever = vectorstore.as_retriever()
    docs = retriever.invoke(question)

    final_prompt = prompt.format(question=question, context=docs)

    response = get_result(final_prompt)

    # print(response)

    return response


# handle_user_query("CEO of Google is?")




    
