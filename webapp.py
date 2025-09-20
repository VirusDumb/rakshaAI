import streamlit as st
from wpmain import phishingtextagent
from agno.agent import Agent, RunResponse
st.title("Raksha AI")
mail=st.text_area("Email text",height=200)
if st.button("Check Phising Probability"):
    with st.spinner(text="Evaluating...."):
        try:
            response: RunResponse = phishingtextagent.run(mail)
            st.write("**Evaluation**")
            st.write(response.content)
        except Exception as e:
            st.error(f"error: {e}")