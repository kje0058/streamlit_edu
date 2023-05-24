import streamlit as st

def main():
    st.title('내 앱 대시보드')
    
    # 텍스트입력
    name = st.text_input('이름을 입력하세요!',max_chars=10) # input은 str로 입력!, 10글자 제한
    st.text('입력하신 이름은 '+name+'입니다')
    message = st.text_area('메시지를 입력하세요', height=1)
    st.text(message)

    # 숫자입력
    number = st.number_input('숫자를 입력하세요~', 1,100) # int(정수형)
    st.text(number*3)
    number2 = st.number_input('숫자를 입력하세요~', 1.0, 100.0) # float(실수형)
    st.text(number2*3)

    # 날짜입력
    my_date = st.date_input('약속 날짜 입력') # 기본값 : 오늘날짜
    print(my_date)
    print(type(my_date)) # datetime.date
    st.text(my_date)

    # 시간입력
    my_time = st.time_input('시간 선택')
    print(my_time)
    st.text(my_time)

    # 비밀번호 처리방법
    password=  st.text_input('비밀번호 입력', type='password') # 앱 대시보드에서 실제로 쓰이지않음
    st.text(password)

    # 색깔
    color = st.color_picker('색을 선택하세요')
    st.text(color)


if __name__=='__main__':
    main()