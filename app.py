import streamlit as st
# streamlit 프레임워크(정해져있는 틀이 있어 방법만 알면 쉽게 쓸 수 있음)
# 규칙
def main():
    st.title('내 앱 대시보드')
    st.text('데이터 분석 앱입니다.')
    st.text('테스트 앱입니다.')


if __name__=='__main__':
    main()

# $streamlit run app.py
# 서버 종료 = ctrl+c

# st. --> 화면(웹브라우저)에 표시할 때 사용
