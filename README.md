# The program requires no additional packages or libraries
# To exexute this solution, do ensure you have python installed preferrably python 3+
# Steps to take

locate the main.py file in the root of the project
main.py initializes a class named DataReader also located in the root folder, it then proceeds to call the run method of the class which can take two optional arguments which would be the source file to read JSON data from and the destination file where the read output would be dumped into.

# The run method can be excuted as called as follows

-- obejct = DataReader()
-- object.run() // without arguments.
 # OR

-- object = DataReader()
-- object.run('sourcefilenameasstring', 'destinationfilenameasstring')
# object.run('data_1.json', 'schema_2.json')
 no need adding their respective directories as it has already been predefined in the DataReader class.

# Run python main.py to execute program.
