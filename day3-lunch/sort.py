#!/usr/bin/env python

import random
#r = random.randint(1,100)
#print r

#nums = []

#to get 10 things, it'll pick 0-9
#for i in xrange(10):
    #print i
   # r = random.randint(1,100)
   # print "the %dth number is %d" % (i, r)
   # nums.append(r)

#print nums

#nums.sort()
#print nums

#key = 42

#same as enumerate
#for i in xrange(len(nums)):
   # v = nums [i]
    #print "scanning the %dth number is %d" % (i, v)
    #if v == key:
        #print "found it at position %d" % (i)

#assignment I guess

#nums = range(10)
#print nums
#key = 3

#for x in nums:
    #min = 0
    #max = len(nums)-1
    #v = (max-min)/2
    #while True:
        #if key > v:
            #min = v
            #v = (max-min)/2
            #print "too large"
        #elif key < v:
            #max = v
            #v = (max-min)/2
            #print "too small"
        #else:
            #print v
            #break

nums = range(0, 100, 10)
print nums

key = 40

#initialize what'll be searched
lo = 0
hi = len(nums) - 1

while lo < hi:
    #find middle item
    mididx = (lo+hi)/2
    mid = nums[mididx]
    
    print "checking in range [%d, %d] mididx[%d] = %d" % (lo, hi, mididx, mid)

#compare the middle item to the list
    if mid == key:
        print "god, finally. freaking found %d==%d at %d" % (key, mid, mididx)
        break
    elif key > mid:
        lo = mididx
    else:
        hi = mididx

#yeah that's basically what i was trying to do























