from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Pinecone API key and environment
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# Load and process PDF data
extracted_data = load_pdf("Data/")
text_chunks = text_split(extracted_data)

# Download embeddings
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

# Create a Pinecone index client
index_name = "medicalchatbot"
if index_name not in [index.name for index in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=386,
        metric='cosine',
        spec=pinecone.ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Use Pinecone to store embeddings
index = pc.Index(index_name)
docsearch = Pinecone.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name=index_name
)
