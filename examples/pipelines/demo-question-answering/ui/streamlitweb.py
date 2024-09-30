import os
import streamlit as st
import time
import re
from dotenv import load_dotenv
import requests

# Set up paths
base_dir = os.path.dirname(os.path.abspath(__file__))
submissions_path = os.path.join(base_dir, '..', 'data', 'submission_data.jsonl')
problems_path = os.path.join(base_dir, '..', 'data', 'problems_data.jsonl')

def question_page():
    # Load environment variables
    load_dotenv()
    api_host = os.environ.get("HOST", "0.0.0.0")
    api_port = int(os.environ.get("PORT", 8000))

   
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.pinimg.com/originals/1d/4d/26/1d4d265e5158caf580175ab222bc020f.jpg");
    background-size: cover;
    background-position: centre;
    background-repeat: no-repeat;
    background-attachment: fixed;
    }
    </style>
    """


    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Streamlit UI elements
    square_logo_html = """
        <div style="text-align: center;">
            <img src="https://i.pinimg.com/originals/6e/6c/30/6e6c30f9e433896d22045b63c1d400ea.jpg" alt="Square Logo" width="200" height="200">
            <br>
        </div>
    """
    st.markdown(square_logo_html, unsafe_allow_html=True)
    st.title("CiviCraft")

    # Specify the type of question about Codeforces problems
    question = st.text_input(
        "Which help you need related to civil engineering?(example: 'what are steps to calculate watercontent in Soil Sample?')",
        placeholder="Which practical help you need?",
    )

    # Handle API request if a question is provided
    if question:
        if not os.path.exists(submissions_path) and not os.path.exists(problems_path):
            st.error("Failed to process file. Please check the Codeforces data.")
        else:
            url = f'http://{api_host}:{api_port}/v1/pw_ai_answer'  # Endpoint of your RAG server
            data = {
                "prompt": question,  # Ensure you are using the right key based on your RAG API
            }

            try:
                response = requests.post(url, json=data)  # Sending the query to the RAG system
                
                if response.status_code == 200:
                    #st.write("### Raw Response Text:")
                    raw_string = response.text
                    #st.write(raw_string)  # Display raw response for debugging
                    empty_string=raw_string.split('\\n')
                    formatted_output = "\n".join(empty_string)

                    st.write(formatted_output)
                    # Attempt to parse the raw response
                    
                    
                else:
                    st.error(f"Unsuccessfull")
            except requests.exceptions.RequestException as e:
                st.error(f"Unsuccessfull")

# Run the central page
if __name__ == "__main__":
    question_page()
