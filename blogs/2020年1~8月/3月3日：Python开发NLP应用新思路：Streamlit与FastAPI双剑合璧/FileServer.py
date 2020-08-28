#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from fastapi import FastAPI
from starlette.responses import FileResponse


@app.get('/record/{filename}')
def get_record(filename: str):
    path = os.path.join('output', filename)
    if not os.path.exists(path):
        return {'success': False, 'msg': '文件不存在！'}
    response = FileResponse(path)
    return response