import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title('내 앱 대시보드')
    
    df=pd.read_csv('data/iris.csv')
    
    st.dataframe(df)

    # sepal_length, sepal_width의 관계를 차트로 --> scatter
    fig = plt.figure() # 차트영역
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2=plt.figure()
    sns.regplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig2)

    correlation = df[['sepal_length', 'sepal_width']].corr()
    st.dataframe(correlation) # 피어슨 상관계수 위키백과 참고(상관도) / (양수:비례/음수:반비례)

    # sepal_length로 히스트그램 그리자
    # bin(범위)의 갯수는 20개로
    fig3=plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1) # 1행 2열중에 1번째
    plt.hist(data=df, x='sepal_length', rwidth=0.8, bins=20) 

    plt.subplot(1, 2, 2) # 1행 2열중에 2번째
    plt.hist(data=df, x='sepal_length', rwidth=0.8) # bins 기본값 10개
    st.pyplot(fig3)

    # species 컬럼에는 종에 대한 정보가 들어있는데,
    # 각 종별로 몇 개의 데이터가 있는지
    # 차트로 나타내시오.

    st.dataframe( df['species'].value_counts() ) # 먼저 dataframe으로 수치 확인

    fig4=plt.figure()
    sns.countplot( data=df, x='species' )
    st.pyplot(fig4)

    ## pandas의 dataframe 차트 그리는 코드도 실행 가능!
    fig5=plt.figure()
    df['species'].value_counts().plot(kind='barh') # 기본값 : 선그래프, barh:가로막대, bar: 세로막대
    st.pyplot(fig5)

    # dataframe 자체 plot 함수는 streamlit에서 실행 불가!
    # fig6=plt.figure()
    # df.plot() # 쥬피터노트북은 가능
    # st.pyplot(fig6)

    fig7=plt.figure()
    df['sepal_length'].hist(rwidth=0.8)
    st.pyplot(fig7)

    
if __name__=='__main__':
    main()
