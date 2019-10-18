#!/usr/bin/env python

import fast_com
import paho.mqtt.client as mqtt


# This is the MQTT Publisher
client = mqtt.Client()
client.connect("localhost",1883,60)



print "Start speedtest against fast.com ..."
result = fast_com.fast_com()
print "Result:", result, "Mbps"
print "... Done sending to MQTT"

client.publish("topic/fastspeedtest",result);

print "... Done"

