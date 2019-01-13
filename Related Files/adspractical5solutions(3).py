#adspractical5solutions.py
#algorithms and data structures practical solutions week 5
#matthew johnson 2 november 2012
#revised 31 october 2018

#####################################################


############
#Question 3#
############

def hash(d):
    """given a list d of integers returns a list of length 13
    describing the hash table obtained when the hash function
    h(k)=k mod 13 is applied to each integer k in d"""
    #initialize table
    table = ["-"]*13
    #consider each integer k in the input
    for k in d:
        #if k is already in the table this is a duplicate so move to next integer in the input
        #note this check for a duplicate is using the functionality of python rather than checking using a linear probe
        if k in table:
            continue
        #apply the hash function
        i = k % 13
        #initialize count that checks whether linear probe has considered each bucket and is now full
        count = 0
        #while bucket is already filled
        while table[i] != "-":
            #move to next bucket
            i = (i + 1) % 13
            #increment count
            count += 1
            #if table is full
            if count == 12:
                #can return table as nothing further can be added
                return table
        #table[i] is empty so k can be added here
        table[i] = k
    #now each part of the input has been considered return the table
    return table

def testq3():
    assert hash([25,6,39,17,12,15,53]) == [39, 12, 15, 53, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    assert hash([0,1,2,3,4,5,6,7,8,9,10,11,12]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([10,11,12,0,1,2,3,4,5,6,7,8,9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([-1,-2,-3]) == ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', -3, -2, -1]
    assert hash([53,25,6,39,17,12,15]) == [39, 53, 12, 15, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    print ("all basic tests passed")
    assert hash([25,6,39,17,12,15,53,53]) == [39, 12, 15, 53, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    assert hash([1,1,1,1,2,2,2,3,3,3]) == ['-', 1, 2, 3, '-', '-', '-', '-', '-', '-', '-', '-', '-']    
    print ("all tests involving duplicates passed")
    print ("now  we test inputs containing more integers than the size of the table")
    print ("you will wait forever if you have not considered this case")
    assert hash([0,1,2,3,4,5,6,7,8,9,10,11,12,13]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([0,1,1,1,7,1,2,3,4,0,5,6,7,8,9,9,9,10,11,12,13]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print ("all tests passed")






############
#Question 4#
############

def modulus(m ,n):
    """returns value of m mod n"""
    if m < n:
        return m
    else:
        return modulus(m - n, n)

############
#Question 5#
############

def DigitSum(n):
    """returns sum of the digits of a positive integer"""
    if n < 10:
        return n
    else:
        return (n % 10) + DigitSum(n // 10)

#####################################################



#for lucas and fibonacci numbers we use memoization 
luc_memo = {0:2, 1:1}
def lucas(n):
    """finds the nth lucas number using memoized recursion"""
    if not n in luc_memo:
        luc_memo[n] = lucas(n-1) + lucas(n-2)
    return luc_memo[n]
    
fib_memo = {0:0, 1:1}
def fibonacci(n):
    """finds the nth fibonacci number using memoized recursion"""
    if not n in fib_memo:
        fib_memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_memo[n]

def lucas_vs_fibonacci(n=51):
    """prints out lucas and fibonacci numbers
    and their ratio"""
    print ("n".rjust(3), end=" ")
    print ("lucas".rjust(12), end=" ")
    print ("fib".rjust(12), end=" ")
    print ("ratio".rjust(6), end=" ")
    print ("ratio squared".rjust(19))
    for i in range(n)[1:]:
        l, f = lucas(i), fibonacci(i)
        print (repr(i).rjust(3), end=" ")
        print (repr(l).rjust(12), end=" ")
        print (repr(f).rjust(12), end=" ")
        print (repr(round(1.0*l/f,3)).rjust(6), end=" ")
        print (repr((1.0*l**2)/(f**2)).rjust(19))

def pascal(row, pos):
    """calculates the value at (row, pos) of Pascal's triangle;
    could be improved with memoization"""
    if row == 0 or pos % row == 0:
        return 1
    return pascal(row-1,pos-1) + pascal(row-1,pos)
                
def mult(x, n):
    """finds the product using the Egyptian method"""
    if n == 1:
        return x
    if n % 2 == 0:
        return mult(2*x, n/2)
    return x + mult(2*x, (n-1)/2)

def exp(x ,n):
    """finds x to the power n using exponentiation by squaring"""
    if n == 0:
        return 1
    if n % 2 == 0:
        return exp(x*x, n/2)
    return x * exp(x*x, (n-1)/2)

def gcd(a,b):
    """Euclid's algorithm for finding the greatest common
    divisor of a and b"""
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)
