import json

def main():
    FILE = 'online_1.json'

    f = open(FILE)

    dataset = json.load(f)
    print(dataset[""])

if __name__ == "__main__": 
    main()