from pathlib import Path


files = [f for f in Path(r'C:\Users\admin\Documents\PDF BOOKS').glob('**/*.pdf')]

for file in files:
	name = str(file).split('\\')[-1:][0]
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
