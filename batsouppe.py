import pandas as pd
import numpy
import json
from Dropbox_Setup import *
import streamlit as st

st.title('Batsouppe Inventory')

dbx = initializeToken(st.secrets.access.access)

historicalData = pd.DataFrame(fromDBX(dbx,st.secrets.file.filepath))

st.dataframe(historicalData)
