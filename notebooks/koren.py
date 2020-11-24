import csv

def read_csv(file_obj):
    reader = csv.reader(file_obj)
    return reader

def find_root(row):
    s=" ".join(row)
    n=0
    x=0
    result_string=""
    while n!=3:
        if s[x]=="	":
            n+=1
        x+=1
    derived=""
    while s[x]!="	":
        if ord(s[x+1])==805:
            if s[x]=="l":
                derived+="L"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="r":
                derived+="R"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="n":
                derived+="N"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="m":
                derived+="M"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="j":
                derived+="J"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
        else:
            derived+=s[x]
            result_string+=s[x]
            x+=1
    x+=1
    result_string+=","
    ex=0 #TEMP

    while s[x]!="	":
        x+=1
    derivator=""
    x+=1
    while s[x]!="	":
        if ord(s[x+1])==805:
            if s[x]=="l":
                derivator+="L"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="r":
                derivator+="R"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="n":
                derivator+="N"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="m":
                derivator+="M"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
            elif s[x]=="j":
                derivator+="J"
                result_string+=s[x]
                result_string+=s[x+1]
                x+=2
        else:
            derivator+=s[x]
            result_string+=s[x]
            x+=1

    result_string+=","
    x+=1
    n=0
    while n!=2:
        if s[x]=="	":
            n+=1
        x+=1
    print(derived+" | "+derivator)
    meaning=""

    if (derived==derivator):

        n=0
        while n!=4:
            if s[x]=="	":
                n+=1
            x+=1
        while s[x]!="	":
            meaning+=s[x]
            x+=1
        result_string=result_string+meaning+","

        print("ROOT WORD")
        result_string=result_string+"ROOT WORD"+","

    else:
        if (derivator!="k'ee") and (derivator[len(derivator)-1]=="e"):
            derivator=derivator[0:len(derivator)-1]
            if (s[x:x+4]=="Verb") and (derived[len(derived)-1]=="e"):
                derived=derived[0:len(derived)-1]
        elif (s[x:x+4]=="Verb") and (derived[len(derived)-1]=="e"):
            derived=derived[0:len(derived)-1]
            x+=4

        n=0
        while n!=4:
            if s[x]=="	":
                n+=1
            x+=1
        while s[x]!="	":
            meaning+=s[x]
            x+=1
        result_string=result_string+meaning+","

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

        def compar(a,b):
            c=False
            for i in range(0,len(a)):
                for j in range(0,len(b)):
                    if ((a[i]==b[j]) or ((a[i]=='š') & (b[j]=='ž')) or ((a[i]=='ž') & (b[j]=='š')) or ((a[i]=='c') & (b[j]=='ʒ')) or ((a[i]=='ʒ') & (b[j]=='c')) or ((a[i]=='m') & (b[j]=='M')) or ((a[i]=='M') & (b[j]=='m')) or ((a[i]=='n') & (b[j]=='N')) or ((a[i]=='N') & (b[j]=='n')) or ((a[i]=='r') & (b[j]=='R')) or ((a[i]=='R') & (b[j]=='r')) or ((a[i]=='j') & (b[j]=='J')) or ((a[i]=='J') & (b[j]=='j')) or ((a[i]=='l') & (b[j]=='L')) or ((a[i]=='L') & (b[j]=='l')) or ((a[i]=='č') & (b[j]=='ǯ')) or ((a[i]=='ǯ') & (b[j]=='č')) or ((a[i]=='s') & (b[j]=='z')) or ((a[i]=='z') & (b[j]=='s')) or ((a[i]=='f') & (b[j]=='v')) or ((a[i]=='v') & (b[j]=='f')) or ((a[i]=='d') & (b[j]=='t')) or ((a[i]=='t') & (b[j]=='d')) or ((a[i]=='g') & (b[j]=='k')) or ((a[i]=='k') & (b[j]=='g')) or ((a[i]=='b') & (b[j]=='p')) or ((a[i]=='p') & (b[j]=='b'))) & (a[i]!='\'') & (b[j]!='\''):
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
                        if (i<len(a)) & (j<len(b)):
                            for l in range(i+1,len(a)+1):
                                for m in range(j+1,len(b)+1):
                                    if (a[i:l]==b[j:m]) & (l-i>h):
                                        h=l-i
                        ator=i+h
                        ed=j+h
                        s=a[ator-1]
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
                        break
                if c==True:
                    break
            return c,ator,ed

        if derived==" ":
            result_string=result_string+"WARNING! Dictionary error"+","
            print("WARNING! Dictionary error")
        else:
            leftover=""
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

                    if k+1<len(derivator_diss):
                        if (derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k-1][len(derived_diss[k-1])-1]) & (derived_diss[k-1][len(derived_diss[k-1])-1]!='\''):
                            ex=2
                        elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]=='\'':
                            if derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
                                if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-2]:
                                    ex=2
                            elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-1]:
                                ex=2
                        elif derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
                            if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k-1][len(derived_diss[k-1])-2]:
                                ex=2

                elif(derivator_diss[k][0] not in "aoiueɨ"):
                    root_limit=k
                    if k<len(derivator_diss)-2:
                        if derivator_diss[k+2][len(derivator_diss[k+2])-1]==derived_diss[k][len(derived_diss[k])-1]:
                            extra=2
                        elif derivator_diss[k+2][len(derivator_diss[k+2])-1]=='\'':
                            if derived_diss[k][len(derived_diss[k])-1]=='\'':
                                if derivator_diss[k+2][len(derivator_diss[k+2])-2]==derived_diss[k][len(derived_diss[k])-2]:
                                    extra=2
                            elif derivator_diss[k+2][len(derivator_diss[k+2])-2]==derived_diss[k][len(derived_diss[k])-1]:
                                extra=2
                        elif derivator_diss[k][len(derivator_diss[k])-1]=='\'':
                            if derivator_diss[k+2][len(derivator_diss[k+2])-1]==derived_diss[k][len(derived_diss[k])-2]:
                                extra=2
                    if extra==0:
                        u,v,w=comparcut(derivator_diss[k],derived_diss[k])
                        if u==True:
                            derivator_diss[k]=derivator_diss[k][0:v]
                            leftover+=derived_diss[k][w:len(derived_diss[k])]
                            derived_diss[k]=derived_diss[k][0:w]
                else:
                    root_limit=k
                    if k!=0:
                        if k-1<len(derived_diss)-2:
                            if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k-1][len(derived_diss[k-1])-1]:
                                extra=2
                            elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]=='\'':
                                if derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
                                    if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-2]:
                                        extra=2
                                elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-1]:
                                    extra=2
                            elif derivator_diss[k-1][len(derivator_diss[k-1])-1]=='\'':
                                if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k][len(derived_diss[k])-2]:
                                    extra=2
                        if extra==0:
                            u,v,w=comparcut(derivator_diss[k-1],derived_diss[k-1])
                            if u==True:
                                derivator_diss[k-1]=derivator_diss[k-1][0:v]
                                leftover+=derived_diss[k-1][w:len(derived_diss[k-1])]
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

                    if k+1<len(derivator_diss):
                        if (derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k-1][len(derived_diss[k-1])-1]) & (derived_diss[k-1][len(derived_diss[k-1])-1]!='\''):
                            ex=2
                        elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]=='\'':
                            if derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
                                if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-2]:
                                    ex=2
                            elif derivator_diss[k-1+2][len(derivator_diss[k-1+2])-2]==derived_diss[k-1][len(derived_diss[k-1])-1]:
                                ex=2
                        elif derived_diss[k-1][len(derived_diss[k-1])-1]=='\'':
                            if derivator_diss[k-1+2][len(derivator_diss[k-1+2])-1]==derived_diss[k-1][len(derived_diss[k-1])-2]:
                                ex=2

                elif(derivator_diss[k][0] not in "aoiueɨ"):
                    root_limit=k
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
                            if derivator_diss[k+2][len(derivator_diss[k+2])-1]==derived_diss[k][len(derived_diss[k])-2]:
                                extra=2
                    if extra==0:
                        u,v,w=comparcut(derivator_diss[k],derived_diss[k])
                        if u==True:
                            derivator_diss[k]=derivator_diss[k][0:v]
                            leftover+=derived_diss[k][w:len(derived_diss[k])]
                            derived_diss[k]=derived_diss[k][0:w]

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
                            if u==True:
                                if (derivator_diss[k-1]!=derivator_diss[k-1][0:v]) or (derived_diss[k-1]!=derived_diss[k-1][0:w]):
                                    root_limit-=1
                                derivator_diss[k-1]=derivator_diss[k-1][0:v]
                                leftover+=derived_diss[k-1][w:len(derived_diss[k-1])]
                                derived_diss[k-1]=derived_diss[k-1][0:w]

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
            while r<len(derived_diss):
                leftover+=derived_diss[r]
                r+=1
            result_string=result_string+root_ed+","
            result_string=result_string+leftover+","
            print("Word root: {0}".format(root_ed))

            loa=""
            dlina=""
            soft=""
            voice=""
            feature=""
            if extra==0:
                for o in range(0,root_limit+1):

                    if(derivator_diss[o]!=derived_diss[o]):

                        loa+="{0} // {1}; ".format(derivator_diss[o], derived_diss[o])

                        if derivator_diss[o][0] not in "aoiueɨ":

                            if ((derivator_diss[o][0]=='v') & (derived_diss[o][0]=='f')) or ((derivator_diss[o][0]=='ʒ') & (derived_diss[o][0]=='c')) or ((derivator_diss[o][0]=='l') & (derived_diss[o][0]=='L')) or ((derivator_diss[o][0]=='r') & (derived_diss[o][0]=='R')) or ((derivator_diss[o][0]=='j') & (derived_diss[o][0]=='J')) or ((derivator_diss[o][0]=='n') & (derived_diss[o][0]=='N')) or ((derivator_diss[o][0]=='m') & (derived_diss[o][0]=='M')) or ((derivator_diss[o][0]=='ǯ') & (derived_diss[o][0]=='č')) or ((derivator_diss[o][0]=='z') & (derived_diss[o][0]=='s')) or ((derivator_diss[o][0]=='ž') & (derived_diss[o][0]=='š')) or ((derivator_diss[o][0]=='d') & (derived_diss[o][0]=='t')) or ((derivator_diss[o][0]=='g') & (derived_diss[o][0]=='k')) or ((derivator_diss[o][0]=='b') & (derived_diss[o][0]=='p')):
                                voice="+ // -"
                            elif ((derivator_diss[o][0]=='f') & (derived_diss[o][0]=='v')) or ((derivator_diss[o][0]=='c') & (derived_diss[o][0]=='ʒ')) or ((derivator_diss[o][0]=='L') & (derived_diss[o][0]=='l')) or ((derivator_diss[o][0]=='R') & (derived_diss[o][0]=='r')) or ((derivator_diss[o][0]=='J') & (derived_diss[o][0]=='j')) or ((derivator_diss[o][0]=='N') & (derived_diss[o][0]=='n')) or ((derivator_diss[o][0]=='M') & (derived_diss[o][0]=='m')) or ((derivator_diss[o][0]=='č') & (derived_diss[o][0]=='ǯ')) or ((derivator_diss[o][0]=='s') & (derived_diss[o][0]=='z')) or ((derivator_diss[o][0]=='š') & (derived_diss[o][0]=='ž')) or ((derivator_diss[o][0]=='t') & (derived_diss[o][0]=='d')) or ((derivator_diss[o][0]=='k') & (derived_diss[o][0]=='g')) or ((derivator_diss[o][0]=='p') & (derived_diss[o][0]=='b')):
                                voice="- // +"
                            elif derivator_diss[o][0]!=derived_diss[o][0]:
                                feature="Different consonants"
                            else:
                                voice="Same"

                            if feature=="":
                                if len(derivator_diss[o])>1:
                                    if derivator_diss[o][1]=='\'':
                                        if len(derived_diss[o])>1:
                                            if derived_diss[o][1]=='\'':
                                                soft="+ // +"
                                            else:
                                                soft="+ // -"
                                        else:
                                            soft="+ // -"
                                    elif len(derived_diss[o])>1:
                                        if derived_diss[o][1]=='\'':
                                            soft="- // +"
                                        else:
                                            soft="- // -"
                                    else:
                                        soft="- // -"
                                elif len(derived_diss[o])>1:
                                    if derived_diss[o][1]=='\'':
                                        soft="- // +"
                                    else:
                                        soft="- // -"
                                else:
                                    soft="- // -"

                                if len(derivator_diss[o])>1:
                                    h=1
                                    j=0
                                    while h<len(derivator_diss[o]):
                                        if ((derivator_diss[o][0]==derivator_diss[o][h]) or ((derivator_diss[o][0]=='š') & (derivator_diss[o][h]=='ž')) or ((derivator_diss[o][0]=='ž') & (derivator_diss[o][h]=='š')) or ((derivator_diss[o][0]=='c') & (derivator_diss[o][h]=='ʒ')) or ((derivator_diss[o][0]=='ʒ') & (derivator_diss[o][h]=='c')) or ((derivator_diss[o][0]=='m') & (derivator_diss[o][h]=='M')) or ((derivator_diss[o][0]=='M') & (derivator_diss[o][h]=='m')) or ((derivator_diss[o][0]=='n') & (derivator_diss[o][h]=='N')) or ((derivator_diss[o][0]=='N') & (derivator_diss[o][h]=='n')) or ((derivator_diss[o][0]=='r') & (derivator_diss[o][h]=='R')) or ((derivator_diss[o][0]=='R') & (derivator_diss[o][h]=='r')) or ((derivator_diss[o][0]=='j') & (derivator_diss[o][h]=='J')) or ((derivator_diss[o][0]=='J') & (derivator_diss[o][h]=='j')) or ((derivator_diss[o][0]=='l') & (derivator_diss[o][h]=='L')) or ((derivator_diss[o][0]=='L') & (derivator_diss[o][h]=='l')) or ((derivator_diss[o][0]=='č') & (derivator_diss[o][h]=='ǯ')) or ((derivator_diss[o][0]=='ǯ') & (derivator_diss[o][h]=='č')) or ((derivator_diss[o][0]=='s') & (derivator_diss[o][h]=='z')) or ((derivator_diss[o][0]=='z') & (derivator_diss[o][h]=='s')) or ((derivator_diss[o][0]=='f') & (derivator_diss[o][h]=='v')) or ((derivator_diss[o][0]=='v') & (derivator_diss[o][h]=='f')) or ((derivator_diss[o][0]=='d') & (derivator_diss[o][h]=='t')) or ((derivator_diss[o][0]=='t') & (derivator_diss[o][h]=='d')) or ((derivator_diss[o][0]=='g') & (derivator_diss[o][h]=='k')) or ((derivator_diss[o][0]=='k') & (derivator_diss[o][h]=='g')) or ((derivator_diss[o][0]=='b') & (derivator_diss[o][h]=='p')) or ((derivator_diss[o][0]=='p') & (derivator_diss[o][h]=='b'))):
                                            j=1
                                        h+=1
                                    if j==1:
                                        if len(derived_diss[o])>1:
                                            h=1
                                            j=0
                                            while h<len(derived_diss[o]):
                                                if ((derived_diss[o][0]==derived_diss[o][h]) or ((derived_diss[o][0]=='š') & (derived_diss[o][h]=='ž')) or ((derived_diss[o][0]=='ž') & (derived_diss[o][h]=='š')) or ((derived_diss[o][0]=='c') & (derived_diss[o][h]=='ʒ')) or ((derived_diss[o][0]=='ʒ') & (derived_diss[o][h]=='c')) or ((derived_diss[o][0]=='m') & (derived_diss[o][h]=='M')) or ((derived_diss[o][0]=='M') & (derived_diss[o][h]=='m')) or ((derived_diss[o][0]=='n') & (derived_diss[o][h]=='N')) or ((derived_diss[o][0]=='N') & (derived_diss[o][h]=='n')) or ((derived_diss[o][0]=='r') & (derived_diss[o][h]=='R')) or ((derived_diss[o][0]=='R') & (derived_diss[o][h]=='r')) or ((derived_diss[o][0]=='j') & (derived_diss[o][h]=='J')) or ((derived_diss[o][0]=='J') & (derived_diss[o][h]=='j')) or ((derived_diss[o][0]=='l') & (derived_diss[o][h]=='L')) or ((derived_diss[o][0]=='L') & (derived_diss[o][h]=='l')) or ((derived_diss[o][0]=='č') & (derived_diss[o][h]=='ǯ')) or ((derived_diss[o][0]=='ǯ') & (derived_diss[o][h]=='č')) or ((derived_diss[o][0]=='s') & (derived_diss[o][h]=='z')) or ((derived_diss[o][0]=='z') & (derived_diss[o][h]=='s')) or ((derived_diss[o][0]=='f') & (derived_diss[o][h]=='v')) or ((derived_diss[o][0]=='v') & (derived_diss[o][h]=='f')) or ((derived_diss[o][0]=='d') & (derived_diss[o][h]=='t')) or ((derived_diss[o][0]=='t') & (derived_diss[o][h]=='d')) or ((derived_diss[o][0]=='g') & (derived_diss[o][h]=='k')) or ((derived_diss[o][0]=='k') & (derived_diss[o][h]=='g')) or ((derived_diss[o][0]=='b') & (derived_diss[o][h]=='p')) or ((derived_diss[o][0]=='p') & (derived_diss[o][h]=='b'))):
                                                    j=1
                                                h+=1
                                            if j==1:
                                                dlina="+ // +"
                                            else:
                                                dlina="+ // -"
                                        else:
                                            dlina="+ // -"
                                    elif len(derived_diss[o])>1:
                                        h=1
                                        j=0
                                        while h<len(derived_diss[o]):
                                            if ((derived_diss[o][0]==derived_diss[o][h]) or ((derived_diss[o][0]=='š') & (derived_diss[o][h]=='ž')) or ((derived_diss[o][0]=='ž') & (derived_diss[o][h]=='š')) or ((derived_diss[o][0]=='c') & (derived_diss[o][h]=='ʒ')) or ((derived_diss[o][0]=='ʒ') & (derived_diss[o][h]=='c')) or ((derived_diss[o][0]=='m') & (derived_diss[o][h]=='M')) or ((derived_diss[o][0]=='M') & (derived_diss[o][h]=='m')) or ((derived_diss[o][0]=='n') & (derived_diss[o][h]=='N')) or ((derived_diss[o][0]=='N') & (derived_diss[o][h]=='n')) or ((derived_diss[o][0]=='r') & (derived_diss[o][h]=='R')) or ((derived_diss[o][0]=='R') & (derived_diss[o][h]=='r')) or ((derived_diss[o][0]=='j') & (derived_diss[o][h]=='J')) or ((derived_diss[o][0]=='J') & (derived_diss[o][h]=='j')) or ((derived_diss[o][0]=='l') & (derived_diss[o][h]=='L')) or ((derived_diss[o][0]=='L') & (derived_diss[o][h]=='l')) or ((derived_diss[o][0]=='č') & (derived_diss[o][h]=='ǯ')) or ((derived_diss[o][0]=='ǯ') & (derived_diss[o][h]=='č')) or ((derived_diss[o][0]=='s') & (derived_diss[o][h]=='z')) or ((derived_diss[o][0]=='z') & (derived_diss[o][h]=='s')) or ((derived_diss[o][0]=='f') & (derived_diss[o][h]=='v')) or ((derived_diss[o][0]=='v') & (derived_diss[o][h]=='f')) or ((derived_diss[o][0]=='d') & (derived_diss[o][h]=='t')) or ((derived_diss[o][0]=='t') & (derived_diss[o][h]=='d')) or ((derived_diss[o][0]=='g') & (derived_diss[o][h]=='k')) or ((derived_diss[o][0]=='k') & (derived_diss[o][h]=='g')) or ((derived_diss[o][0]=='b') & (derived_diss[o][h]=='p')) or ((derived_diss[o][0]=='p') & (derived_diss[o][h]=='b'))):
                                                j=1
                                            h+=1
                                        if j==1:
                                            dlina="- // +"
                                        else:
                                            dlina="- // -"
                                    else:
                                        dlina="- // -"
                                elif len(derived_diss[o])>1:
                                    h=1
                                    j=0
                                    while h<len(derived_diss[o]):
                                        if ((derived_diss[o][0]==derived_diss[o][h]) or ((derived_diss[o][0]=='š') & (derived_diss[o][h]=='ž')) or ((derived_diss[o][0]=='ž') & (derived_diss[o][h]=='š')) or ((derived_diss[o][0]=='c') & (derived_diss[o][h]=='ʒ')) or ((derived_diss[o][0]=='ʒ') & (derived_diss[o][h]=='c')) or ((derived_diss[o][0]=='m') & (derived_diss[o][h]=='M')) or ((derived_diss[o][0]=='M') & (derived_diss[o][h]=='m')) or ((derived_diss[o][0]=='n') & (derived_diss[o][h]=='N')) or ((derived_diss[o][0]=='N') & (derived_diss[o][h]=='n')) or ((derived_diss[o][0]=='r') & (derived_diss[o][h]=='R')) or ((derived_diss[o][0]=='R') & (derived_diss[o][h]=='r')) or ((derived_diss[o][0]=='j') & (derived_diss[o][h]=='J')) or ((derived_diss[o][0]=='J') & (derived_diss[o][h]=='j')) or ((derived_diss[o][0]=='l') & (derived_diss[o][h]=='L')) or ((derived_diss[o][0]=='L') & (derived_diss[o][h]=='l')) or ((derived_diss[o][0]=='č') & (derived_diss[o][h]=='ǯ')) or ((derived_diss[o][0]=='ǯ') & (derived_diss[o][h]=='č')) or ((derived_diss[o][0]=='s') & (derived_diss[o][h]=='z')) or ((derived_diss[o][0]=='z') & (derived_diss[o][h]=='s')) or ((derived_diss[o][0]=='f') & (derived_diss[o][h]=='v')) or ((derived_diss[o][0]=='v') & (derived_diss[o][h]=='f')) or ((derived_diss[o][0]=='d') & (derived_diss[o][h]=='t')) or ((derived_diss[o][0]=='t') & (derived_diss[o][h]=='d')) or ((derived_diss[o][0]=='g') & (derived_diss[o][h]=='k')) or ((derived_diss[o][0]=='k') & (derived_diss[o][h]=='g')) or ((derived_diss[o][0]=='b') & (derived_diss[o][h]=='p')) or ((derived_diss[o][0]=='p') & (derived_diss[o][h]=='b'))):
                                            j=1
                                        h+=1
                                    if j==1:
                                        dlina="- // +"
                                    else:
                                        dlina="- // -"
                                else:
                                    dlina="- // -"

            else:
                for o in range(0,root_limit):
                    if(derivator_diss[o]!=derived_diss[o]):
                        loa+="{0} // {1}; ".format(derivator_diss[o], derived_diss[o])
                compound=derivator_diss[root_limit]+derivator_diss[root_limit+1]+derivator_diss[root_limit+2]
                loa+="{0} // {1}; ".format(compound, derived_diss[root_limit])
            if loa=="":
                result_string=result_string+"No alternations"+","
                print("No alternations")
            elif extra==0:
                result_string=result_string+loa[0:len(loa)-2]+","+dlina+","+soft+","+voice+","+feature
                print(loa[0:len(loa)-2])
            elif extra!=0:
                result_string=result_string+loa[0:len(loa)-2]+","+","+","+","+"Runaway vowel"
                print(loa[0:len(loa)-2])
    result_string=result_string[0:len(result_string)]
    result_massive=list(result_string.split(","))
    return result_massive


def save_results(path, result_massive):
    with open(path, "a", encoding='utf-16') as file:
        writer=csv.writer(file)
        writer.writerow(result_massive)



csv_path = "../done/kuruch_revised_november_fixed.tsv"
result_path = "../done/roots.csv"
heading=["Derived","Derivator","Meaning","Original root","Word root","Remainder","Alternations","Length","Palatalization","Voicing","Smth strange"]
with open(result_path, "w", encoding='utf-16') as file:
    writer=csv.writer(file)
    writer.writerow(heading)


with open(csv_path, "r", encoding='utf-8') as f_obj:
    reader = read_csv(f_obj)
    for row in reader:
        result = find_root(row)
        save_results(result_path, result)