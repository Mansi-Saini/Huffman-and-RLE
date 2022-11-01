import Huffman
import RunLengthEncode
import pandas as pd

inp = open("input1.txt", "r")
data = inp.readlines()
output = []
Soutput = []
Houtput = []
for d in data:
    ro = RunLengthEncode.runLengthEncode(d)
    rl = RunLengthEncode.totalGain(ro)
    rcr = RunLengthEncode.compressionRatio(d, ro)

    ho = Huffman.huffmanEncoding(d)
    hl = Huffman.totalGain(ho)
    hcr = Huffman.compressionRatio(d, ho)
    output.append([len(d) * 8, rl, rcr, hl, hcr])
    
print(Soutput)
print(Houtput)

df = pd.DataFrame(output, columns = ['input size','RunLengthEncode size', 'RunLengthEncode Compression Ratio', 'Huffman size', 'Huffman Compression Ratio'])
print(df)
df.to_csv('output.csv')
