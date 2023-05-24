#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub = rospy.Publisher('/my_robot/base_lidar_to_motor_joint_position_controller/command', Float64, queue_size=10)
    rospy.init_node('lidar_position_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    turn_left = False
    turn_right = True
    i = 0
    while not rospy.is_shutdown():
        
        pub.publish(i)

        rate.sleep()

        if turn_left:
            if i < math.pi/3:
                i += 0.02
            else:
                turn_left = False
                turn_right = True
        if turn_right:
            if i > - math.pi/3:
                i -= 0.02
            else:
                turn_right = False
                turn_left = True

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass