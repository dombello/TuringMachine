#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 1: Up and Running
# 
# 
# _csc427, semester 222
# <br>
# university of miami
# <br>
# date: 20 january 2022
# <br>
# update: 22 january 2022_
# 
# 
# 

# ---
# 
# ### Student name:
# 
# ---
# 
# 
# ### General Remarks
# 
# You are to edit this notebook to complete the described tasks. There are test sections in this code that should automatically run to test your work. You will note that there is also a Makefile in the directory along with the file. It runs at the command line and automates the testing of your notebook.
# 

# ## A. Fibonacci Series
# 
# 
# Write a program that given n calculates the n-th fibonacci number. Make sure your program passes the test suite.
# 
# Things to learn in this project,
# - how to define a function in python
# - how to create a range object, and to iterate on that object
# More about iterators can be found in the C part of the [ABC of Python](https://www.cs.miami.edu/home/burt/learning/csc427.222/index.html?p=cn).
# 
# 

# In[17]:



def fib_series(n):
    a = 0
    b = 1

    if n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            
        return b

print(fib_series(8))
    


# ## Part B: Sort a string
# 
# Given a string, break it into words, sort the words, and then put the words back into a string.
# 
# Things to learn in this project, 
# - how to split a string, see [string.split](https://docs.python.org/3/library/stdtypes.html#str.split).
# - how to join a list of strings, see [string.join](https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join).
# - how to sort a list, see [list.sort](https://docs.python.org/3/library/stdtypes.html?highlight=sort#list.sort).

# In[16]:



def sort_words_in_line(line):
    
    unsortedString = line.split(" ")
    unsortedString.sort()
    sortedString = " ".join(unsortedString)

    return sortedString

print(sort_words_in_line("Hello how are you"))


# ## Testing section

# In[ ]:



def test_fib_series(ans):
    wrong = 0
    for n in ans:
        ok = ""
        if fib_series(n[0])!=n[1]:
            wrong += 1
            ok = "*"
        print(f'{ok}fib_series({n[0]}) = {n[1]}')
    print(f'\n{len(ans)-wrong} out of {len(ans)} correct')
    return wrong==0

def test_sort_words_in_line(ans):
    wrong = 0
    for test in ans:
        ok = ""
        s = sort_words_in_line(test[0])
        if s != test[1]:
            wrong += 1
            ok = "*"
        print(f'{ok}|{s}|?=|{test[1]}|')
    print(f'\n{len(ans)-wrong} out of {len(ans)} correct')
    return wrong==0


ans = [(1, 1), (8, 21), (27, 196418), (64, 10610209857723), 
    (125, 59425114757512643212875125), (216, 619220451666590135228675387863297874269396512)]

print()
if test_fib_series(ans):
    print('*** passed the test!')
else:
    print('*** did not pass the test.')
    
# thanks to alex for the extra test case. to clarify the sort order to be used.    
ans = [("a b c d e","a b c d e"),("now is the time for all","all for is now the time"),("z y z c b a","a b c y z z"),
       ("it was the best of times it was the worst of times","best it it of of the the times times was was worst"),
      ("a b B A c cc Cc","A B Cc a b c cc")]

print()
if test_sort_words_in_line(ans):
    print('*** passed the test!')
else:
    print('*** did not pass the test.')
    


# ## Part C: Finite Automata
# 
# Write a basic program to simulate a finite automata. The automata examples are from Siper's book.
# 
# Things to learn in this project:
# - the set data type, see [class Set](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#sets),
# - the tuple data type, see [class Tuple](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#tuples-and-sequences),
# - the dictionary data type, see [class Dict](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries).
# - how to define a class

# In[32]:


class SimpleFiniteAutomata:

    def __init__(self, fa_description):
        self.fa = fa_description
        self.state = self.fa['start']

    def one_step(self, symbol):
        """
        takes a symbol (a string) and returns a state
        it is the state arrived at given the symbol at the current state
        """
        current = (self.state, symbol)
        if current in self.fa["transitions"]:
            self.state = self.fa["transitions"][current]

        else: 
            self.state = None

    def compute(self, string):
        """
        takes a string and put the FA in the start state, then applies one_step
        to each symbol in the string.
        returns True if the FA ends in an accepting state; else returns False
        """

        # write code here
        start = self.state
        for c in string:
            self.one_step(c)
        
        res = self.state in self.fa["accept"]   # do not takes this as a hint
        self.state=start
        return res

# end class SimpleFiniteAutomata


# ## Part D: Finite Automata Specification
# 
# The specification for Finite Automata M1 (page 34) is given. Also test strings are defined in a 2-tuple of lists. The first entry in the tuple is a list of strings accepted by M1; the second entry, strings not accepted by M1.
# 
# Write the specification for Finite Automata M2 (page 37), M3 (page 38) and M4 (page 38). Write the test cases associated with each of M2, M3 and M4.
# 

# In[19]:



# example of a Finite Automata Description. 
# this one is M1, from figure 1.4 in Sipser

x=0

m1 = {
    'states':{'q1','q2','q3'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q1',
        ('q1','1'):'q2',
        ('q2','1'):'q2',
        ('q2','0'):'q3',
        ('q3','0'):'q2',
        ('q3','1'):'q2'
    },
    'start':'q2',
    'accept':{'q2'}
}

m1_test = (["1","01","11","0101010101","100","0100","010000"],["0","10","101000"])

# change m2, m3, m4 and associated test vectors

m2 = {
    'states': {'q1', 'q2'},
    'alphabet': {'0', '1'},
    'transitions': {
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q2',
        ('q2', '0'): 'q1',
        ('q2', '1'): 'q2',
    },
    'start': 'q1',
    'accept': {'q2'}
}

m2_test = (["1", "11", "101", "01001011011"],["0","00","010","111010"])

m3 = {
    'states':{'q1','q2'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q2',
        ('q2', '0'): 'q1',
        ('q2', '1'): 'q2',
        },
    'start':'q1',
    'accept': {'q1'} 
}

m3_test = (['0','10','00110'],['1','01','1101'])


m4 = {
    'states':{'s','q1','q2','r1','r2'},
    'alphabet':{'a','b'},
    'transitions':{
        ('s','a'):'q1',
        ('s','b'):'r1',
        ('q1','a'):'q1',
        ('q1','b'):'q2',
        ('q2','a'):'q1',
        ('q2','b'):'q2',
        ('r1','a'):'r2',
        ('r1','b'):'r1',
        ('r2','a'):'r2',
        ('r2','b'):'r1',
        },
    'start':'s',
    'accept': {'q1','r1'} 
}

m4_test = (['aa','aba','abba','bb','bbab','bbaabb'],["ab",'abab','abbab','ba','bba','baa','babbbababa'])


fa = SimpleFiniteAutomata(m4)
print(fa.compute('bb'))


# ## Testing Part C

# In[33]:





def simple_fa_test(fa_desc,test_vect,verbose=False):
    fa = SimpleFiniteAutomata(fa_desc)
    tv_true, tv_false = test_vect
    correct = 0 

    for string in tv_true:
        if fa.compute(string):
            correct += 1
    for string in tv_false:
        if not fa.compute(string):
            correct += 1
    return (correct,len(test_vect[0]) + len(test_vect[1]))

fa_all = [
    ('M1',m1,m1_test),
    ('M2',m2,m2_test),
    ('M3',m3,m3_test),
    ('M4',m4,m4_test),
]

for fa in fa_all:
    correct, total = simple_fa_test(fa[1],fa[2])
    print(f'\nMachine {fa[0]}: {correct} correct out of {total} tests.')


# In[ ]:




