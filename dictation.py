#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt, importlib, random
from colorprint import ColorPrint

def getConfig():
    return getopt.getopt(
        sys.argv[2:], 
        'cehs', 
        ['lang=', 'partcn', 'help', 'range=']
    )[0]

class Dictation:

    def __init__(self, wordList, config):
        self._wordList = wordList
        self.preInit()
        self.setConfig(config)

    def preInit(self):
        self._file = open(1, 'w', encoding='utf-8')
        # dictate chinese
        self._dictFunc = None
        self.dictateCN()
        # shuffle the list
        self._random = False
        # statistics
        self._rightCnt = 0
        self._wrongCnt = 0
        # range
        self._start  = None
        self._end    = None

    def dictateEN(self):
        # lang
        self._lang = 'en'
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
            if arg == '-c':
                self.dictateCN()
            if arg == '-e':
                self.dictateEN()
            if arg == '--lang':
                if value.lower() == 'en':
                    self.dictateEN()
                else:
                    self.dictateCN()
            if arg == '--range':
                self.setRange(value)
            if arg == '-s':
                self._random = True
            if arg == '--partcn':
                self._dictFunc = self.printPartChinese
            if arg == '--help' or arg == '-h':
                self.printHelpInfo()

    def setRange(self, rangeString):
        start, end = map(lambda x:  int(x) if x.isdecimal() else False,
                         rangeString.split(':'))
        
        if start:
            self._start  = start - 1
        if end:
            self._end    = end

    @staticmethod
    def printHelpInfo():
        info = '''Usage: dictation ListNum [options]

  -c             Show chinese meanings while having dictation.
  -e             Show english words while having dictation.
  -h --help      This help.
  -s             Shuffle the word list.

  --lang=[cn|en] Which equals to -c and -e.
  --partcn       Only show one chinese meaning.Only useful with the `-c` or 
                 `--lang=cn` parameter.
  --range=       Set the range. e.g. --range 12:40, which starts from the
                 12th word and ends at the 40th word. The default setting
                 is --range 1:{length of the word list}.You can only set the
                 start point or end point like :40, which starts from the 1st
                 word.
'''
        print(info)
        sys.exit()

    def getInputAnswer(self):
        return input('>>> ')

    def scoreEnglishAnswer(self, word):
        answer = self.getInputAnswer().strip()
        if answer.lower() == 'exit':
            sys.exit()
        if answer.lower() == word.lower():
            ColorPrint.printGreen('T', end=' ')
            self._rightCnt += 1
        else:
            ColorPrint.printRed('F', end=' ')
            self._wrongCnt += 1

        ColorPrint.printBlue(word, end=' ')
        print('=>', answer)

    def combineFullChinese(self, word):
        string = ''
        for form, chinese in self._wordList[word].items():
            string += form + '；'.join(chinese) + ' '
        return string

    def printFullChinese(self, word):
        fullChinese = self.combineFullChinese(word)
        print(fullChinese, file=self._file)
        self.scoreEnglishAnswer(word)

    def printPartChinese(self, word):
        items = self._wordList[word]
        form = list(items)[random.randrange(0, len(items))]
        index = random.randrange(0, len(items[form]))
        item = items[form][index]
        print(form, item, sep='', end='\n', file=self._file)
        self.scoreEnglishAnswer(word)

    def printEnglish(self, item):
        print(item)
        answer = self.getInputAnswer().strip()
        if answer.lower() == 'exit':
            sys.exit()
        ColorPrint.printBlue(self.combineFullChinese(item), file=self._file)



    def printEnglishAnswer(self):
        lineNumber = 1
        for item in self._dictation:
            print(item)
            time.sleep(int(self._answerTime))

    def printStatistics(self):
        print('-'*15, 'statistics', '-'*15)
        total = self._rightCnt + self._wrongCnt
        print('total:', total)
        print('correct:', self._rightCnt)
        print('wrong:', self._wrongCnt)
        rate = round(self._rightCnt / total * 100, 2) if total != 0 else 0
        print('correct rate: ', rate, '%', sep='')

    def run(self):
        # user sets the range
        if self._start is None and self._end is None:
            self._dictation = list(self._wordList)
        else:
            self._dictation = list(self._wordList)[self._start:self._end]
            
        if self._random:
            random.shuffle(self._dictation)

        lineNumber = 1 if self._start is None else self._start + 1
        for items in self._dictation:
            print(lineNumber, end='. ', flush=True)
            lineNumber += 1
            self._dictFunc(items)

        if self._lang == 'cn':
            self.printStatistics()



if __name__ == '__main__':
    listName = sys.argv[1]
    if listName == '-h' or listName == '--help':
        Dictation.printHelpInfo();

    config = getConfig()
    wordList = importlib.import_module('lists.'+listName).L
    dictation = Dictation(wordList, config)
    print('Word List '+listName[1:])
    dictation.run()
