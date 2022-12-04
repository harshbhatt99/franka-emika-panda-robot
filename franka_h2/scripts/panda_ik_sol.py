#!/usr/bin/env python3

from __future__ import print_function 
import rospy 
import actionlib 
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal 
from trajectory_msgs.msg import JointTrajectoryPoint 

import math
from spatialmath.base import *
from spatialmath import SE3
import spatialmath.base.symbolic as sym
import numpy as np

import roboticstoolbox as rtb




def move_robot_arm(joint_values):

  arm_client = actionlib.SimpleActionClient('panda_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
 
  arm_client.wait_for_server()
     
  arm_goal = FollowJointTrajectoryGoal()
 
  arm_goal.trajectory.joint_names = ['panda_joint1', 'panda_joint2','panda_joint3' ,'panda_joint4', 'panda_joint5','panda_joint6','panda_joint7']
   
  point = JointTrajectoryPoint()
 
  point.positions = joint_values
  #point.velocities = [0.5,0.5,0.5,0.5,0.5,0.5,0.5]


  point.time_from_start = rospy.Duration(20)
 
  arm_goal.trajectory.points.append(point)
  print(arm_goal.trajectory.points)
 
  exec_timeout = rospy.Duration(100)
  prmpt_timeout = rospy.Duration(100)

  # arm_client.send_goal(arm_goal)
 
  arm_client.send_goal_and_wait(arm_goal, exec_timeout, prmpt_timeout)


panda = rtb.models.URDF.Panda()
# print(panda)

T = panda.fkine(panda.qz, end='panda_hand')
#print(T)
x = float(input("Enter X Co-ordinate: "))
y = float(input("Enter Y Co-ordinate: "))
z = float(input("Enter Z Co-ordinate: "))


point = SE3(x,y,z)
point_sol = panda.ikine_LM(point)
#print("IK Solution: ",point_sol)


if __name__ == '__main__':

  try:

    rospy.init_node('send_goal_to_arm_py')

    #move_robot_arm([point_sol[0] , point_sol[1] , point_sol[2] , point_sol[3] , point_sol[4]])
    move_robot_arm(point_sol[0])

    print("Robotic arm has successfully reached the goal!")
     
  except rospy.ROSInterruptException:
    print("Program interrupted before completion.", file=sys.stderr)

