import streamlit as st 
from pandasai.llm.openai import OpenAI

#from dotenv import load_dotenv

import os

import pandas as pd
from pandasai import PandasAI

from PIL import Image

#load_dotenv()

from googletrans import Translator

file_path = os.path.join('data','record.csv')
data = pd.read_csv(file_path)

translator = Translator()

#openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_key="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"


def chat_with_csv(df,prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = PandasAI(llm)

    try:
        result = pandas_ai.run(df, prompt=prompt)
        result = translator.translate(text=result, dest='es')
        result=result.text
    except:
        result="Intenta mas tarde porfavor"

    return result

st.set_page_config(layout='wide')

file_path = os.path.join('data','logo.png')
logo_image = Image.open(file_path) 

st.sidebar.image(logo_image, use_column_width=True)
st.title("CHAT IA DELFOS INTEIA")

col1, col2 = st.columns([2,1])

with col1:
    st.info("INFORME INCIDENTES POR COMUNAS")
    st.dataframe(data, use_container_width=True)

with col2:

    st.info("IA DELFOS INCIDENTES DE MOVILIDAD BETA")
    
    input_text = st.text_area("ESCRIBE TU PREGUNTA?")

    if input_text is not None:
        if st.button("ENVIAR PREGUNTA"):
            st.info("DELFOS IA INTEIA: "+input_text)
            result = chat_with_csv(data, input_text)
            st.success(result)

