#!/usr/bin/python
import time
import datetime
import pymon_lib
from pymon_lib import *


print("Version 0.1");
#sendmail("test");
while True:
	date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M:%S" )
	print("Date: "+date+" Temp: "+str(get_tempC()));
	time.sleep(1);




