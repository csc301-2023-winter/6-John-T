# Group 6: EXgoblins
​
> _Note:_ This document is intended to be relatively short. Be concise and precise. Assume the reader has no prior knowledge of your application and is non-technical. 
​
## Description 
Keep this section very brief.
 * Provide a high-level description of your application and it's value from an end-user's perspective
 * What is the problem you're trying to solve? Is there any context required to understand **why** the application solves this problem?
 
  In a time where mental health is a very high priority to many, practices such as mindfulness can go a long way in helping people. Forest therapy or forest bathing, as it is known in Japan, is one such practice. The intention of this project is to allow users to initiate guided meditation based on where they are in the park. Users can scan a QR code at a bench which will take them to an audio file for that specific bench, which will lead them through the exercise. From the admin side, they can create new benches, update existing benches, edit the details of a given bench, and they can also delete benches. 
## Key Features
 * Describe the key features in the application that the user can access.
 * Provide a breakdown or detail for each feature.
 * This section will be used to assess the value of the features built
 
 Users can scan QR codes on Ontario Park benches either via their phone's camera app or the website to access the media behind them. A small preview of the media's album name, author and an album image can be previewed before continuing if on the website.
 
 Users can play the media behind a bench's QR code and can be guided through context-specific meditation sessions. The page displays the album art, author, and will have buttons that will rewind, pause and fast forward the media. The media can be rewinded or fast forwarded by 10 seconds.
 
 Park managers can make manager accounts for the website, be able to log into said website and get access to manager actions. The actions are listed below:
 - Park managers can make new bench objects for their park in the database
 - Park managers can upload corresponding audio recordings and get a corresponding QR code to place on the physical park bench
 - Park managers can view and filter parks in the database so they can quickly and easily manage their benches
 - Park managers can obtain copies of existing QR codes in case the existing printed version is damaged
 - Park managers can create audio-to-QR code mapping to an existing bench (assigning a new audio recording to an existing bench with a QR code in the database) so they can cycle between themes based on certain occasions
 
​
## Instructions
 * Clear instructions for how to use the application from the end-user's perspective
 * How do you access it? For example: Are accounts pre-created or does a user register? Where do you start? etc. 
 * Provide clear steps for using each feature described in the previous section.
 * This section is critical to testing your application and must be done carefully and thoughtfully.
 
 To access the website, first, either go to https://6-john-t-one.vercel.app/#/. When prompted, grant the webpage access to your phone camera. Then, use your phone camera to scan one of the QR codes given. Alternatively, you can scan a QR code straight from your camera without going to the website above. \
 Doing either of the steps above will bring you to the corresponding media page where you can listen to a small meditative audio clip. You can rewind or fast forward 10 seconds by clicking the corresponding buttons. \
 To scan another QR code, either go back to https://6-john-t-one.vercel.app/#/ or open your phone camera app, and scan another QR code.
 
 ## Development requirements
 * What are the technical requirements for a developer to set up on their machine or server (e.g. OS, libraries, etc.)?
 * Briefly describe instructions for setting up and running the application. You should address this part like how one would expect a README doc of real-world deployed application would be.
 * You can see this [example](https://github.com/alichtman/shallow-backup#readme) to get started.
 
 ## Deployment and Github Workflow
​
Describe your Git/GitHub workflow. Essentially, we want to understand how your team members share codebase, avoid conflicts and deploys the application.
​
 * Be concise, yet precise. For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Describe your overall deployment process from writing code to viewing a live application
 * What deployment tool(s) are you using? And how?
 * Don't forget to **briefly justify why** you chose this workflow or particular aspects of it!
​
 ## Licenses 
​
 Keep this section as brief as possible. You may read this [Github article](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository) for a start.
​
 * What type of license will you apply to your codebase? And why?
 * What affect does it have on the development and use of your codebase?
