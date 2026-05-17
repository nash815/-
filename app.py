import streamlit as st

st.title("مستشار الطاقة")

مستوى_الطاقة = st.slider("ما مستوى طاقتك اليوم؟", 1, 10, 5)

if st.button("نصيحة"):
    if مستوى_الطاقة <= 4:
        st.write("تناول السبانخ والمكسرات والتمر")
    else:
        st.write("طاقتك جيدة. تناول البروتين")
