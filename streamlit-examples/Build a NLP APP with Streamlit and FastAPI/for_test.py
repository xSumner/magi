import requests


# doc0= "小明 NLP 是一款开源的轻量级中文自然语言处理工具🔧，当前版本发布时间为2019年9月，改版本修复了一些 bug 也增加了一些特性，主要新增特性如下：分词/词性标注支持日期、email、url、html标签、书📖的识别。如果您有什么建议/疑问欢迎联系我 xmlee97@gmail.com"
# data_bin = {'model_name': 'flag0', 'input': [doc0]}
# rlt0 = requests.post('http://127.0.0.1:8000/flag0', json=data_bin).json()

# print(rlt0)

# doc1= "小明 NLP 是一款开源的轻量级中文自然语言处理工具🔧，当前版本发布时间为2019年9月，改版本修复了一些 bug 也增加了一些特性，主要新增特性如下：分词/词性标注支持日期、email、url、html标签、书📖的识别。如果您有什么建议/疑问欢迎联系我 xmlee97@gmail.com"
# data_bin = {'model_name': 'flag1', 'input': [doc1]}
# rlt1 = requests.post('http://127.0.0.1:8000/flag1', json=data_bin).json()

# print(rlt1)


# doc2= "中国人敏共和国"
# data_bin = {'model_name': 'flag2', 'input': [doc2]}
# rlt2 = requests.post('http://127.0.0.1:8000/flag2', json=data_bin).json()

# print(rlt2)


# doc3= """自然语言处理: 是人工智能和语言学领域的分支学科。
# 在这此领域中探讨如何处理及运用自然语言；自然语言认知则是指让电脑“懂”人类的语言。 
# 自然语言生成系统把计算机数据转化为自然语言。自然语言理解系统把自然语言转化为计算机程序更易于处理的形式。"""
# data_bin = {'model_name': 'flag3', 'input': [doc3]}
# rlt3 = requests.post('http://127.0.0.1:8000/flag3', json=data_bin).json()

# print(rlt3)

# doc4= """这件衣服的质量也太差了吧！"""
# doc4_= """这酒店真心不错"""
# data_bin = {'model_name': 'flag3', 'input': [doc4, doc4_]}
# rlt4 = requests.post('http://127.0.0.1:8000/flag4', json=data_bin).json()

# print(rlt4)


# doc5= '自然语言处理'
# data_bin = {'model_name': 'flag5', 'input': [doc5]}
# rlt5 = requests.post('http://127.0.0.1:8000/flag5', json=data_bin).json()

# print(rlt5)

doc6= """面朝大海，春暖花开"""
data_bin = {'model_name': 'flag6', 'input': [doc6]}
rlt6 = requests.post('http://127.0.0.1:8000/flag6', json=data_bin).json()

print(rlt6)