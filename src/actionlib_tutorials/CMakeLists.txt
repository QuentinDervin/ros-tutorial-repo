cmake_minimum_required(VERSION 2.8.3)

project(actionlib_tutorials)

find_package(catkin REQUIRED COMPONENTS
	roscpp 
	std_msgs
	actionlib_msgs
	actionlib
	message_generation
	)
find_package(Boost REQUIRED COMPONENTS
	system
	)
	
	
add_action_files(
  DIRECTORY action
  FILES Fibonacci.action
  FILES Turtle1.action
)


generate_messages(
  DEPENDENCIES actionlib_msgs std_msgs  # Or other packages containing msgs
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs std_msgs message_runtime
)

catkin_install_python(PROGRAMS src/fibonacci_server.py src/fibonacci_client.py src/turtle1_client.py src/turtle1_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(include ${catkin_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})

#add_executable(
 # src/fibonacci_server.py 
  #src/turtle1_client.py 
  #src/turtle1_server.py)

#target_link_libraries(
  #fibonacci_server 
  #${catkin_LIBRARIES}
  #turtle1_server
  #${catkin_LIBRARIES}
#)

#add_dependencies(
  #fibonacci_server
  #turtle1_server
  #${actionlib_tutorials_EXPORTED_TARGETS}
#)
