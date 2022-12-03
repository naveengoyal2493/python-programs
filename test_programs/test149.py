from logging.handlers import NTEventLogHandler


a = [1,3,4,5,6,2,2]

b = {}

for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
