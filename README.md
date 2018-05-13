# rover-thetacontroller


# Build local container
docker build -t thetacontroller .

# Get camera info
Note: the camera is not recognized in live mode
docker run -it --device=/dev/bus/usb/`lsusb | grep Ricoh|awk {'print $2'}`/`lsusb | grep Ricoh|awk {'print $4'}|sed 's/:$//'` thetacontroller ptpcam -l


docker run -it -v `pwd`:/srv/rover-thetacontroller --device=/dev/bus/usb/`lsusb | grep Ricoh|awk {'print $2'}`/`lsusb | grep Ricoh|awk {'print $4'}|sed 's/:$//'` thetacontroller

# ptcam useful commands
Read camera info:
`ptpcam -l`
Get battery state:
`ptpcam --show-property=0x5001`

# ToDo
Clean Dockerfile-arm
Activate streaming mode
supervisor
environment variables
