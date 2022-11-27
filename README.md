# AirBnB_clone - The console Project

![image](https://user-images.githubusercontent.com/54449260/203245543-887fb536-2f25-4e95-bae2-6105f2ca99b5.png)

# First step: Write a command interpreter to manage your AirBnB objects

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    create the first abstracted storage engine of the project: File storage.
    create all unittests to validate all our classes and storage engine

# What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file, a database etc…
    Do operations on objects (count, compute stats, etc…)
    Update attributes of an object
    Destroy an object

# More Info

# Execution

Your shell should work like this in interactive mode:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $

But also in non-interactive mode: (like the Shell project in C)

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![image](https://user-images.githubusercontent.com/54449260/203246511-e38d5cab-e469-450f-a878-aaf94c2561f2.png)

Format of Command Input
In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.

In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.

Arguments
Most commands have several options or arguments that can be used when executing the program. In order for the Shell to recognize those parameters, the user must separate everything with spaces.

Example:

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

or

user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
Available commands and what they do
The recognizable commands by the interpreter are the following:

Command Description
quit or EOF Exits the program
Usage By itself
----- -----
help Provides a text describing how to use a command.
Usage By itself --or-- help <command>
----- -----
create Creates a new instance of a valid Class, saves it (to the JSON file) and prints the id. Valid classes are: BaseModel, User, State, City, Amenity, Place, Review.
Usage create <class name>
----- -----
show Prints the string representation of an instance based on the class name and id
Usage show <class name> <id> --or-- <class name>.show(<id>)
----- -----
destroy Deletes an instance based on the class name and id (saves the change into a JSON file).
Usage destroy <class name> <id> --or-- .destroy()
----- -----
all Prints all string representation of all instances based or not on the class name.
Usage By itself or all <class name> --or-- <class name>.all()
----- -----
update Updates an instance based on the class name and id by adding or updating attribute (saves the changes into a JSON file).
Usage update <class name> <id> <attribute name> "<attribute value>" ---or--- <class name>.update(<id>, <attribute name>, <attribute value>) --or-- <class name>.update(<id>, <dictionary representation>)
----- -----
count Retrieve the number of instances of a class.
Usage <class name>.count()

Authors
Amanuel Fenta Dejen <amanuelf44@gmail.com>
Elias-Dewa <elias.dewa19@gmail.com>
