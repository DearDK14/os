
# First Fit, Best Fit and Worst Fit

# Input number of memory blocks
n = int(input("Enter number of memory blocks: "))

blocks = []

for i in range(n):
    size = int(input(f"Enter size of Block {i+1}: "))
    blocks.append(size)

# Input number of processes
m = int(input("\nEnter number of processes: "))

processes = []

for i in range(m):
    size = int(input(f"Enter size of Process {i+1}: "))
    processes.append(size)


# Memory Allocation Function
def allocation(method):

    memory = blocks.copy()
    allocated = [-1] * m

    for i in range(m):

        idx = -1

        for j in range(n):

            if memory[j] >= processes[i]:

                if method == "First Fit":
                    idx = j
                    break

                elif method == "Best Fit":
                    if idx == -1 or memory[j] < memory[idx]:
                        idx = j

                elif method == "Worst Fit":
                    if idx == -1 or memory[j] > memory[idx]:
                        idx = j

        if idx != -1:
            allocated[i] = idx
            memory[idx] -= processes[i]

    # Display Result
    print("\n", method)
    print("-" * 55)
    print("Process\tSize\tBlock\tRemaining Space")
    print("-" * 55)

    for i in range(m):

        if allocated[i] != -1:
            b = allocated[i]
            print(f"P{i+1}\t{processes[i]}\tB{b+1}\t{memory[b]}")
        else:
            print(f"P{i+1}\t{processes[i]}\tNot Allocated\t-")

    print("-" * 55)


# Execute all three strategies
allocation("First Fit")
allocation("Best Fit")
allocation("Worst Fit")
