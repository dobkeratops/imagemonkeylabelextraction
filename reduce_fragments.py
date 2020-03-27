frags={};
with open("label_fragments.txt") as fp:
	while 1 is 1:
		line = fp.readline()[:-1]
		if not line: break
		if line in frags: frags[line]+=1 
		else: frags[line]=1

sorted_frags = {k: v for k, v in sorted(frags.items(), key=lambda item: item[1])}
for k,v in sorted_frags.items():
	print(str(k))

