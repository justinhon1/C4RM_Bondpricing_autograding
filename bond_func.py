# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def Bond(y,face,couponRate,m,ppy=1):   
    PV =((face*couponRate/ppy*(1-(1+y/ppy)**(-ppy*m)))/(y/ppy)) + face*(1+(y/ppy))**(-ppy*m)
    return PV
