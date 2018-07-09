#  SUGGESTIONS ====  Add colors to the table,
# adjust width to fit numbers in a better way

from beautifultable import BeautifulTable
from operator import itemgetter
import requests
import pprint


def mk_list(codes,c_list):
    for key in codes.keys():
        inner = codes[key]
        price = inner["quotes"]["USD"]
        info  = {
            "name" : inner['name'],
            "rank" : inner['rank'],
            "symbol":inner["symbol"],
            "circulating_supply":inner["circulating_supply"],
            'price' : price["price"],
            "volume": price["volume_24h"],
            "market cap": price["market_cap"],
            "percent_1hr" : price["percent_change_1h"],
            "percent_24h": price["percent_change_24h"],
            "percent_7d" : price["percent_change_7d"]
          } 
        c_list.append(info)

    newlist = sorted(c_list, key=itemgetter('rank'))
    return newlist

# making the table
def mk_table(newlist):
    table = BeautifulTable()
    table.column_headers = ["S.No", "Name", "Symbol", "Market cap", "price", "Circulating Supply","Volume (24h)","% 1h","%24 h","% 7d"]
    for i,item in enumerate(newlist):
        table.append_row([i+1, newlist[i]["name"],newlist[i]["symbol"],newlist[i]["market cap"],
                                    newlist[i]["price"],newlist[i]["circulating_supply"],newlist[i]["volume"],
                                    newlist[i]["percent_1hr"],newlist[i]["percent_24h"],newlist[i]["percent_7d"]])

    table.left_border_char = '|'
    table.right_border_char = '|'
    table.top_border_char = '='
    table.bottom_border_char = '='
    table.header_separator_char = '='
    table.row_separator_char = '='
    table.intersection_char = '|'
    table.column_separator_char = '|'
    return table

def do_crypto():
    url = ('https://api.coinmarketcap.com/v2/ticker/?limit=10')
    res= requests.get(url)
    dic = res.json()
    codes= dic['data']
    c_list = []
    newlist = mk_list(codes,c_list)
    table = mk_table(newlist)
    BeautifulTable.WEP_WRAP
    print(table) 