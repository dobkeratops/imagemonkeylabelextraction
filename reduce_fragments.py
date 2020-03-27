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
		

frags={};
nlines=0;
lfrag=open("label_fragments.txt","r").readlines()
unique_words={};

for line in lfrag:
	line=line[:-1] #strip trailing '\n'
	if line in frags: frags[line]+=1 
	else: frags[line]=1
	line=camelToSnakeCase(line).replace("("," ").replace(")"," ").replace("|"," ").replace("["," ").replace("]"," ").replace("_"," ").replace("."," ").replace("~"," ").replace("-"," ")
	
	for word in line.split(): unique_words[word]=()

sorted_frags = {k: v for k, v in sorted(frags.items(), key=lambda item: -item[1])}
unique_frags=[k for k,v in sorted_frags.items()]

out=open("unique_fragments.txt","w")
for item in unique_frags:
	out.write(item+"\n")


out=open("unique_words.txt","w")
for item in unique_words:
	out.write(item+"\n")

print(camelToSnakeCase("fooBarBaz_theCamel"))
