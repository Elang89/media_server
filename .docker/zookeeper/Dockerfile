FROM ubuntu:18.04
LABEL maintainer="Rad <matt.m@radskunkworks.com>"

ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64/
EXPOSE 22
ENV ZK_VERSION '3.6.4'
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
RUN export PATH=$JAVA_HOME/bin:$PATH
EXPOSE 2181 2888 3888

# Download, install, and set up zookeeper
COPY install.sh /run/
COPY downloads.sh /run/
RUN chmod +x /run -R
RUN /run/install.sh
RUN /run/downloads.sh "/zookeeper" "${ZK_VERSION}"
RUN chmod +x /zookeeper -R

# Finish up with containerized features
WORKDIR "/zookeeper"
VOLUME ["/zookeeper"]
HEALTHCHECK CMD ping -c3 -i 10 127.0.0.1
CMD ["/bin/bash", "/zookeeper/bin/zkServer.sh", "start-foreground"]
