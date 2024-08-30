"""
課題2: 課題1に習って、mainファイルを作成
"""
import os
from machine import Machine
from utils import load_json
from utils import save_dict_to_json


def main():
    # 商品と購入物のファイル名
    item_table_name = "item_table_1.json"
    products_name = "products_table_1.json"
    money_name = "money_1.json"
    # 読み込みのためのパスの設定
    current_dir = os.getcwd()
    item_table_path = current_dir + "/handson_class/data/in/item_tables/" + item_table_name
    product_table_path = current_dir + "/handson_class/data/in/shopping_data/" + products_name
    money_table_path = current_dir + "/handson_class/data/in/money_data/" + money_name
    # データの読み込み
    item_table = load_json(item_table_path)
    products = load_json(product_table_path)
    money_list = load_json(money_table_path)

    # マシンのインスタンス化
    machine = Machine(item_table)
    # 購入物の計算
    machine.calc_total_amount(products)
    # 金額の表示
    machine.display_total_amount()

    # 書き込みのためのパスの設定
    change_table_path = current_dir + "/handson_class/data/out/change.json"
    # データの書き込み
    data = machine.change_count(money_list)
    save_dict_to_json(data, change_table_path)
    print('change dict:', data)
    

if __name__ == "__main__":
    main()
