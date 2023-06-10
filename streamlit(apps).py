import streamlit as st
import time as t
st.image("download (1).jfif")
st.title("welcome to the site")
st.header("machine learning ")
st.subheader("what is learning ")
st.info("give the information about the user")
st.warning("come on the right time else you will marked abs")
st.error("wrong")
st.success("you have got the A grade ")
st.markdown(  "#  site ")
st.markdown(":moon:")
st.caption("here is the caption")
st.latex(r'''a+b x^2+c''')
st.write("this is the text")
st.checkbox("login")
st.button("enter")
st.radio("enter the city want to choose",["fsd ","lahore "])
st.selectbox("enter the course you want to choose",["cyber","no"])
st.multiselect("enter you choose",["sales,marketing,evaluation"])
st.select_slider("enter from the below ",["good","bad ","none "])
st.slider("enter the number from the 1 to 1000",0,1000)
st.number_input("enter the number please from below",0,1000)
st.date_input("enter the date please s")
st.time_input("enter the time")
st.text_area("enter the area ")
st.file_uploader("upload the file here/folder")
st.progress(90)
with st.spinner("just wait"):
             t.sleep(5)

st.balloons()
st.sidebar.title("welcome to the site ")
st.sidebar.text_input("Enter name ")
st.sidebar.text_input("Enter password")
st.sidebar.button("submit")
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("line chart")
st.line_chart(data)
st.code("#print(hellow world)")

st.video(data, format="video/mp4", start_time=0)
video_file = open('DSC_0015.jpg', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
st.title("hy this is ")
st.button("submit this ")





