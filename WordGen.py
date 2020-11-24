import Base
import Clusters
import random
__author__ = 'Aster'


def letterfreqs(lets):
    """
    :param lets: a list of tuples (letter, frequency)
    :return: a list of each letter frequency times
    """
    lfreqs = []
    for (i, j) in lets:
        c = 0
        while c < j:
            lfreqs.append(i)
            c += 1
    return lfreqs


def rep(l, let, rp='.'):
    """
    :param l: a list of one-letter strings
    :param let: a one-letter string
    :param rp: what to replace let with
    :return: first instance of let replaced with rp
    """
    l[l.index(let)] = rp


def allophones(string):
    """
    :param string: a string
    :return: the string calibrated for allophones in the language
    """
    working = list(string)
    while 'ɾ' in working:
        l = 0
        try:
            if working[working.index('ɾ') - 1] in 'ŋkxgɣ':
                rep(working, 'ɾ', 'l')
            else:
                l += 1
        except:
            l += 1
        if l == 1:
            try:
                if working.index('ɾ') == len(working) - 1:
                    rep(working, 'ɾ', 'l')
                else:
                    rep(working, 'ɾ')
            except:
                rep(working, 'ɾ')
        else:
            if 'ɾ' in working:
                rep(working, 'ɾ')
    while '.' in working:
        rep(working, '.', 'ɾ')
    while 'x' in working:
        try:
            if working[working.index('x') - 1] == 'i':
                rep(working, 'x', 'ç')
            else:
                rep(working, 'x')
        except:
            rep(working, 'x')
    while '.' in working:
        rep(working, '.', 'x')
    while 'ɣ' in working:
        try:
            if working[working.index('ɣ') - 1] == 'i':
                rep(working, 'ɣ', 'ʝ')
            else:
                rep(working, 'ɣ')
        except:
            rep(working, 'ɣ')
    while '.' in working:
        rep(working, '.', 'ɣ')
    done = ''
    for j in working:
        done += j
    return done


def clustcheck(string, lnth):
    """
    :param string: a string
    :param lnth: length of final name
    :return: checks for legality of continuing consonant or vowel clusters
    """
    conscount = 0
    vowlcount = 0
    poslets = {}
    if string == "":
        poslets = Base.phons.copy()
        poslets = list(poslets.items())
        return letterfreqs(poslets)
    for i in string:
        if i in Base.cons:
            conscount += 1
            vowlcount = 0
        else:
            conscount = 0
            vowlcount += 1
    if conscount == 0:
        poslets = Base.cons.copy()
        poslets = list(poslets.items())
        vlfreq = Base.vowls.copy()
        vlfreq = list(vlfreq.items())
        if vowlcount == 1:
            for (i, j) in vlfreq:
                vlfreq[vlfreq.index((i, j))] = (i, j/12)
            poslets += vlfreq
    elif vowlcount == 0:
        prvclust = string[len(string)-conscount:]
        if conscount == len(string):
            if conscount == 1:
                for i in Clusters.ini.copy():
                    if len(prvclust) < len(i) and prvclust in i:
                        poslets[i[len(prvclust)]] = Base.phons[i[len(prvclust)]]
            elif conscount == 2:
                for i in Clusters.ini.copy():
                    if len(prvclust) < len(i) and prvclust in i:
                        poslets[i[len(prvclust)]] = Base.phons[i[len(prvclust)]]/4
            else:
                poslets = Base.vowls.copy()
        elif conscount == 1 and lnth - 1 == len(string):
            for i in Clusters.finl.copy():
                if len(prvclust) < len(i) and prvclust in i:
                    poslets[i[len(prvclust)]] = Base.phons[i[len(prvclust)]]
        elif lnth - len(string) >= 2:
            if prvclust[:2] in Clusters.finl:
                for i in Clusters.invo.copy():
                    if prvclust in i[:len(prvclust)]:
                        poslets[i[len(string)]] = Base.phons[i[len(string)]]
        poslets = list(poslets.items())
        vls = Base.vowls.copy()
        vls = list(vls.items())
        poslets += vls
    poslets = dict(poslets)
    poslets = list(poslets.items())
    return letterfreqs(poslets)


def words(lnth=random.randrange(2, 10), pos=""):
    """
    :param lnth: length of word
    :param pos: part of speech
    :return: a word
    """
    n = ""
    if pos == "":
        pos = input('What part of speech? Noun (n), verb (v), adjective or adverb (a), or none of the above (x)?')
    while len(n) < lnth:
        poslets = clustcheck(n, lnth)
        n += poslets[random.randrange(0, len(poslets))][0]
    if pos == 'n':
        declen = int(input('Declension 1, 2, 3, or 4?'))
        n = noun(n, declen)
    elif pos == 'v':
        conj = int(input('Conjugation 1 or 2? Choose 3 for random.'))
        n = verb(n, conj)
    elif pos == 'a':
        n += 'zæ'
    n = allophones(n)
    return n


def verb(root, conj):
    """
    :param root: a verb root
    :param conj: which conjugation
    :return: a verb finished in the infinitive
    """
    if conj == 3:
        conj = random.randrange(1, 3)
    if conj == 1:
        root += 'viç'
    elif conj == 2:
        root += 'soz'
    return root


def noun(root, declen):
    """
    :param root: a noun root
    :param declen: which declension
    :return: noun finished in nominative case
    """
    try:
        if declen == 1:
            root += 'ɪn'
        elif declen == 2:
            nroot = ''
            root = list(root)
            while root[len(root) - 1] in Base.cons:
                root = root[:len(root) - 1]
            for i in root:
                nroot += i
            root = nroot + 't'
        elif declen == 3:
            root += 'ɑd'
        elif declen == 4:
            gen = input('Gender m, f, or n?')
            if gen not in 'mfn' and gen != '':
                gen = 'mfn'[random.randrange(1, 4)]
            if gen == 'm':
                root += 'ɪn, -eb'
            elif gen == 'f':
                nroot = ''
                root = list(root)
                while root[len(root) - 1] in Base.cons:
                    root = root[:len(root) - 1]
                for i in root:
                    nroot += i
                root = nroot + 't, eb'
            elif gen == 'n':
                root += 'ɑd, -eb'
    except:
        root = noun(root, random.randrange(1, 4))
    return root

print(words(random.randrange(3, 8)))

#sheysht