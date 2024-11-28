# PDF Question Answering App

This repository contains a **Streamlit** application for querying the content of uploaded PDF documents using **LangChain** and **OpenAI embeddings**. 

## Features
- Upload a PDF file to the app.
- Automatically splits the content into smaller chunks for efficient processing.
- Embedding-based similarity search using **FAISS**.
- Ask questions about the content of the uploaded PDF and get AI-powered answers.

## Getting Started

### Prerequisites
- OpenAI API key (stored in a `.env` file)

### Installation
1. Install dependencies using Pipenv:
    ```bash
    pipenv install
    ```

2. Create a `.env` file in the root directory with your OpenAI API key:
    ```env
    OPENAI_API_KEY=your-api-key
    ```

4. Run the application:
    ```bash
    pipenv run python main.py
    ```

### Usage
1. Launch the Streamlit app in your browser.
2. Upload a PDF file.
3. Ask questions about the content of the PDF and receive responses.

## How It Works
1. **PDF Processing**: Uploaded PDF files are read and split into chunks using **LangChain's RecursiveCharacterTextSplitter**.
2. **Embeddings Generation**: If embeddings for the PDF have not been computed before, they are generated using **OpenAI embeddings** and saved locally using **FAISS**.
3. **Question Answering**: Queries are matched against the embeddings using FAISS similarity search, and the top matches are passed to a **LangChain QA chain** powered by an OpenAI language model.

## Dependencies
- **Streamlit**: For building the interactive web application.
- **LangChain**: For text splitting, embeddings, and chain processing.
- **FAISS**: For efficient similarity search.
- **PyPDF2**: For reading and extracting text from PDFs.
- **python-dotenv**: For managing environment variables.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Streamlit](https://streamlit.io)
- [LangChain](https://www.langchain.com)
- [OpenAI](https://openai.com)

---

Feel free to fork, modify, and contribute to this project!
