# -*-coding:utf-8-*-
import string
def celsius_to_fehrenheit():
	print "Convert Celsius To Ferenheit"
	celsius = int(raw_input("Type A Celsius Degree: "))
	celsius = celsius * 9 / 5 + 32
	fehrenheit = "°F"
	print "Its %s%s" % (celsius, fehrenheit)
	print ""
	return
	
def fehrenheit_to_celsius():
	print "Convert Fehrenheit To Celsius"
	fehrenheit = int(raw_input("Type A Fehrenheit Degree: "))
	fehrenheit -= 32
	fehrenheit = fehrenheit / 1.8
	celsius = "°C"
	print "Its %s%s" % (fehrenheit, celsius)
	print ""
	
	return 	

def celsius_to_kelvin():
	print "Convert Celsius To Kelvin"
	celsius = int(raw_input("Type A Celsius Degree: "))
	celsius = celsius + 273.15
	kelvin = "K"
	print "Its %s%s" % (celsius, kelvin)
	print ""
	return

def kelvin_to_celsius():
	print "Convert Kelvin To Fehrenheit"
	kelvin = int(raw_input("Type A Kelvin Degree: "))
	kelvin = kelvin - 273.15
	celsius = "°C"
	print "Its %s%s" % (kelvin, celsius)
	print ""
	return

def fehrenheit_to_kelvin():
	print "Convert Fehrenheit To Kelvin"
	fehrenheit = int(raw_input("Type A Fehrenheit Degree: "))
	fehrenheit = fehrenheit + 459.67
	fehrenheit = fehrenheit * 5/9
	kelvin = "K"
	print "Its %s%s" % (fehrenheit, kelvin)
	print ""
	return

def kelvin_to_fehrenheir():
	print "Convert Fehrenheit To Kelvin"
	kelvin = int(raw_input("Type A Kelvin Degree: "))
	kelvin = kelvin * 9/5
	kelvin = kelvin - 459.67
	fehrenheit = "°F"
	print "Its %s%s" % (kelvin, fehrenheit)
	print ""
	return

def main():
	menu = [celsius_to_fehrenheit, fehrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fehrenheit_to_kelvin, kelvin_to_fehrenheit]
	while(True):
		print "Select Option: "
		print "1\tCelsius To Fehrenheit"
		print ""
		print "2\tFehrenheit To Celsius"
		print ""
		print "3\tCelsius To Kelvin"
		print ""
		print "4\tKelvin To Celsius"
		print ""
		print "5\tFehrenheit To Kelvin"
		print ""
		print "5\tKelvin To Fehrenheit"
		choice = int(raw_input("Selection: "))
		choice -= 1
		menu[choice]()
			

	return
main()
