import paho.mqtt.client as paho
import time
import subprocess


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish

#use env vars for password
client.username_pw_set("david", "mckelvie")
client.connect("127.0.0.1", 1883)
client.loop_start()

while True:
    result = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
    #print(result.stdout)
    temperature=str(result.stdout)[7:-3]
    print("temperature=" +temperature)
    (rc, mid) = client.publish('raspberry/cpu/temperature', temperature, qos=1)
    time.sleep(1)
