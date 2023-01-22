# Video Stream Manager

## Description
This project is a video stream manager for ant media server. Below this description
there is a set of steps that describes how to use this project. 

## Steps before running 

1. Create an AWS account, and set up a user for S3 with read and write permissions. 
2. Create an .env file for the `server` and `backup` folders, please follow the the structures outlined in their respective .env.examples
3. Run `python -m venv .venv` for the backup folder and then run `pip install -r requirements.txt` while present on the directory of that folder. 
4. `cd` to the `.docker` folder and build each docker image
   1.  `cd` to the kafka directory and run `docker build -t kafka .`
   2.  `cd` to the zookeeper directory and run `docker build -t zookeeper .`
   3.  `cd` to the media_server directory and run `export ZIP_FILE=ant-media-server-community-2.5.1.zip` then run `docker build --network=host -t antmediaserver --build-arg AntMediaServer=$ZIP_FILE .`
   4.  `cd` to the gstreamer directory and run `docker build -t gstreamer .`
   5.  `cd` to the server folder and run `docker build -t server .`
5. Run docker compose with `docker-compose up -d`, this will start all applications and services.
6. Go to http://localhost:5080 and disable ip filtering for the WebRTCApp.
7. Create a new stream through POST request. 
8. Connect into gstreamer and run the command `export VID=/start/sample.mp4` and `export AMS_URL='rtmp://172.23.0.2:1935/WebRTCApp/test-001'`. Then run `gst-launch-1.0 videotestsrc ! videoconvert ! x264enc ! flvmux ! rtmpsink location=$AMS_URL`
9. `cd` to the backup folder and run `python -m main`

## Grafana 

To use Grafana please go to http://localhost:3000 and set it up with elastic search and logstash as specified in this (https://resources.antmedia.io/docs/how-to-monitor-ant-media-servers)[guide]