def isUpperCase(c): return c>=ord('A') and c<=ord('Z')
def camelToSnakeCase(inp):
	out=""
	for i in range(0,len(inp)):
		c=ord(inp[i])
		if i>0:
			if (not isUpperCase(ord(inp[i-1]))) and isUpperCase(c):
				c+=ord('a')-ord('A')
				out+='_'
		out+=chr(c)
	return out
		
def add_use(items,item):
	if item in items: items[item]+=1
	else: items[item]=1

def sort_by_neg_val(items):
	tmp = {k: v for k, v in sorted(items.items(), key=lambda item: -item[1])}
	return [k for k,v in tmp.items()]

frags={};
nlines=0;
lfrag=open("label_fragments.txt","r").readlines()
unique_words={};

for line in lfrag:
	line=line[:-1] #strip trailing '\n'
	add_use(frags,line)
	line=camelToSnakeCase(line).replace("("," ").replace(")"," ").replace("|"," ").replace("["," ").replace("]"," ").replace("_"," ").replace("."," ").replace("~"," ").replace("-"," ")
	
	for word in line.split(): add_use(unique_words,word)

out=open("unique_fragments.txt","w")
for item in sort_by_neg_val(frags):
	out.write(item+"\n")


out=open("unique_words.txt","w")
for item in sort_by_neg_val(unique_words):
	out.write(item+"\n")

