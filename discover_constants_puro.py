def discover_pi():
    values = []
    for n in range(1000, 2000, 10):
        pi_estimate = 0
        sign = 1
        for k in range(n):
            pi_estimate += sign / (2 * k + 1)
            sign *= -1
        values.append(4 * pi_estimate)
    return round(sum(values[-20:]) / 20, 5)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def discover_e():
    e_estimate = 0
    for n in range(0, 18):
        e_estimate += 1 / factorial(n)
    return round(e_estimate, 5)

if __name__ == "__main__":
    pi = discover_pi()
    e = discover_e()
    print(f"🔍 π scoperto: {pi}")
    print(f"🔍 e scoperto: {e}")

    with open("output/scoperte_costanti_pure.json", "w") as f:
        f.write(f'{{"pi": {pi}, "e": {e}}}')


