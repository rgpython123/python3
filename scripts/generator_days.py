>>> def testgen():
...   weekdays = ['sun','mon','tue','wed','thu','fri','sat']
...   
...   for index in range(7):
...     yield weekdays[index]
... 

>>> day = testgen()
>>> day
<generator object testgen at 0x7fea079bc938>

>>> next(day)
'sun'
>>> next(day)
'mon'
>>> next(day)
'tue'
>>> next(day)
'wed'
>>> next(day)
'thu'
>>> next(day)
'fri'
>>> next(day)
'sat'
>>> next(day)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 

