--Configure a 10-point source voltage sweep
smua.trigger.source.linearv(10,100,10)
smua.trigger.source.action=smua.ENABLE

-- configure TRIG key press as input trigger for source action
smua.trigger.source.stimulus=display.trigger.EVENT_ID

--command SMU to execute a single 10-point sweep
smua.trigger.count=10
smua.trigger.arm.count=1

--Turn on the output in preparation for the sweep
smua.source.output=smua.OUTPUT_ON

--start the sweep and clear the event detectors
smua.trigger.initiate()

-- The SMU will wait for the front panel TRIG key press before executing each source action
-- wait for the sweep to complete
waitcomplete()