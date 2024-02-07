#alias command shortcuts
alias turtle_launch="rosrun turtlesim turtlesim_node"
alias turtle_server="rosrun actionlib_tutorials turtle1_server.py"

alias move_turtle_1='rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "{linear:  {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}"'

turtle_move (){
  rosrun actionlib_tutorials turtle1_client.py $1

}

