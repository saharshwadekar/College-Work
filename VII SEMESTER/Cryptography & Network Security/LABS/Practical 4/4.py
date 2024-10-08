def splitWord(word: str) -> tuple:
  while(len(word)%2):
    word += '0'
  n: int = len(word)
  
  return word[:n//2] , word[n//2:]
  
def combineWord(word1: str, word2: str) -> str:
  return word1+word2

def swapWord(word: str) -> str:
  while(len(word)%2):
    word += '0'
  n: int = len(word)
  return word[n//2:]+word[:n//2]

def leftShift(word: str, k: int) -> str:
  return word[k:] + word[:k]

def RightShift(word: str, k: int) -> str:
  return word[:k] + word[k:]


# TODO: check wheather the rule is applicable or not for expansion p-box 
def mapPBox(word: str, PTable: list[int]) -> str:
  result: list = list()
  for i, v in enumerate(PTable):
    result[i] = word[v]
  return "".join(result)

def mapSBox():
  ...
  
  
def main():
  ...
  
if __name__ == '__main__':
  main()