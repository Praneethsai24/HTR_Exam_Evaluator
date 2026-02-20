# Handwritten Exam Evaluation using HTR + Ollama

## Overview
This project extracts handwritten answers using Tesseract OCR (HTR simulation)
and evaluates them using a local LLM via Ollama.

## Requirements
- Python 3.9+
- Ollama installed (https://ollama.ai)
- Pull a model:
    ollama pull llama3

## Install Dependencies
pip install -r requirements.txt

## Run App
streamlit run app/main.py