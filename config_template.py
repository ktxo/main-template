"""
Template configuration tool for main-template
"""
import os
import pprint
import json
import re
import shutil
import sys

from datetime import datetime

#---------------------------------------------------------------------------
DEFAULT = {
    "proj_name": "main_template",
    "proj_version" :"0.1.0",
    "proj_date":  datetime.today().strftime('%Y-%m-%d'),
    "proj_author": "ktxo",
    "proj_author_email" : "support@ktxo.com",
    "proj_url" : "git@github.com:ktxo/main-template.git",
    "proj_description" : "Application template",
    "proj_description_message" : "Brief description of this script",
    "proj_license" : "Copyright 2020, Ktxo",
    "proj_app_script_name": "main_template",
    "app_package": "ktxo.app",
    "app_min_python": "3.7",
    "app_keyword": "app template"
}
config={}
#---------------------------------------------------------------------------
def read_config():
    print("---------------------------------------------")
    print("Please enter values (ENTER to use default or 'None' to empty):")
    for k,v in DEFAULT.items():
        val = input(f"{k + ' (' + v + ')':<50}:")
        if val == "":
            config[k] = DEFAULT[k]
        elif val.lower() == "none":
            config[k] = ""
        else:
            config[k] = val
    print("---------------------------------------------")
    print("Configuration to apply:")
    for k,v in config.items(): print(f"{k:<50}: {v}")
    print("")
    input("ENTER to confirm or CTRl+C to cancel")

    return config
#---------------------------------------------------------------------------
def read_file(filename):
    fd = open(filename, "r")
    return fd.readlines()
def update_file(filename, lines):
    fd = open(filename, "w")
    [fd.write(line) for line in lines]
    fd.close()
def update_content(lines, pattern, value):
    if isinstance(pattern,str):
        lines_ = [w.replace(pattern,value)  if  pattern in w else w for w in lines]
    else:
        lines_ = [value if pattern.search(w)  else w for w in lines]
    return lines_



#---------------------------------------------------------------------------
def refactor_setup_py():
    ## setup.py :
    # aboutpath = join(abspath(dirname(__file__)),'ktxo','app', '_about.py')
    # entry_points={'console_scripts': ['main_template = ktxo.app.main_template:main']},
    # packages=setuptools.find_packages(include=['ktxo.*']),
    # classifiers=['Programming Language :: Python :: 3.7'],
    # keywords='app template'
    filename = "setup.py"
    lines = read_file(filename)
    values_ = config["app_package"].split(".")
    value = ",".join([f"'{w}'" for w in values_])
    lines = update_content(lines, "'ktxo','app'", value)
    lines = update_content(lines, "ktxo.app.main_template", config["app_package"] + "." + config["proj_app_script_name"])
    lines = update_content(lines, "main_template", config["proj_name"])
    value = config["app_package"].split(".")[0]
    lines = update_content(lines, "ktxo.*", value + ".*")
    lines = update_content(lines, "Python :: 3.7", config["app_min_python"])
    lines = update_content(lines, "app template", config["app_keyword"])

    lines = update_file(filename, lines)

#---------------------------------------------------------------------------
def refactor_main_template_py():
    ## main_template.py
    # @@Application Template@@
    # _log = logging.getLogger("ktxo.app") # loggers
    #     "proj_description" : "Application template",
    #     "app_package": "ktxo.app",
    filename = os.path.join("ktxo", "app", "main_template.py")
    lines = read_file(filename)

    lines = update_content(lines, "@@Application Template@@", config["proj_description"])
    lines = update_content(lines, "ktxo.app", config["app_package"])

    update_file(filename, lines)
#---------------------------------------------------------------------------
def refactor__about_py():
    ## _about.py
    # __name__ ='main_template'
    # __version__ = '0.1.0'
    # __date__ = '2019-01-01'
    # __author__ = 'ktxo'
    # __author_email__ = 'support@ktxo.com'
    # __url__ = 'git@github.com:ktxo/main-template.git'
    # __description__ = 'Application template'
    # __description_message__ = 'Brief description of this script'
    # __license__ = 'Copyright 2020, Ktxo'
    #     "proj_name": "main_template",
    #     "proj_version" :"0.1.0",
    #     "proj_date":  datetime.today().strftime('%Y-%m-%d'),
    #     "proj_author": "ktxo",
    #     "proj_author_email" : "support@ktxo.com",
    #     "proj_url" : "git@github.com:ktxo/main-template.git",
    #     "proj_description" : "Application template",
    #     "proj_description_message" : "Brief description of this script",
    #     "proj_license" : "Copyright 2020, Ktxo",
    #     "proj_app_script_name": "main_template",
    #     "app_package": "ktxo.app",
    #     "app_min_python": "3.7",
    #     "app_keyword": "app template"
    filename = os.path.join("ktxo", "app", "_about.py")
    lines = read_file(filename)
    for k,v in config.items():
        if k.startswith("app_"): continue
        key = k.replace("proj_", "__")+ "__"
        lines = update_content(lines, re.compile(f'{key}.*$'), f"{key} = '{v}'\n")
    update_file(filename, lines)

#---------------------------------------------------------------------------
def refactor_package():
    p = os.path.join(*config["app_package"].split("."))
    os.makedirs(p, exist_ok=True)
    curdir = os.getcwd()
    for p in config["app_package"].split("."):
        os.chdir(p)
        open("__init__.py", 'w').close()
    os.chdir(curdir)
    os.rename(os.path.join("ktxo","app","_about.py"), os.path.join(*config["app_package"].split("."),"_about.py"))
    os.rename(os.path.join("ktxo", "app", "main_template.py"), os.path.join(*config["app_package"].split("."), config["proj_app_script_name"]+".py"))
    P1 = "ktxo.app".split(".")
    P2 = config["app_package"].split(".")
    for i in range(0, len(P2)):
        if i < len(P1):
            if P1[i] != P2[i]:
                shutil.rmtree(os.path.join(*P1[0:i + 1]))
                break

#---------------------------------------------------------------------------
# Main
#---------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['-h', '--help','?']:
        print("""
Usage: python config_template.py [arg] 

 Dump default values to 'config_template.json'
   $> python config_template.py default
   
 Load values from a file (e.g. config_template.json)
   $> python config_template.py <path to configuration file>
 
 Prompt for values
   $> python config_template.py
 
""")
    elif len(sys.argv) > 1 and sys.argv[1] == "default":
        with open("config_template.json", "w") as fd:
            json.dump(DEFAULT,fd,sort_keys=False, indent=4)
        print("Default configuration saved to 'config_template.json'")
    elif len(sys.argv) > 1:
        print(f"Using configuration from '{sys.argv[1]}'")
        with open(sys.argv[1], "r") as fd:
            config.update(json.load(fd))
        refactor__about_py()
        refactor_setup_py()
        refactor_main_template_py()
        refactor_package()
    else:
        config = read_config()
        refactor__about_py()
        refactor_setup_py()
        refactor_main_template_py()
        refactor_package()

