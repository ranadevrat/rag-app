from flask import Flask, request, render_template
import openai
from data.dataprovider import key, hg_key
from langchain.embeddings import HuggingFaceEmbeddings
#from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub

app = Flask(__name__)



llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    model_kwargs={
        "max_new_tokens": 512,
        "top_k": 30,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    },
    huggingfacehub_api_token= hg_key,# Replace with your actual huggingface token
)

# Define your rag chatbot function
def chat_with_rag(message):

    full_text = open(r"C:\chatbot_llms\data\doc_rag.txt", "r").read()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_text(full_text)

    embeddings = HuggingFaceEmbeddings()
    #db = Chroma.from_texts(texts, embeddings)
    db = FAISS.from_texts(texts, embeddings)
    retriever = db.as_retriever()
    template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    model = llm


    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])


    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    
    return chain.invoke(message)

# Define your Flask routes
@app.route('/')
def home():
    return render_template('bot_1.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_input']
    bot_message = chat_with_rag(user_message)
    return {'response': bot_message}

if __name__ == '__main__':
    app.run()
