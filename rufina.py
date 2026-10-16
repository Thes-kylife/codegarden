n=int(input('Enter your number:'))
f=1
for i in range(1,n+1):
  f=f*i
print('The factorial of your number is:',f)
r=0
while n>0:
  j=n%10
  r=(r*10)+j
  n=n//10
print('reversed number is:',r)
