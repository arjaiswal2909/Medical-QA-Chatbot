
# **Medical QA Chatbot**

## **Project Description**

This project is a Medical QA Chatbot that leverages Llama2, LangChain, and Pinecone to provide an interactive chatbot for answering medical-related questions. It uses a pre-trained large language model (LLM) for real-time, accurate responses, and a vector-based search engine for efficient query handling. The front-end is a simple web interface using HTML and Bootstrap, while the Flask backend processes the chatbot logic.

## **Tech Stack**

- **Backend Framework:** Flask (Python)
- **LLM Model:** Llama2 (via Hugging Face)
- **Embeddings & Vector Search:** Pinecone
- **Frontend:** HTML, CSS, Bootstrap, jQuery
- **Language Models & Chaining:** LangChain
- **Environment Variables Management:** Python Dotenv
- **Vector Store:** Pinecone
- **Database:** None (data handled in memory)

## **Features**

- Interactive chatbot UI
- Powered by Llama2 as the Large Language Model
- Retrieval-based QA with LangChain and Pinecone
- Responsive design with Bootstrap
- Real-time user interaction via AJAX

## **Screenshots**

### **Chatbot Interface**
![alt text](<Screenshot 2024-09-13 003705-1.png>)


## **Project Setup**

### **1. Installation**

#### **Clone the repository:**
```bash
git clone https://github.com/arjaiswal2909/Medical-QA-Chatbot
```

### **2. Virtual Environment Setup**
Create a virtual environment and activate it:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate

# For Linux/MacOS
source venv/bin/activate
```

### **3. Install Dependencies**
Once the virtual environment is active, install the project dependencies:

```bash
pip install -r requirements.txt
```

### **4. Pinecone Setup**
Create an account on [Pinecone](https://www.pinecone.io), obtain your API Key and Environment, and create an index named `medicalchatbot`.

### **5. Llama2 Model Setup**
Download the Llama2 model from Hugging Face. Ensure the model is stored locally and integrated with the CTransformers package.

### **6. .env Setup**
Create a `.env` file in the project root with the following configuration:

```
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_API_ENV=your_pinecone_api_environment
```

### **7. Running the Application**
Start the Flask app by running the following command:

```bash
python app.py
```

The app will be accessible at: `http://127.0.0.1:8080/`

## **How It Works**

1. The user interacts with a chatbot UI built using HTML, Bootstrap, and jQuery.
2. The message is sent to the Flask backend via AJAX.
3. The backend processes the request using LangChain, which integrates the Llama2 model and Pinecone for retrieving answers.
4. The bot's response is sent back to the frontend and displayed in real-time.

## **Folder Structure**

```plaintext
medical-qa-chatbot/
├── app.py                  # Flask server
├── templates/
│   └── chat.html           # Front-end HTML file
├── static/
│   └── style.css           # CSS for UI
├── src/
│   ├── helper.py           # Helper functions (e.g., for downloading embeddings)
│   └── prompt.py           # Prompt template for the chatbot
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

## **Contributing**

If you want to contribute to this project, feel free to submit a pull request or raise an issue.
