import json
import paho.mqtt.client as mqtt


class MQTTProvider(object):
    """ MQTT provider """

    def __init__(self, engine):
        self.engine = engine
        self.mqttc = mqtt.Client()

    def command_publish(self, command):
        """ Publish a MQTT message """
        command = json.dumps(command)
        self.mqttc.connect(
            command['host'],
            port=int(command['port']))

        self.mqttc.loop_start()

        try:
            self.mqttc.publish(
                command['endpoint'],
                command['payload'])
        finally:
            self.mqttc.loop_stop(force=False)
