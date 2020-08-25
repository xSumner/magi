from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': '你已经正确创建 FastApi 服务！'}

@app.get('/query/{uid}')
def query(uid):
    msg = f'你查询的 uid 为：{uid}'
    return {'success': True, 'msg': msg}