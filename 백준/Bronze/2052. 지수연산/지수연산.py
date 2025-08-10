N = int(input())

frac = str(5**N)
frac = "0" * (N - len(frac)) + frac
print("0." + frac)