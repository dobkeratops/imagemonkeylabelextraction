frags={};
nlines=0;
lfrag=open("label_fragments.txt","r").readlines()

for line in lfrag:
	line=line[:-1] #strip trailing '\n'
	if line in frags: frags[line]+=1 
	else: frags[line]=1

sorted_frags = {k: v for k, v in sorted(frags.items(), key=lambda item: -item[1])}
unique_frags=[k for k,v in sorted_frags.items()]
for item in unique_frags:
	print(item)

