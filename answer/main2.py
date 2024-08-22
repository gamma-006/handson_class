"""
課題2: 課題1に習って、mainファイルを作成
"""
import os
from machine import Machine
from utils import load_json, save_dict_to_json

def main():
    # 商品と購入物のファイル名
    item_table_name = "item_table_1.json"
    products_name = "products_table_1.json"
    money_name = "money_1.json"
    # 読み込みのためのパスの設定
    current_dir = os.getcwd()
    item_table_path = current_dir + "/data/in/item_tables/" + item_table_name
    product_table_path = current_dir + "/data/in/shopping_data/" + products_name
    money_path = current_dir + "/data/in/money_data/" + money_name
    # データの読み込み
    item_table = load_json(item_table_path)
    products = load_json(product_table_path)
    money = load_json(money_path)
    # マシンのインスタンス化
    machine = Machine(item_table)
    # 購入物の計算
    machine.calc_total_amount(products)
    # 金額の表示
    machine.display_total_amount()
    # おつりの計算
    machine.calc_change(money)
    # お釣りに必要な紙幣と硬貨を数える
    machine.count_change()
    # おつりの紙幣と硬貨の枚数を
    change_dict = machine.output_change()
    # jsonへ書き出し
    output_path = current_dir + "/data/out/change.json"
    save_dict_to_json(change_dict, output_path)
    

if __name__ == "__main__":
    main() 