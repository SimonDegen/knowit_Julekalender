f = open("tall.txt", "r", encoding="utf-8")
numbers = f.readline()
stringNumbers = ['en', 'to', 'tre', 'fire', 'fem', 'seks', 'sju', 'åtte', 'ni', 'ti', 'elleve', 'tolv',
                 'tretten', 'fjorten', 'femten', 'seksten', 'sytten', 'atten', 'nitten', ('tjue', 20),  ('tretti', 30), ('førti', 40), ('femti', 50)]
current = 0
for stringen in stringNumbers[::-1]:
    count, value = (numbers.count(stringen[0]), stringen[1]) if type(
        stringen) == tuple else (numbers.count(stringen), (stringNumbers.index(stringen)+1))
    current += count * value
    numbers = numbers.replace(stringen[0], "") if type(
        stringen) == tuple else numbers.replace(stringen, "")
print(current)
