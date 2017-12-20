
def collatz_sequence(n):
    collatz_seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 2 * n + 1
        collatz_seq.append(n)
    return collatz_seq


while True:
    n_input = input("Enter starting value (enter 0 to exit): ")
    try:
        n = int(n_input)
    except ValueError:
        print('Invalid integer: {}'.format(n_input))
        continue
    if n < 0:
        print('n must be positive')
    if n == 0:
        break
    cseq = collatz_sequence(n)
    print('Collatz sequence for n={}:\n{}'.format(n, cseq))

print('Thanks for playing, I hope you had fun.')
