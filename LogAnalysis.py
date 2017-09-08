#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: LogAnalysis.py
@time: 2017/09/08/9:45
1秒=1000毫秒=1000*1000微秒
"""
import time
with open("FMRoomSrv-AliSZSrv12-17-30-20.log","r") as f:
    line_list=f.readlines()
#info need to add
info_list=[]
for line in line_list:
    if "Session Accept" in line:
        info_list.append(line)
    elif "OnLoginReq" in line:
        info_list.append(line)
    elif "TryActiveToken2" in line:
        info_list.append(line)
    elif "GetUserRoleNotify" in line:
        info_list.append(line)
    elif "Get room mode" in line:
        info_list.append(line)
    elif "HandleSendUserListToUser" in line:
        info_list.append(line)
    elif "OnSessionClosed" in line :
        info_list.append(line)

def count_time(startTime,endTime):
        st=startTime.split(":")
        et=endTime.split(":")
        h=0
        m=0
        s=0
        if et[0]!=st[0]:
            h=int(et[0])-int(st[0])
        elif et[1]!=st[1]:
            m=int(et[1])-st(st[1])
        else:
            et_second_list=et[2].split(".")
            st_second_list = st[2].split(".")
            if et_second_list[0]!=st_second_list[0]:
                s=int(et_second_list[0])-int(st_second_list[0])
            else:
                last=int(et_second_list[1])-int(st_second_list[1])
        if h !=0 and m!=0 and s!=0:
            timestap=float(h*3600+m*60+s)+float(last)/1000000
        elif h ==0 and m!=0 and s!=0:
            timestap =float(m * 60 + s)+float(last)/1000000
        elif h==0 and m==0 and s!=0:
            timestap = float(s)+float(last)/1000000
        elif h==0 and m==0 and s==0:
            timestap = float(s) + float(last) / 1000000
        else:
            timestap=999999999999999999999
            print "时间差计算有误！！！"
        return timestap

def get_time_string(time_string):
    for i in time_string.split(" "):
        if ":" in i:
            return i

得分
# print info_list
for line in info_list:
    if "Session Accept" in line:
        SessionAccepTime=get_time_string(line.split("T")[0])

    elif "OnLoginReq" in line:

        OnLoginReqTime=get_time_string(line.split("T")[0])
        aa=count_time(SessionAccepTime,OnLoginReqTime)
        print aa


    elif "TryActiveToken2" in line:
        TryActiveToken2Time=line.split("T")[0]

    elif "GetUserRoleNotify" in line:
        GetUserRoleNotifyTime=line.split("T")[0]
    elif "Get room mode" in line:
        GetRoomModeTime=line.split("T")[0]



