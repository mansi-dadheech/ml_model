From centos:latest

RUN yum install wget -y
RUN yum install net-tools -y
RUN yum install python3 -y
RUN python3 -m pip --no-cache-dir install --upgrade \
    pip \
    setuptools
RUN pip3 install tensorflow
RUN pip3 install numpy
RUN pip3 install pillow
RUN pip3 install keras
RUN mkdir /python
