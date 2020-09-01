[blog](https://medium.com/1mgofficial/how-to-override-uvicorn-logger-in-fastapi-using-loguru-124133cdcd4e)

## Installation and Setup

- **Create Virtual Environment**

```
# Install python virtual environment
$ pip install virtualenv# Check virtual environment version
$ virtualenv --version# Now Create virtual environment
$ virtualenv my_name# Activate Virtual environment
$ source virtualenv_name/bin/activate
```

- **Install requirements**

```
$ pip install -r requirement.txt
```

- **Run your Application**

```
$ uvicorn main:app --port 5008 --access-log
```

## **The Final Output**

Using our custom logger implementation, we are able to achieve logging in the desired format.

![Image for post](https://miro.medium.com/max/1242/1*kV6It0YwCF2AaRCYFtg7CQ.png)

<center><b>Logging with Custom Logger</b></center>

![Image for post](https://miro.medium.com/max/1113/1*a7U-Rkg4sE4NdXbAnbp03Q.png)

<center><b>Exception</b></center>

## **Conclusion**

- We can use uvicorn default logging, there is no harm in it but your web application logs must be customize as per your needs. So you can try this solution.
- Easy to use and customize with loguru. (You can change you logging config for more customization)
- Produce full details of error.
- Easy to store in a specific log file. (which you mention in logging config)
- Better traceback.

