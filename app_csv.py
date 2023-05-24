import streamlit as st
from datetime import datetime
import pandas as pd

from app_utils import save_uploaded_file

def run_app_csv() :
    st.subheader('csv 파일 업로드')
    csv_file = st.file_uploader('csv 파일을 업로드하세요.',type=['csv']) # 파일 확장자명
    if csv_file is not None: # 파일이 있음녀
        current_time = datetime.now()
        filename = current_time.isoformat().replace(':','-')+'.csv'

        csv_file.name = filename
        save_uploaded_file('csv', csv_file)
        df = pd.read_csv('csv/'+filename)
        st.dataframe(df)