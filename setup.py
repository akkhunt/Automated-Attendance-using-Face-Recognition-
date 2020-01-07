from cx_Freeze import setup, Executable

setup( name = "firstpage.py" ,
       version = "0.1" ,
       description = "frsa" ,
       executables = [Executable("C:\python27\FRSA\\firstpage.py")] ,
       )
