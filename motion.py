from aktoren.motor import Motor as MOTOR

"""
Diese Klasse stellt alle Motion-Funktionen fuer den Erinaco Roboter zur Verfuegung.
@author kf
@since 2017-04-15
"""
class Motion(object):
        def __init__(self):
                self.motorLeft=MOTOR(23,18,1) #Initialisierung des linken Motors
                self.motorRight=MOTOR(24,25,0) #Initialisierung des rechten Motors
        def turnLeft(self):
                self.motorRight.forward()
                self.motorLeft.backward()
        def turnRigh(self):
                self.motorRight.backward()
                self.motorLeft.forward()
        def forward(self):
                self.motorRight.forward()
                self.motorLeft.forward()
        def backward(self):
                self.motorRight.backward()
                self.motorLeft.backward()
        def stop(self):
                self.motorRight.stop()
                self.motorLeft.stop()

