# Microservices on Docker

This repository is built to run microservices on Docker. The microservices are designed to run on AWS ECS with MongoDB. This is built in a way so that they can be easily run by a single line of command.

## Setup

To run on Docker, the prerequisites are Docker, Docker Compose and AWS CLI.

1. Install docker by following this [link](https://docs.docker.com/engine/install/).
1. Install docker-compose by following this [link](https://docs.docker.com/compose/install/).
1. Install aws-cli by following this [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

Note: If you get permission denied error after installation, or to run Docker without `sudo` command, please follow [this guide](https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket).

## Building Docker image

The next step is to build the docker image of the source code.

1. Go to root directory (same level as `docker-compose.yml`)
1. Build the image file
   ```
   docker-compose build --no-cache
   ```
1. Check if the docker image is built. The image repository should be named `awsdockerscheduledtaskblueprint_product-services`.
   ```
   docker image ls
   ```

## Run a microservice

There are multiple microservices in this repository. The microservices are referred as `handlers`. You can find them in `microservices/src/handlers`. The name of each handler is simply the file name without `.py` extension. Here is a list of the available handlers:

- `example_handler_1`
- `example_handler_2`

To run a microservice handler,

```
docker run -e AWS_ACCESS_KEY_ID="<aws_access_key>" -e AWS_SECRET_ACCESS_KEY="<aws_secret_key>" <image_name> <handler_name>
```

For example, to run `example_handler_1` microservice,

```
docker run -e AWS_ACCESS_KEY_ID="123" -e AWS_SECRET_ACCESS_KEY="456" awsdockerscheduledtaskblueprint_product-services example_handler_1
```

You should expect:

```
message: Success!
data: 3
```

## Deploying image to AWS

1. Set up AWS Credentials for development by following this [link](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html)
1. Retrieve an authentication token and authenticate your Docker client to your registry.<br/>Use the AWS CLI:
   ```
   aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin <ecr_repo_link>
   ```
1. Build a Docker image by referring to section above "Building Docker Image".
1. After the build completes, tag your image so you can push the image to this repository:
   ```
   docker tag <image_name>:<tag_name> <repo_uri>:<tag_name>
   ```
1. Run the following command to push this image to your newly created AWS repository:
   ```
   docker push <repo_uri>:<tag_name>
   ```
1. Check if the image is successfully uploaded on AWS. Go to AWS Console -> Amazon Container Services, on sidebar, under Amazon ECR find Repositories -> Images.

## Adding new tasks

A task can be understood as a command to run on AWS cluster. For each task, we can define a `handler_name` and environment variables. Therefore, one task should only run one handler.

1. Go to AWS Console -> Amazon Container Services, under Amazon ECS click on "Task Definitions" tab.
1. To create new task, press "Create new Task Definition" button.
1. Choose FARGATE as launch type.
1. Fill up the form until you reach "Container Definition", click "add container".
1. Make sure "Image" is filled in with the image URI on AWS ECR. Fill in the form and create container.
1. Scroll down and click on "Configure via JSON". This shows a JSON configuration file.
1. Under `"command"`, add `handler_name`. For example:
   ```
   "command": ["example_handler_1"]
   ```
1. Under `"environment"`, add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. For example:
   ```
   "environment": [
      {
         "name": "AWS_SECRET_ACCESS_KEY",
         "value": "12345678910"
      },
      {
         "name": "AWS_SECRET_ACCESS_KEY",
         "value": "abcdefghijklmnop"
      }
   ]
   ```
1. Create task and done!

## Scheduling tasks

As the microservices are run on Amazon ECS (Elastic Container Service), we can easily schedule to run a specific command. We can either run the commands manually, schedule to run between fixed intervals, or schedule to run repeatedly (in cycle).

1. Go to AWS Console -> Amazon Container Services, on sidebar, under Amazon ECS find Clusters.
1. Select cluster to run the task.
1. Go to "Scheduled Tasks" tab to manage the schedule.
