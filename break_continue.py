# def run():
#     for i in range(10000):
#         print(i)
#         if i == 5678:
#             break

# if __name__ == '__main__':
#     run()


# def run():
#     for contador in range(1000):
#         if contador % 2 != 0:
#             continue
#         print(contador)

# if __name__ == '__main__':
#     run()


def run():
    texto= input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()