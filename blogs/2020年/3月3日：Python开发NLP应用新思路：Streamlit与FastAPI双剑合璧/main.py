#!/usr/bin/python
# -*- coding: UTF-8 -*-

from fastapi import FastAPI
from pydantic import BaseModel
import hanlp

# 应用实例化
app = FastAPI()

# 导入Hanlp相关模型
tokenizer_zh = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')
tokenizer_en = hanlp.utils.rules.tokenize_english
recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)
syntactic_parser = hanlp.load(hanlp.pretrained.dep.CTB7_BIAFFINE_DEP_ZH)


# 定义数据格式
class Data(BaseModel):
    model_name: str
    input: list

# 中文分词接口
@app.post('/tok_zh')
def split_cn(data_zh: Data):
    msg = data_zh.input
    rlt = [tokenizer_zh(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 英文分词接口
@app.post('/tok_en')
def split_en(data_en: Data):
    msg = data_en.input
    rlt = [tokenizer_en(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 中文命名实体识别
@app.post('/ner')
def ner(data_zh: Data):
    msg = data_zh.input
    rlt = [recognizer(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 中文依存句法分析接口
@app.post('/parser')
def parser(data_zh: Data):
    msg = data_zh.input
    rlt = syntactic_parser(msg)
    return {'success': True, 'rlt': rlt}

