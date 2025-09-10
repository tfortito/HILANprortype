# HILAN – Human-in-the-Loop AI (Prototype)

Streamlit demo where:
- Users submit a question → AI generates a draft (OpenAI).
- Validators review (approve / edit / reject) → earn micro-rewards.
- Users get **Human-Verified** answers.

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here  # or use Streamlit secrets
streamlit run hilan_app.py
