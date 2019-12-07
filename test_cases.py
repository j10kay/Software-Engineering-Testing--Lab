# These are models of the actual test cases to be used when testing.

import re

def testCase_1(username):
  if len(username) == 0:
    raise ValueError
  
def testCase_2(username):
  if len(username) == 1:
    raise ValueError

def testCase_3(username):
  if len(username) > 30:
    raise ValueError
  
def testCase_4(username):
  if " " in username:
      raise ValueError

def testCase_5(username):
  regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
    if(regex.search(string) == None):
      pass
    else:
      raise ValueError

# Other cases not already covered should pass