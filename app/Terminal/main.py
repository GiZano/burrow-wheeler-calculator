import sys
import os

# Get absolute path of project directory 
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)                # get project root 
components_path = os.path.join(project_root, 'Components') # get components path

sys.path.insert(0, components_path)
sys.path.insert(0, project_root) 

from Components.bwt_calculator import encoder as bwt


def program():
    
    print("=== Burrow Wheeler Transform Calculator ===")
    while True:
        print('''
=== Menù ===
1) Terminal input
2) File input (./data/input.txt)
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
                print(f"Transformed: {bwt(valore)}")
            case 2:
                ### File Input ###
                with open("./data/input.txt", "r") as in_file:
                    with open("./data/output.txt", "w") as out_file:
                        value = ""
                        for line in in_file:
                           # If the file is made of multiple lines, put it all together in one single line
                           value = value + line.strip("\n").strip()
                        transformed = bwt(value)
                        print(f"Transformed: {transformed}")
                        out_file.write(transformed)
                        out_file.flush()

if __name__ == "__main__":
    print(program())

            