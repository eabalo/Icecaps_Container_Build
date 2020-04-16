FROM continuumio/anaconda3
#FROM nvidia/cudagl:10.2-runtime-centos7

USER 0

RUN apt-get -y install libgl1-mesa-glx

RUN cd /opt; echo $PWD; git clone https://github.com/microsoft/icecaps.git -v;

ADD setup.py /opt/icecaps

RUN cd /opt/icecaps; pip install -r /opt/icecaps/requirements.txt; pip install .

RUN chmod -R 777 /opt/icecaps

LABEL cudagl and anaconda3 with icecaps