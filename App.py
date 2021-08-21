from subprocess import call

"""
The application is running with python3

however 'python3' in 'anaconda environment' 
is running with the command 'python <file name>'  
"""

try:
    #   try to run with 'anaconda environment'
    call(["python", "GUI.py"])
    #   try to run with 'python3'
    call(["python3", "GUI.py"])


except (IOError, OSError) as e:
    print(e.errno)


