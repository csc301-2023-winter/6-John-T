# <p style="text-align: center;"><b>Backend</b></p>
## <p style="text-align: center;"><b>Team 6.2 (EXGoblins Backend Sub-team) - Deployment & Instructions</b></p>

### Backend Development Requirements:
Requires the following tools:
* OS: tested on Windows 10, Ubuntu 22.04 and MacOS
* Python 3.11.1
* Virtualenv (tested with v20.17.1)
* Pip 22.3.1 (or newer)
* Install all libraries and packages in Code/backend/ParkMindfulness/requirements.txt

&nbsp;
&nbsp;
&nbsp;

### Instructions:

Once you have those basic tools, you can start setting up for backend development. Follow the instructions below:
* First clone the repository onto your machine by running the following command on your terminal:&nbsp;

  `git clone git@github.com:csc301-2023-winter/6-John-T.git`
* Next, navigate onto the following path (which will take you onto the base of the Django project):&nbsp;

  `cd 6-John-T/Code/backend/ParkMindfulness`
* Here, create a virtual environment to store the packages the application will need:&nbsp;

  `virtualenv venv`
* Next activate this virtual environment:&nbsp;

  Windows: `venv\Scripts\activate&nbsp`

  Linux: `source venv/bin/activate`
* Now install the requirements for the project by running:&nbsp;

  `pip install -r requirements.txt`
* After this, the Django project should be fully set up. To check the installation worked, you can try running the project on your local server through the command:&nbsp;
	
  `python manage.py runserver`
* Then you can open the link: http://127.0.0.1:8000/benches/get_all_admin_parks/ where, if everything went right, you should be presented with the Django Rest Framework page template, and possibly some data about the Park objects currently in the database.
* If the setup was successful, then you should be ready to start writing code for the project within any of the existing Django applications (such as Benches).

&nbsp;
&nbsp;
&nbsp;

### Github Workflow and Deployment:

- The majority of our submitted code for the backend was implemented within the `backend-upgrades-d2` branch. We later merged this functionality with the code we brought forward from A2 through a Pull Request to main. For hotfixes, we did so on the `d2-backend-hotfixes` branch, first ensuring they worked as intended, before creating a PR to merge. All merging was done in accordance to our Overall Workflow (see above).

- For deployment, we chose to deploy on Railway. This ensures that our deployment builds are automated upon commits to `main`. Additionally, we chose Railway over Vercel due to storage capacity since our backend is also hosting our database. Furthermore, this allows us to communicate with both the Frontend User (FE-U) and Frontend Manager (FE-M) over HTTPS without having to invest into a domain (a requirement to obtain a SSL certificate over AWS EC2). Much like the FE-U hosting, the Railway build is linked to a fork on Tajwaar’s GitHub account that is auto deployed using a GitHub Action. (Note: This is currently not enabled as per our partner’s request due to an upcoming presentation in which he plans to showcase our work so far)

&nbsp;
&nbsp;
&nbsp;

### Testing: 

* Testing Details:
    * Testing was conducted using the ``django.test`` library in Django. This library allows us to both unit test our code, in addition to testing API payloads/information, and returned paths/pages. In total, we had **a total of 12 test cases testing nearly 100% of our models, forms, views, and URLs**
    * Here is a brief description of each of our test files within the ``~/ParkMindfulness/Benches/tests`` directory:
        * ``test_urls.py``: tests all URLs and paths within the ``~/ParkMindfulness/Benches/urls.py`` file
        * ``test_views.py``: tests all REST views within the ``~/ParkMindfulness/Benches/RESTviews.py`` file
        * ``test_models.py``: tests both Parks and Benches models within the ``~/ParkMindfulness/Benches/models.py`` file
        * ``test_forms.py``: tests both of the `` BenchesCreateForm`` and ``BenchesUpdateForm`` forms within the ``~/ParkMindfulness/Benches/forms.py`` file

&nbsp;
* Testing Instructions:
    1) Please make sure to first have ``Python`` and ``pip`` installed
    2) Then, please clone the GitHub repo
    3) If you wish to preserve your current working version of ``Django``, you can run the tests in your own virtual environment with the command ``python -m venv <environment_name>`` after installing the ``virtualenv`` library through ``pip``
    5) If you choose to do this in a virtual environment, after creation, please activate the virtual environment via the command ``source ~/<environment_name>/bin/activate``
    3) Now, once you have cloned the repo, navigate to the root directory (``~/ParkMindfulness``) and run the following command: ``pip install -r requirements.txt``
    4) After doing so, from the same directory, please run the following command:
    ``python manage.py test Benches`` (depending on your installation of ``python`` and your OS, you may need to alternatively run ``python3 manage.py test Benches``)
        * After doing so, you should then receive feedback on the test cases that have run


