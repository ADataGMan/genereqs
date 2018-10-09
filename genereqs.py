#!/usr/bin/env python3
def generate_requirements(globals):
    """ 
        Purpose
        ----------
        Generate requirements from a python file.

        Parameters
        ----------
        globals : globals()
        
        To Use
        ---------- 
        Import this file into the file you wish to it in.
        This can be done using "import genereqs" above where you
        call the function. 

        Once you have imported genereqs, call it by using
        "genereqs.generate_requirements(globals())".        
        This calls the module name, then the function name
        and passes in a function containing the 
        global namespace as a dictionary. The globals()
        function is the only parameter and should be inserted
        into the function call.     
    """

    from pip._internal.operations import freeze
    import sys
    import os

    # Get a list of installed modules from sys and get the intersection
    # with the result from the global variables defined in the file.
    global_module_list = list(set(sys.modules) & set(globals))

    # Get list of modules from the python Freeze Command.
    # This is done for versioning.
    pip_freeze_list = list(freeze.freeze())

    module_dictionary = dict()

    for item in pip_freeze_list:
        module_name = item.split("=")[0].lower()
        module_dictionary[module_name] = item

    modules_result = list()

    # Get the list of each item that intersects between the 
    # global module list  from above  
    # and the keys of the dictionary from the Freeze list.

    for key in (global_module_list & module_dictionary.keys()):
        modules_result.append(module_dictionary[key])

    with open('requirements.txt', 'w') as open_file:
        for row in modules_result:
            open_file.write(f"{row}\n")
        # truncate the last \n and use os.linesep to determine 
        # where this should be on linux or windows.
        open_file.truncate(open_file.tell() - len(os.linesep))