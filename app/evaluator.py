import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3.5:3.8b"

def evaluate_answer(question, student_answer):
    prompt = f"""
You are an exam evaluator.

Question:
{question}

Student Answer:
{student_answer}

Evaluate strictly.
Give:
1. Score out of 10
2. Feedback
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]