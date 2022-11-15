#!usr/bin/env python

def tobin(dec, maxBit):
    if dec <2 and dec > maxBit:
            maxBit =1
    elif dec <4 and dec > maxBit:
        maxBit =2
    elif dec <8 and dec > maxBit:
        maxBit=3
    elif dec <16 and dec > maxBit:
        maxBit=4
    elif dec <32 and dec > maxBit:
        maxBit=5
    return maxBit
#-------------------------------------------------------------------------

def decompress(tags,x):
    text=[]
    i=0
    while i <len(tags):
        start=-int(tags[i][0])
        end=-int(tags[i][0])+int(tags[i][1])
        if int(tags[i][1]) ==1:
            decom=text[start]
        if end <0 and int(tags[i][1]) !=1:
            decom=text[start:end] 
            if len(decom)< int(tags[i][1]) :
                decom.append(text[end])
        elif end >=0 and int(tags[i][1]) !=1:
            decom=text[start:] 
        decom+=tags[i][2]
        text+=decom
        i+=1
    
    print(f"the decompressed string is: {''.join(text)}")
    print(''.join(text)==x)
#------------------------------------------------------------------------------------

#By default zlib uses a 32K sliding window. The maximum match length is 258.
#aabababbabababaabab
def compress(x):
    i=0
    offset=0
    lookahead=""
    search=""
    lastvalid=0
    maxBit=0
    maxlen=0
    global vec
    vec=[]
    while i<len(x):
        offset=0
        if i==0:
            vec.append([0,0,x[i]])
            i+=1
        else: #aabababbabababaabab
            lookahead=x[i]
            search=x[0:i]
            offset=search.rfind(lookahead) #return index of found substring, if not found deturn -1
            while offset != -1:
                lastvalid=offset
                if i+1<len(x):
                    i+=1
                    lookahead=lookahead+x[i]
                    offset=search.rfind(lookahead) # can be -1
                else:
                    offset=-1
            maxBit=tobin(len(search)-lastvalid,maxBit)
            maxlen=tobin(len(lookahead)-1, maxlen)
            vec.append([len(search)-lastvalid,len(lookahead)-1,x[i]])
            i=i+1    
    print("\033[96m {}\033[00m" .format('─' * 50))
    print(f"tags after text compression without sliding window: {vec}")
    print(f"text size before compression: {len(x)*8}")
    print(f"size after compression: {len(vec)*(maxlen+maxBit+8)}")
    print("\033[96m {}\033[00m" .format('─' * 50)) #ANSI Code
    decompress(vec,x)


#------------------------------------------------------------------------------------
print("Welcome to data compression and decompression with LZ77 Algorithm!")
print("choose 1 if you want no restrictions on search buffer and lookahead buffer size, and 0 otherwise")
choice=input("0/1 ? ")
text=input("enter your string to compress:  ")
if choice:
    compress(text)
else:
    
    searchWindow=input("enter search window size: ")
    lookAhead=input("enter lookahead window size: ")
    compress(text)
# #tag <offset, chnum, next>
# #ABAABACAADCCABBBDCABD

