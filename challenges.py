def challenge0():
    print(str(2**38)+'.html')

def challenge1(url:str):
    '''
    This is a string manipulation challenge.
    Once we have the text working, we can do the url.
    I'm sure there is a cleaner way to do this.
    k->m
    o->q
    e->g
    :return:
    '''
    raw = url
    new = ''
    for i in raw:
        if i.isalpha():
            trans = chr(ord(i)+2)
            new += trans
        else:
            new += i
    final = ''
    for i in new:
        if i == '{':
            final += 'a'
        elif i == '|':
            final += 'b'
        else:
            final += i

    print(final)

def challenge2():
    '''
    Find rare chars in mess
    :return:
    '''
    mess = ''
    with open('mess', 'r') as file:
        mess = file.read()
    counts = {}
    for i in mess:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    firstPass = ''
    for i in mess:
        if counts[i] > 6000 or i == '\n':
            pass
        else:
            firstPass += i

    print(firstPass)

def challenge3():
    '''
    One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    :return:
    '''
    raw = ''
    with open('challenge3', 'r') as f:
        raw = f.read()
    print(raw)

challenge3()