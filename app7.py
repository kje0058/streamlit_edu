import streamlit as st
from datetime import datetime
import os # 파일이나 폴더 작업시 사용
import pandas as pd

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


def main():
    st.title('내 앱 대시보드')

    # 업로드
    menu = ['이미지업로드', 'csv업로드', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
    print( choice ) # 누를때마다 터미널에 표시
    if choice == menu[0]: # 리스트 수정시 인덱스면 일일이 입력할 필요 없어 편리
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
            
    elif choice == menu[1]:
        st.subheader('csv 파일 업로드')
        csv_file = st.file_uploader('csv 파일을 업로드하세요.',type=['csv']) # 파일 확장자명
        if csv_file is not None: # 파일이 있음녀
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':','-')+'.csv'

            csv_file.name = filename
            save_uploaded_file('csv', csv_file)
            df = pd.read_csv('csv/'+filename)
            st.dataframe(df)

    else:
        st.subheader('이 대시보드 설명')

if __name__=='__main__':
    main()
