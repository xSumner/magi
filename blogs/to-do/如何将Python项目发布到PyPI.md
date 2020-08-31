# [如何将Python项目发布到PyPI](https://www.cnblogs.com/hiyang/p/12631931.html)

The Python Package Index (PyPI) is a repository of software for the Python programming language.

如何打包可以参考[官方文档](https://packaging.python.org/tutorials/packaging-projects/)，如果看英文比较费劲，参考这个[译文](https://www.osgeo.cn/python-packaging/overview.html)。也可以参考官方提供的[例子](https://github.com/pypa/sampleproject)。

## 创建项目

目录结构

```text
复制├── LICENSE.txt
├── MANIFEST.in
├── README.md
├── pyproject.toml
├── setup.cfg
├── setup.py
└── app
	├── __init__.py
	└── app.py
```

接下来我们来逐一编写除了代码以外的文件。

1. README.md

   是关于项目的描述文件，一般包含怎样安装项目，怎样使用项目等。markdown 语法可以参考 [adam-p/markdown-here](https://link.zhihu.com/?target=https%3A//github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)。

2. LICENSE.txt

   开源License，如MIT，Apache license 2.0等。关于项目用什么License，可参考 [Choose an open source license](https://link.zhihu.com/?target=https%3A//choosealicense.com/)

3. setup.cfg

   一个配置信息文件，运行setup.py程序打包的时候会用到里面的配置，作为setup.py的命令行参数。内容如下

   ```text
   [metadata]
   # This includes the license file(s) in the wheel.
   # https://wheel.readthedocs.io/en/stable/user_guide.html#including-license-files-in-the-generated-wheel-file
   license_files = LICENSE.txt
   desciption-file = README.md
   
   [bdist_wheel]
   # This flag says to generate wheels that support both Python 2 and Python
   # 3. If your code will not run unchanged on both Python 2 and 3, you will
   # need to generate separate wheels for each Python version that you
   # support. Removing this line (or setting universal to 0) will prevent
   # bdist_wheel from trying to make a universal wheel. For more see:
   # https://packaging.python.org/guides/distributing-packages-using-setuptools/#wheels
   universal=1
   ```

   关于setup.cfg更详细的信息，可参考 [Building and Distributing Packages with Setuptools](https://link.zhihu.com/?target=https%3A//setuptools.readthedocs.io/en/latest/setuptools.html%23configuring-setup-using-setup-cfg-files)。

4. setup.py

   用来描述项目，打包的时候会用到这个文件。它告诉PyPI我们的项目叫什么名字，是什么版本，依赖哪些库，支持哪些操作系统，可以在哪些版本的Python上运行，等等

   ```python
   """A setuptools based setup module.
   See:
   https://packaging.python.org/guides/distributing-packages-using-setuptools/
   https://github.com/pypa/sampleproject
   """
   import setuptools
   import os
   
   CUR_DIR = os.path.abspath(os.path.dirname(__file__))
   README = os.path.join(CUR_DIR, "README.md")
   with open("README.md", "r") as fd:
       long_description = fd.read()
   
   # Arguments marked as "Required" below must be included for upload to PyPI.
   # Fields marked as "Optional" may be commented out.
   
   setuptools.setup(
       # This is the name of your project. The first time you publish this
       # package, this name will be registered for you. It will determine how
       # users can install this project, e.g.:
       #
       # $ pip install sampleproject
       #
       # And where it will live on PyPI: https://pypi.org/project/sampleproject/
       #
       # There are some restrictions on what makes a valid project name
       # specification here:
       # https://packaging.python.org/specifications/core-metadata/#name
       # Required
       name = "tobe",
   
       # Versions should comply with PEP 440:
       # https://www.python.org/dev/peps/pep-0440/
       #
       # For a discussion on single-sourcing the version across setup.py and the
       # project code, see
       # https://packaging.python.org/en/latest/single_source_version.html
       # Required
       version = "0.1.2",
   
       # This is a one-line description or tagline of what your project does. This
       # corresponds to the "Summary" metadata field:
       # https://packaging.python.org/specifications/core-metadata/#summary
       # Optional
       description="A small ssh display tool",
   
       # This is an optional longer description of your project that represents
       # the body of text which users will see when they visit PyPI.
       #
       # Often, this is the same as your README, so you can just read it in from
       # that file directly (as we have already done above)
       #
       # This field corresponds to the "Description" metadata field:
       # https://packaging.python.org/specifications/core-metadata/#description-optional
       # Optional
       long_description=long_description,
   
       # Denotes that our long_description is in Markdown; valid values are
       # text/plain, text/x-rst, and text/markdown
       #
       # Optional if long_description is written in reStructuredText (rst) but
       # required for plain-text or Markdown; if unspecified, "applications should
       # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
       # fall back to text/plain if it is not valid rst" (see link below)
       #
       # This field corresponds to the "Description-Content-Type" metadata field:
       # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
       # Optional
       long_description_content_type="text/markdown",
   
       # This should be a valid link to your project's main homepage.
       #
       # This field corresponds to the "Home-Page" metadata field:
       # https://packaging.python.org/specifications/core-metadata/#home-page-optional
       # Optional
       url="https://github.com/PoplarYang/tobe",
   
       # This should be your name or the name of the organization which owns the
       # project.
       # Optional
       author="PoplarYang",
   
       # This should be a valid email address corresponding to the author listed
       # above.
       # Optional
       author_email="echohiyang@foxmail.com",
   
       # You can just specify package directories manually here if your project is
       # simple. Or you can use find_packages().
       #
       # Alternatively, if you just want to distribute a single Python file, use
       # the `py_modules` argument instead as follows, which will expect a file
       # called `my_module.py` to exist:
       #
       #   py_modules=["my_module"],
       #
       # Required
       packages = ["tobe"],
       #packages=setuptools.find_packages(),
   
       # This field lists other packages that your project depends on to run.
       # Any package you put here will be installed by pip when your project is
       # installed, so they must be valid existing projects.
       #
       # For an analysis of "install_requires" vs pip's requirements files see:
       # https://packaging.python.org/en/latest/requirements.html
       # Optional
       install_requires = [
           "colorama>=0.4.1"
       ],
   
       # To provide executable scripts, use entry points in preference to the
       # "scripts" keyword. Entry points provide cross-platform support and allow
       # `pip` to create the appropriate form of executable for the target
       # platform.
       #
       # For example, the following would provide a command called `sample` which
       # executes the function `main` from this package when invoked:
       # Optional
       entry_points={
           'console_scripts': [
               'tobe=tobe:main'
           ],
       },
   
       # Specify which Python versions you support. In contrast to the
       # 'Programming Language' classifiers above, 'pip install' will check this
       # and refuse to install the project if the version does not match. If you
       # do not support Python 2, you can simplify this to '>=3.5' or similar, see
       # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
       # Optional
       #python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
   
       # If there are data files included in your packages that need to be
       # installed, specify them here.
       #
       # If using Python 2.6 or earlier, then these have to be included in
       # MANIFEST.in as well.
       #package_data={  # Optional
       #    'sample': ['package_data.dat'],
       #},
   
       # Although 'package_data' is the preferred approach, in some case you may
       # need to place data files outside of your packages. See:
       # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
       #
       # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
       # Optional
       #data_files=[('my_data', ['data/data_file'])],
   
       # Classifiers help users find your project by categorizing it.
       #
       # For a list of valid classifiers, see https://pypi.org/classifiers/
       # Optional
       classifiers=(
           # How mature is this project? Common values are
           #   3 - Alpha
           #   4 - Beta
           #   5 - Production/Stable
           'Development Status :: 3 - Alpha',
   
           # Indicate who your project is intended for
           'Intended Audience :: Developers',
           'Topic :: Software Development :: Build Tools',
   
           # Pick your license as you wish
           'License :: OSI Approved :: MIT License',
   
           # Specify the Python versions you support here. In particular, ensure
           # that you indicate whether you support Python 2, Python 3 or both.
           # These classifiers are *not* checked by 'pip install'. See instead
           # 'python_requires' below.
           'Programming Language :: Python :: 2',
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3',
           'Programming Language :: Python :: 3.5',
           'Programming Language :: Python :: 3.6',
           'Programming Language :: Python :: 3.7',
           'Programming Language :: Python :: 3.8',
           "Programming Language :: Python",
       ),
   
       # This field adds keywords for your project which will appear on the
       # project page. What does your project relate to?
       #
       # Note that this is a string of words separated by whitespace, not a list.
       # Optional
       keywords='ssh linux',
   
       # When your source code is in a subdirectory under the project root, e.g.
       # `src/`, it is necessary to specify the `package_dir` argument.
       # Optional
       #package_dir={'': 'src'},
       # List additional URLs that are relevant to your project as a dict.
       #
       # This field corresponds to the "Project-URL" metadata fields:
       # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
       #
       # Examples listed include a pattern for specifying where the package tracks
       # issues, where the source is hosted, where to say thanks to the package
       # maintainers, and where to support the project financially. The key is
       # what's used to render the link text on PyPI.
       #project_urls={  # Optional
       #    'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
       #    'Funding': 'https://donate.pypi.org',
       #    'Say Thanks!': 'http://saythanks.io/to/example',
       #    'Source': 'https://github.com/pypa/sampleproject/',
       #},
   )
   ```

   - name - 项目的名称
   - version - 项目的版本。需要注意的是，PyPI上只允许一个版本存在，如果后续代码有了任何更改，再次上传需要增加版本号
   - author和author_email - 项目作者的名字和邮件
   - description - 项目的简短描述
   - long_description - 项目的详细描述，会显示在PyPI的项目描述页面。上面的例子里直接用了README.md中的内容做详细描述
   - long_description_content_type - 用于指定long_description的markup类型，上面的例子是markdown
   - url - 项目主页的URL，一般给出代码仓库的链接
   - packages - 指定最终发布的包中要包含的packages。上面的例子中find_packages() 会自动发现项目根目录下所有的packages，当然也可以手动指定package的名字
   - install_requires - 项目依赖哪些库，这些库会在pip install的时候自动安装
   - entry_points - 上面的例子中entry_points用来自动创建脚本，上面的例子在pip install安装成功后会创建tobe这个命令，直接可以在命令行运行，即执行 `tobe:main`
   - classifiers - 其他信息，一般包括项目支持的Python版本，License，支持的操作系统。上面的例子中，我们指定项目只能在Python 3上运行，使用MIT License，不依赖操作系统。关于classifiers的完整列表，可参考 [https://pypi.org/classifiers/](https://link.zhihu.com/?target=https%3A//pypi.org/classifiers/)。

5. MANIFEST.in

   记录需要放在包中的除了代码之外的其他文件。

   ```text
   include pyproject.toml
   
   # Include the README
   include *.md
   
   # Include the license file
   include LICENSE.txt
   
   # Include the data files
   #recursive-include data *
   ```

6. pyproject.toml

   在配置文件中将会有一个`[build-system]`表来存储与构建相关的数据。最初，表中只有一个关键字是有效的和必需的：requires。该键将包含一个字符串列表的值，代表执行构建系统所需的PEP 508依赖.

   ```text
   [build-system]
   # These are the assumed default build requirements from pip:
   # https://pip.pypa.io/en/stable/reference/pip/#pep-517-and-518-support
   requires = ["setuptools>=40.8.0", "wheel"]
   build-backend = "setuptools.build_meta"
   ```

## 打包项目

1. 打包项目需要用到setuptools和wheel，先安装这两个库

```bash
pip install setuptools
pip install wheel
```

2. 安装完后，运行下面的命令打包

```bash
python setup.py sdist bdist_wheel
```

上面的命令会在dist/目录下生成一个tar.gz的源码包和一个.whl的Wheel包。

```text
dist/
  *.whl
  *.tar.gz
```

打包完之后，我们可以从本地安装库，来验证我们的项目能否被成功安装，如下

```bash
pip install dist/*.whl
```

## 发布项目到PyPI

使用twine上传项目，先安装twine

```bash
pip install twine
```

安装完之后，运行下面的命令将库上传

```bash
twine upload dist/*
```

上传完成后，我们的项目就成功地发布到PyPI了。

> 这里需要先注册一个 PyPI 账户

## 附录

1. pypi 免密上传，通过twine配置文件实现。

   $HOME/.pypirc` file with your username and password：

   ```ini
   [pypi]
   username = <username>
   password = <password>
   ```

   > 不建议将密码放入文件中

2. pypi 官方测试环境 [test.pypi.org](https://test.pypi.org/)。参考[使用testpypi](https://www.osgeo.cn/python-packaging/guides/using-testpypi.html)。

3. 直接从代码仓库安装python 包

   ```bash
   pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
   pip install -e hg+https://hg.repo/some_pkg#egg=SomeProject                # from mercurial
   pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
   pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomeProject  # from a branch
   ```

4. 使 python 包在任何地方都能安装

   This is a wheel that can be installed anywhere by [pip](https://python-packaging-user-guide.readthedocs.io/key_projects/#pip).

   `setup.cfg` (e.g., see [sampleproject/setup.cfg](https://github.com/pypa/sampleproject/blob/master/setup.cfg)):

   ```ini
   [bdist_wheel]
   universal=1
   ```