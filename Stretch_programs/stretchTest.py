#!/usr/bin/env python

import time
import stretch_body.robot
from stretch_body.hello_utils import ThreadServiceExit

robot = stretch_body.robot.Robot()
robot.startup()

if not robot.is_calibrated():
    robot.home() #blocking

for i in range(10):
	robot.pretty_print()
	time.sleep(0.25)

robot.stop()