import streamlit as st

def main():
    st.title('앱 대시보드')
    
    name='홍길동'

    print('제 이름은 {}입니다.'.format(name))

    st.text('제 이름은 {}입니다.'.format(name)) # 웹브라우저에 표시할 때 st 사용(text:작은 글씨로 나옴)

    st.header('이 영역은 헤더 영역')

    st.subheader('이 영역은 서브헤더 영역')
    
    st.success('성공했을 때 나타내고 싶은 문장')
    st.warning('경고하고싶을 때 문장')
    st.info('알림을 주고 싶을 때')
    st.error('문제가 발생했음을 알려주고 싶을 때')

    st.help(range) # 도움말(range함수가 뭔지 알려줌)

if __name__=='__main__':
    main()

# http://localhost:8501 8501(prot번호)