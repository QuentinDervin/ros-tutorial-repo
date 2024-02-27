docker_up(){
  cd ~/ros-tutorial-repo/docker 
  docker-compose up &
  sleep 5
  gnome-terminal -- docker-compose exec -it ros-source-test bash
}

alias docker_exec="docker-compose exec -it ros-source-test bash"
alias docker_down="docker-compose down"

docker_build(){
  cd ~/ros-tutorial-repo/docker
  docker build -t $1 .
 }


docker_push(){
  docker push quentindervin/ros-turtlebot:$1
}

docker_pull(){
  docker pull quentindervin/ros-turtlebot:$1
}
