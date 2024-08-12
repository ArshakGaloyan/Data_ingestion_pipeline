# Docker
## Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.
## Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. 
![Docker architecture](https://docs.docker.com/guides/images/docker-architecture.webp)
## The Docker daemon
### The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.
## The Docker client
### The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.
## Docker registries
### A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker looks for images on Docker Hub by default. You can even run your own private registry.When you use the docker pull or docker run commands, Docker pulls the required images from your configured registry. When you use the docker push command, Docker pushes your image to your configured registry.
## Docker objects
### When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.
## Images
### An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run. You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt. This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.
## Containers
### A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state. By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container's network, storage, or other underlying subsystems are from other containers or from the host machine. A container is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that aren't stored in persistent storage disappear.
# Docker container create
## Description
### The docker container create (or shorthand: docker create) command creates a new container from the specified image, without starting it.
### When creating a container, the Docker daemon creates a writeable container layer over the specified image and prepares it for running the specified command. The container ID is then printed to STDOUT. This is similar to docker run -d except the container is never started. You can then use the docker container start (or shorthand: docker start) command to start the container at any point.
### This is useful when you want to set up a container configuration ahead of time so that it's ready to start when you need it. The initial status of the new container is created.
### The docker create command shares most of its options with the docker run command (which performs a docker create before starting it). 
## Docker image
### First, we need a Docker image for our container. An image is essential if our container is to come to life. If we were to draw a parallel, the container represents a computer from a hardware point of view, and the image represents all the digital resources present on it: OS, binary files, software. Just as a computer is useless if nothing is installed on it, software is useless if it isn’t installed somewhere.
### We’re back to the architecture of a container and a content.
### Let’s import a Linux image from the Docker Hub. Open a terminal and run the following command:
## Dockerfile
### A dockerfile is a file that allows us to build a custom docker image. It also contains a set of commands to run in the container, applications to install, environment variables to initialize…
### In a basic python file, let’s just write a simple function :
## Let’s explain what our Dockerfile contains:
### The FROM keyword allows us to retrieve an image from the Docker Hub.
### RUN allows us to add an intermediate layer to the construction of our image. We want our image to have a Debian base (Linux distribution) and Python installed.
### ADD allows us to add a local file to our container. Be careful to specify the path.
### Finally, in a terminal and in the folder containing the Dockerfile, run the following command:
##  Build the Docker Container
### If you prepare a new Dockerfile, navigate to the same directory as said file and run the Docker build command to start a new image build process. Remember to replace the <image name or image id> option with your tag name.

### docker build -t <image name or image id>

### Starts a new container from the image you just built using the Docker run command:

### docker run <image name or image id>

### Otherwise, run a pre-built image imported from Docker Hub. Let’s use the MySQL image that we pulled previously:

### docker run mysql