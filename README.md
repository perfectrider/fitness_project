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

To launch the project, you need python version 3.10 and high.

1. To activate the virtual environment with the command:
source fitness_project/venv/bin/activate

2. Next, you need to install the django package at least the version specified in the file fitnessblog/requirements.txt (Django 4.1.2)
pip install django   or   pip install django==4.1.2

3. The next step to install the dependencies from the requirements.txt file. To do this, you need to run the command:
pip install -r fitnessblog/requirements.txt

4. To run the local server and test the project, you need run command:
python3 fitnessblog/manage.py runserver   or   python3 fitnessblog/manage.py runserver (for windows os)
