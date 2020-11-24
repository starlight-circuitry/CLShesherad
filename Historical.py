import WordGen
import Base
import random

__author__ = 'Aster'

# This is 800 years change, from old common 2 to Sheysht. For the sake of simplicity (and my sanity), let's say, 4-5
# individual changes. Also, these should be sequential, not simultaneous, obviously.

# Also, note that this is a reverse-order list, as they are aged backwards.

# Also, loanwords exist. They can be introduced at any point, remember this. There is a chance for any word that it
# only goes through the last few of these.
# Also, words can be derived from ancient texts and skip a level or two of changes. It could be worth keeping track of
# when words enter the language. See this link:
# https://www.reddit.com/r/conlangs/comments/3gf8mu/a_guide_to_sound_changes/

# List of changes, in chronological order (bpd=before present day):

# 700 bpd: Spirantization of /p/, /b/, /t/, /d/ prevocalically
# 550 bpd: rhotacism of /s/ and /z/
# 400 bpd: monophthongization of several diphthongs
# 300 bpd: deaffricatization
# 150 bpd: delete final vowel following stop


voiced_cons = ['z', 'ʒ', 'v', 'ɣ', 'd', 'b', 'x', 'g']

voiceless_cons = ['s', 'f', 'p', 'ʃ', 'x', 't', 'k']


def historicalWord(word="", gen=""):
    if word == "":
        word = WordGen.words(pos="x")
    change_chance = 0
    change_threshold = 30

    # define new word as a copy of word
    new_word = ""
    for i in range(len(word)):
        new_word = new_word + word[i]

    # loop 1:


    # update word to reflect this change
    word = ""
    for i in range(len(new_word)):
        word = word + new_word[i]

    # loop 2


    # update word to reflect this change
    word = ""
    for i in range(len(new_word)):
        word = word + new_word[i]

    # loop 3


    # update word to reflect this change
    word = ""
    for i in range(len(new_word)):
        word = word + new_word[i]

    # loop 4

    # update word to reflect this change
    word = ""
    for i in range(len(new_word)):
        word = word + new_word[i]

    return word


print(historicalWord())
