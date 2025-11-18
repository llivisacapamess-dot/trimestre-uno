import network
import socket
import time
import dht
from machine import Pin
import gc

gc.collect()

# Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(0.1)
wlan.active(True)
wlan.connect("josue", "merchan2")

print("Conectando como sensor1...")
while not wlan.isconnected():
    time.sleep(0.5)
print(" sensor1 conectado. IP:", wlan.ifconfig()[0])

# Sensor DHT11 en GPIO15
d = dht.DHT11(Pin(12))

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        payload = f"sensor1:{temp},{hum}"

        # Enviar
        s = socket.socket()
        s.connect(("192.168.4.1", 8888))
        s.send(payload.encode())
        s.close()
        print(f" jimmy1 enviado: {temp}°C, {hum}%")
    except Exception as e:
        print(" sensor1 error:", e)
    time.sleep(5)

#ESP32 sensor 2

import network
import socket
import time
import dht
from machine import Pin
import gc

gc.collect()

wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(0.1)
wlan.active(True)
wlan.connect("josue", "merchan2")

print("Conectando como sensor2...")
while not wlan.isconnected():
    time.sleep(0.5)
print("sensor2 conectado. IP:", wlan.ifconfig()[0])

# Pueden usar otro pin si desean, ej. GPIO4
d = dht.DHT11(Pin(14))  # o Pin(4)

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        payload = f"sensor2:{temp},{hum}"

        s = socket.socket()
        s.connect(("192.168.4.1", 8888))
        s.send(payload.encode())
        s.close()
        print(f" sensor2 enviado: {temp}°C, {hum}%")
    except Exception as e:
        print(" sensor2 error:", e)
    time.sleep(5)

#ESP32 sensor 3

import network
import socket
import time
import dht
from machine import Pin
import gc

gc.collect()

# Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(0.1)
wlan.active(True)
wlan.connect("josue", "merchan2")

print("Conectando como sensor3...")
while not wlan.isconnected():
    time.sleep(0.5)
print(" sensor1 conectado. IP:", wlan.ifconfig()[0])

# Sensor DHT11 en GPIO15
d = dht.DHT11(Pin(12))

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        payload = f"sensor3:{temp},{hum}"

        # Enviar
        s = socket.socket()
        s.connect(("192.168.4.1", 8888))
        s.send(payload.encode())
        s.close()
        print(f" jimmy1 enviado: {temp}°C, {hum}%")
    except Exception as e:
        print(" sensor3 error:", e)
    time.sleep(5)

#ESP32 sensor 4

import network
import socket
import time
import dht
from machine import Pin
import gc

gc.collect()

wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(0.1)
wlan.active(True)
wlan.connect("josue", "merchan2")

print("Conectando como sensor4...")
while not wlan.isconnected():
    time.sleep(0.5)
print("sensor2 conectado. IP:", wlan.ifconfig()[0])

# Pueden usar otro pin si desean, ej. GPIO4
d = dht.DHT11(Pin(14))  # o Pin(4)

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        payload = f"sensor4:{temp},{hum}"

        s = socket.socket()
        s.connect(("192.168.4.1", 8888))
        s.send(payload.encode())
        s.close()
        print(f" sensor4 enviado: {temp}°C, {hum}%")
    except Exception as e:
        print(" sensor4 error:", e)
    time.sleep(5)
#ESP32 sensor 5

import network
import socket
import time
import dht
from machine import Pin
import gc

gc.collect()

wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(0.1)
wlan.active(True)
wlan.connect("josue", "merchan2")

print("Conectando como sensor5...")
while not wlan.isconnected():
    time.sleep(0.5)
print("sensor2 conectado. IP:", wlan.ifconfig()[0])

# Pueden usar otro pin si desean, ej. GPIO4
d = dht.DHT11(Pin(14))  # o Pin(4)

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        payload = f"sensor4:{temp},{hum}"

        s = socket.socket()
        s.connect(("192.168.4.1", 8888))
        s.send(payload.encode())
        s.close()
        print(f" sensor5 enviado: {temp}°C, {hum}%")
    except Exception as e:
        print(" sensor5 error:", e)
    time.sleep(5)
