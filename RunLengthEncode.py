import time

def runLengthEncode(message):
    result = []
    i = 0
    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while(j < len(message) - 1):
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break

        result.append(count)
        result.append(ch)
        i = j + 1
        
    return result

##t1 = time.time()
##data = "AAAAAAABBBBCCCDDDEEEEEAAAA"
##print("".join(str(e) for e in runLengthEncode(data)))
##t2 = time.time()
##print(t2 - t1)

def totalGain(coding):
    
    afterCompression = 0
    for i in coding:
        if isinstance(i, int):
            if i < 255:
                afterCompression += 1
            else:
                afterCompression += 2
        else:
            afterCompression += 1

    return afterCompression * 8

def compressionRatio(data, code):
    beforeCompression = len(data) * 8
    afterCompression = totalGain(code)
    ratio = beforeCompression/afterCompression

    return round(ratio, 3)
