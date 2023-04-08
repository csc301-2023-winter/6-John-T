# <p style="text-align: center;"><b>User Frontend</b></p>

### User Stories
- As a user, I want to be able to scan the QR codes on Ontario Park benches, so that I can access the content.
- As a user, I want to be able to play the media related to a bench's QR code, so that I can be guided through the context-specific meditation session.
- As a user, I want to be able to visit https://6-john-t-one.vercel.app/#/ to view head of site, then find a QR code to scan.

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
  - We have a branch that we make our initial code changes on called “qrscanner_change”. And once the changes are ready, we merge to the main branch if the change is small (hotfix), and make a PR for large potentially code breaking changes. Because one of us will be making the change, the other person has to review it. Anyone can merge once ready. &nbsp;

  - For deployment, we are deploying on Vercel. We chose Vercel because Vercel looks for commits/merges to the main branch and runs build everytime main updates. This makes it very convenient as there isn't much for us to do to deploy other than merge to the main branch. Because this repo is on an organization account, we first forked it out to Parth’s personal account, and connected Vercel from there. But because it is from a fork, we must first update the fork from upstream. To automate this process, there is a github action on Parth’s fork that checks for updates every 30 minutes and updates accordingly. The action file is in “main/.github/workflows/updateAndDeploy.yml”. 
  
&nbsp;
&nbsp;
&nbsp;

### Testing: 
  - run `npm test` to run the auto tests. These tests also automatically run through our GitHub Actions and Deployment partners (Vercel and Netlify).
