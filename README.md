
# Basic template

Basic template for python application

----

# What is is this?
Well, purpose is to provide a *simple* skeleton for application, including :

- Simple skeleton for app
- Command arg parse (argparse) (including common options: -h=help, -l=logging ,-c=configuratio)
- Logging module (https://docs.python.org/3.9/library/logging.html)
- Installation (as module and script)


## How to use

- Clone sources 
```
# "mybot" application
git clone git@github.com:ktxo/main-template.git mybot
```

- Change 

- Rename the following according to your app:
    1. Package directories "ktxo/app" to something related to your app, for example: "myorg/bot" (for a "bot" app)
    2. Rename file [main_template.py](ktxo/app/main_template.py), for example: "mybot_app.py",
    3. Config file [_about.py](ktxo/app/_about.py)
    4. Config file [setup.py](setup.py)
        - Note the following line: 
          ```
          {'console_scripts': ['main_template = ktxo.app.main_template:main']}
          ```
           *main_template*: this name should be used to call your app from shell, for example:
          ```
          $> main_template --help
          ```
           *ktxo.app.main_template*: must match your configuration, for example:
           ```
          {'console_scripts': ['mybot = myorg.bot.mybot_app:main']}
          ``` 
    ![example](example.png)
  
    5. Add the code to *mybot_app.py*, **don't forget to change doc and logger name!**
    
- If you don't need a configuration file, remove the following lines:
    - Parse config option 
    ```
        parser.add_argument("-c", "--config",
                            help="Application configuration file")
    ```

    - Custom handler: init_cfg
    ```
    def init_cfg(args):
        ....
    ```
    - CONFIG dict
    ```
    CONFIG={}
    ```

- If you need a configuration , use [config.json](config.json) as a reference and add the required code to **init_cfg()** to handle the configuration
- Review command args for your app, see **parse_args()**
- Code your app
- Enjoy it!

## Application installation and execution

- Build app 
``` 
# Build a wheel
cd myboot
python setup.py bdist_wheel
``` 
- Install app
``` 
# Install app
cd  dist ; pip install *whl;cd -

> pip list | grep mybot 
mybot                              0.1.0
> 
> pip show mybot
Name: mybot
Version: 0.1.0
Summary: This bot is for......
Home-page: some url
Author: Your name
Author-email: myemail@domain.com
License: Copyright 2020
Location: /sw/anaconda/lib/python3.8/site-packages
Requires: 
Required-by: 
```

- Run app
```
> mybot --version
mybot v0.1.0 (2019-01-01) by Your name
Python version 3.8.5 (default, Sep  4 2020, 07:30:14) [GCC 7.3.0]
Other version n.n.n

# or

    > python -m myorg.bot.mybot_app --version
mybot v0.1.0 (2019-01-01) by Your name
Python version 3.8.5 (default, Sep  4 2020, 07:30:14) [GCC 7.3.0]
Other version n.n.n

```