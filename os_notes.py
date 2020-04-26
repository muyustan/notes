import os
print("os.getcwd():", os.getcwd())
print("__file__:", __file__)
print("os.path.dirname(__file__):", os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))
print(os.listdir(os.getcwd()))  # lists the files in the path
print(os.listdir(os.path.dirname(__file__)))

"""
os.getcwd()
os.chdir()
os.listdir()
os.mkdir('filename')
os.mkdirs('filename/subfilename/subfilename')
os.rmdir('filename')
os.removedirs('filename/subfilename/subfilename')
os.rename('old','new')
os.stat('document')
game_folder = os.path.dirname(__file__)
"""
