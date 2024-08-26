class Machine:
    def __init__(self, item_list: dict[str, int]) -> None:
        self.item_list = item_list
        self.total_amount = 0

    def calc_total_amount(self, products: dict[str, int]) -> None:
        """
        課題１：ここを記述する。
        """
        raise NotImplementedError
    
    def display_total_amount(self) -> None:
        """
        課題１：ここを記述する。
        """
        raise NotImplementedError
    
    """
    課題2: 追加で関数を作成
    """
