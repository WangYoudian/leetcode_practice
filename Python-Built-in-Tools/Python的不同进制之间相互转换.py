if __name__ == '__main__':
    n = 19
    binary = bin(n)  # class 'str'
    print("十进制%d转二进制%s" % (n, binary))
    print("二进制%s转十进制%d" % (binary, int(binary, 2)))

    octal = oct(n)
    print("十进制%d转八进制%s" % (n, octal))
    print("二进制%s转十进制%d" % (octal, int(octal, 8)))

    hexadecimal = hex(n)
    print("十进制%d转八进制%s" % (n, hexadecimal))
    print("二进制%s转十进制%d" % (octal, int(hexadecimal, 16)))
