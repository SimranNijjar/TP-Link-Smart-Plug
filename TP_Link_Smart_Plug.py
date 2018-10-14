#TP Link Smart Plug - Energy Monitoring for YuMi Work Cell
#Author: Simran Nijjar

from pyHS100 import Discover, SmartPlug
from pprint import pformat as pf

#Smart Plug Discovery
for dev in Discover.discover().values():
    print(dev)


#Connect to Smart Plug (IP address determined by Discover)
plug = SmartPlug("10.0.2.36")

#Get Plug Information
##print("Hardware: %s" % pf(plug.hw_info))
##print("System Information: %s" % pf(plug.get_sysinfo()))

#Get Plug Status
print("Current State: %s" % plug.state)

#Turn Plug Off
plug.turn_off()

#Turn Plug On
######plug.turn_on()

#Energy Monitoring Data
print("Current Consumption: %s" % plug.get_emeter_realtime())
print("Per Day: %s" % plug.get_emeter_daily(year=2018, month=9))
print("Per Month: %s" % plug.get_emeter_monthly(year=2018))
