# rover-thetacontroller


# Build local container
docker build -t thetacontroller .

# Get camera info
Note: the camera is not recognized in live mode
docker run -it --device=/dev/bus/usb/`lsusb | grep Ricoh|awk {'print $2'}`/`lsusb | grep Ricoh|awk {'print $4'}|sed 's/:$//'` thetacontroller ptpcam -l

# read camera info
ptpcam -l
