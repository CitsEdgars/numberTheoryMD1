# Uzrakstīt programmu, kas dotiem veseliem pozitīviem skaitļiem k, m1,
# m2, …, mk, a1, a2, …, ak (ieejas dati atrodas failā “ieeja.txt” šajā secībā,
# katrs skaitlis jaunā rindiņā), kur skaitļi mi ir savstarpēji pirmskaitļi,
# atrod un izvada tādu a, ka 0 ≤ a < m1m2 . . . mk un a ≡ a1 (mod m1),
# a ≡ a2 (mod m2), …, a ≡ ak (mod mk).

from audioop import mul
from math import gcd, prod

def find_gcd(a:int, b:int):
    if (a == 0):
        return b
    return find_gcd(b % a, a)

def verify_coprimeness(prime_arr: list):
    if len(set(prime_arr)) == len(prime_arr):
        for i in prime_arr:
            for j in prime_arr:
                if i != j:
                    if gcd(i, j) != 1: 
                        return False
    else: return False
    return True

if __name__ == "__main__":
    k = 0
    m_list = []
    a_list = []
    counter = 0
    first = True
    for line in open("ieeja.txt","r").readlines():
        if first: 
            k = int(line.replace("\n", ""))
            first = False
            continue
        else: 
            counter += 1
            if counter <= k: 
                m_list.append(int(line.replace("\n", "")))
            else: 
                a_list.append(int(line.replace("\n", "")))
    if len(a_list) != len(m_list):
        print("Input data is invalid")
    else:
        print("Input:", k, m_list, a_list)
        if verify_coprimeness(m_list):
            for pot_a in range(prod(m_list)):
                modulo_verified = 0
                for m_idx, a in enumerate(a_list):
                    if pot_a % m_list[m_idx] != a % m_list[m_idx]: break
                    else: modulo_verified += 1

                    if modulo_verified == k:
                        print("------------------------------",pot_a,"--------------------------------")
        else:
            print("m values are not co-prime")

