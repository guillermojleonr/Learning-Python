# Guide on how to create a virtual enviroment

Before starting a new Python Project, no matter what type is.

If this project will have dependencies, its necessary to create a virtual enviroment. 

It's a main folder where a copy of the python will be stored among with the dependencies. 

Inside that virtual enviroment you create you project.

## Find your local pythons installations

To find your python installations added to the PATH system enviroment variable
`echo %PATH%`

Using python interpeter:
`import sys`
`locate_python = sys.exec_prefix`
`print(locate_python)`

## Create virtual enviroment
Look for the python executable that you want to use in your project and run the following command

``C:\path\to\python_installation\python.exe -m venv .venv``

## Activate virtual enviroment on console.

Inside your virtual enviroment folder run the following script

``.venv\Scripts\activate.bat``

## Maintain a requirements.txt file

You need to keep track of all the dependencies that you are using inside a requirements.txt file, if you have testing dependencies for developments purposes, register them inside a requirements-dev.txt.

Requirements.txt Example:
flask==1.0.0
requests>=1.1.2,<2.0
gunicorn

### Creating a log of all dependencies already installed

`pip freeze > requirements.txt`

If you don't remember all the packages that you've installed in your project this command would help, however, this new file will have a lot of packages that your project does not actually need.

### Using requirements.txt to install dependencies

When you want to install all the dependencies stored in requirements.txt file:

- Activate the virtual enviroment

- `pip install -r requirements.txt`

## Should I create a virtual enviroment every time a star a new project?

It is always a good practice to create different virtual env for each django project. For example if you have multiple django projects that are using one virtualenv, and you want to host one of the django apps on a platform like Heroku which will require you create a requirements.txt file for python apps, so when you run pip freeze to get the requirements, you will find out that there are many packages in that env that is not required by your current project. And installing all those packages on your Heroku might make you run out of space before you know it. So try and keep the virtualenv different according to your project and keep the requirement.txt as well.