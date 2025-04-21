import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$"
    return bool(re.fullmatch(pattern, ip))



if __name__ == "__main__":
    main()
