if __name__ == '__main__':
    mes = ""
    for h in range(1, 101):
        if h % 3 == 0:
            mes += "Fizz"
        if h % 5 == 0:
            mes += "Buzz"
        print(mes if mes != "" else h)
        mes = ""
