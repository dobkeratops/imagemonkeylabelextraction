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

def stripPrecedingTrailingWhitespace(s):
	istart=0
	for i in range(0,len(s)):
		istart=i
		if not (s[i] in " \t\n"):
			break

	iend=istart
	for i in range(istart,len(s)):
		if not (s[i] in " \t\n"):
			iend=i+1
	return s[istart:iend]

frags={};
nlines=0;
lfrag=open("label_fragments.txt","r").readlines()
unique_words={};

for line in lfrag:
	line=line[:-1] #strip trailing '\n'
	line=stripPrecedingTrailingWhitespace(line)
	add_use(frags,line)
	#split all the words (even grouped) to accumulate the individual phrases
	line=camelToSnakeCase(line).replace("("," ").replace(")"," ").replace("|"," ").replace("["," ").replace("]"," ").replace("_"," ").replace("."," ").replace("~"," ").replace("-"," ")
	
	for word in line.split(): add_use(unique_words,word)

out=open("unique_fragments.txt","w")
for item in sort_by_neg_val(frags):
	out.write(item+"\n")


out=open("unique_words.txt","w")
for item in sort_by_neg_val(unique_words):
	out.write(item+"\n")

print(stripPrecedingTrailingWhitespace("foo bar\tbaz"))

print(stripPrecedingTrailingWhitespace(" \tfoo bar\tbaz"))

print(stripPrecedingTrailingWhitespace(" \tfoo bar\tbaz\t "))
