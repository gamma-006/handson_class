class Machine:
    def __init__(self, item_list: dict[str, int]) -> None:
        self.item_list = item_list
        self.total_amount = 0
        self.money_count = 0

    def calc_total_amount(self, products: dict[str, int]) -> None:
        """
        課題１：ここを記述する。
        """

        for item_name, item_amount in products.items():
            self.total_amount += self.item_list[item_name] * item_amount


    def display_total_amount(self) -> None:
        """
        課題１：ここを記述する。
        """
        print('total_amount:', self.total_amount)

    """
    課題2: 追加で関数を作成
    """

    def change_count(self, money_list: dict[str, int]):
        # お釣りの計算
        for change_name, count in money_list.items():
            self.money_count += int(change_name) * count
            if self.money_count >= self.total_amount:
                change = self.money_count - self.total_amount
                
        print('money:', self.money_count)
        print('change :', change)

        # お釣りの紙幣と硬貨をカウント
        self.change_dict = {}
        change_new = change
        
        for change_name, i in money_list.items():
            change_count = change_new // int(change_name)
            self.change_dict.update({change_name: change_count})
            change_new = change_new % int(change_name)


        return self.change_dict