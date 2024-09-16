def splitWord(word: str):
  while(len(word)%2):
    word += '0'
  n: int = len(word)
  
  return word[:n//2] , word[n//2:]
  
def combineWord(word1: str, word2: str):
  return word1+word2

def swapWord(word: str):
  while(len(word)%2):
    word += '0'
  n: int = len(word)
  return word[n//2:]+word[:n//2]

def leftShift(word: str, k: int):
  return word[k:] + word[:k]

def RightShift(word: str, k: int):
  return word[:k] + word[k:]


def pBox()