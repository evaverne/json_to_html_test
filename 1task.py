import json

file = open("/Users/evaverne/Documents/Programming/jsontohtml/source.json", "r")
s = file.read()
book = json.loads(s)

l=[]
for item in book:
	[l.extend([k,v]) for k,v in item.items()]
	index_of_value = l.index("title") + 2
	l[l.index("title")] = "<h>"
	l.insert(index_of_value, "</h>")

	index_of_body = l.index("body") + 2
	l[l.index("body")] = "<p>"
	l.insert(index_of_body, "</p>")

print(''.join(l))

#2 hours including research 