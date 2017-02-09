from __future__ import division
import numpy as np
import matplotlib as plt
import math

infile=open("C:\\Users\\123\\Desktop\\2016122813.txt","r")
outfile=open("C:\\Users\\123\\Desktop\\fft1.txt","a")
ax=[0]*18070
ay=[0]*18070
az=[0]*18070
mx=[0]*18070
my=[0]*18070
mz=[0]*18070
kp=100
ki=0.002
halfT=0.1
q0=1
q1=0
q2=0
q3=0
exint=0
eyint=0
ezint=0
def normalization(x1,x2,x3):
    a=pow(x1,2)+pow(x2,2)+pow(x3,2)
    if(a==0):
        print "normalization processing is fail."
    if(a!=0):
        x=[x1/pow(a,0.5),x2/pow(a,0.5),x3/pow(a,0.5)]
        return x
def normalization1(x1,x2,x3,x4):
    a=pow(x1,2)+pow(x2,2)+pow(x3,2)+pow(x4,2)
    if(a==0):
        print "normalization processing is fail."
    if(a!=0):
        x=[x1/pow(a,0.5),x2/pow(a,0.5),x3/pow(a,0.5),x4/pow(a,0.5)]
        return x

def IMU(gx,gy,gz,ax,ay,az):
    a=normalization(ax,ay,az)
    g=normalization(gx,gy,gz)
    ax=a[0]
    ay=a[1]
    az=a[2]
    gx=g[0]
    gy=g[1]
    gz=g[2]
    vx=2*(q1*q3-q0*q2)
    vy=2*(q0*q1+q2*q3)
    va=q0*q0-q1*q1-q2*q2+q3*q3
    ex=(ay*vz-az*vy)
    ey=(az*vx-ax*vz)
    ez=(ax*vy-ay*vx)
    exint=exint+ex*ki
    eyint=eyint+ey*ki
    ezint=ezint+ez*ki
    gx=gx+kp*ex+exint
    gy=gy+kp*ey+ezint
    gz=gz+kp*ez+ezint
    q0=q0+(-q1*gx-q2*gy-q3*gz)*halfT
    q1=q1+(q0*gx+q2*gz-q3*gy)*halfT
    q2=q2+(q0*gy-q1*gz+q3*gx)*halfT
    q3=q3+(q0*gz+q1*gy-q2*gx)*halfT
    q=normalization1(q0,q1,q2,q3)
    pitch=asin(-2 * q1 * q3 + 2 * q0* q2)* 57.29578049
    roll = atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1)* 57.29578049
    yaw = atan2(2*(q1*q2 + q0*q3),q0*q0+q1*q1-q2*q2-q3*q3) *  57.29578049
    x=[pitch,roll,yall]
    return x
