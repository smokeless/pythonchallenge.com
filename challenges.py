import re
import requests

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

    st = ''.join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", raw))
    print(st)

def challenge4():
    '''
    follow the chain.
    :return:
    '''
    firstHit = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    r = requests.get(firstHit)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    prevNothing = ''
    regex = re.compile('and the next nothing is (\d+)')
    num = ''
    for i in range(400):
        print(r.text)
        match = regex.search(r.text)
        if match == None and 'Divide' in r.text:
            num = str(16044/2) #hardcoded is gross.
            r = requests.get(url+num)
        elif match == None:
            break
        else:
            num = match.group(1)
            r = requests.get(url + num)



challenge4()