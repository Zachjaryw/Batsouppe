import pandas as pd
import numpy
import json
from Dropbox_Setup import *
import streamlit as st

st.title('Batsouppe Inventory')

dbx = initializeToken(st.secrets.access.access)

historicalData = pd.DataFrame(fromDBX(dbx,st.secrets.file.filepath))

with st.expander('Select Items to Bring to Convention:'):
  with st.form('items'):
    st.write('Select all items that you will bring to the convention or select ALL if brining all items:')
    c0, c1, c2 = st.columns(3)
    select0 = c0.checkbox("ALL",key = 'ALL')
    j = 1
    for i in historicalData.STANDEES:
      exec(f'select{j} = c{j%3}.checkbox("{i}",key = "{i}")')
      j+=1
    button = st.form_submit_button('Submit')
    
