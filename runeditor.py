run = open('run.ps1', 'w')
runCommand = '& ' + __file__.replace('runeditor.py', '\\scripts\\python.exe ' + __file__.replace('runeditor.py', 'nongloader.py'))
run.write(runCommand)
print(runCommand)