

Build docker container
```shell
docker build . -t socket_app
```

Rin the container with the application
```shell
docker run -p 3000:3000 -p 5000:5000 socket_app -v .:/socket_app
```