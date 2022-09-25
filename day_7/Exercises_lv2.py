A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# task 1
C = A.union(B)
print("{}\n{}\n{}".format(A, B, C))
# task 2
inter = A.intersection(B)
print(inter)
# task 3
sub = A.issubset(B)
print("Is A subset of B ", sub)
# task 4
dis = A.isdisjoint(B)
print("Are A and B disjoint sets", dis)
# task 5
AB = A.union(B)
BA = B.union(A)
print("AB is {} and BA is {}".format(AB, BA))
# task 6
diff = A.symmetric_difference(B)
print("The symmetric difference between A and B is ", diff)
# task 7
del A, B