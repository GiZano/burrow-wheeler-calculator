# Import requests library 
import requests

# Connection settings
HOST = 'localhost'
PORT = '8000'

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
                    # Elaboration endpoint URL
                    url = f"http://{HOST}:{PORT}/calculator/{original}"
                    # Encoding request to the server
                    response = requests.get(url)
                    # Get transformed from the response body
                    transformed = response.json()['encoded']
                    # Print results
                    print(f"Original: {original}")
                    print(f"Transformed: {transformed}")

if __name__ == "__main__":
    print(program())