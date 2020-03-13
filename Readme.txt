*********************************************************
*							*
*							*
*    INSTRUCTIONS FOR HOW TO RUN PYTHON SCRIPT          *
*		 Tommy Truong				*
*		  12/15/2019				*
*							*
*********************************************************

Before running:
	Please make sure the following dependency are installed:
	- sympy
	if none of these are installed, open up the terminal and do the following command:
		pip install sympy

Supplied is two input file: input.txt, and test.txt

This program takes in the input txt file as a command line argument 
so for example to run the program the command would look like this:

python Check-Jacobian.py input.txt

How to run Check-Jacobian.py
	if using terminal:

	1) Open up terminal
	2) cd into the file path
	3) type the following into the terminal:
		python Check-Jacobian.py [name of txt file]
	4) if script does not run, type the following into the terminal:
		chmod +x Check-Jacobian.py
		python Check-Jacobian.py [name of txt file]
	5) Program will then output a text file called output.txt in the same directoy of the file

	if using python IDLE:
	
	1) Open up python IDLE:
	2) Open up MotionPlanner_PRM.py
	3) On the toolbar where it says run, click on Run Module 
	4) Program will then output a text file called output.txt in the same directoy of the file


Inside the output file: 
	output is list of 0 or 1, 0’s indicate the determinant of the Jacobian is NOT too small, 1’s indicate that the determinant of the Jacobian is too small) 
	

