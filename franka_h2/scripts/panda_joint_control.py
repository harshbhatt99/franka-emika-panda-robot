# #!/usr/bin/env python3
# import rospy
# from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
# import sys

# def perform_trajectory():
#     rospy.init_node('panda_trajectory_publisher')
#     contoller_name='panda_controller'
#     trajectory_publisher = rospy.Publisher(contoller_name,JointTrajectory, queue_size=10)
#     panda_joints = [-1.57 , 0.0 , 0.0 , -2.0 , 0.0 , 0.5 , 0.2]
#     goal_positions = panda_joints
#     rospy.loginfo("Goal Position set lets go ! ")
#     rospy.sleep(1)
#     print(goal_positions)


#     trajectory_msg = JointTrajectory()
    
#     trajectory_msg.joint_names = panda_joints
#     trajectory_msg.points.append(JointTrajectoryPoint())
#     trajectory_msg.points[0].positions = goal_positions
#     trajectory_msg.points[0].velocities = [0.2 for i in panda_joints]
#     trajectory_msg.points[0].accelerations = [0.05 for i in panda_joints]
    
#     trajectory_msg.points[0].time_from_start = rospy.Duration(3)
#     rospy.sleep(1)
#     print(trajectory_msg)
#     trajectory_publisher.publish(trajectory_msg)



# if __name__ == '__main__':
#     perform_trajectory()