
import csv

def csv_reader(file_obj):

	reader = csv.reader(file_obj)
	for row in reader:
	    s=" ".join(row)
	    n=0
	    x=0
	    while n!=3:
	    	if s[x]=="	":
	    		n+=1
	    	x+=1
	    derived=""
	    while s[x]!="	":
	    	derived+=s[x]
	    	x+=1
	    x+=1
	    while s[x]!="	":
	    	x+=1
	    derivator=""
	    x+=1
	    while s[x]!="	":
	    	derivator+=s[x]
	    	x+=1
	    result_string=""
	    result_string=result_string+derived+","+derivator+","
	    print(derived+" | "+derivator)

	    if (derived==derivator):
	        print("ROOT WORD")
	        result_string=result_string+"ROOT WORD"+","
	    else:

	        derived+=" "
	        derivator+=" "

	        derived_string=""
	        g=0
	        f=0
	        if derived[f] in "aoiueɨ":
	        	while derived[f]!=" ":
	        		while derived[f] in "aoiueɨ":
	        			derived_string+=derived[f]
	        			f+=1
	        		derived_string+=","
	        		if derived[f]!=" ":
	        			while (derived[f] not in "aoiueɨ "):
	   	    				derived_string+=derived[f]
	        				f+=1
	       				derived_string+=","

	       	elif derived[f]=="j":
	       		derived_string+=derived[f]
	       		f+=1
	        	while derived[f]!=" ":
	        		while derived[f] in "aoiueɨ":
	        			derived_string+=derived[f]
	        			f+=1
	        		derived_string+=","
	        		if derived[f]!=" ":
	        			while (derived[f] not in "aoiueɨ "):
	   	    				derived_string+=derived[f]
	        				f+=1
	       				derived_string+=","

	        else:
	        	while derived[f]!=" ":
	        		while derived[f] not in "aoiueɨ ":
	        			derived_string+=derived[f]
	        			f+=1
	        		derived_string+=","
	        		if derived[f]!=" ":
	        			while (derived[f] in "aoiueɨ"):
	   	    				derived_string+=derived[f]
	        				f+=1
	       				derived_string+=","

	       	derived_string=derived_string[0:len(derived_string)-1]
	       	derived_diss=list(derived_string.split(","))
	       	print(derived_diss)

	        derivator_string=""
	        g=0
	        f=0
	        if derivator[f] in "aoiueɨ":
	        	while derivator[f]!=" ":
	        		while derivator[f] in "aoiueɨ":
	        			derivator_string+=derivator[f]
	        			f+=1
	        		derivator_string+=","
	        		if derivator[f]!=" ":
	        			while (derivator[f] not in "aoiueɨ "):
	   	    				derivator_string+=derivator[f]
	        				f+=1
	       				derivator_string+=","

	       	elif derivator[f]=="j":
	       		derivator_string+=derivator[f]
	       		f+=1
	        	while derivator[f]!=" ":
	        		while derivator[f] in "aoiueɨ":
	        			derivator_string+=derivator[f]
	        			f+=1
	        		derivator_string+=","
	        		if derivator[f]!=" ":
	        			while (derivator[f] not in "aoiueɨ "):
	   	    				derivator_string+=derivator[f]
	        				f+=1
	       				derivator_string+=","

	        else:
	        	while derivator[f]!=" ":
	        		while derivator[f] not in "aoiueɨ ":
	        			derivator_string+=derivator[f]
	        			f+=1
	        		derivator_string+=","
	        		if derivator[f]!=" ":
	        			while (derivator[f] in "aoiueɨ"):
	   	    				derivator_string+=derivator[f]
	        				f+=1
	       				derivator_string+=","

	       	derivator_string=derivator_string[0:len(derivator_string)-1]
	       	derivator_diss=list(derivator_string.split(","))
	       	print(derivator_diss)

	       	#beginning of the analysis module
	       	def compar(a,b):
	       		c=False
	       		for i in range(0,len(a)):
	       			for j in range(0,len(b)):
	       				if ((a[i]==b[j]) or ((a[i]=='d') & (b[j]=='t')) or ((a[i]=='t') & (b[j]=='d')) or ((a[i]=='g') & (b[j]=='k')) or ((a[i]=='k') & (b[j]=='g')) or ((a[i]=='b') & (b[j]=='p')) or ((a[i]=='p') & (b[j]=='b'))) & (a[i]!='\'') & (b[j]!='\''):
	       					c=True

	       		return c

	       	def comparcut(a,b):
	       		c=False
	       		ator=0
	       		ed=0
	       		for i in range(0,len(a)):
	       			for j in range(0,len(b)):
	       				if (a[i]==b[j]) & (a[i]!='\'') & (b[j]!='\''):
	       					c=True
	       					h=0
	       					s=a[i]
	       					#0000

	       					#d=0
	       					#while (i<len(a)) & (j<len(b)) & (d!=1):
	       					#	if (a[i]==b[j]):
	       					#		i+=1
	       					#		j+=1
	       					#	elif (a[i]=='\''):
	       					#		i+=1
	       					#	elif (b[j]=='\''):
	       					#		j+=1
	       					#	else:
	       					#		d=1
	       					i+=1
	       					j+=1
	       					if 1<i<len(a):
	       						if ((a[i-1]=='d') & (a[i]=='t')) or ((a[i-1]=='g') & (a[i]=='k')) or ((a[i-1]=='b') & (a[i]=='p')):
	       							i+=1
	       					if 0<i<len(a):
	       						if (a[i]=='\'') or (a[i]==s):
	       							i+=1
	       							if i<len(a)-1:
	       								if (a[i]=='\'') or (a[i]==s):
	       									i+=1
	       									if i<len(a)-1:
	       										if (a[i]=='\''):
	       											i+=1
	       					if 1<j<len(b):
	       						if ((b[j-1]=='d') & (b[j]=='t')) or ((b[j-1]=='g') & (b[j]=='k')) or ((b[j-1]=='b') & (b[j]=='p')):
	       							j+=1
	       					if 0<j<len(b):
	       						if (b[j]=='\'') or (b[j]==s):
	       							j+=1
	       							if j<len(b)-1:
	       								if (b[j]=='\'') or (b[j]==s):
	       									j+=1
	       									if j<len(b)-1:
	       										if (b[j]=='\''):
	       											j+=1

	       					#++++
	       					#print(i,j)
	       					if (i<len(a)) & (j<len(b)):
	       						for l in range(i+1,len(a)+1):
	       							for m in range(j+1,len(b)+1):
	       								if (a[i:l]==b[j:m]) & (l-i>h):
	       									h=l-i
	       					ator=i+h
	       					ed=j+h
	       					s=a[ator-1]
	       					#print(ator,ed)
	       					if 0<ator<len(a):
	       						if ((a[ator-1]=='d') & (a[ator]=='t')) or ((a[ator-1]=='g') & (a[ator]=='k')) or ((a[ator-1]=='b') & (a[ator]=='p')):
	       							ator+=1
	       					if 0<ator<len(a):
	       						if (a[ator]=='\'') or (a[ator]==s):
	       							ator+=1
	       							if ator<len(a)-1:
	       								if (a[ator]=='\'') or (a[ator]==s):
	       									ator+=1
	       									if ator<len(a)-1:
	       										if (a[ator]=='\''):
	       											ator+=1
	       					if 0<ed<len(b):
	       						if ((b[ed-1]=='d') & (b[ed]=='t')) or ((b[ed-1]=='g') & (b[ed]=='k')) or ((b[ed-1]=='b') & (b[ed]=='p')):
	       							ed+=1
	       					if 0<ed<len(b):
	       						if (b[ed]=='\'') or (b[ed]==s):
	       							ed+=1
	       							if ed<len(b)-1:
	       								if (b[ed]=='\'') or (b[ed]==s):
	       									ed+=1
	       									if ed<len(b)-1:
	       										if (b[ed]=='\''):
	       											ed+=1
	       					#print(ator,ed)
	       					break
	       			if c==True:
	       				break
    	   		return c,ator,ed

	       	if derived==" ":
	       		result_string=result_string+"WARNING! Dictionary error"+","
	       		print("WARNING! Dictionary error")
	       	else:
	       		if len(derivator_diss)>len(derived_diss):
	       			k=len(derived_diss)-1

	       			while (compar(derivator_diss[k],derived_diss[k])==False) or (k==-1):
	       				k-=1
	       				if (k==-1):
	       					break
	       			root_limit=0
	       			extra=0
	       			if (k==-1):
	       				result_string=result_string+"WARNING! Dictionary error"+","
	       				print("WARNING! Dictionary error")
	       			elif(derivator_diss[k][0] in "aoiueɨ") & (k!=len(derived_diss)-1):
	       				root_limit=k+1
	       			elif(derivator_diss[k][0] not in "aoiueɨ"):
	       				root_limit=k
	       				if k<len(derivator_diss)-3:
	       					if derivator_diss[k+2][len(derivator_diss)-1]==derived_diss[k][len(derived_diss)-1]:
	       						extra=2
	       					elif derivator_diss[k+2][len(derivator_diss)-1]=='\'':
	       						if derived_diss[k][len(derived_diss)-1]=='\'':
	       							if derivator_diss[k+2][len(derivator_diss)-2]==derived_diss[k][len(derived_diss)-2]:
	       								extra=2
	       						elif derivator_diss[k+2][len(derivator_diss)-2]==derived_diss[k][len(derived_diss)-1]:
	       							extra=2
	       					elif derived_diss[k][len(derivator_diss)-1]=='\'':
	       						if derivator_diss[k+2][len(derivator_diss)-1]==derived_diss[k][len(derived_diss)-2]:
	       							extra=2
	       				if extra==0:
	       					u,v,w=comparcut(derivator_diss[k],derived_diss[k])
	       					#print(228)
	       					if u==True:
	       						#if 1<v<len(derivator_diss[k]):
	       						#	if (derivator_diss[k][v-1]=='\'') or ((derivator_diss[k][v-2]=='d') & (derivator_diss[k][v-1]=='t')) or ((derivator_diss[k][v-2]=='g') & (derivator_diss[k][v-1]=='k')) or ((derivator_diss[k][v-2]=='b') & (derivator_diss[k][v-1]=='p')):
	       						#		v+=1
	       						derivator_diss[k]=derivator_diss[k][0:v]
	       						#if 1<w<len(derived_diss[k]):
	       						#	if (derived_diss[k][w-1]=='\'') or ((derived_diss[k][w-2]=='d') & (derived_diss[k][w-1]=='t')) or ((derived_diss[k][w-2]=='g') & (derived_diss[k][w-1]=='k')) or ((derived_diss[k][w-2]=='b') & (derived_diss[k][w-1]=='p')):
	       						#		w+=1
	       						derived_diss[k]=derived_diss[k][0:w]
	       			else:
	       				root_limit=k
	       				if k!=0:
	       					if k-1<len(derived_diss)-2:
	       						if derivator_diss[k-1+2][len(derivator_diss)-1]==derived_diss[k-1][len(derived_diss)-1]:
	       							extra=2
	       						elif derivator_diss[k-1+2][len(derivator_diss)-1]=='\'':
	       							if derived_diss[k-1][len(derived_diss)-1]=='\'':
	       								if derivator_diss[k-1+2][len(derivator_diss)-2]==derived_diss[k-1][len(derived_diss)-2]:
	       									extra=2
	       							elif derivator_diss[k-1+2][len(derivator_diss)-2]==derived_diss[k-1][len(derived_diss)-1]:
	       								extra=2
	       						elif derived_diss[k-1][len(derivator_diss)-1]=='\'':
	       							if derivator_diss[k-1+2][len(derivator_diss)-1]==derived_diss[k][len(derived_diss)-2]:
	       								extra=2
	       					if extra==0:
	       						u,v,w=comparcut(derivator_diss[k-1],derived_diss[k-1])
	       						#print(254)
	       						if u==True:
	       							#if 1<v<len(derivator_diss[k-1]):
	       							#	if (derivator_diss[k-1][v-1]=='\'') or ((derivator_diss[k-1][v-2]=='d') & (derivator_diss[k-1][v-1]=='t')) or ((derivator_diss[k-1][v-2]=='g') & (derivator_diss[k-1][v-1]=='k')) or ((derivator_diss[k-1][v-2]=='b') & (derivator_diss[k-1][v-1]=='p')):
	       							#		v+=1
	       							derivator_diss[k-1]=derivator_diss[k-1][0:v]
	       							#if 1<w<len(derived_diss[k-1]):
	       							#	if (derived_diss[k-1][w-1]=='\'') or ((derived_diss[k-1][w-2]=='d') & (derived_diss[k-1][w-1]=='t')) or ((derived_diss[k-1][w-2]=='g') & (derived_diss[k-1][w-1]=='k')) or ((derived_diss[k-1][w-2]=='b') & (derived_diss[k-1][w-1]=='p')):
	       							#		w+=1
	       							derived_diss[k-1]=derived_diss[k-1][0:w]

	       		else:
	       			k=len(derivator_diss)-1

	       			while (compar(derivator_diss[k],derived_diss[k])==False) or (k==-1):
	       				k-=1
	       				if (k==-1):
	       					break
	       			root_limit=0
	       			extra=0
	       			if (k==-1):
	       				result_string=result_string+"WARNING! Dictionary error"+","
	       				print("WARNING! Dictionary error")
	       			elif(derivator_diss[k][0] in "aoiueɨ") & (k!=len(derivator_diss)-1):
	       				root_limit=k+1
	       			elif(derivator_diss[k][0] not in "aoiueɨ"):
	       				root_limit=k
	       				#print(derivator_diss[k],derived_diss[k])
	       				if k<len(derivator_diss)-2:
	       					if (derivator_diss[k+2][len(derivator_diss[k+2])-1]==derived_diss[k][len(derived_diss[k])-1]) & (derived_diss[k][len(derived_diss[k])-1]!='\''):
	       						extra=2
	       					elif derivator_diss[k+2][len(derivator_diss[k+2])-1]=='\'':
	       						if derived_diss[k][len(derived_diss[k])-1]=='\'':
	       							if derivator_diss[k+2][len(derivator_diss[k+2])-2]==derived_diss[k][len(derived_diss[k])-2]:
	       								extra=2
	       						elif derivator_diss[k+2][len(derivator_diss[k+2])-2]==derived_diss[k][len(derived_diss[k])-1]:
	       							extra=2
	       					elif derived_diss[k][len(derived_diss[k])-1]=='\'':
	       						#print("V")
	       						if derivator_diss[k+2][len(derivator_diss[k+2])-1]==derived_diss[k][len(derived_diss[k])-2]:
	       							extra=2
	       							#print("V")
	       				if extra==0:
	       					u,v,w=comparcut(derivator_diss[k],derived_diss[k])
	       					#print(294)
	       					if u==True:
	       						#print(w)
	       						#if 1<v<len(derivator_diss[k]):
	       						#	if (derivator_diss[k][v-1]=='\'') or ((derivator_diss[k][v-2]=='d') & (derivator_diss[k][v-1]=='t')) or ((derivator_diss[k][v-2]=='g') & (derivator_diss[k][v-1]=='k')) or ((derivator_diss[k][v-2]=='b') & (derivator_diss[k][v-1]=='p')):
	       						#		v+=1
	       						derivator_diss[k]=derivator_diss[k][0:v]
	       						#print(derivator_diss[k])
	       						#if 1<w<len(derived_diss[k]):
	       						#	if (derived_diss[k][w-1]=='\'') or ((derived_diss[k][w-2]=='d') & (derived_diss[k][w-1]=='t')) or ((derived_diss[k][w-2]=='g') & (derived_diss[k][w-1]=='k')) or ((derived_diss[k][w-2]=='b') & (derived_diss[k][w-1]=='p')):
	       						#		w+=1
	       						derived_diss[k]=derived_diss[k][0:w]
	       						#print(derived_diss[k])
	       			else:
	       				root_limit=k
	       				if k!=0:
	       					if k-1<len(derivator_diss)-2:
	       						if (derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k-1][len(derived_diss[k-1])-1]) & (derived_diss[k][len(derived_diss[k])-1]!='\''):
	       							extra=2
	       						elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]=='\'':
	       							if derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
	       								if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-2]:
	       									extra=2
	       							elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-1]:
	       								extra=2
	       						elif derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
	       							if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k][len(derived_diss[k])-2]:
	       								extra=2
	       					if extra==0:
	       						u,v,w=comparcut(derivator_diss[k-1],derived_diss[k-1])
	       						#print(324)
	       						if u==True:
	       							if (derivator_diss[k-1]!=derivator_diss[k-1][0:v]) or (derived_diss[k-1]!=derived_diss[k-1][0:w]):
	       								root_limit-=1
	       							#if 1<v<len(derivator_diss[k-1]):
	       							#	if (derivator_diss[k-1][v-1]=='\'') or ((derivator_diss[k-1][v-2]=='d') & (derivator_diss[k-1][v-1]=='t')) or ((derivator_diss[k-1][v-2]=='g') & (derivator_diss[k-1][v-1]=='k')) or ((derivator_diss[k-1][v-2]=='b') & (derivator_diss[k-1][v-1]=='p')):
	       							#		v+=1
	       							derivator_diss[k-1]=derivator_diss[k-1][0:v]
	       							#if 1<w<len(derived_diss[k-1]):
	       							#	if (derived_diss[k-1][w-1]=='\'') or ((derived_diss[k-1][w-2]=='d') & (derived_diss[k-1][w-1]=='t')) or ((derived_diss[k-1][w-2]=='g') & (derived_diss[k-1][w-1]=='k')) or ((derived_diss[k-1][w-2]=='b') & (derived_diss[k-1][w-1]=='p')):
	       							#		w+=1
	       							derived_diss[k-1]=derived_diss[k-1][0:w]

	       				#u,v,w=comparcut(derivator_diss[k-1],derived_diss[k-1])
	       				#if (u==True) & (derived_diss[k-1]!=derived_diss[k-1][0:w]):
	       				#	if v<len(derivator_diss[k]):
	       				#		if (derivator_diss[k][v]=='\'') or ((derivator_diss[k][v-1]=='d') & (derivator_diss[k][v]=='t')) or ((derivator_diss[k][v-1]=='g') & (derivator_diss[k][v]=='k')) or ((derivator_diss[k][v-1]=='b') & (derivator_diss[k][v]=='p')):
	       				#			v+=1
	       				#	derivator_diss[k]=derivator_diss[k][0:v]
	       				#	if w<len(derivator_diss[k]):
	       				#		if (derivator_diss[k][w]=='\'') or ((derivator_diss[k][w-1]=='d') & (derivator_diss[k][w]=='t')) or ((derivator_diss[k][w-1]=='g') & (derivator_diss[k][w]=='k')) or ((derivator_diss[k][w-1]=='b') & (derivator_diss[k][w]=='p')):
	       				#			w+=1
	       				#	derived_diss[k]=derived_diss[k][0:w]
	       				
	       		root_ator=""
	       		p=0
	       		while p<=root_limit+extra:
	       			root_ator+=derivator_diss[p]
	       			p+=1
	       		result_string=result_string+root_ator+","
	       		print("Original root: {0}".format(root_ator))
	       		root_ed=""
	       		r=0
	       		while r<=root_limit:
	       			root_ed+=derived_diss[r]
	       			r+=1
	       		result_string=result_string+root_ed+","
	       		print("Word root: {0}".format(root_ed))
	       		loa=""
	       		if extra==0:
	       			for o in range(0,root_limit+1):
	       				if(derivator_diss[o]!=derived_diss[o]):
	       					#comparcut()
	       					loa+="{0} // {1}; ".format(derivator_diss[o], derived_diss[o])
	       		else:
	       			for o in range(0,root_limit):
	       				if(derivator_diss[o]!=derived_diss[o]):
	       					#comparcut()
	       					loa+="{0} // {1}; ".format(derivator_diss[o], derived_diss[o])
	       			compound=derivator_diss[root_limit]+derivator_diss[root_limit+1]+derivator_diss[root_limit+2]
	       			loa+="{0} // {1}; ".format(compound, derived_diss[root_limit])
	       		if loa=="":
	       			result_string=result_string+"No alternations"+","
	       			print("No alternations")
	       		else:
	       			result_string=result_string+loa[0:len(loa)-2]+","
	       			print(loa[0:len(loa)-2])
	    path = "E:/My_documents/result.csv"
	    result_string=result_string[0:len(result_string)-1]
	    result_massive=list(result_string.split(","))

	    with open(path, "a", encoding='utf-16') as file:
	    	writer=csv.writer(file)
	    	writer.writerow(result_massive)

csv_path = "E:/My_documents/kuruch_1.csv"
result_path = "E:/My_documents/result.csv"
heading=["Derived","Derivator","Original root","Word root","Alternations"]
with open(result_path, "a", encoding='utf-16') as file:
	writer=csv.writer(file)
	writer.writerow(heading)
with open(csv_path, "r", encoding='utf-8') as f_obj:
    csv_reader(f_obj)