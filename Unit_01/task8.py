
#TASK 8 - UNIT 1

#Task no. 8 is hosted on the https://cryptohack.org platform.
#Use the same account to solve the challenge called Point Addition ( https://cryptohack.org/challenges/ecc/ ).
#Please submit your potential solution/result on the platform to ensure it is correct.

#Y^2=X^3+497X+1768 mod 9739

# Elliptic curve: y^2 = x^3 + a*x + b  (mod p)
a = 497
b = 1768
p = 9739

O = None  # point at infinity


def point_add(P, Q):
    # (a) P = O
    if P is O:
        return Q
    # (b) Q = O
    if Q is O:
        return P
    # (c)
    x1, y1 = P
    x2, y2 = Q
    # (d) P = -Q
    if x1 == x2 and y1 == (-y2) % p:
        return O
    # (e)
    if P != Q:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p          # (e1)
    else:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p   # (e2)
    # (f), (h)
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    # (i)
    return (x3, y3)


if __name__ == "__main__":
    P = (493, 5564)
    Q = (1539, 4742)
    R = (4403, 5202)

    S = point_add(point_add(point_add(P, P), Q), R)
    print(f"crypto{{{S[0]},{S[1]}}}")

# Rasp: crypto{4215,2162}