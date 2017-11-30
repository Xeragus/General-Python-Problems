import datetime
import glob2

# get all .txt files
file_names = glob2.glob("*.txt")

# open the result file
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
	for file_name in file_names:
		# open the files one by one and write their content
		# in the result file opened previously
		with open(file_name, 'r') as f:
			file.write(f.read()+"\n")