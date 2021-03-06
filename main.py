def get_largest_prime_below(x):
    '''
    Determina cel mai mic numar prim mai mic decat n
    :param x: numar intreg
    :return: Cel mai mic numar prim mai mic decat n
    '''
    if (x == 1):
        return print("Nu exista numere prime mai mici decat 1!")
    if (x == 2):
        return 1
    for i in range(x - 1, 0, -1):
        a = 0
        for j in range(2, i // 2):
            if i % j == 0:
                a = 1
        if a == 0:
            return i

def test_get_largest_prime_below():
    assert get_largest_prime_below(6) == 5
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(100) == 97


def is_palindrome(n):
    '''
Verifica daca un numar este palindrom
    :param n:  numar intreg
    :return: Retruneaza adevarat daca nr este palindrom si False in caz contrar
    '''
    if n < 10:
        return False
    ogl = 0
    aux = n
    while aux > 0:
        ogl = ogl * 10 + aux % 10
        aux = aux // 10
    if ogl == n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(1) is False
    assert is_palindrome(123421) is False
    assert is_palindrome(1234321) is True


def get_n_choose_k(n: int, k: int):
    '''
Calculeaza combinari de n luate cate k
    :param n: nr intreg
    :param k: nr intreg
    :return: Combinari de n luate cate k
    '''
    if k > n:
        return print("Nu exista")
    if n == k:
        return 1
    factn = 1
    factk = 1
    factnk = 1
    for i in range(1, n):
        factn = factn * i
    for j in range(1, k):
        factk = factk * j
    for z in range(1, n - k):
        factnk = factnk * z
    result = 0
    result = factn // (factk * factnk)
    return result


def test_get_n_choose_k():
    assert get_n_choose_k(2, 1) == 1
    assert get_n_choose_k(10, 4) == 504
    assert get_n_choose_k(10, 9) == 9

def main():
    print(""""
       1 ,Găsește ultimul număr prim mai mic decât un număr dat.
       2 ,Verifica daca un numar este palindrom.
       3 ,Calculeaza Combinari de n luate cate k
       b ,Inapoi la meniu
       x, Iesire
       """"")
    while True:
        option = input("Alegeti o optiune")
        if option == "1":
            z = int(input())
            print(get_largest_prime_below(z))
        elif option == '2':
            print("introduceti un numar:")
            w = int(input())
            if is_palindrome(w) is True:
                print("Este palindrom")
            else:
                print("Nu este palindrom")
        elif option == "3":
            print("Introduceti un numar")
            a = int(input())
            b = int(input())
            print(get_n_choose_k(a, b))
        elif option == 'b':
            print(""""
        1 ,Găsește ultimul număr prim mai mic decât un număr dat.
        2 ,Verifica daca un numar este palindrom.
        3 ,Calculeaza Combinari de n luate cate k
        b, Inapoi la meniu
        x, Iesire
        """"")

        elif option == 'x':
            break

        else:
            print("Nu ati ales o optiune valida")

if __name__ == '__main__':
    main()