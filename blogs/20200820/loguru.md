### 使用loguru记录日志

#### 安装：

```
pip install loguru
```

#### 基本使用：

```python
from loguru import logger

logger.debug('this is a debug message')
```

不需要进行配置，直接引入一个 `logger` ，然后调用其 `debug` 方法即可。

在 `loguru` 里面有且仅有一个主要对象，那就是 `logger` ，`loguru` 里面有且仅有一个 `logger` ，而且它已经被提前配置了一些基础信息，比如比较友好的格式化、文本颜色信息等。

以上的日志信息是直接输出到控制台的，并没有输出到其他的地方，如果想要输出到其他的位置，比如存为文件，我们只需要使用一行代码声明即可。

例如将结果同时输出到一个 `runtime.log` 文件里面，可以这么写：

```python
from loguru import logger

logger.add('runtime.log')
logger.debug('this is a debug')
```

不需要再声明一个 `FileHandler` 了，就一行 `add` 语句搞定，运行之后会发现目录下 `runtime.log` 里面同样出现了刚刚控制台输出的 `DEBUG` 信息。

```
2020-08-18 15:38:07.571 | DEBUG    | __main__:<module>:1 - this is a debug mesage
```

#### 详细使用：

既然是日志，那么最常见的就是输出到文件了。`loguru` 对输出到文件的配置有非常强大的支持，比如支持输出到多个文件，分级别分别输出，过大创建新文件，过久自动删除等等。

下面我们分别看看这些怎样来实现，这里基本上就是 `add` 方法的使用介绍。因为这个 `add` 方法就相当于给 `logger` 添加了一个 `Handler`，它给我们暴露了许多参数来实现 `Handler` 的配置，下面我们来详细介绍下。

首先看看它的方法定义吧：

```python
def add(
    self,
    sink,
    *,
    level=_defaults.LOGURU_LEVEL,
    format=_defaults.LOGURU_FORMAT,
    filter=_defaults.LOGURU_FILTER,
    colorize=_defaults.LOGURU_COLORIZE,
    serialize=_defaults.LOGURU_SERIALIZE,
    backtrace=_defaults.LOGURU_BACKTRACE,
    diagnose=_defaults.LOGURU_DIAGNOSE,
    enqueue=_defaults.LOGURU_ENQUEUE,
    catch=_defaults.LOGURU_CATCH,
    **kwargs
):
    r"""Add a handler sending log messages to a sink adequately configured.
```

看看它的源代码，它支持这么多的参数，如 `level`、`format`、`filter`、`color` 等等，另外我们还注意到它有个非常重要的参数 `sink`，我们看看官方文档：[sink](https://loguru.readthedocs.io/en/stable/api/logger.html#sink)，可以了解到通过 `sink` 我们可以传入多种不同的数据结构，汇总如下：

- `sink` 可以传入一个 `file` 对象，例如 `sys.stderr` 或者 `open('file.log', 'w')` 都可以。
- `sink` 可以直接传入一个 `str` 字符串或者 `pathlib.Path` 对象，其实就是代表文件路径的，如果识别到是这种类型，它会自动创建对应路径的日志文件并将日志输出进去。
- `sink` 可以是一个方法，可以自行定义输出实现。
- `sink` 可以是一个 `logging` 模块的 `Handler`，比如 `FileHandler`、`StreamHandler` 等等，或者上文中我们提到的 `CMRESHandler` 照样也是可以的，这样就可以实现自定义 `Handler` 的配置。
- `sink` 还可以是一个自定义的类，具体的实现规范可以参见官方文档。

所以说，刚才我们所演示的输出到文件，仅仅给它传了一个 `str` 字符串路径，他就给我们创建了一个日志文件，就是这个原理。

#### 基本参数

下面我们再了解下它的其他参数，例如 `format`、`filter`、`level` 等等。

其实它们的概念和格式和 `logging` 模块都是基本一样的了，例如这里使用`format`、`filter`、`level`来规定输出的格式：

```python
logger.add('runtime.log', format="{time} {level} {message}", filter="my_module", level="INFO")
```

#### 删除 sink

另外添加 `sink` 之后我们也可以对其进行删除，相当于重新刷新并写入新的内容。

删除的时候根据刚刚 `add` 方法返回的 `id` 进行删除即可，看下面的例子：

```python
from loguru import logger
 
trace = logger.add('runtime.log')
logger.debug('this is a debug message')
logger.remove(trace)
logger.debug('this is another debug message')
```

看这里，我们首先 `add` 了一个 `sink`，然后获取它的返回值，赋值为 `trace`。随后输出了一条日志，然后将 `trace` 变量传给`remove` 方法，再次输出一条日志，看看结果是怎样的。

控制台输出如下：

```
2019-11-06 23:03:24.368 | DEBUG    | __main__:<module>:4 - this is a debug message
2019-11-06 23:03:24.369 | DEBUG    | __main__:<module>:6 - this is another debug message
```

日志文件 `runtime.log` 内容如下：

```
cat runtime.log
2019-11-06 23:03:24.368 | DEBUG    | __main__:<module>:4 - this is a debug message
```

可以发现，在调用 `remove` 方法之后，确实将历史 `log` 删除了。

这样我们就可以实现日志的刷新重新写入操作。

#### rotation 配置

用了 `loguru` 我们还可以非常方便地使用`rotation` 配置，比如我们想一天输出一个日志文件，或者文件太大了自动分隔日志文件，我们可以直接使用 `add` 方法的 `rotation` 参数进行配置。

我们看看下面的例子：

```python
logger.add('runtime_{time}.log', rotation="500 MB")
```

通过这样的配置我们就可以实现每 500MB 存储一个文件，每个 log 文件过大就会新创建一个 log 文件。我们在配置 log 名字时加上了一个 `time` 占位符，这样在生成时可以自动将时间替换进去，生成一个文件名包含时间的 log 文件。

另外我们也可以使用 `rotation` 参数实现定时创建 log 文件，例如：

```python
logger.add('runtime_{time}.log', rotation='00:00')
```

这样就可以实现每天 0 点新创建一个 log 文件输出了。

另外我们也可以配置 log 文件的循环时间，比如每隔一周创建一个 log 文件，写法如下：

```python
logger.add('runtime_{time}.log', rotation='1 week')
```

这样我们就可以实现一周创建一个 log 文件了。

```python
- an |int| which corresponds to the maximum file size in bytes before that the current
  logged file is closed and a new one started over.
- a |timedelta| which indicates the frequency of each new rotation.
- a |time| which specifies the hour when the daily rotation should occur.
- a |str| for human-friendly parametrization of one of the previously enumerated types.
  Examples: ``"100 MB"``, ``"0.5 GB"``, ``"1 month 2 weeks"``, ``"4 days"``, ``"10h"``,
  ``"monthly"``, ``"18:00"``, ``"sunday"``, ``"w0"``, ``"monday at 12:00"``, ...
- a |function|_ which will be called before logging. It should accept two
  arguments: the logged message and the file object, and it should return ``True`` if
  the rotation should happen now, ``False`` otherwise.
```

#### retention 配置

很多情况下，一些非常久远的 log 对我们来说并没有什么用处了，它白白占据了一些存储空间，不清除掉就会非常浪费。`retention` 这个参数可以配置日志的最长保留时间。

比如我们想要设置日志文件最长保留 10 天，可以这么来配置：

```python
logger.add('runtime.log', retention='10 days')
```

这样 log 文件里面就会保留最新 10 天的 log，妈妈再也不用担心 log 沉积的问题啦。

我们看下源码看下这个参数可以设置为哪些值:

```python
- an |int| which indicates the number of log files to keep, while older files are removed.
- a |timedelta| which specifies the maximum age of files to keep.
- a |str| for human-friendly parametrization of the maximum age of files to keep.
  Examples: ``"1 week, 3 days"``, ``"2 months"``, ...
- a |function|_ which will be called before the retention process. It should accept the list
  of log files as argument and process to whatever it wants (moving files, removing them,
  etc.).
```

#### compression 配置

`loguru` 还可以配置文件的压缩格式，比如使用 `zip` 文件格式保存，示例如下：

```python
logger.add('runtime.log', compression='zip')
```

这样可以更加节省存储空间。

我们看下源码看下这个参数可以设置为哪些值:

```python
- a |str| which corresponds to the compressed or archived file extension. This can be one
  of: ``"gz"``, ``"bz2"``, ``"xz"``, ``"lzma"``, ``"tar"``, ``"tar.gz"``, ``"tar.bz2"``,
  ``"tar.xz"``, ``"zip"``.
- a |function|_ which will be called before file termination. It should accept the path
  of the log file as argument and process to whatever it wants (custom compression,
  network sending, removing it, etc.).
```

#### enqueue配置

`loguru`可以配置在多进程同时往日志文件写日志的时候使用队列达到异步功效。

```python
logger.add("somefile.log", enqueue=True)  # 异步写入
```

看下源码的解释:

```python
enqueue : |bool|, optional
    Whether the messages to be logged should first pass through a multiprocess-safe queue
    before reaching the sink. This is useful while logging to a file through multiple
    processes.
```

#### 字符串格式化

`loguru` 在输出 log 的时候还提供了非常友好的字符串格式化功能，像这样：

```python
logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
```

这样在添加参数就非常方便了。

#### Traceback 记录

在很多情况下，如果遇到运行错误，而我们在打印输出 log 的时候万一不小心没有配置好 Traceback 的输出，很有可能我们就没法追踪错误所在了。

但用了 loguru 之后，我们用它提供的装饰器就可以直接进行 Traceback 的记录，类似这样的配置即可：

```python
@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)
```

我们做个测试，我们在调用时三个参数都传入 0，直接引发除以 0 的错误，看看会出现什么情况：

```python
my_function(0, 0, 0)
```

运行完毕之后，可以发现 log 里面就出现了 Traceback 信息，而且给我们输出了当时的变量值，真的是不能再赞了！结果如下：

```python
> File "run.py", line 15, in <module>
    my_function(0, 0, 0)
    └ <function my_function at 0x1171dd510>
 
  File "/private/var/py/logurutest/demo5.py", line 13, in my_function
    return 1 / (x + y + z)
                │   │   └ 0
                │   └ 0
                └ 0
 
ZeroDivisionError: division by zero
```

因此，用 loguru 可以非常方便地实现日志追踪，debug 效率可能要高上十倍了？

```python
class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Retrieve context where the logging call occurred, this happens to be in the 6th frame upward
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=0)
```



### Python编程：loguru管理日志输出

#### 输出日志

```python
from loguru import logger

logger.debug("这是一条debug日志")
```

#### 输出到文件

```python
from loguru import logger

logger.add("file_{time}.log")

logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
```

#### 日志规则

```python
from loguru import logger

logger.add("file.log", format="{time} {level} {message}", filter="", level="INFO")

logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
```

输出：

```
2019-03-14T20:01:25.392454+0800 INFO 这是一条info日志
```

#### 日志文件

文件管理方式

```python
logger.add("file_1.log", rotation="500 MB")    # 文件过大就会重新生成一个文件
logger.add("file_2.log", rotation="12:00")     # 每天12点创建新文件
logger.add("file_3.log", rotation="1 week")    # 文件时间过长就会创建新文件

logger.add("file_X.log", retention="10 days")  # 一段时间后会清空

logger.add("file_Y.log", compression="zip")    # 保存zip格式
```

#### 其他参数

```python
logger.add("somefile.log", enqueue=True)  # 异步写入

logger.add("somefile.log", serialize=True)  # 序列化为json
```

#### 时间格式化

```python
logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
```

配合notifiers模块
github： https://github.com/notifiers/notifiers
文档：https://notifiers.readthedocs.io/en/latest/

#### 在工程中创建多个文件处理器对象并解决中文乱码问题

```python
# coding=utf-8
import os
import sys
from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_file_path = os.path.join(BASE_DIR, 'Log/my.log')
err_log_file_path = os.path.join(BASE_DIR, 'Log/err.log')

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
# logger.add(s)
logger.add(log_file_path, rotation="500 MB", encoding='utf-8')  # Automatically rotate too big file
logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8',
           level='ERROR')  # Automatically rotate too big file
logger.debug("That's it, beautiful and simple logging!")
logger.debug("中文日志可以不")
logger.error("严重错误")
```



### 更优美的python日志管理库Loguru

#### Loguru 简介

**Loguru**的主旨就是让程序员能方便优美的实现日志记录。您还记得配置记录器的繁琐过程吗？因为对此感到厌烦？让我们看看以前python日志记录器的创建过程吧。

```python
import logging

#创建日志级别
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#创建日志文件
handler_warn = logging.FileHandler('warning_log.txt')
handler_warn.setLevel(logging.INFO)

#定义日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_warn.setFormatter(formatter)

#将日志处理程序记录到记录器
logger.addHandler(handler_warn)
```

以上还是最简单的配置过程，是否感到很繁琐。确实如此，但是记录是每个应用程序的基础，并简化了调试过程。使用**Loguru，**您没有理由不从一开始就使用日志记录，这很简单。只需要引入loguru库即可，而且loguru的性能也非常好，因为Loguru的关键功能将以C语言实现，以实现最高速度。

```python
from loguru import logger
```

另外，该库旨在通过添加一堆有用的功能来减轻Python日志记录的痛苦，这些功能可以解决标准记录器的问题。在您的应用程序中使用日志应该是自动的，**Loguru**试图使其变得既愉快又强大。

#### Loguru 安装

```python
pip install loguru
```

#### Loguru 使用

##### 1、简单使用

```python
from loguru import logger

logger.debug("That's it, beautiful and simple logging!")
```

结果显示彩色，非常的优美。

##### 2、日志格式

根据自己的需求配置日志格式，也非常简单，只需要简单配置即可完成。如下：

```python
import sys
from loguru import logger

#配置日志格式
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

logger.info("That's it, beautiful and simple logging!")
logger.debug("That's debug")
logger.warning("That's warning")
```

结果，不同的颜色显示：

##### 3、日志文件

如果要将记录的消息保存到文件，则只需使用字符串路径作为接收器。配置如下：

```python
logger.add("file_{time}.log")
```

如果需要设置日志文件大小、删除较旧的日志文件或希望在关闭时压缩文件，并设置压缩格式，这些都可以进行配置，而且配置起来非常简单。如下：

```python
#rotation参数
logger.add("file_1.log", rotation="500 MB")    # 设置日志文件大小
logger.add("file_2.log", rotation="12:00")     # 中午12点创建日志文件
logger.add("file_3.log", rotation="1 week")    # 一周创建一个日志文件

#retention参数
logger.add("file_X.log", retention="10 days")  # 日志文件最长保留 10 天

#compression参数
logger.add("file_Y.log", compression="zip")    # 日志文件压缩格式为ZIP
```

##### 4、字符串格式化

Loguru倾向于使用更优雅，更强大的`{}`格式`%`，日志记录功能实际上等效于`str.format()`。

```python
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
```

##### 5、Traceback捕获

您是否曾经看到程序意外崩溃而没有在日志文件中看到任何内容？您是否注意到没有记录线程中发生的异常？这可以使用`catch()`装饰器/上下文管理器解决，该管理器可以确保将任何错误信息正确保存到`logger`中。配置如下：

```python
import sys
from loguru import logger

@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

my_function(1,-1,0)
```

##### 6、色彩斑斓的日志

如果您的终端兼容，Loguru会自动为日志添加颜色。您可以通过使用接收器格式来自定义自己喜欢的样式。配置方式如下：

```python
logger.add(sys.stderr, colorize=True, format="<green>{time}</green> <level>{message}</level>",level="DEBUG")
```

结果，DEBUG及以上的信息或被自定义显示样式。

##### 7、异步写入日志

`logger`默认情况下，添加到的所有接收器都是线程安全的。它们不是多进程安全的，但是您可以`enqueue`通过消息来确保日志的完整性。如果要异步记录，也可以使用相同的参数。

```python
logger.add("somefile.log", enqueue=True)
```

##### 8、序列化日志

希望对日志进行序列化以便于解析或传递日志？使用该`serialize`参数，每条日志消息在发送到已配置的接收器之前将转换为JSON字符串。

```python
logger.add(custom_sink_function, serialize=True)
```

##### 9、配置日期格式

```python
logger.add(sys.stderr, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",level="DEBUG")

logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
logger.debug("That's debug")
logger.warning("That's warning")
```

##### 10、配置编码格式

```
logger.add(log_file_path, rotation="500 MB", encoding='utf8')
```

还有更多的配置方法，详细请参考官方文档。

[文档](https://loguru.readthedocs.io/en/stable/overview.html)

[官方github](https://github.com/Delgan/loguru)



### Flask中的 logging 使用

#### 一、日志等级说明

- **等级：** **DEBUG < INFO < WARNING < ERROR < CRITICAL**
- **DEBUG ：** 最详细的日志信息，主要的应用场景问题的诊断，只限于开发人员使用的，用来在开发过程中进行调试
- **INFO ：** 详细程度仅次于debug模式，主要来记录关键节点的信息，确定程序是否正常如预期完成，一般的使用场景是重要的业务处理已经结束，我们通过这些INFO级别的日志信息，可以很快的了解应用正在做什么。
- **WARNING ：** 当某些不被期望的事情发生的时候，需要记录的信息，比如磁盘即将存满，注意当前的程序一依旧可以正常运行，不报错。也就是说发生这个级别的问题时，处理过程可以继续，但必须要对这个问题给予额外的关注。
- **ERROR ：** 出现严重问题，导致某些功能不能正常运行记录信息
- **CRITICAL：** 系统即将崩溃或者已经崩溃

#### 二、应用实例

###### 2.1 简单使用demo

```python
from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def root():
    app.logger.info('info log')
    app.logger.warning('warning log')
    return 'hello'

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log')
    app.logger.addHandler(handler)
    app.run()
```

###### 2.2 自定义设置打印格式（2+）

```python
import logging.handlers

handler = logging.FileHandler('flask.log', encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)
```

```python
import logging
from logging.handlers import RotatingFileHandler

# 默认日志等级的设置
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
file_log_handler = RotatingFileHandler('WarningLogs.log', maxBytes=1024 * 1024, backupCount=10)
# 设置日志的格式                   发生时间    日志等级     日志信息文件名      函数名          行数        日志信息
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 日志等级的设置
# file_log_handler.setLevel(logging.WARNING)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)
```

```python
# 测试
app.logger.info('info log')
app.logger.debug('debug log')
app.logger.warning('warning log')
app.logger.error('error log')
app.logger.critical('critical')
```

###### 2.3 自定义文件和格式设置

```python
import os
import logging
import time
from logging.handlers import RotatingFileHandler

# log配置，实现日志自动按日期生成日志文件
def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)

log_dir_name = "Logs"
log_file_name = 'logs-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
log_file_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
make_dir(log_file_folder)
log_file_str = log_file_folder + os.sep + log_file_name

# 默认日志等级的设置
logging.basicConfig(level=logging.WARNING)
# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
file_log_handler = RotatingFileHandler(log_file_str, maxBytes=1024 * 1024, backupCount=10)
# 设置日志的格式                   发生时间    日志等级     日志信息文件名      函数名          行数        日志信息
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 日志等级的设置
# file_log_handler.setLevel(logging.WARNING)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)
```

#### 三、使用体验

简单讲，logging的使用就是三个步骤：

- 创建记录器
- 日志的格式、等级设置
- 添加记录器

#### 四、日志记录等级设置

如果是使用 **logging.basicConfig(level=logging.DEBUG)** 设置的话，那么使用 **app.logger** 打印的日志仍会不分等级均记录，而 **系统运行日志** 才会按照设置的等级进行记录。

使用 **file_log_handler.setLevel(logging.WARNING)** 设置等级的话，那么不管是 **app.logger** 打印的日志 还是 **系统运行日志** 均按照设置等级进行记录。

#### 五、日志格式的常用参数说明

| 参数                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| %(name)s            | Logger的名字                                                 |
| %(levelno)s         | 数字形式的日志级别                                           |
| %(levelname)s       | 文本形式的日志级别                                           |
| %(pathname)s        | 调用日志输出函数的模块的完整路径名，可能没有                 |
| %(filename)s        | 调用日志输出函数的模块的文件名                               |
| %(module)s          | 调用日志输出函数的模块名                                     |
| %(funcName)s        | 调用日志输出函数的函数名                                     |
| %(lineno)d          | 调用日志输出函数的语句所在的代码行                           |
| %(created)f         | 当前时间，用UNIX标准的表示时间的浮 点数表示                  |
| %(relativeCreated)d | 输出日志信息时的，自Logger创建以 来的毫秒数                  |
| %(asctime)s         | 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒 |
| %(thread)d          | 线程ID。可能没有                                             |
| %(threadName)s      | 线程名。可能没有                                             |
| %(process)d         | 进程ID。可能没有                                             |
| %(message)s         | 用户输出的消息                                               |

------

参考文章：

【1】[Flask-log,日志](https://blog.csdn.net/weixin_43158056/article/details/95163598)
【2】[如何优雅的在flask中记录log](https://segmentfault.com/a/1190000018087099)
【3】[python web开发-flask中日志的使用](https://www.cnblogs.com/itxb/p/8635056.html)
【4】[Flask使用日志记录到文件示例](https://www.bbsmax.com/A/QW5YLRBBJm/)
【5】[flask 日志集成](https://blog.csdn.net/m0_37392631/article/details/84968416)
【6】[Logging — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/master/logging/)
【7】[logging.config — Logging configuration — Python 3.7.5rc1 documentation](https://docs.python.org/3/library/logging.config.html?highlight=logging)
【8】[logging — Logging facility for Python — Python 3.7.5rc1 documentation](https://docs.python.org/3/library/logging.html#logger-objects)



































