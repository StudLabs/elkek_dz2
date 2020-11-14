def hex_to_bin_list(Q):
    binary = bin(int(Q, base=16))[2:]
    while len(binary) < 16:
        binary = '0' + binary
    return [int(x) for x in binary]

def num_to_bits(x):
    binary = bin(x)[2:]
    while len(binary) < 4:
        binary = '0' + binary
    return [int(bit) for bit in binary]

def check(F, answers):
    for i in range(16):
        A, B, C, D = num_to_bits(i)
        variant = F(A, B, C, D)
        if variant != answers[-i-1]:
            return False
    return True

def F(A, B, C, D):
    X = not(C&(not D))
    Y = not(A&(not B)&(not C))
    W = not((not A)&B&(not D))
    Z = not((not A)&(not B)&D)
    # твой вариант преобразования
    res = (not(X&Y))&(not(W&Z))
    # Рабочая функция без преобразования в базис И-НЕ
    roboty = C&(not D) | A&(not B)&(not C) | (not A)&B&(not D) | (not A)&(not B)&D
    return not(X&Y&W&Z) # Мой ебанутый вариант

def main():
    Q = input("Введите 16-ричное число: ")
    answers = hex_to_bin_list(Q)
    if check(F, answers):
        print("Сократили правильно")
    else:
        print("Логическая функция F НЕПРАВИЛЬНАЯ")

if __name__ == "__main__":
    main()