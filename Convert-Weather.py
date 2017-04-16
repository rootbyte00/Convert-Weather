# -*-coding:utf-8-*-
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
def main():
	menu = [celsius_to_fehrenheit, fehrenheit_to_celsius,]
	while(True):
		print "Select Option: "
		print "1\tCelsius To Fehrenheit"
		print ""
		print "2\tFehrenheit To Celsius"
		choice = int(raw_input("Selection: "))
		choice -= 1
		menu[choice]()
			
	return
main()
