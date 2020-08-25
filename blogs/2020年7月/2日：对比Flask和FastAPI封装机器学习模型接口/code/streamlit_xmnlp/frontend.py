#!/usr/bin/python
# -*- coding: UTF-8 -*-

import streamlit as st
import requests

# 定义接口查询函数
def send2back(data_bin):
    rlt = requests.post('http://127.0.0.1:8000/flag0', json=data_bin).json()

st.title("自然语言处理APP")
html_tmp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">基于XMNLP与FastAPI制作</h2>
    </div>
    """
st.markdown(html_tmp, unsafe_allow_html=True)

st.markdown('---')

option = st.selectbox('请选择你想要使用的功能：',
                      ('', '中文分词', '词性标注', '拼写检查', '文本摘要', '情感分析', '汉字部首', '转化拼音'))
content = st.text_input('请输入待分析的内容：')

if option == '中文分词':
    if st.button("中文分词") & (content != ''):
        data_bin = {'model_name': 'flag0', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag0', json=data_bin).json()
        st.text(rlt['rlt'][0])
elif option == '词性标注':
    if st.button("词性标注") & (content != ''):
        data_bin = {'model_name': 'flag1', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag1', json=data_bin).json()
        st.text(rlt['rlt'][0])
elif option == '拼写检查':
    if st.button("拼写检查") & (content != ''):
        data_bin = {'model_name': 'flag2', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag2', json=data_bin).json()
        st.write(rlt['rlt'][0])
elif option == '文本摘要':
    if st.button("文本摘要") & (content != ''):
        data_bin = {'model_name': 'flag3', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag3', json=data_bin).json()
        st.write(rlt)
elif option == '情感分析':
    if st.button("情感分析") & (content != ''):
        data_bin = {'model_name': 'flag4', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag4', json=data_bin).json()
        # st.write(rlt['rlt'][0])
        if rlt['rlt'][0] < 0.5:
            st.write(":angry:", rlt['rlt'][0])
        else:
            st.write(":smile:", rlt['rlt'][0])
elif option == '汉字部首':
    if st.button("汉字部首") & (content != ''):
        data_bin = {'model_name': 'flag5', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag5', json=data_bin).json()
        st.write(rlt['rlt'][0])
elif option == '转化拼音':
    if st.button("转化拼音") & (content != ''):
        data_bin = {'model_name': 'flag6', 'input': [content]}
        rlt = requests.post('http://127.0.0.1:8000/flag6', json=data_bin).json()
        st.write(rlt['rlt'][0])
else:
    pass