import pandas as pd
import numpy
import json
from Dropbox_Setup import *
import streamlit as st

st.title('Batsouppe Inventory')

dbx = initializeToken(st.secrets.access.access)

historicalData = pd.DataFrame(fromDBX(dbx,st.secrets.file.filepath))

with st.form('items'):
  c0, c1, c2 = st.columns(3)
  j = 0
  for i in historicalData.STANDEES:
    exec(f'c{j%3}.checkbox("{i}",key = "{i}")')
    
