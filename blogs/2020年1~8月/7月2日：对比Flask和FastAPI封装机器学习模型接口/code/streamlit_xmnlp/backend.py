
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from fastapi import FastAPI
from pydantic import BaseModel
import xmnlp

# 应用实例化
app = FastAPI()

'''
xmnlp相关模型的模型有：
- 中文分词：xmnlp.seg(doc, hmm=True)
- 词性标注：xmnlp.tag(doc)
- 拼写检查：xmnlp.checher(doc, level=0)
- 文本摘要：xmnlp.keyword(doc) / xmnlp.keyphrase(doc)
- 情感分析：xmnlp.sentiment(doc)
- 汉字部首：xmnlp.radical(doc)
- 转化拼音：xmnlp.pinyin(doc)
'''

# 定义数据格式
class Data(BaseModel):
    model_name: str
    input: list

# 中文分词接口
@app.post('/flag0')
def flag0(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.seg(x, hmm=True) for x in msg]
    return {'success': True, 'rlt': rlt}

# 词性标注接口
@app.post('/flag1')
def flag1(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.tag(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 拼写检查接口
@app.post('/flag2')
def flag2(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.checker(x, level=0) for x in msg]
    return {'success': True, 'rlt': rlt}

# 文本摘要接口
@app.post('/flag3')
def flag3(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.keyphrase(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 情感分析接口
@app.post('/flag4')
def flag4(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.sentiment(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 汉字部首接口
@app.post('/flag5')
def flag5(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.radical(x) for x in msg]
    return {'success': True, 'rlt': rlt}

# 转化拼音接口
@app.post('/flag6')
def flag6(data_zh: Data):
    msg = data_zh.input
    rlt = [xmnlp.pinyin(x) for x in msg]
    return {'success': True, 'rlt': rlt}

