from __future__ import print_function
#This is very implementations specific
#Works in python 3 on windows 64 in idle
#Hello World Program
#__builtins__=None 

(lambda object="".__class__.__bases__[0]:(
    lambda allClasses=object.__subclasses__():(
        lambda findClass=(lambda x:[y for y in allClasses if y.__name__==x][0]):(
            lambda importer=findClass('BuiltinImporter'):(
                lambda sys=importer.load_module('sys'):(
                    lambda print=sys.stdout.writelines:(
                        print('Hello World')))())())())())())()

