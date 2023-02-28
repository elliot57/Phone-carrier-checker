import requests

def phone_list():
    try:
        with open('phones.txt', 'r') as file:
            file = file.readlines()
        phones = [string.rstrip()for string in file]
        return phones
    except FileNotFoundError:
        print("File Not Found")

def check(phones=phone_list()):
    API_KEY = str(input('Enter your API Key: '))
    req = requests.session()
    length_of_phones = len(phones)   
    try:
        for each_phone in phones:
            resp = req.get(f'https://api.veriphone.io/v2/verify?phone=%2B{each_phone}&key={API_KEY}')
            length_of_phones -= 1
            resp = resp.json()
            carrier = resp["carrier"]
            status = resp["status"]
            print(f"Status: {status} | {carrier} : {each_phone}")
    except Exception:
        pass

if __name__ == "__main__":
    check()

