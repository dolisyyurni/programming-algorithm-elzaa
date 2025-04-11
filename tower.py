# Program Tower of Hanoi
def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print(f"Move disk 1 from {from_peg} to {to_peg}")
        return
    tower_of_hanoi(n - 1, from_peg, aux_peg, to_peg)
    print(f"Move disk {n} from {from_peg} to {to_peg}")
    tower_of_hanoi(n - 1, aux_peg, to_peg, from_peg)

# Contoh penggunaan
jumlah_cakram = 3
tower_of_hanoi(jumlah_cakram, 'A', 'C', 'B')