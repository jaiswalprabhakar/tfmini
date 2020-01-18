import Jetson.GPIO as GPIO
import time

RX = ttyTHS1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RX, GPIO.IN)
GPIO.input(RX)


def getTFminiData():
  while True:
    #print("#############")
    time.sleep(0.05)	#change the value if needed
    (count, recv) = GPIO.input(RX)
    if count > 8:
      for i in range(0, count-9):
        if recv[i] == 89 and recv[i+1] == 89: # 0x59 is 89
          checksum = 0
          for j in range(0, 8):
            checksum = checksum + recv[i+j]
          checksum = checksum % 256
          if checksum == recv[i+8]:
            distance = recv[i+2] + recv[i+3] * 256
            strength = recv[i+4] + recv[i+5] * 256
            if distance <= 1200 and strength < 2000:
              print(distance, strength) 
