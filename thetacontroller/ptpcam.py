import subprocess

'''
References for USB commands can be found here
https://developers.theta360.com/en/docs/v2/usb_reference/
'''
def getBatteryState():
    # ptpcam returns an output like this:
    # Camera: RICOH THETA S
    # 'Battery Level' is set to: 100
    ptpbattery = subprocess.Popen(["ptpcam", "--show-property=0x5001"], stdout=subprocess.PIPE)

    # keeping only the second line
    ptpbattery = ptpbattery.stdout.readlines()[2]

    # Splitting the string
    ptpbattery = ptpbattery.split()

    return(ptpbattery[-1])

## example of taking a picture
def takePicture():
    subprocess.call("ptpcam -c", shell=True)

# takePicture()

def getInfo():
    # example of grabbing device info and using it in your python program.
    ptpinfo = subprocess.Popen(["ptpcam", "--info"], stdout=subprocess.PIPE)
    for line in ptpinfo.stdout.readlines():
        print(line.rstrip())

def getState():
    # example of grabbing device info and using it in your python program.
    ptpstate = subprocess.Popen(["ptpcam", "--info"], stdout=subprocess.PIPE)

# although this simply prints to stdout, you can parse
# the response for your program
# for line in ptpinfo.stdout.readlines():
#     print(line.rstrip())
#
# # find the last picture taken. Modify to parse for date or other
# files = []
# listFiles = subprocess.Popen(["ptpcam", "-L"], stdout=subprocess.PIPE)
# for line in listFiles.stdout.readlines():
#     files.append(line.rstrip())
# print("listFiles: " + str(listFiles))
# print("Files:" + str(files))
#
# lastLine = files[len(files) - 2].split(" ")
# lastPicture = lastLine[0][:-1]
#
# print("The handle for the last picture taken is " + lastPicture)
#
#
# # download the picture
# ptpcommand = "ptpcam --get-file=" + lastPicture
#
# subprocess.call(ptpcommand, shell=True)
