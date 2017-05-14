# FROM armhfbuild/debian
FROM resin/rpi-raspbian
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-venv \
    subversion \
    libtool \
    make \
    automake \
    tar \
    libusb-dev

ADD https://downloads.sourceforge.net/project/libptp/libptp2/libptp2-1.2.0/libptp2-1.2.0.tar.gz /
RUN tar zxvf /libptp2-1.2.0.tar.gz
RUN cd /libptp2-1.2.0 && \
    ./configure && \
    make && \
    make install && \
    ldconfig

# RUN svn checkout svn://svn.code.sf.net/p/libptp/code/trunk /libptp-code
# RUN cd /libptp-code && \
# ./autogen.sh && \
# ./configure && \
# make && \
# make install && \
# ldconfig

# ptpcam -l

# Virtualenv and pip requirements
ADD thetacontroller/requirements.txt /srv/rover-thetacontroller/requirements.txt

RUN python3 -m venv /opt/rover-thetacontroller && \
    cd /srv/rover-thetacontroller && \
    /opt/rover-thetacontroller/bin/pip install -r requirements.txt

ADD thetacontroller /srv/rover-thetacontroller

# Packages to remove
# subversion
# tar
# make

WORKDIR /srv/rover-thetacontroller
RUN echo "source /opt/rover-thetacontroller/bin/activate" >> /root/.bashrc
