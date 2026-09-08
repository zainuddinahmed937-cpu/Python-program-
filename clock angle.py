hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

hour = hour % 12

h_angle = hour * 30 + minute * 0.5
m_angle = minute * 6

angle = abs(h_angle - m_angle)

if angle > 180:
    angle = 360 - angle

print("Smaller angle =", angle)
