class Machine:
    def __init__(self, item_list: dict[str, int]) -> None:
        self.item_list = item_list
        self.total_amount = 0

    def calc_total_amount(self, products: dict[str, int]) -> None:
        """
        課題１：ここを記述する。
        """
        for item_name, num_of_items in products.items():
            self.total_amount += self.item_list[item_name] * num_of_items

    def display_total_amount(self) -> None:
        """
        課題１：ここを記述する。
        """
        print(self.total_amount)

    """
    課題2: 追加で関数を作成
    """

    def calc_change(self, money: dict[int, int]) -> int:
        """
        お釣りを計算するメソッド
        """
        self.received = 0
        for price, count in money.items():
            self.received += int(price) * count
        self.change = self.received - self.total_amount

    def count_change(self) -> None:
        """
        お釣りに必要な紙幣と硬貨の枚数を計算します。
        """
        denominations = [5000, 1000, 500, 100, 50, 10, 5, 1]
        self.money_dict = {}

        for denomination in denominations:
            if self.change >= denomination:
                self.money_dict[str(denomination)] = self.change // denomination
                self.change %= denomination

    def output_change(self) -> dict[int, int]:
        """
        count_changeで数えたお釣りを出力します。
        """
        return self.money_dict
