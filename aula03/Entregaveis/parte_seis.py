#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

distancia = 0

def scaneou(dado):
    print("Faixa valida: ", dado.range_min , " - ", dado.range_max)
    print("Leituras:")
    print(np.array(dado.ranges).round(decimals=2))
    #print("Intensities")
    #print(np.array(dado.intensities).round(decimals=2))
    global distancia
    distancia = dado.ranges[0]


if __name__=="__main__":

    rospy.init_node("le_scan")

    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3)
    recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)

    r = rospy.Rate(5.0)


    while not rospy.is_shutdown():

        if distancia <= 1.0:
            velocidade = Twist()
            velocidade.linear.x = -0.3
            velocidade_saida.publish(velocidade)
            r.sleep()
        elif distancia >= 1.02:
            velocidade = Twist()
            velocidade.linear.x = 0.3
            velocidade_saida.publish(velocidade)
            r.sleep()