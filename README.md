# Student-app (Flask-sqlite3 Docker)
Created a Flask application using sqlite3 database that helps the user to perform CRUD operations on a database.I have also added the instruction to deploy the application on jenkins and build a CI/CD pipeline as it was one of the objective that I wanted to achieve with this application.

## Running Dockerfile:
1. Clone the repository and open it in terminal.
2. RUN ON TERMINAL => docker build --pull -t student-app .   (here student-app is the name of the docker image)
3. RUN ON TERMINAL => docker run -p 5000:5000 student-app

## Running docker-compose.yml:
1. Clone the repository and open it in terminal.
2. RUN ON TERMINAL => docker-compose up 

I have added docker-compose.yml so that if anyone wants to add more services to this particular application they can.

## Jenkins CI/CD pipeline:
1. Log in to jenkins and click on 'new item'.
2. Enter item name and click on 'Freestyle Project'.
3. In [Source Code Management] select git. (make sure the git repository contains the DockerFile,flaskapp and requirements.txt file)
4. Add Git Repository url and and branch name.
5. In [Build Triggers] select 'GitHub hook trigger for GITScm polling'. 
6. In [Build] select 'execute shell', a shell will open.
7. In shell enter the following command:

                        docker build --pull -t student-app .
                        docker run -p 5000:5000 student-app
                        
8. Save, Apply and click on Build now.

At this point of time jenkins will be able to fetch files from github, build docker containers and run your application on them. But it won't show the build as complete and a new build won't start if you push changes to your git repository for that you have to create a webhook in your git repository.

## Git Webhook for jenkins:
1. Go to your Repository Settings>>Webhooks>>Add Webhook.It is not possible to add a webhook for the Jenkins running on local host as it doesn’t have a public URL exposed over internet. To resolve this issue we can use a tool like ngrok which will expose the local server to the public internet.
2. To install ngrok , go to https://ngrok.com/download.
3. RUN ON TERMINAL => ifconfig (to get you machine IP).
4. RUN ON TERMINAL => ./ngrok http://(your-machine-ip):8080
5. You will get a url like this : http://9506c53b8hcf.ngrok.io. 
6. Copy the ngrokurl/github-webhook/ on [Payload URL].
7. Set [content type] to application/json.
8. Select 'just push operation'.
9. Check Active and click on create webhook.

Now you need to configure you jenkens CI/CD pipeline as with every build you need to remove images with same name from previous build. You can do it by updating the build execute shell with the following commands :

      docker build --pull -t student-app .
      docker run -p 5000:5000 student-app
      docker stop $(docker ps -aq)
      docker rm $(docker ps -aq)
      docker image rm -f student-app

Save, now with every commit to your git repository jenkins will build a new image of your web application.




