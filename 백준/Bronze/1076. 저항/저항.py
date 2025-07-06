rmap = {
    "black":0,
    "brown":1,
    "red":2,
    "orange":3,
    "yellow":4,
    "green":5,
    "blue":6,
    "violet":7,
    "grey":8,
    "white":9
}

r1, r2, r3 = (input().strip() for _ in range(3))

print((rmap[r1] * 10 + rmap[r2] ) * (10 ** rmap[r3]))


