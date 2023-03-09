This project replicates a clone of AirBnB, limited strictly to the usage of a console with built-in commands to manage packages.

The console allows for tasks such as:

- The creation of a new object
- The retrieval of an object from a file
- The managing of an object to or from a file
- The destruction of a previously created object

All files are stored within file storage in the engine directory.

-----------------------------------------------------------------

To install, simply use "git clone https://github.com/DarianGrabino/holbertonschool-AirBnB_clone.git"

To utilize, simply run "./console.py"

Afterwards, type "help" in order to receive a handy list of all available commands.

-----------------------------------------------------------------

All tests can be found in tests folder.

They were made using the unittest module, as per usual documentation ettiquette.

-----------------------------------------------------------------

For a more in-depth view of all available commands within the console, followed by a brief description for each one, see:

- Create
Creates a new instance of a typed-in class. Class ID is printed and the instance is saved to a json file
"create <class>"

- Show
Displays a given class through its specific ID
"show <class> <id>"

- Destroy
Destroys any instance of a typed-in class via its ID
"destroy <class> <id>"

- All
Prints all instances of a typed-in class OR all instances of all classes if left blank
"all <class>"

- Count
Prints number of instances of typed-in class
"count <class>"

- Update
Updates any instance of a class based on its name, id and kwargs passed
"update <class> <id> <kwargs>"

-----------------------------------------------------------------

This project was a joint effort:

- Darian Grabino

- Mauricio de Betolaza del Puerto
