
from math import gcd, prod
import os

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
    input_data = []
    with open(os.getcwd() + "\\ieeja.txt") as input:
        for line in input.readlines():
            input_data.append(int(line))

    k = input_data[0]
    m_values = input_data[1:k+1]
    a_values = input_data[k+1:]

    if len(a_values) != len(m_values):
        print("Input data is invalid")
    else:
        print("Input:", k, m_values, a_values)
        if verify_coprimeness(m_values):
            N = prod(m_values)
            N_vals = []
            for m in list(m_values):
                m_values.remove(m)
                N_vals.append(prod(m_values))
                m_values.append(m)
            
            inv_N = []
            for idx, n in enumerate(list(N_vals)):
                N_vals.remove(n)
                inv_N.append(pow(n, -1, m_values[idx]))
                N_vals.append(n)

            x_vals = []
            for idx in range(k):
                x_vals.append(a_values[idx] * N_vals[idx] * inv_N[idx])
            print("------------------------------",sum(x_vals) % N,"--------------------------------")
        else:
            print("m values are not co-prime")