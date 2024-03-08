
## Installation

This requires [Docker](https://www.docker.com/products/docker-desktop//) to run.

Install the dependencies and devDependencies and start the server.

clone git repository 
```sh
cd ML-system
RUN: docker-compose up --build
```
Import following curl into postman
This is for getting access token

curl --location 'http://127.0.0.1:8000/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic M1EwTTBPTFVRUktMVGdielRUMVpsMFNRdzNkSWhDeTBieXhtemZlVzpZVWhnRFk4dFFWclVkY0pLVW9xakZ3b05ZNlNIRVRiUElYNzVUWGZwbmtDaW9RM1h5enFEUW1TdXlQeVlGQ2R6TWxvU1Y5cEVMbDV6ZkpWUkxtejhzVHpOQmlzNDM2amZkVU1lVDVUdXBvbXNzRHlGWnFpNjNGS2I2OXc5VkFKaQ==' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=groot' \
--data-urlencode 'password=root'

Now, again import following curl
This is the API to upload .txt file

curl --location 'http://127.0.0.1:8000/api/upload-img/' \
--header 'Authorization: Bearer Lc1k5BBfaSDY8Hk8EDVlVeIWgvVw0J' \
--form 'files=@"/C:/Users/deepe/Downloads/demo.txt"'

Note: Change token if required

For production environments...

```sh
Now upload text file
Done!
```

