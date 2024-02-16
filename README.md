# flask-on-docker

## Overview
This project was made with instrcutons from https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/ in order to create a web service where you are able to upload images and files onto a server. I have used Docker, Flask, Gunicorn, and Nginx to create the server and it is modeled off of Instagram's tech stack. In order to connect to the server, you will nedd to use port forwarding to localhost:2709 on your local machine. You will then be able to access the server at upload images at http://localhost:2709/upload and then access these images at http://localhost:2709/media/$FILENAME where **$FILENAME** will be the name of the file that you uploaded.

##Build Instructions
1) You will first need to build and spin up the docker containers that are involved in this project. This can be done with:
   ```
   docker-compose -f docker-compose.prod.yml up -d --build
   ```
2) Once completed, you will then need to create the database that will store all the information uploaded to the web server. This can be done with:
   ```
   docker-compose -f docker-compose.prod.yml exec pyhton manage.py create_db
   ```
##Upload Images
Now that the server and database has been created, you will now go to the previoulsy mentioned webpages to upload and acess uploaded photos.
