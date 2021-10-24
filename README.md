# DJANGO CODE CHALLENGE

This repository contains code that represents simple restful web API with DJANGO.


## Getting Started

These repo will get you an idea how to create a simple restful web API with DJANGO. We will walkthrough packages required, code behind how this works, and how all pieces connected together.

Overall Architecture:

![overview architecture](writeups/api.drawio.png)


## Built With

This project makes sure we have used the following packages and versions:

    ```python
        "packages": {
            django = "===3.0.4",
            djangorestframework = "==3.11",
            drf-nested-routers = "0.93.4",
            psycopg2 = "==2.8.6"
		}
    ```


## Estimated Learning/ Implementing Time

This project will use a simple and useful packages; but it would still be a good idea to log how much time I have learn and implement this so that you may be able to follow in later stage:

| Topic | Time (hr) | 
| :---: | :---: | 
| POSTGRES | 1 | 
| DJANGO with PIPENV setup | 1 | 
| Building models and migrations  | X | 
| Implementing DJANGO Rest Framework & DRF Nested Router  | X | 
| Complete unit test  | X | 
| Microservices demonstration  | X | 


## Authors

 [Pongsak](misc/pongsaks_cv.pdf) is a technical leader who has a great passion in technology; he has been working with industries to enable digital platform and manage project delivery; although currently working in project management, [Pongsak](misc/pongsaks_cv.pdf) loves coding and never stop learning technology in depth; [Pongsak](misc/pongsaks_cv.pdf) is looking for assignments with hands-on coding / implementing; find out more in my resume at [Pongsak](misc/pongsaks_cv.pdf)


## Environment File

The environment file .env has been setup as below. Database name will be DBNAMEPREFIX + STATE so that it will get correctly move to different development state.

    ```
        STATE=development
        DBNAMEPREFIX=testchallenge_
        DBUSER=[YOUR DB USER]
        DBPASSWORD=[YOUR DB PASSWORD]
        DBHOST=[YOUR DB HOST]
        DBPORT=[YOUR DB PORT]
    ```

We can place .env file in the main folder:

.
└── django_main
    ├── .env
    ├── Pipfile
    ├── Pipfile.lock
    ├── django_main
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── justapp
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── manage.py

