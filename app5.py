import streamlit as st
from PIL import Image # 이미지 처리 라이브러리

def main():
    st.title('내 앱 대시보드')

    # 사진과 영상을 보여주는 방법
    img = Image.open('data/image_03.jpg')
    st.image(img, use_column_width=True) # use_column_width : 화면 채우기
    # 이미지 URL로 불러와서 보여주기
    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')

    video_file = open('data/video1.mp4', mode='rb')
    st.video(video_file)


if __name__=='__main__':
    main()
