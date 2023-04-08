# <p style="text-align: center;"><b>Manager Frontend</b></p>

### User Stories
- As a website administrator, I want to be able to log into https://6-john-t.vercel.app/
- As a website administrator, I want to be able to manage benches for different parks
- As a website administrator, I want to be able to view, add, edit, and delete benches and parks
- As a website administrator, I want to be able to view and download a printable image of a QR code that links to a given bench

&nbsp;
&nbsp;
&nbsp;

### Frontend Development Requirements:
Setting up the developing environment for the frontend of the application is simple. In terms of tools, you will need:
* OS & hardware: Any computer is fine.
* `Node` installed

&nbsp;
&nbsp;
&nbsp;

### Instructions:

Once you have the basic tools, you can start setting up for frontend development. Follow these instructions:
* First clone the repository onto your machine by running the following command on your terminal:&nbsp;

  `git clone git@github.com:csc301-2023-winter/6-John-T.git`
* Next, navigate onto the following path (which will take you onto the base of the Node project/s) [keep in mind there's two node projects for the two separate frontends, given how different they are]:&nbsp;

  `cd 6-John-T/Code/user-frontend` for user side frontend.
  `cd 6-John-T/Code/manager-frontend` for manager side frontend.
* Here, run `npm install --legacy-peer-deps` to install all the dependencies and `node_modules` for `user-frontend` project; and `npm install` to install all the dependencies and `node_modules` for `manager-frontend` project.

* Now run `npm start` and a localhost version of the user frontend should open up in your default browser. If the setup was successful, you are good to go on and make changes to the project code!

&nbsp;
&nbsp;
&nbsp;

### Github Workflow and Deployment:
  - Code changes were pushed to main. When creating larger merges, we created a PR request that a teammate can review and accept. &nbsp;

  - For deployment, we are deploying on Vercel. We forked the main branch to a personal github page to link to Vercel, and then to deploy, we manually sync the fork with the main repo. We consulted the frontend user team regarding this, as they also are deploying Vercel which makes things easier when both teams are using the same thing.

&nbsp;
&nbsp;
&nbsp;

### Testing: 
