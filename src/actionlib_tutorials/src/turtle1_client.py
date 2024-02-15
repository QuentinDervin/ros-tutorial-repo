#! /usr/bin/env python

from __future__ import print_function
from actionlib_tutorials.msg import Turtle1Goal, Turtle1Result, Turtle1Feedback
import actionlib_tutorials.msg

import rospy
import actionlib
import yaml

import os
import sys



def turtle1_client(motion_call):

    
    client = actionlib.SimpleActionClient('move', actionlib_tutorials.msg.Turtle1Action)
    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    #reads the yaml file and gets the motions dictionary
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, 'ros-tutorial-repo/src/actionlib_tutorials/config/turtle1_moves.yaml')
    file_name = os.path.abspath(os.path.realpath(file_name))
    with open(file_name, 'r') as file:
        motion = yaml.safe_load(file)

    # Creates a goal to send to the action server.
    # Uses str() and eval() serialization method for transport
    
    try:
        #print(motion[motion_call])
        pickle_motion = motion[motion_call]
        #print("picklestring test" + str(pickle_motion))
        goal = Turtle1Goal(str(pickle_motion))
    except:
        print("{} is not a valid motion".format(motion_call))
        return
    

    # Sends the goal to the action server.
    client.send_goal(goal)
    
    # Waits for the server to finish performing the action.
    client.wait_for_result()
    
    # Prints out the result of executing the action
    return client.get_result()  

if __name__ == '__main__':
    if len(sys.argv) == 2:
        motion_call = str(sys.argv[1])
    try:
        # Turotial: "Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS"
        rospy.init_node('turtle1_client_py')
        result = turtle1_client(motion_call)
        print("Result: " + str(result))
    except rospy.ROSInterruptException:
        print("program interrupted before completion")