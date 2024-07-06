# BERT Chatbot with Groq API Integration

This project integrates a BERT-based chatbot with the Groq API for advanced text generation and processing capabilities. The application is built using FastAPI for the backend and Streamlit for the frontend.



## Configuration

1. Create a `config.json` file in the project root directory with the following content:

    ```json
    {
      "api_endpoint": "https://api.groq.com/endpoint",
      "api_key": "YOUR_GROQ_API_KEY"
    }
    ```

2. Update the `config.json` file with your Groq API endpoint and API key.

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

    The FastAPI app will be accessible at `http://localhost:8000`.

2. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

    The Streamlit app will be accessible at the URL provided in the terminal (e.g., `http://localhost:8501`).

## Endpoints

### Generate Text

- **Endpoint:** `/generate/`
- **Method:** `GET`
- **Parameters:**
  - `prompt` (string): The input prompt for generating text.
- **Response:** JSON object containing the generated text.



## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Hugging Face Transformers
Streamlit
FastAPI
javascript
