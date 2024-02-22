import heapq

# first and last index in sorted array

def first_and_last(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      start = i
      while i+1 < len(arr) and arr[i+1] == target:
        i += 1
      return [start, i]
  return [-1, -1]

# kth largest element
# Given an array of ints arr and an int k,
# find the kth largest element
def kth_largest(arr, k):
  arr.sort()
  return arr[len(arr) - k]

# symmetric tree
# see if a binary tree is symmetric
def are_symmetric(root1, root2):
  if root1 is None and root2 is None:
    return True
  elif ((root1 is None) != (root2 is None) or root1.val != root2.val):
    return False
  else:
    return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)
  
def is_symmetric(root):
  if root is None:
    return True
  return are_symmetric(root.left, root.right)

# generate parentheses
def generate(n):
  def rec(n, diff, comb, combs):
    if diff < 0:
      return
    elif n == 0:
      if diff == 0:
        combs.append(''.join(comb))
    else:
      comb.append('(')
      rec(n-1, diff+1, comb, combs)
      comb.pop()
      comb.append(')')
      rec(n-1, diff-1, comb, combs)
      comb.pop()
  combs = []
  rec(2*n, 0, [], combs)
  return combs

def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = 'aeiouAEIOU'

        while start < end:
          while start < end and vowels.find(word[start]) == -1:
            start += 1
          
          while start < end and vowels.find(word[end]) == -1:
            end -= 1

          word[start], word[end] = word[end], word[start]

          start += 1
          end -= 1
        
        return ''.join(word)

def isSubsequence(s, t):
  str_list = []
  for char in t:
    if char in s:
      str_list.append(char)
  new_word = ''.join(str_list)
  return new_word == s

def isDivisibleByFive(n):
  return n % 5 == 0

# sliding window exmaple
def slidingWindow(arr, k):
  if len(arr) < k:
    return 0
  total = sum(arr[:k])
  maxtotal = total
  for i in range(len(arr) - k):
    total -= arr[i]
    total += arr[i+k]
    maxtotal = max(maxtotal, total)
  return maxtotal

def mostVowelsInSubstring(s, k):
  if len(s) < k:
    return 0
  total = 0
  lookUpv = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True}
  for c in s[:k]:
    if c in lookUpv:
      total += 1
  maxTotal = total
  for i in range(len(s)-k):
    char_to_add = s[i+k]
    if char_to_add in lookUpv:
      total += 1
    char_to_remove = s[i]
    if char_to_remove in lookUpv:
      total -= 1
    maxTotal = max(maxTotal,total)
  return maxTotal

def findMaxAverage(nums, k):
  if (len(nums) < k):
    return 0
  total = float(sum(nums[:k]))
  average = float(total / k)
  maxaverage = average
  for i in range(len(nums) - k):
    total -= nums[i]
    total += nums[i+k]
    maxaverage = max(maxaverage, float(total / k))
  return maxaverage

def largestAltitude(gain):
  """
  :type gain: List[int]
  :rtype: int
  """
  if len(gain) == 2:
    return gain[0] + gain[1]
  if len(gain) == 1:
    return gain[0]
  if len(gain) == 0:
    return 0
  altitudes = [0]
  for i in range(len(gain)):
    if i == 0:
      altitudes.append(altitudes[0] + gain[0])
    else:
      altitudes.append(altitudes[i] + gain[i])
  return max(altitudes)

print(largestAltitude([-5, 1, 5, 0, -7]))

nums = [1,2,3,4]
print(sum(nums[:2]))