import rospy
from std_msgs.msg import String

def callback(s):
    print('I received', s)

rospy.init_node('my_sub')
rospy.Subscriber('my_topic', String, callback)

# Infinite loop
# Each time a message is received on a subscribed topic, the corresponding callback
# function is invoked 
rospy.spin()
