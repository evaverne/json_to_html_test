import json 

#read the file
file = open("/Users/evaverne/Documents/Programming/jsontohtml/source.json", "r")
s = file.read()
book = json.loads(s)

#make a list out of it
l=[]
for item in book:
	[l.extend([k,v]) for k,v in item.items()]

#split into two lists: keys and values accordingly
keys = l[::2]
values = l[1::2]

#add extra symbols and put everything in the right order
big_list = []
index = 0 
for key in keys:
	big_list.append('<'+key+'>')
	big_list.append(values[index])
	big_list.append('</'+key+'>')
	index += 1

print(''.join(big_list))

# 40 min, including creating git repo and commint of the first task