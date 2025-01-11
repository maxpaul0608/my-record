import random
import streamlit as st

#------------------------------------
#system
def write_lotto():
    lotto_nums = []
    while len(lotto_nums) < 6:
        num = random.randint(1, 45)
        lotto_nums.append(num)

    container = st.container(border=True)
    cols = container.columns(6)
    for col, num in zip(cols, lotto_nums):
        col.markdown(f'''
                     <div style="
                        display: flex;
                        justify-content: center;
                        margin-bottom: 10px;
                     ">
                     <div 
                     style="
                        width: 50px;
                        height: 50px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        padding: 10px;
                        background-color: blueviolet;
                        border-radius: 50%;
                        border: 2px solid white;
                        font-weight: 600;
                     ">
                        {num}
                     </div></div>
                     ''', unsafe_allow_html=True)


#------------------------------------

#웹페이지 세팅
st.set_page_config(
    page_title="lotto 번호 생성",
    page_icon="🍀",
    layout='wide'
)

#제목 그리기기
st.markdown(
    '''
    # 로또 생성기
    ---
    ''')

#로또 생성 버튼
create_btn = st.button("번호 생성하기🥏")

#버튼을 누르면, 랜덤한 숫자 6개를 보여준다.
if create_btn:
    for i in range(6):
        write_lotto()
   
    
    