# 파일 분리하여 작업
import streamlit as st

from app_image import run_app_image
from app_csv import run_app_csv
from app_about import run_app_about

def main():
    st.title('내 앱 대시보드')

    # 업로드
    menu = ['이미지업로드', 'csv업로드', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
    print( choice ) # 누를때마다 터미널에 표시

    if choice == menu[0]: # 리스트 수정시 인덱스면 일일이 입력할 필요 없어 편리
        run_app_image()
            
    elif choice == menu[1]:
        run_app_csv()

    else:
        run_app_about()

if __name__=='__main__':
    main()
