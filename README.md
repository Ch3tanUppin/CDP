# CDP Chatbot: How-To Guide Assistant for Segment, mParticle, Lytics, and Zeotap

This project is a chatbot designed to assist users with "how-to" questions related to four Customer Data Platforms (CDPs): **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot extracts relevant information from the official documentation of these platforms to provide step-by-step guidance.

---

## Features

- **"How-To" Questions Support**: The chatbot answers questions like:
  - "How do I set up a new source in Segment?"
  - "How can I create a user profile in mParticle?"
  - "How do I build an audience segment in Lytics?"
  - "How can I integrate my data with Zeotap?"

- **Documentation Scraping**: Automatically fetches and indexes the latest information from the official documentation of the four CDPs.

- **Smart Search**: Provides accurate and concise answers by identifying and extracting relevant sections of the documentation.

---


## Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm (Node Package Manager)

### Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
The backend server will start at http://localhost:5000

2. **Frontend Setup**
    cd frontend
    npm install
    npm start

### Usage

1. Start the backend server: Run python app.py in the backend directory.

2. Start the frontend app: Run npm start in the frontend directory.

3. Interact with the chatbot: Open http://localhost:3000 in your browser and enter your question. For example:
        ** Platform: Segment
        ** Question: "How do I set up a new source in Segment?"


