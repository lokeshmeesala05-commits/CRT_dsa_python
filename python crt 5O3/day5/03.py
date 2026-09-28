def isPalindrome(num):
  n=num
  rev=0
  rem=0
  while(n>0):
    rem=n%10
    rev=rev*10 + rem
    n=n//10

  if(num==rev):
    return True
  else:
    return False
            
print(isPalindrome(12321))


