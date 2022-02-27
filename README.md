(Written February 27th, 2022 by Joshua Pryor)

Welcome to the Resistor Assister! 


This is my submission for the VTHacks 9 hackathon. It can find the ideal
combination of resistors to get as close as possible to any resistance. 
I'm working solo for this hackathon, so the entire project was made from
scratch by me.

This project uses minimal add-ons. The only additional module imported is
the sys module to allow for the use of command line arguments


How to run:

	0) if you want to replace or modify the list of available resistors, use
	   resistors.txt. Each line should contain one resistance value with no
	   letters, commas, or spaces.
	
	1) navigate to the folder containing this file in your command line
	
	2) run main.py from the command line with two arguments. The first
	   is your desired resistance, and the second is the maximum number
	   of resistors you want to use to achieve it. The output will tell you
	   the best combination as well as the total resistance of that combination.
