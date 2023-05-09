FROM ubuntu:20.04
RUN apt-get update && apt-get install -y nmap #Install the nmap package, which provides the ncat program used here.
CMD ncat -l 2000 -k --exec /bin/cat # Run the ncat program by default when starting the image.
