#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:18:46 2018

@author: wyw
"""

import math
import sys
import re

def main():
    star=sys.argv[1]
    offsetx=float(sys.argv[2])
    offsety=float(sys.argv[3])
    offsetz=float(sys.argv[4])
    debug=sys.argv[5]
    apix=float(sys.argv[6])
    new_star=sys.argv[7]
    header_dict={}
    starf=open(star,"r")
    new_starf=open(new_star,"w")
    starf_lines=starf.readlines()
    for i in range(0,100):
        tmp_line=starf_lines[i]
        match=re.match(r'_rln(\w+)\s+#(\d+)',tmp_line)
        if match:
            header_dict[match.group(1).lower()]=int(match.group(2))-1
    dU_index=int(header_dict['defocusu'])
    dV_index=int(header_dict['defocusv'])
    phi_index=int(header_dict['anglerot'])
    theta_index=int(header_dict['angletilt'])
    psi_index=int(header_dict['anglepsi'])
    for i in range(0,len(starf_lines)):
        sl=starf_lines[i].split()
        try:
            dU=float(sl[dU_index])
            dV=float(sl[dV_index])
            phi=float(sl[phi_index])/180*math.pi
            theta=float(sl[theta_index])/180*math.pi
            psi=float(sl[psi_index])/180*math.pi
        except (ValueError,IndexError):
            new_starf.write(starf_lines[i])
            continue
        r11=math.cos(psi)*math.cos(theta)*math.cos(phi)-math.sin(psi)*math.sin(phi)
        r12=math.cos(psi)*math.cos(theta)*math.sin(phi)+math.sin(psi)*math.cos(phi)
        r13=-math.cos(psi)*math.sin(theta)
        
        r21=-math.sin(psi)*math.cos(theta)*math.cos(phi)-math.cos(psi)*math.sin(phi)
        r22=-math.sin(psi)*math.cos(theta)*math.sin(phi)+math.cos(psi)*math.cos(phi)
        r23=math.sin(psi)*math.sin(theta)
        
        r31=math.sin(theta)*math.cos(phi)
        r32=math.sin(theta)*math.sin(phi)
        r33=math.cos(theta)
        
        new_x=r11*offsetx+r12*offsety+r13*offsetz
        new_y=r21*offsetx+r22*offsety+r23*offsetz
        new_z=r31*offsetx+r32*offsety+r33*offsetz
        
        if(debug=="1"):
            dU_new=dU+new_z*apix
            dV_new=dV+new_z*apix
        else:
            dU_new=dU-new_z*apix
            dV_new=dV-new_z*apix
        sl[dU_index]=dU_new
        sl[dV_index]=dV_new
        for i in range(0,len(sl)):
            new_starf.write(str(sl[i])+"\t")
        new_starf.write("\n")
    '''print dU_index
    print dV_index
    print phi_index
    print theta_index
    print psi_index'''
    
    
main()
