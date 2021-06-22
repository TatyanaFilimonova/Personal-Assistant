Personal Assistant

Project structure


Code level  				core.py
  					  |
			 ___________________________________________________________________________________
			|		  |			|			|		   |
		addressbook.py	   notebook.py		neural_code.py		  training.py		clean.py
			|		  |			|			|
Data level		|		  |			|			|
			|		  |			|	     		|
		Work telefones.json  Work notes.json	   words.pkl		   intents.json      
								|			|
							   classes.pkl		chatbot_model.model	   

Project description

Project implements CLI BOT as a personal assistant with next features:

Address book administration (Work telefones.json):
    Add a new contact
    Edit the contact detail
    Find the records by phone or name
    Print all the records of address book, page by page
    Delete contact
    Let you the contacts with birthdays in specified period    

Note book administration (Work notes.json)
    Find the notes by text or keywords
    Print all the records of note book, page by page
    Add new text note
    Edit existing text note
    Delete text note
    Sort of the notes by keywords

System maintenance        
    Sort selected folder by file types 
    Save the current state of data to disk
    Print a list of the available commands	


Files in package:
addressbook.py - classes with address book datas and logics
notebook.py - classes with note book datas and logics
neural_code.py - dealing with user input to predict and launch the command which user needs
training.py - create and train the neural network using a dictionary of command synonyms. 
	      source of this code https://www.youtube.com/watch?v=1lwddP0KUEg
core.py - interaction with user and program modules 
 

CLI BOT is based on a simple neural network trained on command classifiers (intents.json). 

How it works:

CLI BOT receives a user's input and tries to predict a command using neural network. BOT launch command if would predict it or let the future list to user in other case.
During the commands execution BOT works with linear user inetrface logic and don't use AI/ML instruments.  
 
To install and launch CLI BOT please:
- donwload distibutive *.tar 
- unzip tar archive
- run next set of commands from system shell:
	cd <path to folder where setup.py situated>
	py setup.py install
	BOT
CLI BOT requires a set of packages, which you could install, if necessary: 
	pip install json
	pip install numpy
	pip install NLTK
	pip install tensorflow
