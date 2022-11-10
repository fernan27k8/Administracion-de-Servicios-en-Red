#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("traficoRED.rrd",
                     "--start",'N',
                     "--step",'300',
                     "DS:inoctets:COUNTER:120:U:U",
                     "DS:inoctet:COUNTER:120:U:U",
                     "DS:inocte:COUNTER:120:U:U",
                     "DS:inoct:COUNTER:120:U:U",
                     "DS:inoc:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:5:500",
                     "RRA:AVERAGE:0.5:1:1000")

if ret:
    print (rrdtool.error())