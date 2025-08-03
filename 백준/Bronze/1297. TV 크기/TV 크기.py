d, h, w = map(int, input().split())
 
height = int((h*d) / (((h**2) + (w**2)) **0.5))
width = int((w*d) / (((h**2) + (w**2)) **0.5))
print(height, width)