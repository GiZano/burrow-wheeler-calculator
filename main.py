import bwt_calculator as bwt

def program():
    
    print("=== Burrow Wheeler Transform Calculator ===")
    while True:
        print('''
=== Menù ===
1) Terminal input
2) File input (input.txt)
0) Exit
        ''')
        select: int = int(input("Select:"))

        match select:
            case 0:
                ### Program Exit ###
                return "=== Program End ==="
            case 1:
                ### Terminal Input ###
                valore = str(input("Insert string to encode with BWT:"))
                print(f"Transformed: {bwt.encoder(valore)}")
            case 2:
                ### File Input ###
                with open("input.txt", "r") as in_file:
                    with open("output.txt", "w") as out_file:
                        value = in_file.read()
                        transformed = bwt.encoder(value)
                        print(f"Transformed: {transformed}")
                        out_file.write(transformed)

                    


if __name__ == "__main__":
    print(program())

            