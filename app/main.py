import streamlit as st
from htr_engine import extract_handwritten_text
from evaluator import evaluate_answer

st.title("Handwritten Exam Answer Sheet Evaluator")

uploaded_file = st.file_uploader("Upload Answer Sheet Image", type=["png", "jpg", "jpeg"])

question_prompt = st.text_area("Enter Question / Model Answer")

if uploaded_file and question_prompt:
    extracted_text = extract_handwritten_text(uploaded_file)
    st.subheader("Extracted Text")
    st.write(extracted_text)

    evaluation = evaluate_answer(question_prompt, extracted_text)
    st.subheader("Evaluation Result")
    st.write(evaluation)