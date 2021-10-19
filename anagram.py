def func(anagrams):
    d = defaultdict(list)
    j = 0
    
    for i in anagrams:
        d[''.join(sorted(i))].append(i)
    
    print(d)

func(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
''''

class Word(object):
	def __init__(self, string, index):
		self.string = string
		self.index = index
def createDupArray(string, size):
	dupArray = []
	for i in xrange(size):
		dupArray.append(Word(string[i], i))
	return dupArray

def printAnagramsTogether(wordArr, size):
	dupArray = createDupArray(wordArr, size)
	for i in xrange(size):
		dupArray[i].string = ''.join(sorted(dupArray[i].string))
	dupArray = sorted(dupArray, key = lambda k: k.string)
	for word in dupArray:
		print wordArr[word.index]
'''