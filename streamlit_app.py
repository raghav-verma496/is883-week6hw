import streamlit as st
import openai

st.title("My Super Awesome OpenAI API Deployment!")

prompt = st.text_input("What is your prompt today?", "Enter your prompt here")
max_tokens = st.number_input("Enter the number of tokens for the response", min_value=1, max_value=100, value=50)

### Load your API Key
my_secret_key = st.secrets['IS883-OpenAIKey-RV']
os.environ["OPENAI_API_KEY"] = my_secret_key

### OpenAI stuff
if prompt:
  response1 = openai.Completion.create(
    model="gpt2",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.9
  )

  response2 = openai.Completion.create(
    model="gpt2",
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.1
  )

### Display
st.subheader("Response 1:")
st.write(response1.choices[0].text)

st.subheader("Response 2:")
st.write(response2.choices[0].text)
