import requests

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

    with open("info.text", "w") as file:
        file.write(response.text)


def get_ticker(coin1="btc",coin2="usd"):
    response  = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")
    print(response.text)
    info = f'High :{response.json()[f"{coin1}_{coin2}"]["high"]} \n Low :{response.json()[f"{coin1}_{coin2}"]["low"]} \n Last:{response.json()[f"{coin1}_{coin2}"]["last"]}\n Buy :{response.json()[f"{coin1}_{coin2}"]["buy"]} \n Sell :{response.json()[f"{coin1}_{coin2}"]["sell"]}'
    return info

def get_depth(coin1="btc",coin2="usd",limit=150):
    response  = requests.get(f"https://yobit.net/api/3/depth/{coin1}_{coin2}?ignore_invalid=1&limit={limit}")
    bids = response.json()[f"{coin1}_{coin2}"]["bids"]
    total_bids_amount = 0

    for item in bids:
        coins_count = item[1]
        price_count = item[0]
        total_bids_amount += price_count * coins_count
    print(total_bids_amount)
    return total_bids_amount

def get_trades(coin1="btc",coin2="usd",limit=2000):
    response  = requests.get(f"https://yobit.net/api/3/trades/{coin1}_{coin2}?ignore_invalid=1&limit={limit}")
    total_bids = 0
    total_ask  = 0
    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "ask":
            total_ask += item["price"] * item["amount"]
        else:
            total_bids += item["price"] * item["amount"]
    info = f"Sell : {total_ask} \n Buy : {total_bids}"
    return info


def main():
    get_ticker()


if __name__ == "__main__":
    main()