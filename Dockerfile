FROM ubuntu:20.04

RUN sudo apt update -y
RUN sudo apt install python3.10

WORKDIR /home
RUN mkdir source_stream

WORKDIR source_stream
RUN mkdir data
COPY data/test.csv data
COPY server_test.py .

EXPOSE 3000
CMD ["python3","server_test.py"]
