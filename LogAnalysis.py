#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: LogAnalysis.py
@time: 2017/09/08/9:45
"""
import time


with open("FMRoomSrv.log","r") as f:
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



for line in info_list:


    if "Session Accept" in line:
        SessionAccepTime=line.split("T")[0]
        print line
    elif "OnLoginReq" in line:
        OnLoginReqTime=line.split("T")[0]

        satl=SessionAccepTime.split(":")
        ortl=OnLoginReqTime.split(":")

        h=0
        m=0
        s=0

        if satl[0]!=ortl[0]:
            h=int(ortl[0])-int(satl[0])
        elif satl[1]!=ortl[1]:
            m=int(ortl[1])-int(satl[1])
        else:

            ortl_second_list=ortl[2].split(".")
            satl_second_list = satl[2].split(".")
            if ortl_second_list[0]!=satl_second_list[0]:
                s=int(ortl_second_list[0])-int(satl_second_list[0])
            else:
                last=int(ortl_second_list[1])-int(satl_second_list[1])

        print line

        print "Session Accept 跟 OnLoginReq 时间差是："
        print last
        # print "{0}:{1}:{2}.{3}".format(h,m,s,last)
        break
    elif "TryActiveToken2" in line:
        TryActiveToken2Time=line.split("T")[0]

    elif "GetUserRoleNotify" in line:
        GetUserRoleNotifyTime=line.split("T")[0]
    elif "Get room mode" in line:
        GetRoomModeTime=line.split("T")[0]



