import pandas as pd
import numpy
import json
from Dropbox_Setup import initializeToken as IT
from Dropbox_Setup import fromDBX
from Dropbox_Setup import toDBX
import streamlit as st

st.title('Batsouppe Inventory')

dbx = IT(st.secrets.file.filepath)

historicalData = pd.DataFrame(fromDBX(dbx,st.secrets.access.access))

st.dataframe(historicalData)
