# FCFS Disk Scheduling

# Input initial head position
head = int(input("Enter the initial head position: "))

# Input number of requests
n = int(input("Enter the number of disk requests: "))

requests = []

# Input disk requests
for i in range(n):
    request = int(input(f"Enter request {i + 1}: "))
    requests.append(request)

# Calculate head movement
current = head
total_movement = 0

for request in requests:
    movement = abs(current - request)
    total_movement += movement
    current = request

# Calculate average head movement
average_movement = total_movement / n

# Output
print("\nFCFS Disk Scheduling")
print("-" * 50)

print("Seek Sequence:")
print(head, end="")

for request in requests:
    print(" ->", request, end="")

print()

print("\nTotal Head Movement :", total_movement)
print("Average Head Movement :", round(average_movement, 2))