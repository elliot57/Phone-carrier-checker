import requests

def phone_list():
    try:
        with open('phones.txt', 'r') as file:
            file = file.readlines()
        phones = [s.rstrip()for s in file]
        return phones
    except FileNotFoundError:
        print("File Not Found")

def check(phones=phone_list()):
    API_KEY = str(input('Enter your api key: '))
    req = requests.session()
    flag = len(phones)
    while flag > 1:
        try:
            for i in phones:
            #print(i)
                resp = req.get(f'https://api.veriphone.io/v2/verify?phone=%2B{i}&key={API_KEY}')
                flag -= 1
                resp = resp.json()
                carrier = resp["carrier"]
                status = resp["status"]
                print(f"Status: {status} | {carrier} : {i}")
        except Exception:
            pass

if __name__ == "__main__":
    check()