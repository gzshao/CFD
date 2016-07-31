# This code is for measuring data off Keithley 2602b sourcemeter
# it should be implemented in Python 3
# requires module pyVisa

import visa
import time
from openpyxl import Workbook

rm=visa.ResourceManager()
keithley=rm.open_resource("TCPIP::169.254.000.100::5025::SOCKET")
keithley.read_termination = '\n'
#keithley.query("*IDN?")
keithley.clear()
#keithley.timeout=3
#keithley.baud_rate=9600
#keithley.data_bits=8
#keithley.stop_bits=1
#keithley.term_chars = '\n'
#keithley.timeout = 65

timeLength=60
dataSize=timeLength*2

keithley.write("*rst; status:preset; *cls")   # this is initialization and reset message
keithley.write("smua.measure.count = dataSize")
keithley.write("smua.measure.interval = 0.5")
keithley.write("format.data = format.ASCII")
keithley.write("format.asciiprecision = 6")

keithley.write("smua.measure.r(smua.nvbuffer1)")

#count down
for i in range(timeLength):
    time.sleep(1)
    print(timeLength-1)

keithley.write("beeper.enable=beeper.ON")
keithley.write("beeper.beep(0.2,2400)")
resist = keithley.ask("printbuffer(1, 10, smua.nvbuffer1)")

#resist = keithley.query("printbuffer(1, 1, smua.nvbuffer1)")
#keithley.write("numberOfReadings = smua.nvbuffer1.n")
#keithley.query("print(numberOfReadings)")

#keithley.write("savebuffer(smua.nvbuffer1,'csv','mybuffer.csv')")
#keithley.query("print(smua.measure.r())")

# save to an .xlsx file
wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(resist.split(','))
wb.save('keithley.xlsx')

# to-do: plot the result as a function of time
