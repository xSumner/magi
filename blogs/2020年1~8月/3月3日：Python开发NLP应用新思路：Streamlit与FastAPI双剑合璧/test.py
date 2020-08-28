#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
content = [list('上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。'),
            list('萨哈夫说，伊拉克将同联合国销毁伊拉克大规模杀伤性武器特别委员会继续保持合作。')]

print(content)

data_bin = {'"model_name': 'tre', 'input': content}
good = requests.post('http://111.229.217.153:80/ner', json=data_bin).json()
print(good)