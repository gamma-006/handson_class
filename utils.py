import json
import os


def load_json(file_path: str) -> dict:
    """
    JSONファイルを読み込んで辞書にする関数
    """
    with open(file_path) as f:
        load_data = json.load(f)
    return load_data


def save_dict_to_json(data: dict, filename: str) -> None:
    """
    辞書をJSONファイルに書き出す関数
    """
    # ディレクトリが存在しない場合は作成
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # JSONファイルに書き出し
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)
