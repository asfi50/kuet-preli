# Recipe Recommendation App

This project is a Recipe Recommendation App built with FastAPI and Streamlit.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/asfi50/kuet-preli.git
    cd challenge_2
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Environment Variables

1. Create a `.env` file in the root directory of the project.
2. Add your Google API key to the `.env` file:
    ```properties
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

2. In a new terminal, start the Streamlit app:
    ```sh
    streamlit run streamlit-app.py
    ```

3. Open your web browser and navigate to:
    - FastAPI: `http://127.0.0.1:8000/docs` for API documentation.
    - Streamlit: `http://localhost:8501` for the Streamlit app.

## Project Structure

- `main.py`: FastAPI application entry point.
- `streamlit-app.py`: Streamlit application entry point.
- `routes/`: Contains the route handlers for FastAPI.
- `views/`: Contains the view functions for Streamlit.
- `database.py`: Database initialization script.
- `.env`: Environment variables file.
- `requirements.txt`: Python dependencies file.

## License

This project is licensed under the MIT License.