# lists

scores = [90, 65, 34, 71, 55, 77, 89]

# access an value
print(scores[0]) # fisrt
print(scores[-1]) # last
print(scores[2]) # third

# add
scores.append(61)
print(scores)

scores.pop(3)
print(scores)

scores.sort(reverse=True)
print(scores)