# 对比Flask和FastAPI封装模型接口

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977724968-792b203f-8414-43a5-a566-974d22719a5c.jpeg#align=left&display=inline&height=640&margin=%5Bobject%20Object%5D&originHeight=640&originWidth=1280&size=0&status=done&style=none&width=690)

在现实开发过程中，经常会遇到不同语言之间通讯的问题。例如在一个 Java 编写的大型系统里需要调用一些机器学习模型，但是这些机器学习模型往往是使用 Python 开发的。这时候除了使用 Java 重写一遍之外，更实用的方法是将这个模型封装成 API 供系统进行调用。

本文以一个简单的机器学习模型为例，然后分别使用 Flask 和 FastAPI 将其封装成 API ，并比较两种接口封装方式的性能和开发复杂度。

- 什么是API
- Flask基础入门
- 构建机器学习模型
- 保存机器学习模型：序列化和反序列化
- 用Flask为模型创建API
- 在Postman中测试API



## Flask基础入门

要入门Flask，首先我们得知道什么是Web服务。Web服务是API的一种形式，它假定API通过服务器托管，并且可以被调用。Web API/Web Service——这些术语通常可以互换使用。

Flask是一个用Python编写的轻量级Web服务框架，当然，它不是Python中的唯一框架，同类竞品还有Django、Falcon、Hug等。但本文只介绍如何用Flask创建API。

如果你下载了Anaconda版，里面就已经包含了Flask。如果你想用pip：

```
pip install flask
```

你会发现它非常小，这也是它深受Python开发人员喜爱的一个原因。而另一个原因就是Flask框架附带内置的轻量级Web服务器，需要的配置少，而且可以用Python代码直接控制。

下面的代码很好地展示了Flask的简约性。它创建一个简单的Web-API，在接收到特定URL时会生成一个特定的输出。

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

if __name__ == '__main__':
    app.run(debug=True)
```
运行后，你可以在终端浏览器中输入这个网址，然后观察结果。

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977724951-bc17732b-472f-4fbf-aab0-d5837d51272b.jpeg#align=left&display=inline&height=145&margin=%5Bobject%20Object%5D&originHeight=145&originWidth=328&size=0&status=done&style=none&width=328)

**一些要点**

- Jupyter Notebook非常适合处理有关Python、R和markdown的东西。但一旦涉及构建web服务器，它就会出现很多奇怪的bug。所以建议大家最好在Sublime等文本编辑器里编写Flask代码，并从终端/命令提示符运行代码。
- 千万不要把文件命名为flask.py。
- 默认情况下，运行Flask的端口号是5000。有时服务器能在这个端口上正常启动，但有时，如果你是在Web浏览器或任何API客户端（如Postman）中用URL启动，它可能会报错，比如下图：

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977725005-7dbc65da-37d2-4f9e-bcce-a1cfbe747685.jpeg#align=left&display=inline&height=72&margin=%5Bobject%20Object%5D&originHeight=72&originWidth=516&size=0&status=done&style=none&width=516)

- 根据Flask的提示，这时服务器已经在端口5000上成功启动了，但是当在浏览器中用URL启动时，它没有输出任何内容。因此，这可能是端口号冲突了。在这种情况下，我们可以把默认端口号5000改成所需的端口号，只需输入`app.run(debug=True,port=12345)`。
- 输入以上代码后，Flask服务器将如下所示：

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977725030-6277c365-1388-438f-acee-a4453fa8324e.jpeg#align=left&display=inline&height=61&margin=%5Bobject%20Object%5D&originHeight=61&originWidth=486&size=0&status=done&style=none&width=486)

现在我们来看看输入的代码：

- 创建Flask实例后，Python会自动生成一个name变量。如果这个文件是作为脚本直接用Python运行的，那么这个变量将为“main”；如果是导入文件，那么“name” 的值将是你导入文件的名称。例如，如果你有`test.py`和`run.py`，并且将`test.py`导入`run.py`，那么`test.py`的“name”值就会是test `(app = Flask(test))`。
- 关于上面`hello()`的定义，可以用[@app](https://link.zhihu.com/?target=https%3A//github.com/app).route(“/“)。同时，装饰器`route()`可以告诉Flask什么URL可以触发定义好的`hello()`。
- `hello()`的作用是在使用API时生成输出。在这种情况下，在Web浏览器转到`localhost:5000/`会产生预期的输出（假设是默认端口）。


如果我们想为机器学习模型创建API，下面是一些需要牢记的东西。

## 构建机器学习模型

这里我们使用泰坦尼克号数据集作为构建一个分类的机器学习模型。模型的任务是根据表格数据预测乘客的生存概率，为了简化只用四个变量：

- age（年龄）
- sex（性别）
- embarked（登船港口：C=Cherbourg, Q=Queenstown, S=Southampton）
- survived（类别标签）

```python
# Import dependencies
import pandas as pd
import numpy as np
# Load the dataset in a dataframe object and include only four features as mentioned
url = r"D:\git_project\mpi\data\titanic\train.csv"
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df_ = df[include]
```

“Sex”和“Embarked”是非数字的分类特征，我们需要对它们进行编码；“age”这个特征有不少缺失值，这点可以汇总统计后用中位数或平均数来填充；Scikit-learn不能识别NaN，所以我们还要为此编写一个辅助函数：

```python
categoricals = []
for col, col_type in df_.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df_[col].fillna(0, inplace=True)
```

上面的代码是为数据集填补缺失值。这里需要注意一点，缺失值对模型性能其实很重要，尤其是当空值过多时，我们用单个值填充要非常谨慎，不然很可能会导致很大的偏差。在这个数据集里，因为有缺失值的列是age，所以我们不应该用0填充NaN。

至于把非数字特征转成数字行驶，你可以用One Hot Encoding，也可以用Pandas提供的`get_dummies()`：

```python
df_ohe = pd.get_dummies(df_, 
                        columns=categoricals, 
                        dummy_na=True)
```

现在我们已经完成了预处理，可以准备训练机器学习模型了：选择Logistic回归分类器。

```python
from sklearn.linear_model import LogisticRegression
dependent_variable = 'Survived'
x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
lr = LogisticRegression()
lr.fit(x, y)
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False)
```

有了模型，之后就是保存模型。从技术上讲这里我们应该对模型做序列化，在Python里，这个操作被称为Pickling。

## 保存机器学习模型：序列化和反序列化

调用sklearn的`joblib`：

```python
from sklearn.externals import joblib
joblib.dump(lr, 'model.pkl')
['model.pkl']
```

Logistic回归模型现在保持不变，我们可以用一行代码把它加载到内存中，而把模型加载回工作区的操作就是反序列化。

```python
lr = joblib.load('model.pkl')
```

## 用Flask为模型创建API

要用Flask为模型创建服务器，我们要做两件事：

- 当APP启动时把已经存在的模型加载到内存中。
- 创建一个API断电，它接受输入变量，将它们转换为适当的格式，并返回预测。


更具体地说，当你输入以下内容时：
```python
[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": '"female"', "Embarked": "C"},
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}
]
```

你希望API的输出会是：

```python
{"prediction": [0, 1, 1, 0]}
```

其中0表示遇难，1表示幸存。这里输入格式是JSON，它是最广泛使用的数据交换格式之一。

要做到上述效果，我们需要先编写一个函数`predict()`，它的目标如前所述：

- 当APP启动时把已经存在的模型加载到内存中。
- 创建一个API断电，它接受输入变量，将它们转换为适当的格式，并返回预测。


我们已经演示了如何加载已有模型，之后是根据接收的输入预测人员生存状态：

```python
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     prediction = lr.predict(query)
     return jsonify({'prediction': list(prediction)})
```

虽然看起来挺简单，但你可能会在这个步骤遇到一个小问题。

为了让你编写的函数能正常运行，传入请求中必需包含这四个分类变量的所有可能值，这些值可能是实时的，也可能不是。如果传入请求里出现必要值缺失，那么根据当前方法定义的`predict()`生成的数据列会比分类器里少，模型就会报错。

要解决这个问题，我们需要在模型训练期间把列保留下来，把任何Python对象序列化为.pkl文件。

```python
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
['model_columns.pkl']
```

由于已经保留了列列表，所以你可以在预测时处理缺失值（记得在APP启动前加载模型）：

```python
@app.route('/predict', methods=['POST']) # Your API endpoint URL would consist /predict
def predict():
    if lr:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = list(lr.predict(query))
            return jsonify({'prediction': prediction})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
```

你已经在“/ predict”API中包含了所有必需元素，现在你只需要编写主类：

```python
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line argument
    except:
        port = 12345 # If you don't provide any port then the port will be set to 12345
    lr = joblib.load(model_file_name) # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load(model_columns_file_name) # Load "model_columns.pkl"
    print ('Model columns loaded')
    app.run(port=port, debug=True)
```

现在，这个API就全部完成可以托管了。

当然，如果你想把Logistic回归模型代码和Flask API代码分离为单独的.py文件，这其实是一种很好的编程习惯。那么你的`model.py`代码应该如下所示：

```python
# Import dependencies
import pandas as pd
import numpy as np
# Load the dataset in a dataframe object and include only four features as mentioned
url = r"D:\git_project\mpi\data\titanic\train.csv"
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df_ = df[include]
# Data Preprocessing
categoricals = []
for col, col_type in df_.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df_[col].fillna(0, inplace=True)
df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)
# Logistic Regression classifier
from sklearn.linear_model import LogisticRegression
dependent_variable = 'Survived'
x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
lr = LogisticRegression()
lr.fit(x, y)
# Save your model
from sklearn.externals import joblib
joblib.dump(lr, 'model.pkl')
print("Model dumped!")
# Load the model that you just saved
lr = joblib.load('model.pkl')
# Saving the data columns from training
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
```

而`api.py`则是：

```python
# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
# Your API definition
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = list(lr.predict(query))
            return jsonify({'prediction': str(prediction)})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345
    lr = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')
    app.run(port=port, debug=True)
```

现在，你可以在名为Postman的API客户端中测试此API 。只要确保model.py与api.py在同一个目录下，并确保两者都已在测试前编译好了，如下图所示：

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977725061-018a4aea-35fb-4d13-b7e7-940e650bbe0a.jpeg#align=left&display=inline&height=321&margin=%5Bobject%20Object%5D&originHeight=321&originWidth=640&size=0&status=done&style=none&width=640)

如果所有文件都已成功编译，目录结构应该如下图所示：

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977724977-e0426df9-f06e-4e6a-a2bf-31c10f3d1536.jpeg#align=left&display=inline&height=109&margin=%5Bobject%20Object%5D&originHeight=109&originWidth=567&size=0&status=done&style=none&width=567)

_注：IPYNB文件是可选的。_


## 用 FastAPI 为模型创建API







## 在Postman中测试API

Postman是测试API最好用的工具之一。如果你下载了最新版本，它的界面应该如下所示：

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977725000-f3523a12-b6d2-468d-bd56-fa9835407ee8.jpeg#align=left&display=inline&height=793&margin=%5Bobject%20Object%5D&originHeight=447&originWidth=720&size=0&status=done&style=none&width=1278)

成功启动Flask服务器后，你需要在Postman中输入包含正确端口号的正确URL：

![](https://cdn.nlark.com/yuque/0/2020/jpeg/772088/1587977725034-149dadb9-e732-4e6c-8aec-06c0c8ffb5fd.jpeg#align=left&display=inline&height=482&margin=%5Bobject%20Object%5D&originHeight=270&originWidth=720&size=0&status=done&style=none&width=1286)

恭喜！你刚刚构建了第一个机器学习API。这是个可以根据泰坦尼克号乘客age、sex和embarked信息预测他们生存状态的API，现在，你的朋友就能用前端代码调用它，输出神奇的结果。

