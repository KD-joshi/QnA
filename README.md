# Question and Answer
## Summary
This web-app allows users to enter text from a Wikipedia article, or Textbox and ask questions with the output being an answer extracted from the text. It is built on HuggingFace Transformer model, and implemented with Streamlit.

## Requirements
To install requirements, run `pip install -r requirements.txt`

## Initialisation
To run the app - in the repo folder: `streamlit run app.py`, which starts a server on port 8501 and runs the app.
The app can be slow on first run as it downloads the necessary transformer model (~500MB).
