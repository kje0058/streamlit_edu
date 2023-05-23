import streamlit as st
import pandas as pd

def main():
    st.title('앱 대시보드')

    df = pd.read_csv('data/iris.csv')

    # 버튼
    if st.button('데이터 보기') : # 버튼을 누르면 True
        st.dataframe(df)

    name='Mike'
    # 대문자 버튼을 누르면, 대문자로 표시하고
    # 소문자 버튼을 누르면, 소문자로 나오게 하자

    if st.button('대문자') :
        st.text(name.upper())
    
    elif st.button('소문자') : 
        st.text(name.lower())
    
    st.dataframe(df)
    # petal_length 컬럼을 정렬하고 싶다.
    # 오름차순 정렬, 내림차순 정렬 두가지 옵션을 선택토록

    status = st.radio('정렬을 선택하세요', ['오름차순','내림차순'])
    print(status)
    if status=='오름차순':
        st.dataframe(df.sort_values('petal_length'))
    elif status=='내림차순':
        st.dataframe(df.sort_values('petal_length',ascending=False))

    # 체크박스 : 설정과 해제

    if st.checkbox('데이터프레임 보이기') :
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다.')

    # 여러개 중에 1개를 선택
    language=['선택', 'Python','Java','C','GO','PHP']

    selected_lang = st.selectbox('선호하는 언어를 선택!', language)

    if selected_lang=='Python':
        st.text('파이썬이 최고지')
    
    elif selected_lang=='Java':
        st.text('클래스가 좀 어렵지')

    elif selected_lang=='C':
        st.text('비타민C가 더 상큼해')
        
    elif selected_lang=='Go':
        st.text('어딜가')
        
    elif selected_lang=='PHP':
        st.text('너는 무엇이냐')

if __name__=='__main__':
    main()