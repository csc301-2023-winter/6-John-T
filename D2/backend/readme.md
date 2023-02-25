# <p style="text-align: center;"><b>CSC301 A2: First Step in Building Modern Software</b></p>
## <p style="text-align: center;"><b>Team 6.2 (EXGoblins Backend Sub-team) - Deployment & Instructions</b></p>

&nbsp;
&nbsp;
&nbsp;

### Overview:

* First of all, the quick links to the main parts of this submission for A2 are as follows:
    * The deployed website (the application itself): -INSERT LINK HERE-
    * The sub-team report: file report.pdf here at the root directory of the repo.
    * The sub-team repo: where you are right now.
    * The main team repo (containing the Project Team Repo Report Submission): https://github.com/csc301-2023-winter/6-John-T/blob/main/documents/team/assignment-2.pdf (submitted on Sunday February 19th, 2023).

&nbsp;
&nbsp;
&nbsp;

* Starting at the root directory of the repo, 4 things can be found:

1) The ParkMindfulness Django project containing the entirety of the backend code that the deployed website runs on. 

2) The CSC30123S Coursework Delay notification file, highlighting our request for an extension (as we have handed in this project on tuesday february 21st, 2023).

3) The readme.md file, which you are currently reading, containing the details and instructions needed to verify our work, and the application itself. This correpsonds to bullet points 3 and 4 on the 'Sub-Team Repo Submission' section of A2's handout.

4) The sub-team report pdf file (report.pdf), containing our decisions and considerations on the tools we have chosen to work with to develop the website's backend, and the contributions of each team member of the sub-team to this iteration of the project. This corresponds to bullet points 1 and 2 on the 'Sub-Team Repo Submission' section of A2's handout.

&nbsp;
&nbsp;
&nbsp;

### Details and Instructions:

* As part of this submission we have implemented the user story of: “As a Park Manager, I want to be able to make up new bench objects for my park, and obtain the QR code corresponding to an existing bench”. Please note that as the backend team, we have not put too much effort into our UI, but rather we just tried to make it functional to show all the features we implemented in the backend that we are actually concerned with. 
* So upon accessing the deployed website at -INSERT LINK HERE-, as a user, you will be able to see the following:
    * A list of all the bench objects currently in the database, along with their corresponding details.
    * A button to add a new bench object to the database, this will lead you over to a form where you can enter the details of the bench you want to add.
    * A button to delete a bench object from the database, which will ask for the bench's ID, and then delete the bench with that ID from the database (in the actual application the front end will incorporate this feature more directly, but as the backend team, the functionality is that given an ID, we wanted to delete that object).
    * A button to update a bench object in the database, which works the same way as bench creation, but instead of creating a new bench, it will update the bench with the given ID with the new details.

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

### Deployment:

* Deployment was conducted via AWS. Since we were all new to DevOps, the first step was learning about the entire process (using both lecture and AWS Educate material). Afterwards, we learned about both AWS EC2 and Elastic Beanstalk, weighing the pros and cons of both. For us, an EC2 instance seemed the more appropriate given its ability to expand and the many resources available that will allow us to use a GitHub repo in tandem.


