try:
    from MC2000B_COMMAND_LIB import *
except OSError as ex:
    print("Warning:",ex)
    
import time

def CommonFunc(serialNumber):
    hdl = MC2000BOpen(serialNumber,115200,3)
    
    if(hdl < 0):
        print("Connect ",serialNumber, "fail" )
        return -1;
    else:
        print("Connect ",serialNumber, "successful")
     
    result = MC2000BIsOpen(serialNumber)
    if(result<0):
         print("Open failed ")
    else:
         print("MC2000B Is Open ")
     
    return hdl

def CheckFunctions(hdl):
        
    result=MC2000BSetBladeType(hdl,3) # Blade type 0:MC1F2, 1:MC1F10, 2:MC1F15, 3:MC1F30, 4:MC1F60, 5:MC1F100, 6:MC1F10HP, 7:MC1F2P10, 8:MC1F6P10, 9:MC1F10A, 10:MC2F330, 11:MC2F47, 12:MC2F57B, 13:MC2F860, 14:MC2F5360 
    if(result<0):
        print("Set Blade Type fail",result)
    else:
        print("Set Blade Type :", "MC1F30")    
    result=MC2000BSetFrequency(hdl,523)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "523Hz")
    time.sleep(2)
    result=MC2000BSetFrequency(hdl,622)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "622Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,698)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "698Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,523)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "523Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,622)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "622Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,740)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "740Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,622)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "622Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,523)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "523Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,622)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "622Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,698)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "698Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,622)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "622Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,523)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "523Hz")
    time.sleep(1)
    result=MC2000BSetFrequency(hdl,400)# Frequency range dependent on blade type
    if(result<0):
        print("Set Frequency fail",result)
    else:
        print("Set Frequency :", "500Hz")
    time.sleep(1)

    
     
    result=MC2000BSetReference(hdl,0)# Dependent on blade type. Reference mode 0:internal,1:external / Reference high precision mode 0:InternalOuter 1:InternalInner 2:ExternalOuter 3:ExternalInner 
    if(result<0):
        print("Set Reference Mode fail",result)
    else:
        print("Set Reference Mode :", "0")
    result=MC2000BSetEnable(hdl,1)# enable state 1:enable, 0:disable
    if(result<0):
        print("Set Enable State fail",result)
    else:
        print("Set Enable State:", "enable") 
    result=MC2000BSetReferenceOutput(hdl,0) # Output mode dependent on blade type
    if(result<0):
        print("Set Output mode",result)
    else:
        print("Set Output mode :", "0")
    result=MC2000BSetVerbose(hdl,1) # When verbose mode is set to 1, status messagesare output on the USB
    if(result<0):
        print("Set Verbose Mode fail",result)
    else:
        print("Set Verbose Mode :", "1")
    print("---------------------------Paras set finnished-------------------------")
     
    bladetype=[0]
    result= MC2000BGetBladeType(hdl,bladetype)
     
    BladeTypeList={0:"MC1F2",1:"MC1F10",2:"MC1F15",3:"MC1F30",4:"MC1F60",5:"MC1F100",6:"MC1F10HP",7:"MC1F2P10",8:"MC1F6P10",9:"MC1F10A",10:"MC2F330",11:"MC2F47",12:"MC2F57B",13:"MC2F860",14:"MC2F5360"}
    if(result<0):
        print("Get Blade Type fail",result)
    else:
        print("Get Blade Type :",BladeTypeList.get(bladetype[0]))
    frequency=[0]
    result=MC2000BGetFrequency(hdl,frequency)
    if(result<0):
        print("Get Frequency fail",result)
    else:
        print("Get Frequency :",frequency)
    reference=[1]
    result=MC2000BGetReference(hdl,reference)
    if(result<0):
        print("Get Reference Mode fail",result)
    else:
        print("Get Reference Mode :",reference)
    enable=[0]
    enableList={0:"disable",1:"enable"}
    result=MC2000BGetEnable(hdl,enable)
    if(result<0):
        print("Get Enable State",result)
    else:
        print("Get Enable State :",enableList.get(enable[0]))
    referenceOutput=[0]
    result=MC2000BGetReferenceOutput(hdl,referenceOutput)
    if(result<0):
        print("Get Output Mode fail",result)
    else:
        print("Get Output Mode :",referenceOutput)
    verbose=[0]
    result=MC2000BGetVerbose(hdl,verbose)
    if(result<0):
        print("Get Verbose Mode fail",result)
    else:
        print("Get Verbose Mode :",verbose)
    print("---------------------------Paras get finnished-------------------------")
def main():
    print("*** MC2000B device python example ***")
    try:
        devs = MC2000BListDevices()
        print(devs)
        if(len(devs)<=0):
            print('There is no devices connected')
            exit()
        MC2000B= devs[0]
        hdl=CommonFunc(MC2000B[0])
        print("---------------------------Device initialize finished-------------------------")
        CheckFunctions(hdl)
        MC2000BClose(hdl)
    except Exception as ex:
        print("Warning:", ex)
    print("*** End ***")
    input()
main()
