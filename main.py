import os

import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
chat_id = "-915705267"

# https://us-central1-rsathishx87.cloudfunctions.net/pap_gumroad
# for token, go to BOTFATHER /mybots > apikey


def pap_gumroad(request):
    referrer = request.form.get('referrer')
    country = request.form.get('ip_country')
    currency = request.form.get('currency')
    product = request.form.get('product_name')
    fee = int(request.form.get('gumroad_fee'))
    email = request.form.get('email')
    price = int(request.form.get('price'))
    full_name = request.form.get('full_name')
    variants = request.form.get('variants[]')
    message = f"🤑💰 KACHING KACHING 🤑💰\n*Product:* `{product}`\n*Variant:* `{variants}`\n*Price (After gumroad fee)* - `USD${(price-fee)/100}`\n*User:* `{full_name}`\n*User Email:* `{email}`\n*User Currency | Country:* `{currency.upper()} | {country}` \n*Referral Source:* `{referrer}`\n"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown&disable_web_page_preview=True"

    print(requests.get(url).json())

    return "OK"
