import rospy
from std_msgs.msg import String

rospy.init_node('my_pub')
pub = rospy.Publisher('my_topic', String, queue_size=10)

# 2 HZ
# Sleep about 0.5 seconds
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish("Hello ROS")
    rate.sleep()