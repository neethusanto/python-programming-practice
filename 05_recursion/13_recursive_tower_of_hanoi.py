"""
Q13: Solve Tower of Hanoi puzzle for N disks using recursion.
Constraint: Displays each step of disk movement.
"""

def tower_of_hanoi(n, source, target, auxiliary, counter):
    if n == 1:
        counter[0] += 1
        print(f"Step {counter[0]}: Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, target, counter)
    counter[0] += 1
    print(f"Step {counter[0]}: Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source, counter)

if __name__ == "__main__":
    step_counter = [0]
    print("Solving Tower of Hanoi for 3 disks:")
    tower_of_hanoi(3, 'A', 'C', 'B', step_counter)
