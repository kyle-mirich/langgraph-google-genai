# LangGraph ReAct Agent (Python)

Minimal instructions to install and run this agent with `uv` and `langgraph-cli`.

## Prereqs
- Python 3.12+ (make sure your `uv` venv uses 3.12 or higher)
- `uv` (https://docs.astral.sh/uv/getting-started/installation/)
- Google Gemini API key (https://aistudio.google.com/api-keys)
- Tavily API key (free: https://tavily.com)

## 1) Create and activate a virtualenv (uv)
```bash
# create venv with Python 3.12+
uv venv --python 3.12

# activate
source .venv/bin/activate         # macOS/Linux
# or on Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1
# or on Windows (cmd):
# .\.venv\Scripts\activate.bat
```

## 2) Install project deps with `uv`
```bash
uv sync
```

> Note: If `langgraph-cli` fails to install via `uv`, install it directly in the venv with `pip install -U "langgraph-cli[inmem]"` (or `pip3`).

## 3) Configure environment
Create `.env` (or export env vars) with at least:
```env
GOOGLE_API_KEY=your_key
TAVILY_API_KEY=your_tavily_key
# Optional: override model; default is google_genai/gemini-2.5-flash-lite
MODEL=google_genai/gemini-2.5-flash-lite
```

## 4) Run the dev server
```bash
langgraph dev
```

This uses `langgraph.json` and hot-reloads on code changes.

## Notes
- The agent code lives in `src/react_agent`.
- Models are loaded via `MODEL` (format `provider/model`, underscores allowed).
- If you see a blocking-call warning, the Google GenAI client is async-safe; ensure the provider string uses `_` (`google_genai/...`).
