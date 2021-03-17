import getopt
import sys


def main(argv):
    n = 0
    e = 0
    try:
        opts, args = getopt.getopt(argv, "hn:e:")
    except getopt.GetoptError:
        print("WienerAttackRSA.py -n <12345> -e <12345>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("wienerRSAcrack.py -n <12345> -e <12345>")
            print("Example: WienerAttackRSA.py -n 90581 -e 17993")
            sys.exit()
        elif opt == '-n':
            n = int(arg)
        elif opt == '-e':
            e = int(arg)
    runWiener(n, e)


def runWiener(n, e):
    print("\n\nStarting Wieners Attack for RSA PublicKey(" + str(n) + ", " + str(e) + ")")
    print("Crunching Numbers...\n")
    i = 1
    continuedFraction = calcContinuedFraction(e, n)
    A = calcA(continuedFraction)
    B = calcB(continuedFraction)

    while i < len(continuedFraction):
        if (B[i] % 2) == 1:
            C = (e * B[i] - 1) // A[i]
            if isInt(C):
                solution = solveEquation(n, C)
                p = solution[0]
                q = solution[1]
                if p * q == n:
                    print("Found p and q: " + str(solution))
                    print("\nd (privateKey) is: " + str(B[i]))
                    exit()
                else:
                    i += 2
            else:
                i += 2
        else:
            i += 2

    print("Given RSA Key is NOT vulnerable to Wieners Attack!")


def isInt(x):
    return isinstance(x, int)


def solveEquation(n, C):
    factor = n - C + 1
    p = (factor // 2) + isSqrt((factor // 2) ** 2 - n)
    q = (factor // 2) - isSqrt((factor // 2) ** 2 - n)
    solution = [p, q]
    return solution


def isSqrt(n):
    if n < 0:
        raise ValueError('square root not defined for negative numbers')

    if n == 0:
        return 0
    a, b = divmod(calcBitlength(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def calcBitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n + 1
        x = x >> 1
    return n


def calcA(continuedFraction):
    j = 0
    listOfA = []
    while j < len(continuedFraction):
        if j != 0 and j != 1:
            listOfA.append(continuedFraction[j] * listOfA[j - 1] + listOfA[j - 2])
            j += 1
        if j == 0:
            listOfA.append(continuedFraction[0])
            j += 1
        if j == 1:
            listOfA.append(continuedFraction[0] * continuedFraction[1] + 1)
            j += 1
    return listOfA


def calcB(continuedFraction):
    j = 1
    listOfB = [1]
    while j < len(continuedFraction):
        if j != 1:
            listOfB.append(continuedFraction[j] * listOfB[j - 1] + listOfB[j - 2])
            j += 1
        if j == 1:
            listOfB.append(continuedFraction[1])
            j += 1

    return listOfB


def calcContinuedFraction(a, b):
    continuedFraction = []
    stop = False
    while b != 0:
        contFrac = a // b
        continuedFraction.append(contFrac)
        rest = a % b
        a = b
        b = rest
    return continuedFraction


if __name__ == "__main__":
    main(sys.argv[1:])