# Group 6: EXgoblins


## Iteration 01 - Review & Retrospect


* When: March 9, 2023
* Where: Zoom Meeting


## Process - Reflection




#### Q1. What worked well
<!-- List **process-related** (i.e. team organization and how you work) decisions and actions that worked well.


* 2 - 4 important decisions, processes, actions, or anything else that worked well for you, ordered from most to least important.
* Give a supporting argument about what makes you think that way.
* Feel free to refer/link to process artifact(s). -->

- The front-end deployment was efficiently executed on Vercel, making it a favourable choice for the project. The platform facilitated easy account creation and deployment, requiring only a few minutes, and its free service provided a sense of long-term stability.
- Django/React allowed us to get a substantial amount of work done due to prior familiarity and experience. Therefore, this allowed us to debug other issues (e.g. DevOps) effectively.
   - The team had considerable prior experience from their work in 309, thus knowing how Django/React will behave and what we can and cannot do with each framework.
- Allocation of work with a 3-2-2 split proved to be very effective, as each sub-team carried out their responsibilities without experiencing an overwhelming workload
   - Each team member was able to rely on their respective partner(s), and this resulted in a balanced workload for all 
- Regular meetings via Zoom and the discord server helped communicate deadlines and kept the team up-to-date with other sub-team progress.
   - Fast and effective at keeping everyone updated with each other's contracts and our partner, John's, feedback and new ideas.
   - Small quick decisions, such as the format of JSON, are discussed fluidly over discord chat.

&nbsp;
&nbsp;
&nbsp;


#### Q2. What did not work well
<!--
List **process-related** (i.e. team organization and how you work) decisions and actions that did not work well.


* 2 - 4 important decisions, processes, actions, or anything else that did not work well for you, ordered from most to least important.
* Give a supporting argument about what makes you think that way.
* Feel free to refer/link to process artifact(s). -->


- Auto deployment of Vercel frontend. To do it with every commit to the main branch, we would need to pay for their premium service. So we needed to find a work-around. Parth on the frontend user team found a work-around. He found that we can fork the repo to our personal account and link Vercel auto-deployment to it, and use github actions on a personal repository to auto-deploy every 30 minutes. This didn’t work too well as we had to figure out how to do this from scratch as there weren't many resources online.


- Backend deployment required many workarounds due to complications in paid services/domains, frontend-backend communication, and size of the backend application
   - This required much more time and an analysis between different hosting options (AWS, Vercel, Railway, etc.) comparing prices, deployment complexity, security, and upkeep (in addition to the time required to deploy on our final service of choice, Railway)


&nbsp;
&nbsp;
&nbsp;


#### Q3(a). Planned changes
<!-- List any **process-related** (i.e. team organization and/or how you work) changes you are planning to make (if there are any)


* Ordered from most to least important, with supporting argument explaining a change. -->


1) Swap a member from Front End-User (FE-U) to Front End-Manager (FE-M), as FE-U does not require as much work as FE-M moving forward.
2) Switching our weekly meeting from Saturday afternoons to Thursday after class such that we can maximize the number of members present and the representatives can share the feedback from partner meetings (Thursdays 2-3PM) to the team quicker.




#### Q3(b). Integration & Next steps
<!-- Briefly explain how you integrated the previously developed individuals components as one product (i.e. How did you be combine the code from 3 sub-repos previously created) and if/how the assignment was helpful or not helpful.


* Keep this very short (1-3 lines). -->
- Established the FE-to-BE contracts (which resulted in backend sub team having to support a few more pieces of functionality such that the FE-U could be included in this deliverable).
- FE-U and FE-M changed from using mock data to using API links from the deployed backend to get real data from the database.


&nbsp;
&nbsp;
&nbsp;


## Product - Review


#### Q4. How was your product demo?
<!-- * How did you prepare your demo?
* What did you manage to demo to your partner?
* Did your partner accept the features? And were there change requests?
* What were your learnings through this process? This can be either from a process and/or product perspective.
* *This section will be marked very leniently so keep it brief and just make sure the points are addressed* -->
* How did you prepare your demo?&nbsp;


   We prepared some user stories that involved using the different parts of the application we built, so that the partner could see the full end-to-end functionality.
* What did you manage to demo to your partner?&nbsp;


   We were able to demo the creation of a park bench by uploading information and files, and then seeing the uploaded information being updated and reflected. From the user side, the partner was able to scan the QR code that we automatically generated in the previous bench creation step and see the information presented in a UI for them.
* Did your partner accept the features? And were there change requests?&nbsp;


   The partner accepted the major features that we showed them. There were cosmetic change requests regarding style and the theme of the application, and they gave general feedback regarding features that they would like to see, like administrators being able to change the theme for the site. The partner also requested to demonstrate the application to a tourism officer, and we had to prepare a short demonstration simple enough that the partner could show it without us present.
* What were your learnings through this process? This can be either from a process and/or product perspective.&nbsp;


   We learned to polish up our application so that it could be ready to present. Addressing major functionality issues and being knowledgeable enough to answer any questions about our deployment helped us prepare for the presentation, which felt very similar to an elevator pitch.
