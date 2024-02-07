#! /usr/bin/env python

import rospy
import actionlib
import actionlib_tutorials.msg


from geometry_msgs.msg import Twist


class Turtle1Action(object):
    # create messages that are used to publish feedback/result
    _feedback = actionlib_tutorials.msg.Turtle1Feedback()
    _result = actionlib_tutorials.msg.Turtle1Result()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, actionlib_tutorials.msg.Turtle1Action, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
      
    def execute_cb(self, goal):
        #setting up the publisher variable

        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10, latch=True)

        # helper variables
        r = rospy.Rate(1)
        success = True

        # publish info to the console for the user
        rospy.loginfo('%s: Executing, creating turtle1 move sequence of %s' % (self._action_name, goal))
        
        # sort the string/goal/input from client
        goalString = str(goal)
        #rudimentary solution to the "move: " and quotes embedded into the string
        dict_goal = goalString[7:-1]
        #finishes deserializing
        motion = eval(dict_goal)
        rospy.loginfo("Motion dictionary recieved:" + str(motion))

        
        
        # start executing the action

        for key in (motion): 
            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break

            vel_msg = Twist()
            #print(vel_msg)

            if key == "forward":
                #print("forward placeholder")
                #publish to cmd_vel topic
                vel_msg.linear.x = float(motion["forward"])
                rospy.loginfo(vel_msg)
                pub.publish(vel_msg)

                #print("forward placeholder 2")
            elif key == "backward":
                #publish to cmd_vel toppic using motion["backward"]
                vel_msg.linear.x = float(-abs(motion["backward"]))
                rospy.loginfo(vel_msg)
                pub.publish(vel_msg)
            elif key == "up":
                #publish to cmd_vel toppic using motion["backward"]
                vel_msg.linear.y = float(motion["up"])
                rospy.loginfo(vel_msg)
                pub.publish(vel_msg)
            elif key == "down":
                #publish to cmd_vel toppic using motion["backward"]
                vel_msg.linear.y = float(-abs(motion["down"]))
                rospy.loginfo(vel_msg)
                pub.publish(vel_msg)
            elif key == "rotate":
                vel_msg.angular.z = float(motion["rotate"])
                rospy.loginfo(vel_msg)
                pub.publish(vel_msg)

            else:
                #tp to center?
                rospy.loginfo("Unknown movement")


            

            #feedback method notes from other tutorial work:
            
            self._feedback.moves.append(key)
            # publish the feedback
            self._as.publish_feedback(self._feedback)

            # from tutorial: "this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes"
            r.sleep()
          
        if success:
            self._result.moves = self._feedback.moves
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)
        
if __name__ == '__main__':
    rospy.init_node('move')
    server = Turtle1Action(rospy.get_name())
    rospy.spin()