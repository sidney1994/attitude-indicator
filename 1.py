# -*- coding: utf8-*-
from __future__ import division
import numpy as np
import matplotlib as plt
import math

infile=open("F:\\20170123.txt","r")
outfile=open("C:\\Users\\123\\Desktop\\data\\test.txt","w")
def normalization(x1,x2,x3):
    a=pow(x1,2)+pow(x2,2)+pow(x3,2)
    if(a==0):
        print "normalization processing is fail."
    if(a!=0):
        x=[x1/pow(a,0.5),x2/pow(a,0.5),x3/pow(a,0.5)]
        
        return x


def hangxiang( ax, ay, az, mx, my, mz):
    a=normalization(ax,ay,az)
    
    m=normalization(mx,my,mz)
    
    a=np.array(a)
    m=np.array(m)
    n2=m-np.dot(a,m)*a
    
    n21=normalization(n2[0],n2[1],n2[2])
    x=np.array([1,0,0])
    n3=x-np.dot(a,x)*a
    
    n31=normalization(n3[0],n3[1],n3[2])
    hangxiang=math.acos(np.dot(n31,n21))*57.29578049
    #print hangxiang
    '''
    if(n2[0]*n3[1]-n2[1]*n3[0]>0):
        print "false"
    else:
        print "true"'''
    return hangxiang



for line in infile:
    test=line.split(" ")
    time=int(test[10])
    test=test[:9]
    test1=[0]*9
    test1[0]=float(test[0])
    test1[1]=float(test[1])
    test1[2]=float(test[2])
    test1[3]=float(test[3])
    test1[4]=float(test[4])
    test1[5]=float(test[5])
    test1[6]=float(test[6])/16.8
    test1[7]=float(test[7])/16.8
    test1[8]=float(test[8])/16.8
    test=test1
    #点乘是numpy中的np.dot
    #叉乘是numpy中的np.cross
    result=hangxiang(test[0],test[1],test[2],test[3],test[4],test[5])
    outfile.write(str(result)+'\n')
   

    


infile.close()
outfile.close()


