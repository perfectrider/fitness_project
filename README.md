# fitness_project

The 2nd version of fitness blog. 

Even though the first version of the project was built in such a way that it could be improved, I decided to create a new project from scratch.

The second version is in constant development, during which I improve my django skills.

The second version of the fitness blog.

Even though the first version of the project was built in such a way that it could be improved, I decided to create a new project from scratch.

The second version is in constant development, during which I improve my django skills.

Compared to the first version, registration and authorization have been added. For authorized users, it is possible to leave comments under the post, in a special form for this. Users with superuser rights can create new posts, through a special form access to which appears in the header of the site.
The layout is based on bootstrap.

---

To launch the project, for Linux OS:

1. Create virtual enviroment:

python -m venv djangoenv

2. To activate the virtual environment with the command:

source djangoenv/bin/activate

3. Next, you need to install the django package at least the version specified in the file fitnessblog/requirements.txt (Django 4.1.2)

pip install django   

4. The next step to install the dependencies from the requirements.txt file. To do this, you need to run the command:

pip install -r fitnessblog/requirements.txt

5. To run the local server and test the project, you need run command:

python3 fitnessblog/manage.py runserver

---

To launch the project, for Windows OS:

1. Create virtual enviroment:

python -m venv djangoenv

2. Install dependences  for venv:

pip install requests

3. Activate virtual enviroment:

venv\Scripts\activate.bat

4. Install the Django

pip install django

5. Install dependeces for project:

pip install -r fitnessblog\requirements.txt

6. Run the project 

python fitnessblog\manage.py runserver

You are beautifull!!

---

If you want ro run clear project, without databases and images, you must migrate your models in databases. You must run the command:

python manage.py migrate

before the last command to run the Project, and then you will test a project.




