#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt, time, importlib, random

def getConfig():
    return getopt.getopt(
        sys.argv[2:], 
        'cehst:', 
        ['lang=', 'linenumber', 'partcn', 'help', 'show-answer', 'answer-time=']
    )[0]

class Dictation:

    def __init__(self, wordList, config):
        self._wordList = wordList
        self.preInit()
        self.setConfig(config)

    def preInit(self):
        self._file = utf8stdout = open(1, 'w', encoding='utf-8')
        # sleep time between 2 words
        self._time = 8
        # sleep time between 2 answers
        self._answerTime = 4;
        # dictate chinese
        self._dictFunc = None
        self.dictateCN()
        # if print line number
        self._linenNumber = False
        # shuffle the list
        self._random = False
        # last word
        self._lastWord = None
        # show answer
        self._showAnswer = False


    def dictateEN(self):
        # lang
        self._lang = 'cn'
        self._dictFunc = self.printEnglish

    def dictateCN(self):
        # lang
        self._lang = 'cn'
        # print chinese by default
        # print all properties and chinese of a word
        if self._dictFunc not in (self.printFullChinese, self.printPartChinese):
            self._dictFunc = self.printFullChinese

    def setConfig(self, config):
        for arg, value in config:
            if arg == '-t':
                self._time = value
            if arg == '--linenumber':
                self._linenNumber = True
            if arg == '-c':
                self.dictateCN()
            if arg == '-e':
                self.dictateEN()
            if arg == '--lang':
                if value.lower() == 'en':
                    self.dictateEN()
                else:
                    self.dictateCN()
            if arg == '-s':
                self._random = True
            if arg == '--partcn':
                self._dictFunc = self.printPartChinese
            if arg == '--help' or arg == '-h':
                self.printHelpInfo()
            if arg == '--show-answer':
                self._showAnswer = True
            if arg == '--answer-time':
                self._answerTime = value

    @staticmethod 
    def printHelpInfo():
        info = '''Usage: toefl ListNum [options]

  -c             Show chinese meanings while having dictation.
  -e             Show english words while having dictation. For each word, Press
                 enter to get the correct answer.
  -h --help      This help.
  -s             Shuffle the word list.
  -t             Sleep time between two words while having the dictation.
  
  --answer-time  Sleep time while showing the english answers after the 
                 dictation. Only useful with the `-c` or `--lang=cn` parameter
                 and `--show-answer` parameter.
  --lang=[cn|en] Which equals to -c and -e.
  --linenumber   Show the line number.
  --partcn       Only show one chinese meaning.Only useful with the `-c` or 
                 `--lang=cn` parameter.
  --show-answer  Show the english answer after the dictation.
'''
        print(info)
        sys.exit()


    def printFullChinese(self, item):
        for form, chinese in self._wordList[item].items():
            print(form, '；'.join(chinese), sep='', end=' ', file=self._file, flush=True)

    def printPartChinese(self, item):
        items = self._wordList[item]
        form = list(items)[random.randrange(0, len(items))]
        index = random.randrange(0, len(items[form]))
        item = items[form][index]
        print(form, item, sep='', end='', file=self._file, flush=True)

    def printEnglish(self, item):
        if self._lastWord:
            self.printFullChinese(self._wordList[self._lastWord])
            print()
            time.sleep(1)
        print(item, end='', flush=True)
        self._lastWord = item

    def printEnglishAnswer(self):
        lineNumber = 1
        for item in self._dictation:
            print(item)
            time.sleep(int(self._answerTime))

    def run(self):
        self._dictation = list(self._wordList)
        if self._random:
            random.shuffle(self._dictation)

        lineNumber = 1
        for items in self._dictation:
            if self._linenNumber:
                print(lineNumber, end='. ', flush=True)
                lineNumber += 1
            self._dictFunc(items)
            time.sleep(int(self._time))
            # a newline between 2 words
            print()
        if self._lang == 'cn' and self._showAnswer == True:
            self.printEnglishAnswer()

if __name__ == '__main__':
    listName = sys.argv[1]
    if listName == '-h' or listName == '--help':
        Dictation.printHelpInfo();

    config = getConfig()
    wordList = importlib.import_module('lists.'+listName).L
    dictation = Dictation(wordList, config)
    print('Word List '+listName[1:])
    dictation.run()
