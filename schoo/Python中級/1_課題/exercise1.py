"""作成するツール
想定イメージ: あなたは経理担当です。毎月社員から送られてくるタイムカード Excelファイルを、
必要なシートだけまとめて1つのExcelファイルにしたいと考えています。

以下を一連で行うツールを作成してください：
- あるフォルダの中にあるExcelファイル一覧を取得
- 各Excelファイル内の特定シートのみ取得
- 取得したシートを一つのExcelファイルにして保存
"""

# あるフォルダの中にあるExcelファイル一覧を取得
# 標準ライブラリ
import os

# 外部ライブラリ
import pandas as pd
from pathlib import Path


def get_file_list(dir_path) -> list[str]:
    """フォルダの中にあるExcelファイル一覧を取得"""

    input_path = Path(dir_path)
    # ファイル名を取得する
    file_list = [
        f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))
    ]
    # 一応拡張子がxlsxだけに絞る
    xlsx_file_list = [xf for xf in file_list if xf.endswith(".xlsx") == True]
    return xlsx_file_list


# メイン処理
def main():
    dir_path = "schoo/Python中級/1_課題/input"
    xlsx_file_list = get_file_list(dir_path)
    print(xlsx_file_list)


if __name__ == "__main__":
    main()


# 残タスク
# 各Excelファイル内の特定シートのみ取得
# 取得したシートを一つのExcelファイルにして保存
