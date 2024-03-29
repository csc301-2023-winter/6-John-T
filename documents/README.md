# Group 6: EXgoblins
​
<!-- > _Note:_ This document is intended to be relatively short. Be concise and precise. Assume the reader has no prior knowledge of your application and is non-technical.  -->
​
## Description 
<!-- Keep this section very brief.
 * Provide a high-level description of your application and it's value from an end-user's perspective
 * What is the problem you're trying to solve? Is there any context required to understand **why** the application solves this problem? -->
 
  In a time where mental health is a very high priority to many, practices such as mindfulness can go a long way in helping people. Forest therapy or forest bathing, as it is known in Japan, is one such practice. The intention of this project is to allow users to initiate guided meditation based on where they are in the park. Users can scan a QR code at a bench which will take them to an audio file for that specific bench, which will lead them through the exercise. From the admin side, they can create new benches, update existing benches, edit the details of a given bench, and they can also delete benches. 

&nbsp;
&nbsp;
&nbsp;

## Key Features
 <!-- * Describe the key features in the application that the user can access.
 * Provide a breakdown or detail for each feature.
 * This section will be used to assess the value of the features built -->
 
- Users can scan QR codes on Ontario Park benches either via their phone's camera app or the website to access the media behind them. A small preview of the media's album name, author and an album image can be previewed before continuing if on the website.
 
- Users can play the media behind a bench's QR code to be guided through context-specific meditation sessions. The page displays the album art, author, and will have buttons that will rewind, pause and fast forward the media. The media can be rewinded or fast forwarded by 10 seconds.
 
- Park managers can make manager accounts for the website, be able to log into said website and get access to manager actions. The actions are listed below:
  - Park managers can make new bench objects for their park in the database. During this creation process, they can upload the audio recordings and once finished, they are provided with a corresponding QR code to place on the physical park bench.
  - Park managers can view and filter parks in the database so they can quickly and easily manage their benches.
  - Park managers can obtain copies of existing QR codes in case the existing printed version is damaged.
  - Park managers can update certain attributes of a bench (including the audio-to-bench mapping) such that the update to the bench is reflected on the same QR code that the bench was already assigned (allowing for printed QR codes to stay relevant forever). 
 
&nbsp;
&nbsp;
&nbsp;​

## Instructions
 <!-- * Clear instructions for how to use the application from the end-user's perspective
 * How do you access it? For example: Are accounts pre-created or does a user register? Where do you start? etc. 
 * Provide clear steps for using each feature described in the previous section.
 * This section is critical to testing your application and must be done carefully and thoughtfully. -->
 
* As mentioned in planning.md on 6-John-T/documents/ there are two sides to our project, the administrator side where mindfulness audios are mapped to benches around a park, and the user side where the users are taken to view a bench's information and listen to the corresponding bench audio upon scanning a QR code generated on the administrator side.
* Please keep in mind that while for D2 both sides of the application are accessible to everyone, the administrator side is meant to be accessed by users with registered accounts only (this functionality will be implemented in the following weeks).

#### Accessing the Administrator Side:
* As mentioned above, as of D2, this side of the application can be accessed without the need for an account/special permissions, so anyone can access the page at: https://6-john-t.vercel.app/ 
* Upon first access, you are thrown into a page where you are to select the park that you want to edit benches for (which can be done from either the button or the dropdown). Parks come pre-loaded into the database for now.
* Once a park has been selected you are taken to the page where all of the selected Park’s bench objects are displayed along with all of the options that you are given as an administrator.
* You can create a new bench object for the park you currently find yourself in:
	* Do this by clicking the ‘Create New Bench’ button on the park page, which will take you to a form page where you will be able to upload the bench’s related information (such as the audio, thumbnail, and more).
	* When you are done, you can click on ‘Add Bench’ to register this new object in the database, this automatically creates the QR code mapping to the information that this bench object stores for the users to access through the user-side frontend.
* You can edit and download the QR code for a specific bench by clicking on the respective buttons for each of the instances listed on a park’s page.
	* Editing a bench allows you to either update its corresponding information through a similar form to the one from bench creation, or delete it. Updating does not alter the existing QR code (which allows for the existing QR codes to not become obsolete as their corresponding benches change over time).
	* Deleting a bench from within its edit page, wipes the bench’s information from the database, making the existing QR code for it no longer map to anything.
	* Downloading a QR code lets you access the automatically created QR code so that it can be printed and presented to users throughout an administrator’s park.
* At any moment while exploring a Park’s page, you can switch to another park by clicking on the ‘Select Park’ button which will take you back to the main page.

#### Accessing the User Side:
* User’s have 2 ways of getting to the information that a bench stores and they both involve scanning a QR code that is to be printed/displayed on a park’s benches/zones of interest.
* You can open up your phone’s camera app and scan the QR code, which will take you directly to the page with that bench’s information.
* Or, if your phone doesn’t have QR scanning capabilities, or you are trying to access a bench’s information from a desktop, you can go over to https://6-john-t-one.vercel.app/, grant the permissions to the website to use your camera/webcam, and scan a QR code using the built in camera, once the QR code is identified, you will see a preview of the bench you just scanned with its thumbnail and name, and upon clicking on the arrow to proceed to the bench page, you will be taken to the page with that bench’s information. 
* Once on a bench’s main page, a user will be able to see the bench’s thumbnail, bench title, audio contibutor, as well as a player for the mindfulness audio related to this bench. Users can use the play/pause, and the skip forward and rewind 10 seconds buttons to navigate through the audio to start their Parkfullness Meditation. 
* From within a bench’s main page, users can go to the general landing page (with the built in online scanner) by clicking on the Ontario Parks logo on the top left side of the screen.

&nbsp;
&nbsp;
&nbsp;

 ## Development requirements
 <!-- * What are the technical requirements for a developer to set up on their machine or server (e.g. OS, libraries, etc.)?
 * Briefly describe instructions for setting up and running the application. You should address this part like how one would expect a README doc of real-world deployed application would be.
 * You can see this [example](https://github.com/alichtman/shallow-backup#readme) to get started. -->

 ### Backend Development Requirements:
Setting up the developing environment for the backend of the application is simple. In terms of tools, you will need:
* OS: development has been tested on Windows 10, Ubuntu 22.04 and MacOS.
* Python 3.11.1
* Virtualenv (tested with version 20.17.1).
* Pip 22.3.1 (or latest version).
* All of the libraries and packages within requirements.txt (keep reading for installation instructions).

Once you have those basic tools, you can start setting up for backend development. Just follow the instructions below:
* First clone the repository onto your machine by running the following command on your terminal:&nbsp;

  `git clone git@github.com:csc301-2023-winter/6-John-T.git`
* Next, navigate onto the following path (which will take you onto the base of the Django project):&nbsp;

  `cd 6-John-T/D2/backend/ParkMindfulness`
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


### Frontend Development Requirements:
Setting up the developing environment for the frontend of the application is simple. In terms of tools, you will need:
* OS & hardware: Any computer is fine.

* `Node` installed

Once you have the basic tools, you can start setting up for frontend development. Follow these instructions:
* First clone the repository onto your machine by running the following command on your terminal:&nbsp;

  `git clone git@github.com:csc301-2023-winter/6-John-T.git`
* Next, navigate onto the following path (which will take you onto the base of the Node project/s) [keep in mind there's two node projects for the two separate frontends, given how different they are]:&nbsp;

  `cd 6-John-T/D2/user-frontend` for user side frontend.
  `cd 6-John-T/D2/manager-frontend` for manager side frontend.
* Here, run `npm install --legacy-peer-deps` to install all the dependencies and `node_modules` for `user-frontend` project; and `npm install` to install all the dependencies and `node_modules` for `manager-frontend` project.

* Now run `npm start` and a localhost version of the user frontend should open up in your default browser. If the setup was successful, you are good to go on and make changes to the project code!


 
&nbsp;
&nbsp;
&nbsp;

 ## Deployment and Github Workflow
​
<!-- Describe your Git/GitHub workflow. Essentially, we want to understand how your team members share codebase, avoid conflicts and deploys the application.
​
 * Be concise, yet precise. For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Describe your overall deployment process from writing code to viewing a live application
 * What deployment tool(s) are you using? And how?
 * Don't forget to **briefly justify why** you chose this workflow or particular aspects of it! -->
- Overall Workflow/Naming Conventions: &nbsp;

  - For each sub-team (Frontend User, Frontend Manager, and Backend), we will use branches when in need of major functionality implementations. Additionally, we will also try to include the assignment that it is relevant for, the subteam that will be working on it, and the reasoning behind doing so, e.g. `backend-upgrades-d2`. Upon successful implementation and testing, a member of that sub-team will create Pull Requests that must be approved and reviewed by another member from the same sub-team before they merge with `main`.

- Frontend User:&nbsp;

  - We have a branch that we make our initial code changes on called “qrscanner_change”. And once the changes are ready, we merge to the main branch if the change is small (hotfix), and make a PR for large potentially code breaking changes. Because one of us will be making the change, the other person has to review it. Anyone can merge once ready. &nbsp;

  - For deployment, we are deploying on Vercel. We chose Vercel because Vercel looks for commits/merges to the main branch and runs build everytime main updates. This makes it very convenient as there isn't much for us to do to deploy other than merge to the main branch. Because this repo is on an organization account, we first forked it out to Parth’s personal account, and connected Vercel from there. But because it is from a fork, we must first update the fork from upstream. To automate this process, there is a github action on Parth’s fork that checks for updates every 30 minutes and updates accordingly. The action file is in “main/.github/workflows/updateAndDeploy.yml”. 

- Frontend Manager:&nbsp;

  - Code changes were pushed to main. When creating larger merges, we created a PR request that a teammate can review and accept. &nbsp;

  - For deployment, we are deploying on Vercel. We forked the main branch to a personal github page to link to Vercel, and then to deploy, we manually sync the fork with the main repo. We consulted the frontend user team regarding this, as they also are deploying Vercel which makes things easier when both teams are using the same thing.


- Backend:&nbsp;

    - The majority of our submitted code for the backend was implemented within the `backend-upgrades-d2` branch. We later merged this functionality with the code we brought forward from A2 through a Pull Request to main. For hotfixes, we did so on the `d2-backend-hotfixes` branch, first ensuring they worked as intended, before creating a PR to merge. All merging was done in accordance to our Overall Workflow (see above).&nbsp;

  - For deployment, we chose to deploy on Railway. This ensures that our deployment builds are automated upon commits to `main`. Additionally, we chose Railway over Vercel due to storage capacity since our backend is also hosting our database. Furthermore, this allows us to communicate with both the Frontend User (FE-U) and Frontend Manager (FE-M) over HTTPS without having to invest into a domain (a requirement to obtain a SSL certificate over AWS EC2). Much like the FE-U hosting, the Railway build is linked to a fork on Tajwaar’s GitHub account that is auto deployed using a GitHub Action. (Note: This is currently not enabled as per our partner’s request due to an upcoming presentation in which he plans to showcase our work so far)

​
&nbsp;
&nbsp;
&nbsp;

 ## Licenses 

 <!-- Keep this section as brief as possible. You may read this [Github article](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository) for a start.
​
 * What type of license will you apply to your codebase? And why?
 * What affect does it have on the development and use of your codebase? -->
* Chosen License: [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
* Reasoning:
  * GNU v3.0 allows us to use the codebase for commercial purposes as requested by our partner
  * Additionally, it allows for modification and private use upon a disclosure and copyright notice while implementing a patent - essentially future-proofing for the implementation of future functionality
  * From a development perspective, we can all contribute privately while others can contribute as well towards features that can be used for commercial purposes by our partner and also allows us to distribute this code to hand it off to the next group working on it (whether that be CSC301 students or other parties).

