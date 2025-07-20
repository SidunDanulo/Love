def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num ** 3
        if cube >= end:
            return
        yield cube
        num += 1
        print(list(generate_cube_numbers(10)))  # [8]
        print(list(generate_cube_numbers(100)))  # [8, 27, 64]
        print(list(generate_cube_numbers(1000)))  # [8, 27, 64, 125, 216, 343, 512, 729]