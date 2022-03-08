# Backend-code-challenge
Hey there!!!

--> This an API which supports CRUD operation.
--> This API supports JWT authentication,pagination and ordering.

Do follow the below instructions to test the following API:

---> Clone the repo to your local machine using the command given below.
    "git clone https://github.com/ot-skannur/Backend-code-challenge.git"

---> To build the image make sure docker is installed.
     for Windows:  "https://www.docker.com/products/docker-desktop"
     for linux:    "https://hub.docker.com/search?offering=community&operating_system=linux&q=&type=edition"

---> Open the terminal or commandprompt and navigate to the root project directory.

---> Use the below command to build the image.
     "docker build --tag carbonmanagement ."

---> Use the below command to run the container.
     "docker run --publish 8000:8000 carbonmanagement"

---> Go to your favourite browser and run the local server given below.
      "http://localhost:8000/"

---> Users can get the records without any authentication.However to post,update and delete the records one 
     can use the below credentials for testing purpose.
         username: Tester
         password: testing12

---> To test the API one can use Postman platform and the link is provided below.
     "https://www.postman.com/downloads/"

---> The API documentation link:  "http://localhost:8000/docs/"


Experience:
    An amazing experience to build a REST web service for the first time.It was a bit challenging while implementing authentication classes and dockerizing the api.
    It took around two days approximately to build this api. Unfortunately couldn't do the frontend part since I am not well-versed in javascript framework. Looking forward to learn and grow.
