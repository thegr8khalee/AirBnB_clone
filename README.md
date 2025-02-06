
SE Foundations
Average: 112.81%
0x00. AirBnB clone - The console
Group project
Python
OOP
 Weight: 5
 Project to be done in teams of 2 people
 Project over - took place from May 13, 2024 8:00 AM to May 20, 2024 8:00 AM
 Manual QA review was done by Yara Nazih on Feb 13, 2024 9:50 PM
 An auto review will be launched at the deadline
In a nutshell…
Manual QA review: 48.0/48 mandatory
Auto QA review: 168.75/302 mandatory & 90.3/233 optional
Altogether:  85.93%
Mandatory: 61.93%
Optional: 38.76%
Calculation:  61.93% + (61.93% * 38.76%)  == 85.93%
Overall comment:
Well done and good luck.

Concepts
For this project, we expect you to look at these concepts:

Python packages
AirBnB clone


Background Context
Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Resources
Read or watch:

cmd module
cmd module in depth
packages concept page
uuid module
datetime
unittest module
args/kwargs
Python test cheatsheet
cmd module wiki page
python unittest
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case
GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

More Info
Execution
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



Video library(8 total)
Search by title
HBNB project overview
HBNB - the console
Python: Unique Identifier
Python: Unittests
Python: BaseModel and inheritance
Code consistency
Python: Modules and Packages
HBNB - storage abstraction
Tasks
0. README, AUTHORS
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a README.md:
description of the project
description of the command interpreter:
how to start it
how to use it
examples
You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
You should use branches and pull requests on GitHub - it will help you as team to organize your work
Repo:

GitHub repository: AirBnB_clone
File: README.md, AUTHORS
1. Be pycodestyle compliant!
mandatory
Score: 16.25% (Checks completed: 25.0%)
Write beautiful code that passes the pycodestyle checks.

Repo:

GitHub repository: AirBnB_clone
   
2. Unittests
mandatory
Score: 47.5% (Checks completed: 73.08%)
All your files, classes, functions must be tested with unit tests

guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
Note that this is just an example, the number of tests you create can be different from the above example.

Warning:

Unit tests must also pass in non-interactive mode:

guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
Repo:

GitHub repository: AirBnB_clone
File: tests/
   
3. BaseModel
mandatory
Score: 62.5% (Checks completed: 96.15%)
Write a class BaseModel that defines all common attributes/methods for other classes:

models/base_model.py
Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at with the current datetime
to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$ 
Repo:

GitHub repository: AirBnB_clone
File: models/base_model.py, models/__init__.py, tests/
   
4. Create BaseModel from dictionary
mandatory
Score: 65.0% (Checks completed: 100.0%)
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
Update models/base_model.py:

__init__(self, *args, **kwargs):
you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
*args won’t be used
if kwargs is not empty:
each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
each value of this dictionary is the value of this attribute name
Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
otherwise:
create id and created_at as you did previously (new instance)
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$ 
Repo:

GitHub repository: AirBnB_clone
File: models/base_model.py, tests/
  
5. Store first object
mandatory
Score: 39.0% (Checks completed: 60.0%)
Now we can recreate a BaseModel from another one by using a dictionary representation:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

Python doesn’t know how to convert a string to a dictionary (easily)
It’s not human readable
Using this file with another program in Python or other language will be hard.
So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
Magic right?

Terms:

simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }
JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'
Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

models/engine/file_storage.py
Private class attributes:
__file_path: string - path to the JSON file (ex: file.json)
__objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
Public instance methods:
all(self): returns the dictionary __objects
new(self, obj): sets in __objects the obj with key <obj class name>.id
save(self): serializes __objects to the JSON file (path: __file_path)
reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
Update models/__init__.py: to create a unique FileStorage instance for your application

import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

import the variable storage
in the method save(self):
call save(self) method of storage
__init__(self, *args, **kwargs):
if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
Repo:

GitHub repository: AirBnB_clone
File: models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/
   
6. Console 0.0.1
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a program called console.py that contains the entry point of the command interpreter:

You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF to exit the program
help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything
Your code should not be executed when imported
Warning:

You should end your file with:

if __name__ == '__main__':
    HBNBCommand().cmdloop()
to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
   
7. Console 0.1
mandatory
Score: 62.43% (Checks completed: 100.0%)
Update your command interpreter (console.py) to have these commands:

create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
If the class name is missing, print ** class name missing ** (ex: $ create)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ show)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ destroy)
If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
The printed result must be a list of strings (like the example below)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
Usage: update <class name> <id> <attribute name> "<attribute value>"
Only one attribute can be updated at the time
You can assume the attribute name is valid (exists for this model)
The attribute value must be casted to the attribute type
If the class name is missing, print ** class name missing ** (ex: $ update)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
Let’s add some rules:

You can assume arguments are always in the right order
Each arguments are separated by a space
A string argument with a space must be between double quote
The error management starts from the first argument to the last one
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
  
8. First User
mandatory
Score: 63.78% (Checks completed: 100.0%)
Write a class User that inherits from BaseModel:

models/user.py
Public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string
Update FileStorage to manage correctly serialization and deserialization of User.

Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.

guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
guillaume@ubuntu:~/AirBnB$ 
No unittests needed for the console

Repo:

GitHub repository: AirBnB_clone
File: models/user.py, models/engine/file_storage.py, console.py, tests/
  
9. More classes!
mandatory
Score: 65.0% (Checks completed: 100.0%)
Write all those classes that inherit from BaseModel:

State (models/state.py):
Public class attributes:
name: string - empty string
City (models/city.py):
Public class attributes:
state_id: string - empty string: it will be the State.id
name: string - empty string
Amenity (models/amenity.py):
Public class attributes:
name: string - empty string
Place (models/place.py):
Public class attributes:
city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: it will be the list of Amenity.id later
Review (models/review.py):
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string
Repo:

GitHub repository: AirBnB_clone
File: models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/
  
10. Console 1.0
mandatory
Score: 62.79% (Checks completed: 100.0%)
Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!

No unittests needed for the console

Repo:

GitHub repository: AirBnB_clone
File: console.py, models/engine/file_storage.py, tests/
  
11. All instances by class name
#advanced
Score: 65.0% (Checks completed: 100.0%)
Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
  
12. Count instances
#advanced
Score: 65.0% (Checks completed: 100.0%)
Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
  
13. Show
#advanced
Score: 65.0% (Checks completed: 100.0%)
Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).

Errors management must be the same as previously.

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
  
14. Destroy
#advanced
Score: 65.0% (Checks completed: 100.0%)
Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).

Errors management must be the same as previously.

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Bar")
** no instance found **
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
  
15. Update
#advanced
Score: 52.5% (Checks completed: 100.0%)
Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).

Errors management must be the same as previously.

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
  
16. Update from dictionary
#advanced
Score: 10.83% (Checks completed: 16.67%)
Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

Errors management must be the same as previously.

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 23, 'first_name': 'Bob', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
(hbnb) 
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) 
No unittests needed

Repo:

GitHub repository: AirBnB_clone
File: console.py
   
17. Unittests for the Console!
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write all unittests for console.py, all features!

For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
Otherwise, you will have to re-write the console by replacing precmd by default.

Well done on completing this project! Let the world hear about this milestone achieved.

Click here to tweet!

Repo:

GitHub repository: AirBnB_clone
File: tests/test_console.py
   
Copyright © 2025 ALX, All rights reserved.









SE Foundations
Average: 112.81%
0x01. AirBnB clone - Web static
HTML
CSS
Front-end
 Weight: 1
 Project over - took place from May 23, 2024 8:00 AM to May 28, 2024 8:00 AM
 Manual QA review was done by Prince Nzamuwe on Feb 18, 2024 5:44 PM
In a nutshell…
Manual QA review: 194.5/195 mandatory & 46.0/46 optional
Altogether:  199.48%
Mandatory: 99.74%
Optional: 100.0%
Calculation:  99.74% + (99.74% * 100.0%)  == 199.48%
Overall comment:
Keep up your courage and never hesitate to continue doing hard things!

Concepts
For this project, we expect you to look at these concepts:

HTML/CSS
The trinity of front-end quality


Background Context
Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static pages
Style guide
Fake contents
No Javascript
No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

Resources
Read or watch:

Learn to Code HTML & CSS (until “Creating Lists” included)
Inline Styles in HTML
Specifics on CSS Specificity
CSS SpeciFishity
Introduction to HTML
CSS
MDN
center boxes
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is HTML
How to create an HTML page
What is a markup language
What is the DOM
What is an element / tag
What is an attribute
How does the browser load a webpage
What is CSS
How to add style to an element
What is a class
What is a selector
How to compute CSS Specificity Value
What are Box properties in CSS
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be W3C compliant and validate with W3C-Validator
All your CSS files should be in styles folder
All your images should be in images folder
You are not allowed to use !important and id (#... in the CSS file)
You are not allowed to use tags img, embed and iframe
You are not allowed to use Javascript
Current screenshots have been done on Chrome 56 or more.
No cross browsers
You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots
More Info


Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Inline styling
mandatory
Score: 98.24% (Checks completed: 100.0%)
Write an HTML page that displays a header and a footer.

Layout:

Body:
no margin
no padding
Header:
color #FF0000 (red)
height: 70px
width: 100%
Footer:
color #00FF00 (green)
height: 60px
width: 100%
text Best School center vertically and horizontally
always at the bottom at the page
Requirements:

You must use the header and footer tags
You are not allowed to import any files
You are not allowed to use the style tag in the head tag
Use inline styling for all your tags


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 0-index.html
1. Head styling
mandatory
Score: 99.29% (Checks completed: 100.0%)
Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

You must use the header and footer tags
You are not allowed to import any files
No inline styling
You must use the style tag in the head tag
The layout must be exactly the same as 0-index.html

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 1-index.html
2. CSS files
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:

You must use the header and footer tags
No inline styling
You must have 3 CSS files:
styles/2-common.css: for global style (i.e. the body style)
styles/2-header.css: for header style
styles/2-footer.css: for footer style
The layout must be exactly the same as 1-index.html

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css
3. Zoning done!
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

Common:
no margin
no padding
font color: #484848
font size: 14px
font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
Header:
color: white
height: 70px
width: 100%
border bottom 1px #CCCCCC
Footer:
color white
height: 60px
width: 100%
border top 1px #CCCCCC
text Best School center vertically and horizontally
always at the bottom at the page
Requirements:

No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 3 CSS files:
styles/3-common.css: for the global style (i.e body style)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/
4. Search!
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)

Container:
between header and footer tags, add a div:
classname: container
max width 1000px
margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
center horizontally
Filter section:
tag section
classname filters
inside the .container
color white
height: 70px
width: 100% of the container
border 1px #DDDDDD with radius 4px
Button search:
tag button
text Search
font size: 18px
inside the section filters
background color #FF5A5F
text color #FFFFFF
height: 48px
width: 20% of the section filters
no borders
border radius: 4px
center vertically and at 30px of the right border
change opacity to 90% when the mouse is on the button
Requirements:

You must use: header, footer, section, button tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/4-filters.css: for the filters style
4-index.html won’t be W3C valid, don’t worry, it’s temporary


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/
5. More filters
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

Locations and Amenities filters:
tag: div
classname: locations for location tag and amenities for the other
inside the section filters (same level as the button Search)
height: 100% of the section filters
width: 25% of the section filters
border right #DDDDDD 1px only for the first left filter
contains a title:
tag: h3
font weight: 600
text States or Amenities
contains a subtitle:
tag: h4
font weight: 400
font size: 14px
text with fake contents
Requirements:

You must use: header, footer, section, button, h3, h4 tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/5-filters.css: for the filters style


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/
6. It's (h)over
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
tag ul
classname popover
text should be fake now
inside each div
not displayed by default
color #FAFAFA
width same as the div filter
border #DDDDDD 1px with border radius 4px
no list display
Location filter has 2 levels of ul/li:
state -> cities
state name must be display in a h2 tag (font size 16px)
Requirements:

You must use: header, footer, section, button, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/6-filters.css: for the filters style
 

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/
7. Display results
mandatory
Score: 99.5% (Checks completed: 100.0%)
Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

Add Places section:
tag: section
classname: places
same level as the filters section, inside .container
contains a title:
tag: h1
text: Places
align in the top left
font size: 30px
contains multiple “Places” as listing (horizontal or vertical) describe by:
tag: article
width: 390px
padding and margin 20px
border #FF5A5F 1px with radius 4px
contains the place name:
tag: h2
font size: 30px
center horizontally
Requirements:

You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 5 CSS files:
styles/4-common.css: for the global style (i.e. body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for footer style
styles/6-filters.css: for the filters style
styles/7-places.css: for the places style


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/
8. More details
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)

Add more information to a Place article:

Price by night:
tag: div
classname: price_by_night
same level as the place name
font color: #FF5A5F
border: #FF5A5F 4px rounded
min width: 60px
height: 60px
font size: 30px
align: the top right (with space)
Information section:
tag: div
classname: information
height: 80px
border: top and bottom #DDDDDD 1px
contains (align vertically):
Number of guests:
tag: div
classname: max_guest
width: 100px
fake text
icon
Number of bedrooms:
tag: div
classname: number_rooms
width: 100px
fake text
icon
Number of bathrooms:
tag: div
classname: number_bathrooms
width: 100px
fake text
icon
User section:
tag: div
classname: user
text Owner: <fake text>
Owner text should be in bold
Description section:
tag: div
classname: description
Requirements:

You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 5 CSS files:
styles/4-common.css: for the global style (i.e. body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/6-filters.css: for the filters style
styles/8-places.css: for the places style


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/
9. Full details
#advanced
Score: 100.0% (Checks completed: 100.0%)
Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 8-index.html)

Add more information to a Place article:

List of Amenities:
tag div
classname amenities
margin top 40px
contains:
title:
tag h2
text Amenities
font size 16px
border bottom #DDDDDD 1px
list of amenities:
tag ul / li
no list style
icons on the left: Pet friendly, TV, Wifi, etc… feel free to add more
List of Reviews:
tag div
classname reviews
margin top 40px
contains:
title:
tag h2
text Reviews
font size 16px
border bottom #DDDDDD 1px
list of review:
tag ul / li
no list style
a review is described by:
h3 tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
p tag for the text (font size 12px)
Requirements:

You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 5 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/6-filters.css: for the filters style
styles/100-places.css: for the places style


Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/
10. Flex
#advanced
Score: 100.0% (Checks completed: 100.0%)
Improve the Places section by using Flexible boxes for all Place articles

Flexbox Froggy

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/
11. Responsive design
#advanced
Score: 100.0% (Checks completed: 100.0%)
Improve the page by adding responsive design to display correctly in mobile or small screens.

Examples:

no horizontal scrolling
redesign search bar depending of the width
etc.
Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/
12. Accessibility
#advanced
Score: 100.0% (Checks completed: 100.0%)
Improve the page by adding Accessibility support

Examples:

Colors contrast
Header tags
etc.
Well done on completing this project! Let the world hear about this milestone achieved.

Click here to tweet!

Repo:

GitHub repository: AirBnB_clone
Directory: web_static
File: 103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/
Copyright © 2025 ALX, All rights reserved.







SE Foundations
Average: 112.81%
0x02. AirBnB clone - MySQL
Group project
Python
OOP
Back-end
SQL
MySQL
ORM
SQLAlchemy
 Weight: 2
 Project to be done in teams of 2 people
 Project over - took place from Jun 21, 2024 8:00 AM to Jun 27, 2024 8:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 64.0/191 mandatory
Altogether:  33.51%
Mandatory: 33.51%
Optional: no optional tasks
Background Context
Environment variables will be your best friend for this project!

HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
Resources
Read or watch:

cmd module
packages concept page
unittest module
args/kwargs
SQLAlchemy tutorial
How To Create a New User and Grant Permissions in MySQL
Python3 and environment variables
SQLAlchemy
MySQL 8.0 SQL Statement Syntax
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is Unit testing and how to implement it in a large project
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
How to create a MySQL database
How to create a MySQL user and grant it privileges
What ORM means
How to map a Python Class to a MySQL table
How to handle 2 different storage engines with the same codebase
How to use environment variables
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge cases
SQL Scripts
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
Your files will be executed with SQLAlchemy version 1.4.x
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
GitHub
There should be one project repository per group. If you clone/fork/whatever a partner’s project repository with the same name before the second deadline, you risk a 0% score.

More Info


Comments for your SQL file:
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Video library(2 total)
Search by title
HBNB - storage abstraction
AirBnB console
Tasks
0. Fork me if you can!
mandatory
Score: 100.0% (Checks completed: 100.0%)
In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

“Who did this code?”
“How it works?”
“Where are unittests?”
“Where is this?”
“Why did they do that like this?”
“I don’t understand anything.”
“… I will refactor everything…”
But the worst thing you could possibly do is to redo everything. Please don’t do that! Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!

For this project you will fork this codebase:

update the repository name to AirBnB_clone_v2
update the README.md with your information but don’t delete the initial authors
If you are the owner of this repository, please create a new repository named AirBnB_clone_v2 with the same content of AirBnB_clone

Repo:

GitHub repository: AirBnB_clone_v2
  
1. Bug free!
mandatory
Score: 5.56% (Checks completed: 5.56%)
Do you remember the unittest module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.

guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 
All your unittests must pass without any errors at anytime in this project, with each storage engine!. Same for PEP8!

guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 
Some tests won’t be relevant for some type of storage, please skip them by using the skipIf feature of the Unittest module - 26.3.6. Skipping tests and expected failures. Of course, the number of tests must be higher than the current number of tests, so if you decide to skip a test, you should write a new test!

How to test with MySQL?
First, you create a specific database for it (next tasks). After, you have to remember what the purpose of an unittest?

“Assert a current state (objects/data/database), do an action, and validate this action changed (or not) the state of your objects/data/database”

For example, “you want to validate that the create State name="California" command in the console will add a new record in your table states in your database”, here steps for your unittest:

get the number of current records in the table states (my using a MySQLdb for example - but not SQLAlchemy (remember, you want to test if it works, so it’s better to isolate from the system))
execute the console command
get (again) the number of current records in the table states (same method, with MySQLdb)
if the difference is +1 => test passed
Repo:

GitHub repository: AirBnB_clone_v2
  
2. Console improvements
mandatory
Score: 18.18% (Checks completed: 18.18%)
Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:

Command syntax: create <Class name> <param 1> <param 2> <param 3>...
Param syntax: <key name>=<value>
Value syntax:
String: "<value>" => starts with a double quote
any double quote inside the value must be escaped with a backslash \
all underscores _ must be replace by spaces . Example: You want to set the string My little house to the attribute name, your command line must be name="My_little_house"
Float: <unit>.<decimal> => contains a dot .
Integer: <number> => default case
If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped
Don’t forget to add tests for this new feature!

Also, this new feature will be tested here only with FileStorage engine.

guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create | ./console.py 
(hbnb) d80e0344-63eb-434a-b1e0-07783522124e
(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7
(hbnb) [[State] (d80e0344-63eb-434a-b1e0-07783522124e) {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name': 'California'}, [State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) {'id': '092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), 'name': 'Arizona'}]
(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) [[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) {'number_bathrooms': 2, 'longitude': -122.431297, 'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 'My little house', 'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, 'number_rooms': 4, 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843747)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$
Repo:

GitHub repository: AirBnB_clone_v2
File: console.py, models/, tests/
   
3. MySQL setup development
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that prepares a MySQL server for the project:

A database hbnb_dev_db
A new user hbnb_dev (in localhost)
The password of hbnb_dev should be set to hbnb_dev_pwd
hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
Enter password: 
hbnb_dev_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_dev@localhost
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: setup_mysql_dev.sql
  
4. MySQL setup test
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that prepares a MySQL server for the project:

A database hbnb_test_db
A new user hbnb_test (in localhost)
The password of hbnb_test should be set to hbnb_test_pwd
hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
Enter password: 
hbnb_test_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_test@localhost
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: setup_mysql_test.sql
  
5. Delete object
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update FileStorage: (models/engine/file_storage.py)

Add a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside - if obj is equal to None, the method should not do anything
Update the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. Example below with State - it’s an optional filtering
guillaume@ubuntu:~/AirBnB_v2$ cat main_delete.py
#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

guillaume@ubuntu:~/AirBnB_v2$ ./main_delete.py
All States: 0
New State: [State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 1
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
Another State: [State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 2
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 1
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/engine/file_storage.py
   
6. DBStorage - States and Cities
mandatory
Score: 18.75% (Checks completed: 18.75%)
SQLAlchemy will be your best friend!

It’s time to change your storage engine and use SQLAlchemy



In the following steps, you will make multiple changes:

the biggest one is the transition between FileStorage and DBStorage: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the abstraction: Make your code running without knowing how it’s stored.
add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)
Please follow all these steps:

Update BaseModel: (models/base_model.py)

Create Base = declarative_base() before the class definition of BaseModel
Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.
Add or replace in the class BaseModel:
class attribute id
represents a column containing a unique string (60 characters)
can’t be null
primary key
class attribute created_at
represents a column containing a datetime
can’t be null
default value is the current datetime (use datetime.utcnow())
class attribute updated_at
represents a column containing a datetime
can’t be null
default value is the current datetime (use datetime.utcnow())
Move the models.storage.new(self) from def __init__(self, *args, **kwargs): to def save(self): and call it just before models.storage.save()
In def __init__(self, *args, **kwargs):, manage kwargs to create instance attribute from this dictionary. Ex: kwargs={ 'name': "California" } => self.name = "California" if it’s not already the case
Update the to_dict() method of the class BaseModel:
remove the key _sa_instance_state from the dictionary returned by this method only if this key exists
Add a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete
Update City: (models/city.py)

City inherits from BaseModel and Base (respect the order)
Add or replace in the class City:
class attribute __tablename__ -
represents the table name, cities
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute state_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to states.id
Update State: (models/state.py)

State inherits from BaseModel and Base (respect the order)
Add or replace in the class State:
class attribute __tablename__
represents the table name, states
class attribute name
represents a column containing a string (128 characters)
can’t be null
for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City
New engine DBStorage: (models/engine/db_storage.py)

Private class attributes:
__engine: set to None
__session: set to None
Public instance methods:
__init__(self):
create the engine (self.__engine)
the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
dialect: mysql
driver: mysqldb
all of the following values must be retrieved via environment variables:
MySQL user: HBNB_MYSQL_USER
MySQL password: HBNB_MYSQL_PWD
MySQL host: HBNB_MYSQL_HOST (here = localhost)
MySQL database: HBNB_MYSQL_DB
don’t forget the option pool_pre_ping=True when you call create_engine
drop all tables if the environment variable HBNB_ENV is equal to test
all(self, cls=None):
query on the current database session (self.__session) all objects depending of the class name (argument cls)
if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
this method must return a dictionary: (like FileStorage)
key = <class-name>.<object-id>
value = object
new(self, obj): add the object to the current database session (self.__session)
save(self): commit all changes of the current database session (self.__session)
delete(self, obj=None): delete from the current database session obj if not None
reload(self):
create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
Update __init__.py: (models/__init__.py)

Add a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
If equal to db:
Import DBStorage class in this file
Create an instance of DBStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
Else:
Import FileStorage class in this file
Create an instance of FileStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
This “switch” will allow you to change storage type directly by using an environment variable (example below)
State creation:

guillaume@ubuntu:~/AirBnB_v2$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
guillaume@ubuntu:~/AirBnB_v2$ 
City creation:

guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/base_model.py, models/city.py, models/state.py, models/engine/db_storage.py, models/__init__.py
  
7. DBStorage - User
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update User: (models/user.py)

User inherits from BaseModel and Base (respect the order)
Add or replace in the class User:
class attribute __tablename__
represents the table name, users
class attribute email
represents a column containing a string (128 characters)
can’t be null
class attribute password
represents a column containing a string (128 characters)
can’t be null
class attribute first_name
represents a column containing a string (128 characters)
can be null
class attribute last_name
represents a column containing a string (128 characters)
can be null
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[User] (4f3f4b42-a4c3-4c20-a492-efff10d00c0b) {'updated_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'last_name': 'Snow', 'first_name': 'Guillaume', 'email': 'gui@hbtn.io', 'created_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'password': 'f4ce007d8e84e0910fbdd7a06fa1692d'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
created_at: 2017-11-10 01:17:26
updated_at: 2017-11-10 01:17:26
     email: gui@hbtn.io
  password: guipwd
first_name: Guillaume
 last_name: Snow
guillaume@ubuntu:~/AirBnB_v2$
Repo:

GitHub repository: AirBnB_clone_v2
File: models/user.py
  
8. DBStorage - Place
mandatory
Score: 6.25% (Checks completed: 6.25%)
Update Place: (models/place.py)

Place inherits from BaseModel and Base (respect the order)
Add or replace in the class Place:
class attribute __tablename__
represents the table name, places
class attribute city_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to cities.id
class attribute user_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to users.id
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute description
represents a column containing a string (1024 characters)
can be null
class attribute number_rooms
represents a column containing an integer
can’t be null
default value: 0
class attribute number_bathrooms
represents a column containing an integer
can’t be null
default value: 0
class attribute max_guest
represents a column containing an integer
can’t be null
default value: 0
class attribute price_by_night
represents a column containing an integer
can’t be null
default value: 0
class attribute latitude
represents a column containing a float
can be null
class attribute longitude
represents a column containing a float
can be null
Update User: (models/user.py)

Add or replace in the class User:
class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user
Update City: (models/city.py)

Add or replace in the class City:
class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) ed72aa02-3286-4891-acbc-9d9fc80a1103
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Place' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Place] (ed72aa02-3286-4891-acbc-9d9fc80a1103) {'latitude': 37.774, 'city_id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'price_by_night': 120, 'id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'user_id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'max_guest': 6, 'created_at': datetime.datetime(2017, 11, 10, 1, 22, 30), 'description': None, 'number_rooms': 3, 'longitude': -122.431, 'number_bathrooms': 1, 'name': '"Lovely place', 'updated_at': datetime.datetime(2017, 11, 10, 1, 22, 30)}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: ed72aa02-3286-4891-acbc-9d9fc80a1103
      created_at: 2017-11-10 01:22:30
      updated_at: 2017-11-10 01:22:30
         city_id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
         user_id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
            name: "Lovely place"
     description: NULL
    number_rooms: 3
number_bathrooms: 1
       max_guest: 6
  price_by_night: 120
        latitude: 37.774
       longitude: -122.431
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/place.py, models/user.py, models/city.py
  
9. DBStorage - Review
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update Review: (models/review.py)

Review inherits from BaseModel and Base (respect the order)
Add or replace in the class Review:
class attribute __tablename__
represents the table name, reviews
class attribute text
represents a column containing a string (1024 characters)
can’t be null
class attribute place_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to places.id
class attribute user_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to users.id
Update User: (models/user.py)

Add or replace in the class User:
class attribute reviews must represent a relationship with the class Review. If the User object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his User should be named user
Update Place: (models/place.py)

for DBStorage: class attribute reviews must represent a relationship with the class Review. If the Place object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his Place should be named place
for FileStorage: getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) d93638d9-8233-4124-8f4e-17786592908b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Review place_id="ed72aa02-3286-4891-acbc-9d9fc80a1103" user_id="d93638d9-8233-4124-8f4e-17786592908b" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) a2d163d3-1982-48ab-a06b-9dc71e68a791
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Review' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Review] (f2616ff2-f723-4d67-85dc-f050a38e0f2f) {'text': 'Amazing place, huge kitchen', 'place_id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'id': 'f2616ff2-f723-4d67-85dc-f050a38e0f2f', 'updated_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'created_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'user_id': 'd93638d9-8233-4124-8f4e-17786592908b'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: f2616ff2-f723-4d67-85dc-f050a38e0f2f
created_at: 2017-11-10 04:06:25
updated_at: 2017-11-10 04:06:25
      text: Amazing place, huge kitchen
  place_id: ed72aa02-3286-4891-acbc-9d9fc80a1103
   user_id: d93638d9-8233-4124-8f4e-17786592908b
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/review.py, models/user.py, models/place.py
  
10. DBStorage - Amenity... and BOOM!
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update Amenity: (models/amenity.py)

Amenity inherits from BaseModel and Base (respect the order)
Add or replace in the class Amenity:
class attribute __tablename__
represents the table name, amenities
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute place_amenities must represent a relationship Many-To-Many between the class Place and Amenity. Please see below more detail: place_amenity in the Place update
Update Place: (models/place.py)

Add an instance of SQLAlchemy Table called place_amenity for creating the relationship Many-To-Many between Place and Amenity:
table name place_amenity
metadata = Base.metadata
2 columns:
place_id, a string of 60 characters foreign key of places.id, primary key in the table and never null
amenity_id, a string of 60 characters foreign key of amenities.id, primary key in the table and never null
Update Place class:
for DBStorage: class attribute amenities must represent a relationship with the class Amenity but also as secondary to place_amenity with option viewonly=False (place_amenity has been define previously)
for FileStorage:
Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.
What’s a Many-to-Many relationship?
In our system, we don’t want to duplicate amenities (for example, having 10000 time the amenity Wifi), so they will be unique. But, at least 2 places can have the same amenity (like Wifi for example). We are in the case of:

an amenity can be linked to multiple places
a place can have multiple amenities
= Many-To-Many

To make this link working, we will create a third table called place_amenity that will create these links.

And you are good, you have a new engine!

guillaume@ubuntu:~/AirBnB_v2$ cat main_place_amenities.py 
#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py
OK
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 47321eb8-152a-46df-969a-440aa67a6d59
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Cable
*************************** 2. row ***************************
        id: 4a307e7f-68f9-438f-81c0-8325898dda2a
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Oven
*************************** 3. row ***************************
        id: b80aec52-d0c9-420a-8471-3254572954b6
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Wifi
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 1
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
*************************** 2. row ***************************
              id: db549ae1-4500-4d0c-9b50-4b4978ed229e
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 2
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM place_amenity\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 2. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 3. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 4a307e7f-68f9-438f-81c0-8325898dda2a
*************************** 4. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
*************************** 5. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/amenity.py, models/place.py
  
Copyright © 2025 ALX, All rights reserved.





SE Foundations
Average: 112.81%
0x03. AirBnB clone - Deploy static
DevOps
Python
SysAdmin
Scripting
CI/CD
 Weight: 1
 Project over - took place from Jul 10, 2024 8:00 AM to Jul 12, 2024 8:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 21.5/51 mandatory & 12.5/35 optional
Altogether:  57.22%
Mandatory: 42.16%
Optional: 35.71%
Calculation:  42.16% + (42.16% * 35.71%)  == 57.22%
Concepts
For this project, we expect you to look at these concepts:

CI/CD
AirBnB clone
Background Context
Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

Before starting, please fork the repository AirBnB_clone_v2 from your partner if you don’t have it



Resources
Read or watch:

How to use Fabric
How to use Fabric in Python
Fabric and command line options
CI/CD concept page
Nginx configuration for beginners
Difference between root and alias on NGINX
Fabric for Python 3
Fabric Documentation
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is Fabric
How to deploy code to a server easily
What is a tgz archive
How to execute Fabric command locally
How to execute Fabric command remotely
How to transfer files with Fabric
How to manage Nginx configuration
What is the difference between root and alias in a Nginx configuration
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.0)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the folder of the project is mandatory
Your code should use the PEP 8 style (version 1.7.*)
Your Fabric file must work with Fabric 3 version 1.14.post1 (installation instruction below)
All your files must be executable
The length of your files will be tested using wc
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Bash Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu20.04.1 via apt-get) without any errors
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
More Info
Install Fabric for Python 3 - version 1.14.post1
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
Video library(1 total)
Search by title
Deploy static files with Fabric
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Prepare your web servers
mandatory
Score: 50.0% (Checks completed: 100.0%)
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

Install Nginx if it not already installed
Create the folder /data/ if it doesn’t already exist
Create the folder /data/web_static/ if it doesn’t already exist
Create the folder /data/web_static/releases/ if it doesn’t already exist
Create the folder /data/web_static/shared/ if it doesn’t already exist
Create the folder /data/web_static/releases/test/ if it doesn’t already exist
Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
Use alias inside your Nginx configuration
Tip
Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

In optional, you will redo this task but by using Puppet

ubuntu@89-web-01:~/$ sudo ./0-setup_web_static.sh
ubuntu@89-web-01:~/$ echo $?
0
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 ubuntu ubuntu 4096 Mar 7 22:29 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
ALX
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>
ubuntu@89-web-01:~/$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 0-setup_web_static.sh
  
1. Compress before sending
mandatory
Score: 50.0% (Checks completed: 100.0%)
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack 
Packing web_static to versions/web_static_20170314233357.tgz
[localhost] local: tar -cvzf versions/web_static_20170314233357.tgz web_static
web_static/
web_static/.DS_Store
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170314233357.tgz -> 21283Bytes

Done.
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
-rw-rw-r-- 1 guillaume guillaume 21283 Mar 14 23:33 versions/web_static_20170314233357.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$
Repo:

GitHub repository: AirBnB_clone_v2
File: 1-pack_web_static.py
  
2. Deploy archive!
mandatory
Score: 50.0% (Checks completed: 100.0%)
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:

Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
The script should take the following steps:
Upload the archive to the /tmp/ directory of the web server
Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
Delete the archive from the web server
Delete the symbolic link /data/web_static/current from the web server
Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
All remote commands must be executed on your both web servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
Returns True if all operations have been done correctly, otherwise returns False
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =...)

Disclaimer: commands execute by Fabric displayed below are linked to the way we implemented the archive function do_pack - like the mv command - depending of your implementation of it, you may don’t need it

guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'do_deploy'
[52.55.249.213] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
guillaume@ubuntu:~/AirBnB_clone_v2$ 
guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">ALX </p>
        </footer>
    </body>
</html>
guillaume@ubuntu:~/AirBnB_clone_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 2-do_deploy_web_static.py
  
3. Full deployment
mandatory
Score: 19.23% (Checks completed: 38.46%)
Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:

Prototype: def deploy():
The script should take the following steps:
Call the do_pack() function and store the path of the created archive
Return False if no archive has been created
Call the do_deploy(archive_path) function, using the new path of the new archive
Return the return value of do_deploy
All remote commands must be executed on both of web your servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'deploy'
Packing web_static to versions/web_static_20170315015620.tgz
[localhost] local: tar -cvzf versions/web_static_20170315015620.tgz web_static
web_static/
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170315015620.tgz -> 27280335Bytes
[52.55.249.213] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: rm /tmp/web_static_20170315015620.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: rm /tmp/web_static_20170315015620.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
guillaume@ubuntu:~/AirBnB_clone_v2$ 
guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">ALX</p>
        </footer>
    </body>
</html>
guillaume@ubuntu:~/AirBnB_clone_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 3-deploy_web_static.py
   
4. Keep it clean!
#advanced
Score: 30.0% (Checks completed: 60.0%)
Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean:

Prototype: def do_clean(number=0):
number is the number of the archives, including the most recent, to keep.
If number is 0 or 1, keep only the most recent version of your archive.
if number is 2, keep the most recent, and second most recent versions of your archive.
etc.
Your script should:
Delete all unnecessary archives (all archives minus the number to keep) in the versions folder
Delete all unnecessary archives (all archives minus the number to keep) in the /data/web_static/releases folder of both of your web servers
All remote commands must be executed on both of your web servers (using the env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015414.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015448.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 100-clean_web_static.py do_clean:number=2 -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 100-clean_web_static.py
   
5. Puppet for setup
#advanced
Score: 50.0% (Checks completed: 100.0%)
Redo the task #0 but by using Puppet:

ubuntu@89-web-01:~/$ puppet apply 101-setup_web_static.pp
....
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 root root   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 root root 4096 Mar 7 22:29 releases
drwxr-xr-x 2 root root 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>
ubuntu@89-web-01:~/$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 101-setup_web_static.pp
 
Copyright © 2025 ALX, All rights reserved.





SE Foundations
Average: 112.81%
0x04. AirBnB clone - Web framework
Python
Back-end
Webserver
Flask
 Weight: 2
 Project over - took place from Jul 25, 2024 8:00 AM to Jul 29, 2024 8:00 AM
 Manual QA review was done on Aug 8, 2024 11:28 AM
 An auto review will be launched at the deadline
In a nutshell…
Manual QA review: 0.0/16 mandatory & 0.0/20 optional
Auto QA review: 81.0/143 mandatory
Altogether:  50.94%
Mandatory: 50.94%
Optional: 0.0%
Calculation:  50.94% + (50.94% * 0.0%)  == 50.94%
Overall comment:
Project was failed automatically.

Concepts
For this project, we expect you to look at this concept:

AirBnB clone
Resources
Read or watch:

What is a Web Framework?
A Minimal Application
Routing (except “HTTP Methods”)
Rendering Templates
Synopsis
Variables
Comments
Whitespace Control
List of Control Structures (read up to “Call”)
Flask
Jinja
Recommended YouTube playlist to get you started

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is a Web Framework
How to build a web framework with Flask
How to define routes in Flask
What is a route
How to handle variables in a route
What is a template
How to create a HTML response in Flask by using a template
How to create a dynamic template (loops, conditions…)
How to display in HTML data from a MySQL database
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
HTML/CSS Files
Allowed editors: vi, vim, emacs
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
All your CSS files should be in the styles folder
All your images should be in the images folder
You are not allowed to use !important or id (#... in the CSS file)
All tags must be in uppercase
Current screenshots have been done on Chrome 56.0.2924.87.
No cross browsers
More Info
Install Flask
$ pip3 install Flask


Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

Video library(1 total)
Search by title
Python: Flask the web framework
Tasks
0. Hello Flask!
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 0-hello_route.py, __init__.py
  
1. HBNB
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 1-hbnb_route.py
  
2. C is fun!
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 2-c_route.py
  
3. Python is cool!
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 3-python_route.py
  
4. Is it a number?
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 4-number_route.py
  
5. Number template
mandatory
Score: 100.0% (Checks completed: 100.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 5-number_template.py, templates/5-number.html
  
6. Odd or even?
mandatory
Score: 91.67% (Checks completed: 91.67%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
Directory: web_flask
File: 6-number_odd_or_even.py, templates/6-number_odd_or_even.html
   
7. Improve engines
mandatory
Score: 0.0% (Checks completed: 0.0%)
Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update FileStorage: (models/engine/file_storage.py)

Add a public method def close(self):: call reload() method for deserializing the JSON file to objects
Update DBStorage: (models/engine/db_storage.py)

Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session tips
Update State: (models/state.py) - If it’s not already present

If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!
At this moment, in another tab:

guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 
And let’s go back the Python console:

>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!
And for the getter cities in the State model:

guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/engine/file_storage.py, models/engine/db_storage.py, models/state.py
  
8. List of states
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>
Import this 7-dump to have some data
You must use the option strict_slashes=False in your route definition
IMPORTANT

Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository (Task)
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: web_flask/7-states_list.py, web_flask/templates/7-states_list.html
   
9. Cities by states
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
To load all cities of a State:
If your storage engine is DBStorage, you must use cities relationship
Otherwise, use the public getter method cities
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B>
Import this 7-dump to have some data
You must use the option strict_slashes=False in your route definition
IMPORTANT

Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository (Task)
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B>
                <UL>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479547: <B>Fremont</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479547: <B>Napa</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479547: <B>San Francisco</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479547: <B>San Jose</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479547: <B>Sonoma</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479548: <B>Denver</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479549: <B>Miami</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479549: <B>Orlando</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479551: <B>Honolulu</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479551: <B>Kailua</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479551: <B>Pearl city</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479554: <B>Baton rouge</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479554: <B>Lafayette</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479554: <B>New Orleans</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479555: <B>Saint Paul</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479556: <B>Jackson</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479556: <B>Meridian</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479556: <B>Tupelo</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479557: <B>Eugene</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479557: <B>Portland</B></LI>

                </UL>
            </LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 


Repo:

GitHub repository: AirBnB_clone_v2
File: web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html
   
10. States and State
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
To load all cities of a State:
If your storage engine is DBStorage, you must use cities relationship
Otherwise, use the public getter method cities
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>
/states/<id>: display a HTML page: (inside the tag BODY)
If a State object is found with this id:
H1 tag: “State: ”
H3 tag: “Cities:”
UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B>
Otherwise:
H1 tag: “Not found!”
You must use the option strict_slashes=False in your route definition
Import this 7-dump to have some data
IMPORTANT

Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository (Task)
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
guillaume@ubuntu:~$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: web_flask/9-states.py, web_flask/templates/9-states.html
   
11. HBNB filters
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
To load all cities of a State:
If your storage engine is DBStorage, you must use cities relationship
Otherwise, use the public getter method cities
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/hbnb_filters: display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static
Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
Use 6-index.html content as source code for the template 10-hbnb_filters.html:
Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
You must use the option strict_slashes=False in your route definition
Import this 10-dump to have some data
IMPORTANT

Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository (Task)
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In the browser:

   

Repo:

GitHub repository: AirBnB_clone_v2
File: web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/

Copyright © 2025 ALX, All rights reserved.
2024-08-08 09:28 (GMT+01:00)






SE Foundations
Average: 112.81%
0x05. AirBnB clone - RESTful API
Python
Back-end
API
Webserver
Flask
 Weight: 2
 Project to be done in teams of 2 people (your team: Ibrahim Abdullahi)
 Project over - took place from Aug 1, 2024 8:00 AM to Aug 6, 2024 8:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 28.0/267 mandatory & 1.0/52 optional
Altogether:  10.69%
Mandatory: 10.49%
Optional: 1.92%
Calculation:  10.49% + (10.49% * 1.92%)  == 10.69%
Concepts
For this project, we expect you to look at these concepts:

REST API
AirBnB clone
Resources
Read or watch:

REST API concept page
Learn REST: A RESTful Tutorial
Designing a RESTful API with Python and Flask
HTTP access control (CORS)
Flask cheatsheet
What are Flask Blueprints, exactly?
Flask
Modular Applications with Blueprints
Flask tests
Flask-CORS
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What REST means
What API means
What CORS means
What is an API
What is a REST API
What are other type of APIs
Which is the HTTP method to retrieve resource(s)
Which is the HTTP method to create a resource
Which is the HTTP method to update resource
Which is the HTTP method to delete resource
How to request REST API
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
We strongly encourage you to work together on test cases, so that you don’t miss any edge cases
GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

More Info


Install Flask
$ pip3 install Flask
Video library(2 total)
Search by title
Python: Flask RestAPI
AirBnB API
Tasks
0. Restart from scratch!
mandatory
Score: 100.0% (Checks completed: 100.0%)
No no no! We are already too far in the project to restart everything.

But once again, let’s work on a new codebase.

For this project you will fork this codebase:

Update the repository name to AirBnB_clone_v3
Update the README.md:
Add yourself as an author of the project
Add new information about your new contribution
Make it better!
If you’re the owner of this codebase, create a new repository called AirBnB_clone_v3 and copy over all files from AirBnB_clone_v2
Repo:

GitHub repository: AirBnB_clone_v3
 
1. Never fail!
mandatory
Score: 69.23% (Checks completed: 69.23%)


Since the beginning we’ve been using the unittest module, but do you know why unittests are so important? Because when you add a new feature, you refactor a piece of code, etc… you want to be sure you didn’t break anything.

At ALX, we have a lot of tests, and they all pass! Just for the Intranet itself, there are:

5,213 assertions (as of 08/20/2018)
13,061 assertions (as of 01/25/2021)
The following requirements must be met for your project:

all current tests must pass (don’t delete them…)
add new tests as much as you can (tests are mandatory for some tasks)
guillaume@ubuntu:~/AirBnB_v3$ python3 -m unittest discover tests 2>&1 | tail -1
OK
guillaume@ubuntu:~/AirBnB_v3$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v3$ 
Repo:

GitHub repository: AirBnB_clone_v3
   
2. Improve storage
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update DBStorage and FileStorage, adding two new methods. All changes should be done in the branch storage_get_count:

A method to retrieve one object:

Prototype: def get(self, cls, id):
cls: class
id: string representing the object ID
Returns the object based on the class and its ID, or None if not found
A method to count the number of objects in storage:

Prototype: def count(self, cls=None):
cls: class (optional)
Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.
Don’t forget to add new tests for these 2 methods on each storage engine.

guillaume@ubuntu:~/AirBnB_v3$ cat test_get_count.py
#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))

guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py 
All objects: 1013
State objects: 27
First state: [State] (f8d21261-3e79-4f5c-829a-99d7452cd73c) {'name': 'Colorado', 'updated_at': datetime.datetime(2017, 3, 25, 2, 17, 6), 'created_at': datetime.datetime(2017, 3, 25, 2, 17, 6), '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fc0103a8e80>, 'id': 'f8d21261-3e79-4f5c-829a-99d7452cd73c'}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ ./test_get_count.py 
All objects: 19
State objects: 5
First state: [State] (af14c85b-172f-4474-8a30-d4ec21f9795e) {'updated_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378824), 'name': 'Arizona', 'id': 'af14c85b-172f-4474-8a30-d4ec21f9795e', 'created_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378763)}
guillaume@ubuntu:~/AirBnB_v3$ 
For this task, you must make a pull request on GitHub.com, and ask at least one of your peer to review and merge it.

Repo:

GitHub repository: AirBnB_clone_v3
File: models/engine/db_storage.py, models/engine/file_storage.py, tests/test_models/test_engine/test_db_storage.py, tests/test_models/test_engine/test_file_storage.py
   
3. Status of your API
mandatory
Score: 0.0% (Checks completed: 0.0%)
It’s time to start your API!

Your first endpoint (route) will be to return the status of your API:

guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
In another terminal:

guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
guillaume@ubuntu:~/AirBnB_v3$ 
Magic right? (No need to have a pretty rendered output, it’s a JSON, only the structure is important)

Ok, let starts:

Create a folder api at the root of the project with an empty file __init__.py
Create a folder v1 inside api:
create an empty file __init__.py
create a file app.py:
create a variable app, instance of Flask
import storage from models
import app_views from api.v1.views
register the blueprint app_views to your Flask instance app
declare a method to handle @app.teardown_appcontext that calls storage.close()
inside if __name__ == "__main__":, run your Flask server (variable app) with:
host = environment variable HBNB_API_HOST or 0.0.0.0 if not defined
port = environment variable HBNB_API_PORT or 5000 if not defined
threaded=True
Create a folder views inside v1:
create a file __init__.py:
import Blueprint from flask doc
create a variable app_views which is an instance of Blueprint (url prefix must be /api/v1)
wildcard import of everything in the package api.v1.views.index => PEP8 will complain about it, don’t worry, it’s normal and this file (v1/views/__init__.py) won’t be check.
create a file index.py
import app_views from api.v1.views
create a route /status on the object app_views that returns a JSON: "status": "OK" (see example)
Repo:

GitHub repository: AirBnB_clone_v3
File: api/__init__.py, api/v1/__init__.py, api/v1/views/__init__.py, api/v1/views/index.py, api/v1/app.py
   
4. Some stats?
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create an endpoint that retrieves the number of each objects by type:

In api/v1/views/index.py
Route: /api/v1/stats
You must use the newly added count() method from storage
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/stats
{
  "amenities": 47, 
  "cities": 36, 
  "places": 154, 
  "reviews": 718, 
  "states": 27, 
  "users": 31
}
guillaume@ubuntu:~/AirBnB_v3$ 
(No need to have a pretty rendered output, it’s a JSON, only the structure is important)

Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/index.py
   
5. Not found
mandatory
Score: 0.0% (Checks completed: 0.0%)
Designers are really creative when they have to design a “404 page”, a “Not found”… 34 brilliantly designed 404 error pages

Today it’s different, because you won’t use HTML and CSS, but JSON!

In api/v1/app.py, create a handler for 404 errors that returns a JSON-formatted 404 status code response. The content should be: "error": "Not found"

guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/nop
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/nop HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Fri, 14 Apr 2017 23:43:24 GMT
< 
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ 
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/app.py
   
6. State
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a new view for State objects that handles all default RESTFul API actions:

In the file api/v1/views/states.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all State objects: GET /api/v1/states

Retrieves a State object: GET /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error
Deletes a State object:: DELETE /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a State: POST /api/v1/states

You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key name, raise a 400 error with the message Missing name
Returns the new State with the status code 201
Updates a State object: PUT /api/v1/states/<state_id>

If the state_id is not linked to any State object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
Update the State object with all key-value pairs of the dictionary.
Ignore keys: id, created_at and updated_at
Returns the State object with the status code 200
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/
[
  {
    "__class__": "State", 
    "created_at": "2017-04-14T00:00:02", 
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
    "name": "Louisiana", 
    "updated_at": "2017-04-14T00:00:02"
  }, 
  {
    "__class__": "State", 
    "created_at": "2017-04-14T16:21:42", 
    "id": "1a9c29c7-e39c-4840-b5f9-74310b34f269", 
    "name": "Arizona", 
    "updated_at": "2017-04-14T16:21:42"
  }, 
...
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99
 {
  "__class__": "State", 
  "created_at": "2017-04-14T00:00:02", 
  "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
  "name": "Louisiana", 
  "updated_at": "2017-04-14T00:00:02"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}' -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/states/ HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 22
> 
* upload completely sent off: 22 out of 22 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 195
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sat, 15 Apr 2017 01:30:27 GMT
< 
{
  "__class__": "State", 
  "created_at": "2017-04-15T01:30:27.557877", 
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
  "name": "California", 
  "updated_at": "2017-04-15T01:30:27.558081"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X PUT http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'
{
  "__class__": "State", 
  "created_at": "2017-04-15T01:30:28", 
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
  "name": "California is so cool", 
  "updated_at": "2017-04-15T01:51:08.044996"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{
  "__class__": "State", 
  "created_at": "2017-04-15T01:30:28", 
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
  "name": "California is so cool", 
  "updated_at": "2017-04-15T01:51:08"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X DELETE http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ 
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/states.py, api/v1/views/__init__.py
   
7. City
mandatory
Score: 0.0% (Checks completed: 0.0%)
Same as State, create a new view for City objects that handles all default RESTFul API actions:

In the file api/v1/views/cities.py
You must use to_dict() to serialize an object into valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all City objects of a State: GET /api/v1/states/<state_id>/cities

If the state_id is not linked to any State object, raise a 404 error
Retrieves a City object. : GET /api/v1/cities/<city_id>

If the city_id is not linked to any City object, raise a 404 error
Deletes a City object: DELETE /api/v1/cities/<city_id>

If the city_id is not linked to any City object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a City: POST /api/v1/states/<state_id>/cities

You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the state_id is not linked to any State object, raise a 404 error
If the HTTP body request is not a valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key name, raise a 400 error with the message Missing name
Returns the new City with the status code 201
Updates a City object: PUT /api/v1/cities/<city_id>

If the city_id is not linked to any City object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP request body is not valid JSON, raise a 400 error with the message Not a JSON
Update the City object with all key-value pairs of the dictionary
Ignore keys: id, state_id, created_at and updated_at
Returns the City object with the status code 200
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/not_an_id/cities/
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities
[
  {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
    "name": "New Orleans", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
  }, 
  {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "45903748-fa39-4cd0-8a0b-c62bfe471702", 
    "name": "Lafayette", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
  }, 
  {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "e4e40a6e-59ff-4b4f-ab72-d6d100201588", 
    "name": "Baton rouge", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
  }
]
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683
{
  "__class__": "City", 
  "created_at": "2017-03-25T02:17:06", 
  "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
  "name": "New Orleans", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-03-25T02:17:06"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X POST http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities -H "Content-Type: application/json" -d '{"name": "Alexandria"}' -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities/ HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 22
> 
* upload completely sent off: 22 out of 22 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 249
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 16 Apr 2017 03:14:05 GMT
< 
{
  "__class__": "City", 
  "created_at": "2017-04-16T03:14:05.655490", 
  "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
  "name": "Alexandria", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-04-16T03:14:05.655748"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X PUT http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af -H "Content-Type: application/json" -d '{"name": "Bossier City"}'
{
  "__class__": "City", 
  "created_at": "2017-04-16T03:14:06", 
  "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
  "name": "Bossier City", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-04-16T03:15:12.895894"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
{
  "__class__": "City", 
  "created_at": "2017-04-16T03:14:06", 
  "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
  "name": "Bossier City", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-04-16T03:15:13"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X DELETE http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
{}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ 
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/cities.py, api/v1/views/__init__.py
   
8. Amenity
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a new view for Amenity objects that handles all default RESTFul API actions:

In the file api/v1/views/amenities.py
You must use to_dict() to serialize an object into valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all Amenity objects: GET /api/v1/amenities

Retrieves a Amenity object: GET /api/v1/amenities/<amenity_id>

If the amenity_id is not linked to any Amenity object, raise a 404 error
Deletes a Amenity object:: DELETE /api/v1/amenities/<amenity_id>

If the amenity_id is not linked to any Amenity object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a Amenity: POST /api/v1/amenities

You must use request.get_json from Flask to transform the HTTP request to a dictionary
If the HTTP request body is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key name, raise a 400 error with the message Missing name
Returns the new Amenity with the status code 201
Updates a Amenity object: PUT /api/v1/amenities/<amenity_id>

If the amenity_id is not linked to any Amenity object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP request to a dictionary
If the HTTP request body is not valid JSON, raise a 400 error with the message Not a JSON
Update the Amenity object with all key-value pairs of the dictionary
Ignore keys: id, created_at and updated_at
Returns the Amenity object with the status code 200
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/amenities.py, api/v1/views/__init__.py
   
9. User
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a new view for User object that handles all default RESTFul API actions:

In the file api/v1/views/users.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all User objects: GET /api/v1/users

Retrieves a User object: GET /api/v1/users/<user_id>

If the user_id is not linked to any User object, raise a 404 error
Deletes a User object:: DELETE /api/v1/users/<user_id>

If the user_id is not linked to any User object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a User: POST /api/v1/users

You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key email, raise a 400 error with the message Missing email
If the dictionary doesn’t contain the key password, raise a 400 error with the message Missing password
Returns the new User with the status code 201
Updates a User object: PUT /api/v1/users/<user_id>

If the user_id is not linked to any User object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP body request to a dictionary
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
Update the User object with all key-value pairs of the dictionary
Ignore keys: id, email, created_at and updated_at
Returns the User object with the status code 200
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/users.py, api/v1/views/__init__.py
   
10. Place
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a new view for Place objects that handles all default RESTFul API actions:

In the file api/v1/views/places.py
You must use to_dict() to retrieve an object into a valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all Place objects of a City: GET /api/v1/cities/<city_id>/places

If the city_id is not linked to any City object, raise a 404 error
Retrieves a Place object. : GET /api/v1/places/<place_id>

If the place_id is not linked to any Place object, raise a 404 error
Deletes a Place object: DELETE /api/v1/places/<place_id>

If the place_id is not linked to any Place object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a Place: POST /api/v1/cities/<city_id>/places

You must use request.get_json from Flask to transform the HTTP request to a dictionary
If the city_id is not linked to any City object, raise a 404 error
If the HTTP request body is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key user_id, raise a 400 error with the message Missing user_id
If the user_id is not linked to any User object, raise a 404 error
If the dictionary doesn’t contain the key name, raise a 400 error with the message Missing name
Returns the new Place with the status code 201
Updates a Place object: PUT /api/v1/places/<place_id>

If the place_id is not linked to any Place object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP request to a dictionary
If the HTTP request body is not valid JSON, raise a 400 error with the message Not a JSON
Update the Place object with all key-value pairs of the dictionary
Ignore keys: id, user_id, city_id, created_at and updated_at
Returns the Place object with the status code 200
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/places.py, api/v1/views/__init__.py
   
11. Reviews
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a new view for Review object that handles all default RESTFul API actions:

In the file api/v1/views/places_reviews.py
You must use to_dict() to retrieve an object into valid JSON
Update api/v1/views/__init__.py to import this new file
Retrieves the list of all Review objects of a Place: GET /api/v1/places/<place_id>/reviews

If the place_id is not linked to any Place object, raise a 404 error
Retrieves a Review object. : GET /api/v1/reviews/<review_id>

If the review_id is not linked to any Review object, raise a 404 error
Deletes a Review object: DELETE /api/v1/reviews/<review_id>

If the review_id is not linked to any Review object, raise a 404 error
Returns an empty dictionary with the status code 200
Creates a Review: POST /api/v1/places/<place_id>/reviews

You must use request.get_json from Flask to transform the HTTP request to a dictionary
If the place_id is not linked to any Place object, raise a 404 error
If the HTTP body request is not valid JSON, raise a 400 error with the message Not a JSON
If the dictionary doesn’t contain the key user_id, raise a 400 error with the message Missing user_id
If the user_id is not linked to any User object, raise a 404 error
If the dictionary doesn’t contain the key text, raise a 400 error with the message Missing text
Returns the new Review with the status code 201
Updates a Review object: PUT /api/v1/reviews/<review_id>

If the review_id is not linked to any Review object, raise a 404 error
You must use request.get_json from Flask to transform the HTTP request to a dictionary
If the HTTP request body is not valid JSON, raise a 400 error with the message Not a JSON
Update the Review object with all key-value pairs of the dictionary
Ignore keys: id, user_id, place_id, created_at and updated_at
Returns the Review object with the status code 200
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/views/places_reviews.py, api/v1/views/__init__.py
   
12. HTTP access control (CORS)
mandatory
Score: 0.0% (Checks completed: 0.0%)
A resource makes a cross-origin HTTP request when it requests a resource from a different domain, or port, than the one the first resource itself serves.

Read the full definition here

Why do we need this?

Because you will soon start allowing a web client to make requests your API. If your API doesn’t have a correct CORS setup, your web client won’t be able to access your data.

With Flask, it’s really easy, you will use the class CORS of the module flask_cors.

How to install it: $ pip3 install flask_cors

Update api/v1/app.py to create a CORS instance allowing: /* for 0.0.0.0

You will update it later when you will deploy your API to production.

Now you can see this HTTP Response Header: < Access-Control-Allow-Origin: 0.0.0.0

guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683 -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities/1da255c0-f023-4779-8134-2b1b40f87683 HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Access-Control-Allow-Origin: 0.0.0.0
< Content-Length: 236
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 16 Apr 2017 04:20:13 GMT
< 
{
  "__class__": "City", 
  "created_at": "2017-03-25T02:17:06", 
  "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
  "name": "New Orleans", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-03-25T02:17:06"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$ 
Repo:

GitHub repository: AirBnB_clone_v3
File: api/v1/app.py
   

Copyright © 2025 ALX, All rights reserved.






SE Foundations
Average: 112.81%
0x06. AirBnB clone - Web dynamic
Python
Front-end
JavaScript
 Weight: 2
 Project to be done in teams of 2 people (your team: Ibrahim Abdullahi, Matshidiso Pitswane)
 Project over - took place from Aug 8, 2024 8:00 AM to Aug 12, 2024 8:00 AM
 Manual QA review was done on Aug 20, 2024 12:03 PM
 An auto review will be launched at the deadline
In a nutshell…
Manual QA review: 0.0/117 mandatory & 0.0/63 optional
Auto QA review: 0.0/6 mandatory
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%
Overall comment:
Project was failed automatically.

Concepts
For this project, we expect you to look at this concept:

AirBnB clone
Resources
Read or watch:

Selector
Get and set content
Manipulate CSS classes
Manipulate DOM elements
Document ready
Introduction
GET & POST request
HTTP access control (CORS)
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How cool it is to request your own API
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events
How to listen/bind to user events
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Chrome (version 57.0)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
All your JavaScript must be in the folder scripts
You must use JQuery version 3.x
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data…
GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

More Info
Import JQuery
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
Before starting the project…
You will work on a codebase using Flasgger, you will need to install it locally first before starting the RestAPI:

$ sudo apt-get install -y python3-lxml
$ sudo pip3 install flask_cors # if it was not installed yet
$ sudo pip3 install flasgger
If the RestAPI is not starting, please read the error message. Based on the(ses) error message(s), you will have to troubleshoot potential dependencies issues.

Here some solutions:

jsonschema exception
$ sudo pip3 uninstall -y jsonschema 
$ sudo pip3 install jsonschema==3.0.1
No module named 'pathlib2'
$ sudo pip3 install pathlib2
Expose ports from your Vagrant
In your Vagrantfile, add this line for each port forwarded

# I expose the port 5001 of my vm to the port 5001 on my computer
config.vm.network :forwarded_port, guest: 5001, host: 5001 
if you need to expose other ports, same line but you will need to replace the “guest port” (inside your vagrant) and your “host port” (outside your vagrant, used from your browser for example)

It’s important in your project, to use the AirBnB API with the port 5001





Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

Tasks
0. Last clone!
mandatory
Score: 0.0% (Checks completed: 0.0%)
A new codebase again? Yes!

For this project you will fork this codebase:

Update the repository name to AirBnB_clone_v4
Update the README.md:
Add yourself as an author of the project
Add new information about your new contribution
Make it better!
If you’re the owner of this codebase, create a new repository called AirBnB_clone_v4 and copy over all files from AirBnB_clone_v3
If you didn’t install Flasgger from the previous project, it’s time! sudo pip3 install flasgger
Repo:

GitHub repository: AirBnB_clone_v4
   
1. Cash only
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that starts a Flask web application:

Based on web_flask, copy: web_flask/static, web_flask/templates/100-hbnb.html, web_flask/__init__.py and web_flask/100-hbnb.py into the web_dynamic folder
Rename 100-hbnb.py to 0-hbnb.py
Rename 100-hbnb.html to 0-hbnb.html
Update 0-hbnb.py to replace the existing route to /0-hbnb/
If 100-hbnb.html is not present, use 8-hbnb.html instead

guillaume@ubuntu:~/AirBnB_v4$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_dynamic.0-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
One problem now is the asset caching done by Flask.

To avoid that, you will add a query string to each asset:

In 0-hbnb.py, add a variable cache_id to the render_template. The value of this variable must be an UUID (uuid.uuid4())

In 0-hbnb.html, add this variable cache_id as query string to each <link> tag URL

guillaume@ubuntu:~/AirBnB_v4$ curl -s -XGET http://0.0.0.0:5000/0-hbnb/ | head -6
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" type="text/css" href="../static/styles/4-common.css?e211c9eb-7d17-4f12-85eb-4d50fa50cb1d" />
    <link rel="stylesheet" type="text/css" href="../static/styles/3-header.css?e211c9eb-7d17-4f12-85eb-4d50fa50cb1d" />
guillaume@ubuntu:~/AirBnB_v4$ curl -s -XGET http://0.0.0.0:5000/0-hbnb/ | head -6
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" type="text/css" href="../static/styles/4-common.css?f834413e-0aa9-4767-b64a-c92db9cb1f82" />
    <link rel="stylesheet" type="text/css" href="../static/styles/3-header.css?f834413e-0aa9-4767-b64a-c92db9cb1f82" />
guillaume@ubuntu:~/AirBnB_v4$ 
Repo:

GitHub repository: AirBnB_clone_v4
Directory: web_dynamic
File: 0-hbnb.py, templates/0-hbnb.html
 
2. Select some Amenities to be comfortable!
mandatory
Score: 0.0% (Checks completed: 0.0%)
For the moment the filters section is static, let’s make it dynamic!

Replace the route 0-hbnb with 1-hbnb in the file 1-hbnb.py (based on 0-hbnb.py)

Create a new template 1-hbnb.html (based on 0-hbnb.html) and update it:

Import JQuery in the <head> tag
Import the JavaScript static/scripts/1-hbnb.js in the <head> tag
In 1-hbnb.html and the following HTML files, add this variable cache_id as query string to the above <script> tag
Add a <input type="checkbox"> tag to the li tag of each amenity
The new checkbox must be at 10px on the left of the Amenity name
Add to the input tags of each amenity (<li> tag) the attribute data-id=":amenity_id" => this will allow us to retrieve the Amenity ID from the DOM
Add to the input tags of each amenity (<li> tag) the attribute data-name=":amenity_name" => this will allow us to retrieve the Amenity name from the DOM
Write a JavaScript script (static/scripts/1-hbnb.js):

Your script must be executed only when DOM is loaded
You must use JQuery
Listen for changes on each input checkbox tag:
if the checkbox is checked, you must store the Amenity ID in a variable (dictionary or list)
if the checkbox is unchecked, you must remove the Amenity ID from the variable
update the h4 tag inside the div Amenities with the list of Amenities checked
As example:

  

Repo:

GitHub repository: AirBnB_clone_v4
Directory: web_dynamic
File: 1-hbnb.py, templates/1-hbnb.html, static/scripts/1-hbnb.js
 
3. API status
mandatory
Score: 0.0% (Checks completed: 0.0%)
Before requesting the HBNB API, it’s better to know the status of this one.

Update the API entry point (api/v1/app.py) by replacing the current CORS CORS(app, origins="0.0.0.0") by CORS(app, resources={r"/api/v1/*": {"origins": "*"}}).

Change the route 1-hbnb to 2-hbnb in the file 2-hbnb.py (based on 1-hbnb.py)

Create a new template 2-hbnb.html (based on 1-hbnb.html) and update it:

Import the JavaScript static/scripts/2-hbnb.js in the <head> tag (instead of 1-hbnb.js)
Add a new div element in the header tag:
Attribute ID should be api_status
Align to the right
Circle of 40px diameter
Center vertically
At 30px of the right border
Background color #cccccc
Also add a class available for this new element in web_dynamic/static/styles/3-header.css:
Background color #ff545f
Write a JavaScript script (static/scripts/2-hbnb.js):

Based on 1-hbnb.js
Request http://0.0.0.0:5001/api/v1/status/:
If in the status is “OK”, add the class available to the div#api_status
Otherwise, remove the class available to the div#api_status
To start the API in the port 5001:

guillaume@ubuntu:~/AirBnB_v4$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_PORT=5001 python3 -m api.v1.app
...
For example:

 

Repo:

GitHub repository: AirBnB_clone_v4
File: api/v1/app.py, web_dynamic/2-hbnb.py, web_dynamic/templates/2-hbnb.html, web_dynamic/static/styles/3-header.css, web_dynamic/static/scripts/2-hbnb.js
 
4. Fetch places
mandatory
Score: 0.0% (Checks completed: 0.0%)
Replace the route 2-hbnb with 3-hbnb in the file 3-hbnb.py (based on 2-hbnb.py)

Create a new template 3-hbnb.html (based on 2-hbnb.html) and update it:

Import the JavaScript static/scripts/3-hbnb.js in the <head> tag (instead of 2-hbnb.js)
Remove the entire Jinja section of displaying all places (all article tags)
Write a JavaScript script (static/scripts/3-hbnb.js):

Based on 2-hbnb.js
Request http://0.0.0.0:5001/api/v1/places_search/:
Description of this endpoint here. If this endpoint is not available, you will have to add it to the API (you can work all together for creating this endpoint)
Send a POST request with Content-Type: application/json and an empty dictionary in the body - cURL version: curl "http://0.0.0.0:5001/api/v1/places_search" -XPOST -H "Content-Type: application/json" -d '{}'
Loop into the result of the request and create an article tag representing a Place in the section.places. (you can remove the Owner tag in the place description)
The final result must be the same as previously, but now, places are loaded from the front-end, not from the back-end!

Repo:

GitHub repository: AirBnB_clone_v4
File: web_dynamic/3-hbnb.py, web_dynamic/templates/3-hbnb.html, web_dynamic/static/scripts/3-hbnb.js
 
5. Filter places by Amenity
mandatory
Score: 0.0% (Checks completed: 0.0%)
Replace the route 3-hbnb with 4-hbnb in the file 4-hbnb.py (based on 3-hbnb.py)

Create a new template 4-hbnb.html (based on 3-hbnb.html) and update it:

Import the JavaScript static/scripts/4-hbnb.js in the <head> tag (instead of 3-hbnb.js)
Write a JavaScript script (static/scripts/4-hbnb.js):

Based on 3-hbnb.js
When the button tag is clicked, a new POST request to places_search should be made with the list of Amenities checked
Now you have the first filter implemented, enjoy!

Repo:

GitHub repository: AirBnB_clone_v4
File: web_dynamic/4-hbnb.py, web_dynamic/templates/4-hbnb.html, web_dynamic/static/scripts/4-hbnb.js
 

Copyright © 2025 ALX, All rights reserved.