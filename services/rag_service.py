from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from services.llm_service import (
    LLMService
)


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

llm = LLMService()


def process_pdf(
    file_path: str
):

    loader = PyPDFLoader(
        file_path
    )

    docs = loader.load()

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    )

    chunks = splitter.split_documents(
        docs
    )

    db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding_model
)

    db.add_documents(chunks)

    db.persist()

    vectorstore.persist()

    return True


def answer_question(
    question: str
):

    db = Chroma(
        persist_directory="vectorstore",
        embedding_function=embedding_model
    )

    docs = db.similarity_search_with_score(
        question,
        k=4
    )

    sources = []

    context_parts = []

    for doc, score in docs:

        context_parts.append(
            doc.page_content
        )

        sources.append(
            {
                "page":
                doc.metadata.get(
                    "page",
                    "N/A"
                ),

                "source":
                doc.metadata.get(
                    "source",
                    "Unknown"
                ),

                "score":
                float(score)
            }
        )

    context = "\n\n".join(
        context_parts
    )

    prompt = f"""
Answer ONLY from context.

Context:
{context}

Question:
{question}
"""

    answer = llm.generate(
        prompt
    )

    return {
        "answer": answer,
        "sources": sources
    }