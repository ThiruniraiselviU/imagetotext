import requests
import streamlit as st
st.title("image captioning")
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    data=filename
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
inp_img_link=st.text_input("enter image link")
button_sub=st.button("submit")
if button_sub:
    st.image(inp_img_link,caption="uploaded image")
   
    output = query("https://t4.ftcdn.net/jpg/05/47/97/81/360_F_547978128_vqEEUYBr1vcAwfRAqReZXTYtyawpgLcC.jpg")
    output=query(inp_img_link)
    st.print(output[0]['generated_text'])
