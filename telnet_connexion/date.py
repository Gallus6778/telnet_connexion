from datetime import datetime

hour = datetime.now()

string = str(datetime.now())
string = string.replace(':', '-')

print(string)
file_name = 'new_file-' + string + '.txt'


file_name = open(file_name, 'a')
file_name.close()