FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt install -y python3.10

WORKDIR /home
RUN mkdir source_stream

WORKDIR source_stream
RUN mkdir data
COPY data/test.csv data
COPY server_test.py .

EXPOSE 3000
CMD ["python3","server_test.py"]
