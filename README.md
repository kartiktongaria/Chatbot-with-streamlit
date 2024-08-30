# Chatbot-with-streamlit

Welcome to the KonProz Chatbot! This project utilizes Streamlit to provide a user-friendly interface for interacting with a KonProz chatbot. Follow the steps below to set up and run the application.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [Running the Application](#running-the-application)


## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Setup Instructions

1. **Create a Python Virtual Environment**

   To keep your project dependencies isolated, create a virtual environment using:

   ```bash
   python -m venv env
   ```

2. **Activate the Virtual Environment**

   - **On macOS/Linux:**

     ```bash
     source env/bin/activate
     ```

   - **On Windows:**

     ```bash
     .\env\Scripts\activate
     ```

3. **Install Required Libraries**

   Install all necessary libraries using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit app, run:

```bash
streamlit run main.py
```

Now You'll be redirected to the chatbot.