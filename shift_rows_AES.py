#!/usr/bin/env python

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

print ''+W+'This will print the real array'+P+''

byte_ary=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

for man in range(0,4):
   print byte_ary[man]

for ran in range(0,4):
  if (ran==0):
    for i in range(0,4):
       byte_ary[ran][i]=byte_ary[ran][i]
  elif (ran==1):
    for j in range(3,-1,-1):
      if (j==3):
        a=byte_ary[ran][j]
        byte_ary[ran][j]=byte_ary[ran][j-1]
      elif (j<3 and j>0):
        byte_ary[ran][j]=byte_ary[ran][j-1]
      elif (j==0):
        byte_ary[ran][j]=a
      else:
        print 'Something going wrong'
  elif (ran==2):
    for k in range(3,-1,-1):
       if (k==3):
         b=byte_ary[ran][k]
         byte_ary[ran][k]=byte_ary[ran][k-2]
       elif (k==2):
         c=byte_ary[ran][k]
         byte_ary[ran][k]=byte_ary[ran][k-2]
       elif (k==1):
         byte_ary[ran][k]=b
       elif (k==0):
         byte_ary[ran][k]=c
       else:
         print 'Something going wrong'

  elif (ran==3):
    for l in range(0,4):
        if (l<3 and l>=0):
          if (l==0):
             d=byte_ary[ran][l]
          byte_ary[ran][l]=byte_ary[ran][l+1]
        elif (l==3):
          byte_ary[ran][l]=d
        else:
          print 'Something going wrong'
  else:
     print 'Something going wrong in MAIN_LOOP'
print '\n\n'+W+''
print ''+R'Now it will print the array after rows shuffling'+G+''
print '\n\n'
for kitman in range(0,4):
   print byte_ary[kitman]
