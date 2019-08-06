#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt, time, importlib, random

def getConfig():
    return getopt.getopt(
        sys.argv[2:], 
        'cehs', 
        ['lang=', 'partcn', 'help',]
    )[0]

class Dictation:

    def __init__(self, wordList, config):
        self._wordList = wordList
        self.preInit()
        self.setConfig(config)

    def preInit(self):
        self._file = utf8stdout = open(1, 'w', encoding='utf-8')
        # dictate chinese
        self._dictFunc = None
        self.dictateCN()
        # shuffle the list
        self._random = False
        # statistics
        self._rightCnt = 0
        self._wrongCnt = 0

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
            if arg == '-s':
                self._random = True
            if arg == '--partcn':
                self._dictFunc = self.printPartChinese
            if arg == '--help' or arg == '-h':
                self.printHelpInfo()

    @staticmethod 
    def printHelpInfo():
        info = '''Usage: toefl ListNum [options]

  -c             Show chinese meanings while having dictation.
  -e             Show english words while having dictation.
  -h --help      This help.
  -s             Shuffle the word list.

  --lang=[cn|en] Which equals to -c and -e.
  --partcn       Only show one chinese meaning.Only useful with the `-c` or 
                 `--lang=cn` parameter.
'''
        print(info)
        sys.exit()

    def getInputAnswer(self):
        return input('>>> ')

    def scoreEnglishAnswer(self, word):
        answer = self.getInputAnswer().strip()
        if answer.lower() == 'exit':
            sys.exit()
        if answer.lower() == word:
            print('\033[0;32mT\033[0m', end=' ')
            self._rightCnt += 1
        else:
            print('\033[0;31mF\033[0m', end=' ')
            self._wrongCnt += 1
        print('\033[0;34m'+word+'\033[0m', '=>', answer)

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
        print('\033[0;34m'+self.combineFullChinese(item)+'\033[0m', file=self._file)


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
        rate = round(self._rightCnt / total * 100, 2)
        print('correct rate: ', rate, '%', sep='')

    def run(self):
        self._dictation = list(self._wordList)
        if self._random:
            random.shuffle(self._dictation)

        lineNumber = 1
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