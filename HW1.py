# HW1
#Due Date: 02/06/2021, 11:59PM
import math
import re
"""
### Collaboration Statement:

"""

def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    h = -(-perimeter + math.sqrt((perimeter**2)-16*area))/4
    w = area/h

    if h % 1 != 0 or w % 1 != 0:
      return False
    else:
      if h > w:
        return int(h)
      elif h < w:
        return int(w)
      else:
        return False


def frequency(numList):
  '''
      >>> frequency([3, '7', 5, 5.5, '7', 7, 5.5, 'a', 3, 'a', 'a', 'A'])
      ('a', {3: 2, '7': 2, 5: 1, 5.5: 2, 7: 1, 'a': 3, 'A': 1})
      >>> answer=frequency([6, 5, 7, 7, 7, 5, 5, 5])
      >>> answer[0]
      5
      >>> answer[1]
      {6: 1, 5: 4, 7: 3}
  '''
  newDict = {}
  maximum = 0
  string = ""
  for item in numList:
    if item not in newDict:
      newDict[item] = 1
    else:
      newDict[item] += 1
  for key, value in newDict.items():
      if value > maximum:
          maximum = value
          string = key
  return string, newDict


def successors(file):
  """
      >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
      >>> returnedDict = successors('items.txt')
      >>> expected == returnedDict
      True
      >>> returnedDict['.']
      ['We', 'Maybe']
      >>> returnedDict['to']
      ['learn', 'have', 'make']
      >>> returnedDict['fun']
      ['.']
      >>> returnedDict[',']
      ['eat']
  """
  newDict = {}
  with open(file) as f:
    string = f.read()
  slist = re.findall(r"[\w']+|[.,!?;]", string)
  for word in slist:
    if slist.index(word) < len(slist)-1:
      if slist.index(word) == 0:
        newDict["."] = [slist[slist.index(word)]]
        newDict[word] = [slist[slist.index(word)+1]]
      else:
        if word not in newDict:
          newDict[word] = [slist[slist.index(word)+1]]
        else:
          newlist = []
          slist2 = slist.copy()
          for word2 in slist2:
            if word == word2:
              newlist.append(slist2[slist2.index(word2)+1])
              slist2.remove(slist2[slist2.index(word2)])
          newlist = list(dict.fromkeys(newlist))
          for item in newlist:
            if item not in newDict[word]:
              newDict[word].append(item)
  return newDict


def uniqueDigit(num):
    """
        >>> uniqueDigit(123132)
        False
        >>> uniqueDigit(7264578364)
        True
        >>> uniqueDigit(2)
        True
        >>> uniqueDigit(444444)
        False
    """
    l = []
    count = 0
    while num > 0:
      l.append(num%10)
      num //= 10
    for n in l:
      if n == max(l):
        count += 1
    if count > 1:
      return False
    else:
      return True


def hailstone(n):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if n == 1:
      return [1]
    elif n % 2 == 0:
      return [n] + hailstone(n // 2)
    else:
      return [n] + hailstone(3 * n + 1)
    return [n]


def common(list1, list2):
    """
        >>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
        [1, 3, 12, 44]
        >>> common([1,2,3],[4,5,6])
        []

    """
    l = []
    for item in list1:
      for item2 in list2:
        if item == item2:
          l.append(item)
    l = list(dict.fromkeys(l))
    return sorted(l)
