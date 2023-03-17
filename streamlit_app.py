import streamlit as st
import pandas as pd
import numpy as np
from subprocess import check_output
import os

st.title("Appel réseau")
link=st.text_area('Lien',value='MyLink')
st.button('Appel')#, on_click = lancement_conversion)
