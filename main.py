import streamlit as st
import os.path
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms.openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

load_dotenv()

def main():
    st.header("Hello!")
    pdf = st.file_uploader("Upload your pdf here!", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # st.write(text)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text)

        store_name = pdf.name[:-4]

        if os.path.exists(f"saved_embeddings/{store_name}"):
            VectorStore = FAISS.load_local(f"saved_embeddings/{store_name}",
                                           OpenAIEmbeddings(),
                                           allow_dangerous_deserialization=True)
            st.write("Embeddings loaded from the disk")
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            VectorStore.save_local(f"saved_embeddings/{store_name}")
            st.write("Embeddings Computation Completed.")

        query = st.text_input("Ask a question about your pdf!")

        if query:
            docs = VectorStore.similarity_search(query=query, k=3)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type='stuff')
            response = chain.run(input_documents=docs, question=query)
            st.write(response)

if __name__ == '__main__':
    main()