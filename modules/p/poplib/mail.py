import getpass, poplib

M = poplib.POP3_SSL('pop.gmail.com')
M.user('robert.griffith.sa@gmail.com')
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)
