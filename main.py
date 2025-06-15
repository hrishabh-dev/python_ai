import streamlit as st
import requests
import json

FASTAPI_URL = "http://localhost:8000/chat" 

st.set_page_config(
    page_title="Dynamic Prompt LangGraph Chat",
    page_icon="🤖",
    layout="centered"
)
st.title("🤖 Dynamic Prompt LangGraph Chat")
st.markdown("""
Enter a **system prompt** to define the AI's persona or instructions,
then ask your **query** to get a response from the LangGraph agent.
""")
st.header("Define AI's Persona (System Prompt)")
system_prompt = st.text_area(
    "💡 Example: 'You are a helpful assistant who loves to explain complex topics simply.'",
    height=100,
    placeholder="Enter the system prompt here...",
    key="system_prompt_input"
)
st.header("Your Query")
user_query = st.text_area(
    "❓ Example: 'What is photosynthesis?'",
    height=100,
    placeholder="Enter your query here...",
    key="user_query_input"
)
if st.button("Get AI Response", use_container_width=True, type="primary"):
    # Basic validation
    if not system_prompt and not user_query:
        st.warning("Please provide both a system prompt and a user query.")
    elif not system_prompt:
        st.warning("Please provide a system prompt.")
    elif not user_query:
        st.warning("Please provide a user query.")
    else:
    
        payload = {
            "prompt": system_prompt,
            "query": user_query
        }
        with st.spinner("Thinking... Please wait..."):
            try:
                # Make the POST request to your FastAPI backend
                response = requests.post(FASTAPI_URL, json=payload)
                response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

                # Parse the JSON response
                result = response.json()
                
                # Display the AI's reply
                if "reply" in result:
                    st.success("Here's the AI's response:")
                    st.info(result["reply"])
                else:
                    st.error("Received an unexpected response format from the API.")
                    st.json(result) # Show the full response for debugging
            except  Exception as e: # Catch a broader range of exceptions
                st.error(f"An error occurred: {e}. Please check the server and your input.")
st.markdown("---")
st.caption("Powered by LangGraph, FastAPI, and Streamlit")