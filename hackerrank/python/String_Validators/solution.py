if __name__ == '__main__':
    s = raw_input()
    print(any([var.isalnum() for var in s]))
    print(any([var.isalpha() for var in s]))
    print(any([var.isdigit() for var in s]))
    print(any([var.islower() for var in s]))
    print(any([var.isupper() for var in s]))
