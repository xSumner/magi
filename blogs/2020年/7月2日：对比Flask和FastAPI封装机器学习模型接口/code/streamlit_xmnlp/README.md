演示项目共有三个文件：

- backend.py：使用FastAPI封装XMNLP的后端代码；
- frontend.py：使用Streamlit封装的前端代码；
- for_test.py：使用requests调用的测试代码。

将以上环境使用Docker打包后，在服务器上运行成功。

后端启动命令：

```shell
uvicorn backend:app --reload --host 0.0.0.0 --port 80
```

前端启动命令：

```shell
streamlit run frontend.py
```

