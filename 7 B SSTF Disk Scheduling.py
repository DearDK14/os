
# SSTF Disk Scheduling

head = int(input("Enter initial head position: "))

n = int(input("Enter number of requests: "))

requests = []

for i in range(n):
    value = int(input(f"Enter request {i+1}: "))
    requests.append(value)

current = head
total = 0
sequence = [head]

while requests:

    nearest = min(requests, key=lambda x: abs(current - x))

    movement = abs(current - nearest)

    total += movement

    current = nearest

    sequence.append(nearest)

    requests.remove(nearest)

average = total / n

print("\nSSTF Disk Scheduling")
print("-" * 45)

print("Seek Sequence:")
print(" -> ".join(map(str, sequence)))

print("\nTotal Head Movement:", total)
print("Average Head Movement:", round(average, 2))
