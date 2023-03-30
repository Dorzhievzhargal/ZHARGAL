# Chapter 4: Working with LISTS
states = ['New York', 'New Jersey', 'Connecticut', 'California']

# Loops - within the Loops you create repetitive actions
#  Insert
sq = []
for x in range(5, 13):
    x_sq = x ** 2
    sq.insert(0, x_sq)
print(list(reversed(sq)))

# Append
sq = []
for x in range(5, 13):
    x_sq = x ** 2
    sq.append( x_sq)
print(sq)
