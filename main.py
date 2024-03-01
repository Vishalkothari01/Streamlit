import streamlit as st

headerSection = st.container()
mainSection = st.container()
LeftNav = st.sidebar

with headerSection:
    st.title("Streamlit")
    st.markdown("This is a demo of Streamlit")

with mainSection:
    left_col,right_col = st.columns(2)

    with left_col:
        st.header("Left Column")
        st.markdown("Left Column")
        textvalue = st.text_input("Enter text","")
        st.write(textvalue)

    with right_col:
        st.header("Reft Column")
        st.markdown("Reft Column")


with LeftNav:
    st.button("menu1", on_click=lambda: st.success("menu1"))
    st.button("menu2", on_click=lambda: st.success("menu2"))