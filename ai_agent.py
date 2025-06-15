import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage ,SystemMessage
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException, Request, status
import uvicorn # Import uvicorn for the main execution block
from fastapi.middleware.cors import CORSMiddleware 
load_dotenv()


app = FastAPI(title="Dynamic Prompt LangGraph API")
origins = [
    "http://localhost",
    "http://localhost:8501", # Default Streamlit local port
    # Add any other origins where your frontend might be hosted
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods
    allow_headers=["*"], # Allows all headers
)
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY"))
agent_executor = create_react_agent(llm, tools=[])


class ChatRequest(BaseModel):
    """Defines the structure for a request with a system prompt and a user query."""
    prompt: str  
    query: str

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok", "message": "API is healthy"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest) -> Dict[str, Any]:
    """
    Receives a system prompt and a user query, then returns the agent's response.
    """
    if not request.prompt or not request.query:
        raise HTTPException(status_code=400, detail="The 'prompt' and 'query' fields cannot be empty.")
    state = {
        "messages": [
            SystemMessage(content=request.prompt),
            HumanMessage(content=request.query)
        ]
    }

    try:
        # Run the agent with the specified persona and query
        response = agent_executor.invoke(state)
        
        # Extract the final reply from the agent's messages
        reply = response["messages"][-1].content
        return {"reply": reply}
    except Exception as e:
        # Handle any errors during agent execution
        raise HTTPException(status_code=500, detail=f"Agent failed to respond: {e}")
if __name__ == "__main__":
    # This allows you to run the app directly using `python your_backend_file.py`
    # For production, you'd typically use `uvicorn your_backend_file:app --host 0.0.0.0 --port 8000`
    uvicorn.run(app, host="0.0.0.0", port=8000)
