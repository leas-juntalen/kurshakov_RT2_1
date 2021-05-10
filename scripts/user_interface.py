import rospy
import time
from rt2_assignment1.srv import Command

def main():
    rospy.init_node('user_interface')
    ui_client = rospy.ServiceProxy('/user_interface', Command)
    time.sleep(10)
    rate = rospy.Rate(20)
    x = int(input("\nPrint 1 to start the robot "))
    while not rospy.is_shutdown():
        if (x == 1):
            ui_client("start")
            x = int(input("\nPrint 0 to stop the robot when the position will be reached\nPrint any digit to stop the robot right now "))
        elif (x == 0):
            print("Please wait, the robot is going to stop when the position will be reached")
            ui_client("stop")
            x = int(input("\nPrint 1 to start the robot\nPrint any digit to stop the robot right now "))
        else:
            ui_client("stop_now")
            x = int(input("\nPrint 1 to start the robot "))
            
if __name__ == '__main__':
    main()
