from pathlib import Path

#Prints a list of all pdf files in the in the given the directory.
files = [f for f in Path(r'C:\Users\admin\Documents\PDF BOOKS').glob('**/*.pdf')]



for file in files:
	# The file output includes the directoy's name plus the file name.
	# i.e C:\Users\admin\Documents\PDF BOOKS\file_name.pdf
	name = str(file).split('\\')[-1:][0] # prints the file name and the extenstion alone
	name_list = name.split()

	print(' '.join(name_list[:-3]))



	
# To modifiy the code as to to print the output into a text file:

with open('names.txt', 'w') as f:

    files = [f for f in Path(r'C:\Users\admin\Documents\PDF BOOKS').glob('**/*.pdf')]

    for file in files:
        name = str(file).split('\\')[-1:][0]
        name_list = name.split()

        file_content = ' '.join(name_list[:-3])

        print(file_content, file=f)
