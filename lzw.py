#ABAABABBAABAABAAAABABBBBBBBB
def decompress(list, text):
    table=[None]*128
    for i in range(0,128):
        table[i]=chr(i)
    decom=[]
    listIterator=0
    index=0
    while listIterator<len(list):
        index=list[listIterator]
        if index<len(table):
            decom.append(table[index])
            if listIterator>0:
                if decom[-2]+decom[-1][0] not in table:
                    table.append(decom[-2]+decom[-1][0])
            listIterator+=1
        else:
            last=str(decom[-1])
            new=last+last[0]
            table.append(new)
            decom.append(new)
            listIterator+=1
        
    decom=''.join(decom)
    print(decom)
    print(text==decom)
    if text==decom:
        print("yaay it ended successfully ^^")
    
    
def compress(text):
    table=[None]*128
    for i in range(0,128):
        table[i]=chr(i)
    lookahead=""
    i=0 
    comp=[]
    maxBit=-1
    while i< len(text):
        lookahead=text[i]
        offset=0
        while(offset!=-1 and i<len(text)):
            
                
            if lookahead in table:
                offset=table.index(lookahead)
                if offset> maxBit:
                    maxBit=offset
                if i==len(text)-1:
                    comp.append(offset)
                    offset=-1
                if i+1<len(text):
                    lookahead=lookahead+text[i+1]
                i+=1
            else:
                if lookahead not in table:
                    table.append(lookahead)
                comp.append(offset)
                offset=-1
    print(comp)
    print("\033[96m {}\033[00m" .format('─' * 50))
    sizeAfter=len(comp)*((maxBit).bit_length()+8)
    sizeBefore=8*len(text)
    print(f"size before compression: {sizeBefore} for {len(text)} symbols")
    print(f"size after compression: {sizeAfter} for {len(comp)} tags")
    print(f"compression ratio is {sizeAfter}/{sizeBefore}")
    if sizeAfter>sizeBefore:
        print("LZW compression was not the best choice")
    print("\033[96m {}\033[00m" .format('─' * 50))
    choice=int(input("do you want to show the table? type 1 if so: "))
    if choice==1:
        print(table)
    
    choice=int(input("do you want to decompress the tags? type 1 if so: "))
    if choice==1:
        decompress(comp, text)
    

print("welcome to LZW compression and decompression algorithm!")
x=input("enter the text to compress: ")
print("\033[96m {}\033[00m" .format('─' * 50))
compress(x)
