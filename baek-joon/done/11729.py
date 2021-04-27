n = int(input())
k = 0


def move_disk(disk_num, start_peg, end_peg):
    print(f"{start_peg} {end_peg}")


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks - 1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, other_peg, end_peg)


print((2 ** n) - 1)
hanoi(n, 1, 3)
