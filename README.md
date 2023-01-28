# UOCIS322 - Project 2 #

NAME: Vincent Lanier

CONTACT: vlanier@uoregon.edu

## Project Description

This project implements a simple webserver using flask. It includes a dockerfile for running inside a container.
The server only responds to GET requests.

## Setup

credentials-skel.ini should be replaced by a credentials.ini file specifying the port and debug mode. If no credentials file is provided, it defaults to
port 5000 and debug=True. *Note: The credentials.ini file should be placed in the /web directory so it can be accessed within the container.

* Build the simple flask app image using
  ```
  docker build -t some-image-name .
  ```

* Run the container using
  ```
  docker run -d -p desired-port:5000 some-image-name
  ```

## Usage

The server will serve files contained in the /web/pages directory. A 405 'method not allowed' page will be served for any requests other than GET.
404 not found and 403 forbidden templates are served if unable to locate the requested file, or forbidden characters are found in the request.

Example
```
Request:
curl -X GET "localhost:5000/trivia.css"

Response:
/*
 * Trivial style sheet for a trivial page
 */

body { background-color: rgb(200,255,200); }
p { color:  rgb(200,0,0); }
```

## Shutting Down

Simply shut down the flask app with ctrl-c in your terminal, or stop the docker container.
