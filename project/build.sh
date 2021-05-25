git pull
docker stop prj
docker rm prj
docker rmi prj
docker build -t prj .
docker run --name prj -p 8100:8282 -d --restart always --network dockers_default -v /home/debian/volumes/html/cdn/prj:/www -e MONGO=mongodb  prj

