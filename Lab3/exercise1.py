count = 0
limit = 10

#a count's value is set to 0, therefore it is also equal to 0
print('a.', count == 0)

#b limit's value is 10, so it is greater than or equal to 10
print('b.', limit >= 10)

#c limit is 10 so it is therefore less than or equal to count + 10 = 10
print('c.', limit <= count + 10)

#d 
print('d.', count + 10 <= limit)

#e
print('e.', (count == 0) and (limit < 20))

#f
print('f.', count == 0 and limit < 20)

#g
print('g.', (limit > 20) or (count < 5))

#h
print('h.', not(count == 12))

#i
print('i.', (count == 1) and (x < y))

#j
print('j.', (count < 10) or (x < y))

#k
print('k.', not((count < 10) or (x < y)) and (count >= 0))

#l Division by zero
#print('l.', ((limit / count) > 7) or (limit > 20))

#m
print('m.', (limit < 20) or ((limit / count) > 7))

#n Division by zero
#((limit / count) > 7) and (limit < 0)

#o
print('o.', (limit < 0) and ((limit / count) > 7))
