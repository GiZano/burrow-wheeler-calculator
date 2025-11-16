import requests

def program():
    print("=== BWT Client ===")
    while True:
        print('''
=== Menù ===
1) Request BWT Encoding
0) Exit
              ''')
        choose = int(input("Select:"))

        match choose:
            case 0:
                ### Exit ###
                return "Exiting program..."
            case 1:
                original = str(input("Insert string to transform:"))

                if(len(original) == 0):
                    print("Invalid string!")
                else:
                    url = f"http://localhost:8000/calculator/{original}"
                    response = requests.get(url)
                    print(f"Original: {original}")
                    print(response.json()['encoded'])

if __name__ == "__main__":
    print(program())