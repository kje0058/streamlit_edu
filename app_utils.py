import streamlit as st
import os

# 파일 저장 함수
# 디렉토리 이름과, 파일 이름을 주면 (정의시 파라미터 2개 필요)
# 해당 디렉토리에 파일을 저장해주는 함수
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리가 있는지 확인하고,
    #    없으면 디렉토리(폴더)를 먼저 만든다.
    if not os.path.exists(directory): # 디렉토리가 없니?
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일 저장
    with open(os.path.join(directory,file.name),'wb') as f :
        f.write(file.getbuffer())
    return st.success('파일 저장 완료!')