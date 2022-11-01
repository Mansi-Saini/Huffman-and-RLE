class Node:
    def __init__(self, prob, symbol, left = None, right = None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ""

def calculateProb(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1

    return symbols

codes = dict()
def calculateCodes(node, val = ''):
    newVal = val + str(node.code)
    if(node.left):
        calculateCodes(node.left, newVal)
        
    if(node.right):
        calculateCodes(node.right, newVal)
        
    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes

def outputEncoded(data, coding):
    encodingOutput = []
    for c in data:
##        print(coding[c], end = '')
        encodingOutput.append(coding[c])

    string = ''.join([str(item) for item in encodingOutput])
    return string

def totalGain( coding):
    afterCompression = len(coding)
    return afterCompression

def compressionRatio(data, code):
    beforeCompression = len(data) * 8
    afterCompression = len(code)
    ratio = beforeCompression/afterCompression

    return round(ratio, 3)

def huffmanEncoding(data):
    symbolWithProbs = calculateProb(data)
    symbols = symbolWithProbs.keys()
    probabilities = symbolWithProbs.values()
##    print("symbols: ", symbols)
##    print("probabilities: ", probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append(Node(symbolWithProbs.get(symbol), symbol))

##    for i in nodes:
##        print(i.symbol, i.prob)
        
    while len(nodes) > 1:
        nodes = sorted(nodes, key = lambda x : x.prob)

        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffmanEncoding = calculateCodes(nodes[0])
##    print(huffmanEncoding)
####    totalGain(data, huffmanEncoding)
    encodedOutput = outputEncoded(data, huffmanEncoding)
##    totalGain(data, encodedOutput)
##    print("Encoded output:", encodedOutput)
    return encodedOutput

##data = "AAAAAAABBBBCCCDDDEEEEEAAAA"
##t1 = time.time()
##print(huffmanEncoding(data))
##t2 = time.time()
##print(t1, t2)
##print(t2 - t1)
##
##print(totalGain(data, code))
##print(compressionRatio(data, code))
