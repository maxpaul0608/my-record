import streamlit as st

pages = {
    "menu":[
        st.Page("./navigations/up_and_down.py",title="UP & DOWN 게임🕹️"),
        st.Page("./navigations/lotto.py",title="lotto 번호 생성🍀")
    ]
}

page = st.navigation(pages)
page.run()