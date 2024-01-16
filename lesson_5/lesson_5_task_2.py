numbers = [1, 5, 2, 4, 7, -4, -9]
is_even = []
is_odd = []
negative = []
positive = []
for i in numbers:
    if i % 2 == 0:
        is_even.append(i)
print(is_even)
for q in numbers:
    if q % 2 != 0:
        is_odd.append(q)
print(is_odd)
for a in numbers:
    if a < 0:
        negative.append(a)
print(negative)
for s in numbers:
    if s > 0:
        positive.append(s)
print(positive)

