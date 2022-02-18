import math



def get_dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


x1, y1, r1, x2, y2, r2 = map(float, input().split())

if r1 < r2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1
    r1, r2 = r2, r1

dist = get_dist(x1, y1, x2, y2)
if r1 + r2 <= dist:
    result = 0
elif dist + r2 <= r1:
    result = math.pi*(r2**2)
else:
    theta1 = math.acos((r1 * r1 + dist ** 2 - r2 * r2) / (r1 * dist * 2))
    theta2 = math.acos((r2 * r2 + dist ** 2 - r1 * r1) / (r2 * dist * 2))
    area1 = (r1 * r1 * 2 * theta1) / 2 - r1 * r1 * math.sin(theta1 * 2) / 2
    area2 = (r2 * r2 * 2 * theta2) / 2 - r2 * r2 * math.sin(theta2 * 2) / 2

    result = area1 + area2

print(f'{float(round(result * 1000)) / 1000:.3f}')