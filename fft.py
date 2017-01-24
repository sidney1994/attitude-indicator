from __future__ import division
import numpy as np
import matplotlib as plt
import math

infile=open("C:\\Users\\123\\Desktop\\2016122813.txt","r")
#outfile=open("C:\\Users\\123\\Desktop\\fft1.txt","a")

ax=[0]*18070
ay=[0]*18070
az=[0]*18070
mx=[0]*18070
my=[0]*18070
mz=[0]*18070

def averagefilter(a,n):#nÎª½×Êı
    b=[0]*len(a)
    if n>=len(a):
        print "false"
    if n<=len(a):
        for i in range(n):
            b[i]=a[i]
        for i in range(n-1,len(a)):
            sum1=0
            for j in range(n):
                sum1=sum1+a[i-j]
                
            b[i]=sum1/n
            sum=0
    return b

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


i=0    
for line in infile:
    test=line.split(" ")
    time=float(test[10])
    test=test[:9]
    test1=[0]*9
    ax[i]=float(test[0])
    ay[i]=float(test[1])
    az[i]=float(test[2])
    mx[i]=float(test[3])
    my[i]=float(test[4])
    mz[i]=float(test[5])    
    
    i=i+1


b1=averagefilter(ax,4)
b2=averagefilter(ay,4)
b3=averagefilter(az,4)
b4= averagefilter(mx,4)
b5=averagefilter(my,4)
b6=averagefilter(mz,4)

for i in range(len(b1)):
    print hangxiang(b1[i],b2[i],b3[i],b4[i],b5[i],b6[i])

'''
for i in range(len(b1)):
    awrite=[b1[i],b2[i],b3[i],b4[i],b5[i],b6[i]]
    awrite=str(awrite)+str('\n')
    outfile.write(awrite)


a=np.array(a)
af=np.fft.fft(a)
absaf=abs(af)
print absaf[441000-2]
#for i in range(0,441000):
    #print absaf[i]

#for i in range(0,440999):
#    awrite=absaf[i]
    
#    awrite=str(awrite)
#    outfile.write(awrite)
''' 
outfile.close()
#infile.close()
  
