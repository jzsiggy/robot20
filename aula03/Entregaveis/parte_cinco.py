#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import Twist, Vector3


contador = 0

# Função Twist recebe dois elementos 1: Vel_linear, 2: Vel_angular
# Vector3 recebe valores nos eixos x, y, z

# Parâmetros de seguir em frente
reto = Twist(Vector3(0.2,0,0), Vector3(0,0,0))
# Parâmetros para parar
parar = Twist(Vector3(0,0,0), Vector3(0,0,0))
# Parâmetros para virar
virar = Twist(Vector3(0,0,0), Vector3(0,0,0.5))




contador = 0
if __name__ == "__main__":
    rospy.init_node("roda_exemplo")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():
        	if contador <= 15:
	            
	            pub.publish(reto)
	            rospy.sleep(1.5)

	            pub.publish(parar)
	            rospy.sleep(0.5)

	            pub.publish(virar)
	            rospy.sleep(3.0)

	            contador +=1
	        else:
	        	pub.publish(parar)
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")