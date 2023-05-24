import streamlit as st
from datetime import datetime

from app_utils import save_uploaded_file

def run_app_image() :
    st.subheader( '이미지 파일 업로드' )
    img_file = st.file_uploader( '이미지를 업로드하세요.', type=['png','jpg','jpeg'] ) # 파일 확장자명
    if img_file is not None: # 파일이 있으면
        print( type(img_file) )
        print( img_file.name )
        print( img_file.size ) # 바이트 단위
        print( img_file.type ) # image/jpeg 중요!
            
        # 유저가 올린 파일을
        # 서버에서 유니크하게 처리하기 위해서(중복되지않게)
        # 파일명을 현재시간 조합으로 해서 만든다.(현재시간+유저아이디 등)
        current_time = datetime.now()
        print( current_time )
        print( current_time.isoformat().replace(':','-')+'.jpg' ) # 문자열로 바꾸고 파일이름에 쓸 수 없는 ':' 문자 변경

        filename = current_time.isoformat().replace(':','-')+'.jpg'

        img_file.name = filename

        save_uploaded_file('image', img_file)

        # 밑에 이미지가 나오게 해주세요
        st.image('image/'+filename)