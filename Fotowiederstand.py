# Zuerst alle nötigen Bibliotehken einfügen
import time 
import RPi.GPIO as GPIO
# Danach die Pins als IN PUT Deklarieren
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Zum schluss eine Endlosschleife um im 2 Sek Takt die Durchlassmenge des Fotowiederstandes abzufragen
while (True):
	if (GPIO.input(11) == True):
                print ("es ist hell")
		time.sleep(2)

        else: 
		print ("es ist dunkel")
		time.sleep(2)
