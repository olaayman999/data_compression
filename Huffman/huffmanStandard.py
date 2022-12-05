# A Huffman Tree Node
class Node:
    def __init__(self, probability, symbol, left=None, right=None):
        # probability of symbol
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


def Probability(text):
    symbolsDictionary = dict()
    for i in text:
        if symbolsDictionary.get(i) == None:
            symbolsDictionary[i] = 1
        else: 
            symbolsDictionary[i] += 1     
    return symbolsDictionary


def sizeData(text, coding):
    sizeBefore = len(text) * 8 
    sizeAfter = 0
    symbolsUnique = coding.keys()
    for i in symbolsUnique:
        counter = text.count(i)
        sizeAfter += counter * len(coding[i]) 
    print("size Before ", sizeBefore)    
    print("size After ",  sizeAfter)  
    
#determine codes of symbols by tree traversal
coding = dict()
def HuffmanCodes(node, current=''):
    # huffman code for current node
    newCode = current + str(node.code)
    if(node.left):
        HuffmanCodes(node.left, newCode)
    if(node.right):
        HuffmanCodes(node.right, newCode)
    if(not node.left and not node.right):
        coding[node.symbol] = newCode
    return coding  

#return bit stream
def BitStream(text, coding):
    result = []
    for i in text:
        result.append(coding[i])
    string = ''.join([str(item) for item in result])    
    return string

def Encoding(data):
    frequencyTable = Probability(data)
    symbolsUnique = frequencyTable.keys()
    probabilities = frequencyTable.values()
    print("symbols: ", symbolsUnique)
    print("probabilities: ", probabilities)
    HuffmanNodes = []
    # converting symbols and probabilities into huffman tree nodes
    for i in symbolsUnique:
        HuffmanNodes.append(Node(frequencyTable.get(i), i))
    
    while len(HuffmanNodes) > 1:
        # sort all the nodes in ascending order based on their probability
        HuffmanNodes = sorted(HuffmanNodes, key=lambda x: x.probability)

        right = HuffmanNodes[0]
        left = HuffmanNodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.probability+right.probability, left.symbol+right.symbol, left, right)
    
        HuffmanNodes.remove(left)
        HuffmanNodes.remove(right)
        HuffmanNodes.append(newNode)
            
    huffmanTable = HuffmanCodes(HuffmanNodes[0])
    print("huffman table ", huffmanTable)
    sizeData(data, huffmanTable)
    Output = BitStream(data,huffmanTable)
    return Output, HuffmanNodes[0]  #for decompression
    

def Decoding(bitStream, tree):
    head = tree
    text = []
    for i in bitStream:
        if i == '1':
            tree = tree.right   
        elif i == '0':
            tree = tree.left
        try:
            if tree.left.symbol == None and tree.right.symbol == None:
                pass
        except AttributeError:
            text.append(tree.symbol)
            tree = head
        
    decoded = ''.join([str(item) for item in text])
    return decoded        



inputFile = open("sample.txt", 'r')
data = inputFile.read()
encoding, tree = Encoding(data)
print("Encoded output", encoding)

print("Decoded output", Decoding(encoding,tree))


