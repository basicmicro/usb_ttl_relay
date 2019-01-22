from roboclaw_modified_for_3 import Roboclaw
from time import sleep

roboclaw = Roboclaw("COM6",38400)
roboclaw.Open()

while(1):

	roboclaw.ForwardM1(128, 63)
	sleep(2)
	roboclaw.ForwardM1(128, 0)
	sleep(2)

	#roboclaw.ForwardM1(129, 63)
	#sleep(2)
	#roboclaw.ForwardM1(129, 0)
	#sleep(2)


