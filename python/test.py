phoneBook = [12,88,123,567,1235]

zipped = zip(phoneBook,phoneBook[2:])
print(next(zipped)) #(12,88)
print(next(zipped)) #(88,123)
print(next(zipped)) #(123,567)