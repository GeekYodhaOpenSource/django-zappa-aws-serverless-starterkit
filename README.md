

Django Deployment with aws-lambda using zappa Project Starter Template
=======================

This starter kit will give you basic template to start work with django, zappa and aws lambda. You can modify it as per your requirement.

## Requirements

- Latest Python 3.7+ runtime environment.
- `pip`, `virtualenv`

Installation
------------

To setup a local development environment::

    python -m venv env
    .\env\Scripts\activate
    pip install -r requirements.txt 
    py./manage.py migrate
    ./manage.py runserver
    !hola our app is running successfully 
    
Deploying on AWS-lambda
------------

To deploy on aws lambda serverless::


    To get started with aws please install and configure aws cli download link(https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    After successfully configured aws cli next go to zappa  
    zappa init
    set your aws_region=""
    project_name="****"
    s3_bucket="***"(to store the media and static files and give the credentials)
    For launching our new app:: zappa deploy ourappname
    For release next production update :: zappa update ourappname
    For cheking of logs : zappa tail
## Architecture 
![alt text](https://s3-ap-southeast-2.amazonaws.com/static.davur.net/img/lambda-web-host-arch.png)

The Zappa Architecture 
--------
![alt text](https://www.ginkgobioworks.com/wp-content/uploads/2020/12/image1.png)
