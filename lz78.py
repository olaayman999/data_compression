def decompress(list, text):
    table=[]
    table.append("")
    decom=[]
    i=0
    while i<len(list):
        index=list[i][0]
        letter=list[i][1]
        if index==0:
            decom.append(letter)
            if letter not in table:
                table.append(letter)
            i+=1
        else:
            new=table[index]+letter
            table.append(new)
            decom.append(new)
            i+=1
    decom=''.join(decom)
    print(decom)
    print(table)
    print(text==decom)
    if text==decom:
        print("yaay it ended successfully ^^")
    
    
def compress(text):
    table=[]
    table.append("")
    lookahead=""
    i=0 
    comp=[]
    maxBit=-1
    while i< len(text):
        lookahead=text[i]
        offset=0
        while(offset!=-1):
            if lookahead in table and i+1<len(text):
                offset=table.index(lookahead)
                if offset> maxBit:
                    maxBit=offset
                lookahead=lookahead+text[i+1]
                i+=1
            else:
                if lookahead not in table:
                    table.append(lookahead)
                comp.append([offset,lookahead[-1]])
                offset=-1
                i+=1
    print(comp)
    print(table)
    print("\033[96m {}\033[00m" .format('─' * 50))
    sizeAfter=len(comp)*((maxBit).bit_length()+8)
    sizeBefore=8*len(text)
    print(f"size before compression: {sizeBefore} for {len(text)} symbols")
    print(f"size after compression: {sizeAfter} for {len(comp)} tags")
    print(f"compression ratio is {sizeAfter}/{sizeBefore}")
    if sizeAfter>sizeBefore:
        print("LZW compression was not the best choice")
    print("\033[96m {}\033[00m" .format('─' * 50))
    choice=int(input("do you want to decompress the tags? type 1 if so: "))
    if choice==1:
        decompress(comp, text)
    

print("welcome to LZW compression and decompression algorithm!")
x=input("enter the text to compress: ")
print("\033[96m {}\033[00m" .format('─' * 50))
compress(x)
