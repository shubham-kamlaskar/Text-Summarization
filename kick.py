import streamlit as st 
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
from langchain.prompts import PromptTemplate

def main():
    st.title("Google Gemini-Pro Model")
    question = st.text_area("Ask a question ?")
    words = st.slider("words",100,500)
    
    prompt_template = PromptTemplate.from_template('''Please summarize the following text into a bullet point summary: {text}.Please restrict the word count strictly to {words} words only.
                                                   If your not able to summarize it in {words} words. Please answer Im not able to do it''')
    
    prompt = prompt_template.format(text=question,words=words)
    
    if question:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
    if st.button("Submit"):
        with st.spinner("Processing.."):
            answer =response.text
            st.write(answer)
            st.write('-'*20)
            st.write("Length of original text :",len(question))
            st.write('-'*20)
            st.write("Length of summarized text :",len(answer))
            st.success("Done")
    
    
if __name__ == "__main__":
    main()