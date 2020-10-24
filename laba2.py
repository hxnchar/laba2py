a1 = float(input("Input a1")) #коэф. а первого уравнения
a2 = float(input("Input a2")) #коэф. а второго уравнения
b1 = float(input("Input b1")) #коэф. b первого уравнения
b2 = float(input("Input b2")) #коэф. b второго уравнения
c1 = float(input("Input c1")) #коэф. c первого уравнения
c2 = float(input("Input c2")) #коэф. c второго уравнения
if a1/a2==b1/b2!=c1/c2:
    haveNoSol = True
    print("System has no any solutions.)
else:
    if a1/a2==b1/b2==c1/c2:
        haveManySol = True
        print("System has infinity solutions.")
    else:
        haveOneSol = True
        print("System has only 1 solution")
k = input()