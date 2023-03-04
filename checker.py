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
    checked_list = []
    try:
        for each_phone in phones:
            resp = req.get(f'https://api.veriphone.io/v2/verify?phone=%2B{each_phone}&key={API_KEY}')
            resp = resp.json()
            carrier = resp["carrier"]
            status = resp["status"]
            in_number = resp["international_number"]
            print(f"Number: {each_phone} | {carrier}")
            checked_list.append(f'{carrier}|{in_number}\n')
    except Exception:
        pass
    for checked_number in checked_list:
        with open("checked.txt", 'a') as checked_file:
            checked_file.writelines((checked_number))
    
if __name__ == "__main__":
    check()
    
