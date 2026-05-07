import os
import faiss
import numpy as np
from PyPDF2 import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer

print("Loading AI model. . . ")
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_pdf(pdf_path):
    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text

def read_docx(docx_path):
    doc = Document(docx_path)

    text = ""
    for para in doc.paragraphs:
        text += para.text +"\n"
    return text

def read_file(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return read_pdf(file_path)
    
    elif extension == ".docx":
        return read_docx(file_path)
    
    else:
        raise ValueError("Unsupported file format")
    

 
def split_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks

def create_vector_store(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings, dtype=np.float32))

    return index, embeddings

def search_answer(question, chunks, index):

    question_embedding = model.encode([question])

    distances, indices = index.search(
        np.array(question_embedding, dtype=np.float32),
        k=1
    )

    best_match = chunks[indices[0][0]]

    return best_match

def main():

    file_path = input("Enter file path:")

    if not os.path.exists(file_path):
        print("PDF file not found")
        return
    
    print("Reading . . . .")

    text = read_file(file_path)

    print("Creating text chunks. . .")

    chunks = split_text(text)

    print("Creating semantic AI index. . .")

    index, embeddings = create_vector_store(chunks)

    print("\nPDF loaded successfully!")
    print("Ask qestions from file: ")
    print("Type 'exit to quit\n")

    while True:

        question = input("you: ")

        if question.lower() == 'exit':
            break
        
        answer = search_answer(question, chunks, index)

        print("\nAnswer:")
        print(answer)
        print("\n" + "-" * 60 + "\n")

if _name_ == "_main_":
    main()       


