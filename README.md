# my-demo-container
This project is a simple Docker container for demonstration reasons along with an API to manage it

To build the container run:
docker build -t "image name"

To run the container run:
docker run -i --name "container name" "image-name"

NOTE: It is adviced to specify the name of the container when you run it, because it is needed to manage it from the API

To run the API:
python3 my_api.py [OPTION]

NOTE: options are start, stop, status
