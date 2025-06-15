# python_ai

A modern Python project for experimenting with dynamic prompt engineering, AI agents, and conversational interfaces using the latest in generative AI and web technologies.

## Overview

This repository demonstrates a full-stack AI chat solution, combining:
- **Frontend**: Streamlit-based web UI for user interaction and prompt customization.
- **Backend**: FastAPI server exposing endpoints for health checks and AI chat, powered by LangGraph and Google Gemini models.
- **Agent Logic**: Uses LangGraph's ReAct agent with the Gemini 1.5 flash model for customizable, persona-driven chat.

## Features

- Define a system prompt to set your AI agent's persona or instructions.
- Ask user queries and receive AI-generated responses in real time.
- Modular backend using FastAPI and LangGraph, easily extensible for new tools or model providers.
- Secure API with CORS for local and remote frontend communication.
- Frontend built with Streamlit for simplicity and rapid prototyping.

## Directory Structure

```
python_ai/
├── ai_agent.py        # FastAPI backend with LangGraph agent logic
├── main.py            # Streamlit frontend for chat interface
├── requirements.txt   # Python dependencies
├── .gitignore
├── .devcontainer/     # (Optional) Dev container setup
├── venv/              # (Optional) Virtual environment (not tracked)
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- (Recommended) A virtual environment

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/hrishabh-dev/python_ai.git
   cd python_ai
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   - Create a `.env` file or export as environment variables:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     PORT=8000  # Optional, backend default port
     ```

### Running the Application

#### 1. Start the Backend (FastAPI)

```bash
python ai_agent.py
# or for production:
uvicorn ai_agent:app --host 0.0.0.0 --port 8000
```

#### 2. Launch the Frontend (Streamlit)

```bash
streamlit run main.py
```

- By default, the Streamlit app will connect to the backend at `https://python-ai-s8dj.onrender.com`.
- To use a local backend, change the `FASTAPI_URL` variable in `main.py` to `http://localhost:8000`.

## Usage

- Open the Streamlit web UI.
- Enter a **system prompt** (to define agent persona/instructions).
- Enter your **query** (the question to ask the AI).
- Click **Get AI Response** and view the answer.

## Key Technologies

- [Streamlit](https://streamlit.io/) - Frontend web UI
- [FastAPI](https://fastapi.tiangolo.com/) - REST API backend
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent orchestration
- [Google Gemini](https://ai.google.dev/) - LLM provider (via `langchain_google_genai`)
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Maintainer

Created and maintained by [hrishabh-dev](https://github.com/hrishabh-dev).

---

*Feel free to adapt this README as your project evolves!*
