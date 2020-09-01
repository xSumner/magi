#!/usr/bin/python
# -*- coding: UTF-8 -*-

import streamlit as st
import requests

# 定义接口查询函数
def send2back(data_bin):
    rlt = requests.post('http://111.229.217.153:80/ner', json=data_bin).json()

st.title("自然语言处理APP")
html_tmp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">基于Hanlp与FastAPI制作</h2>
    </div>
    """
st.markdown(html_tmp, unsafe_allow_html=True)

st.markdown('---')

option = st.selectbox('请选择你想要使用的功能：',
                      ('', '中文分词', '英文分词', '中文命名实体识别', '中文依存句法分析'))
content = st.text_input('请输入待分析的内容：')

if option == '中文分词':
    if st.button("中文分词") & (content != ''):
        data_bin = {'model_name': 'tok_zh', 'input': [content]}
        rlt = requests.post('http://111.229.217.153:80/tok_zh', json=data_bin).json()
        st.text(rlt['rlt'][0])
elif option == '英文分词':
    if st.button("英文分词") & (content != ''):
        data_bin = {'model_name': 'tok_en', 'input': [content]}
        rlt = requests.post('http://111.229.217.153:80/tok_en', json=data_bin).json()
        st.text(rlt['rlt'][0])
elif option == '中文命名实体识别':
    if st.button("命名实体识别") & (content != ''):
        data_bin = {'model_name': 'ner', 'input': [list(content)]}
        rlt = requests.post('http://111.229.217.153:80/ner', json=data_bin).json()
        st.write(rlt)
elif option == '中文依存句法分析':
    if st.button("依存句法分析") & (content != ''):
        data_bin = {'model_name': 'parser', 'input': [content]}
        rlt = requests.post('http://111.229.217.153:80/parser', json=data_bin).json()
        st.write(rlt)
else:
    pass