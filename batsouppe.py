import pandas as pd
import numpy
import json
from Dropbox_Setup import *
import streamlit as st

st.title('Batsouppe Inventory')

dbx = initializeToken(st.secrets.file.filepath)

historicalData = pd.DataFrame(fromDBX(dbx,st.secrets.access.access))

st.dataframe(historicalData)
