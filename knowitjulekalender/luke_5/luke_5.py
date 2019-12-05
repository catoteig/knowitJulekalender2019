ELFLIST = 'tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol'


def half(text):
    length = len(text)
    cut = int(length/2)
    text = text[cut: length] + text[0: cut]
    return text


def onebyone(text):
    finished = ''
    for i in range(0, len(text), 2):
        finished = finished + text[i+1] + text[i]
    return finished


def threebythree(text):
    left, right = '', ''
    length = len(text)
    cut = int(length/2)
    for i in range(0, cut, 3):
        left = left + text[length-i-3:length-i]
        right = text[i:i+3] + right
    return left + right


result = threebythree(ELFLIST)
result = onebyone(result)
result = half(result)

print(result)