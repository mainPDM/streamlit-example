import streamlit as st
import pandas as pd
import numpy as np
from subprocess import check_output
import os
import requests

def appel_reseau():
  res = requests.get('link')
  response = res.text
  return response

st.title("Appel réseau")
link=st.text_area('Lien',value='MyLink')
rt=st.button('Appel', on_click = appel_reseau)
response_text=st.text_area('Réponse',value=rt)


