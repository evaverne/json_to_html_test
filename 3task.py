import json

file = open("/Users/evaverne/Documents/Programming/jsontohtml/source.json", "r")
s = file.read()
book = json.loads(s)

big_list = []

l=[]
for item in book:
	[l.extend([k,v]) for k,v in item.items()]

keys = l[::2]
values = l[1::2]

if len(book) > 1:
	big_list.append("<ul>")
	for item in book:
		big_list.append("<li>")
		index = 0 
		for one in item:
			big_list.append('<'+one+'>')
			big_list.append(values[index])
			big_list.append('</'+one+'>')
			index += 1
		big_list.append("</li>")
	big_list.append("</ul>")

print(''.join(big_list))