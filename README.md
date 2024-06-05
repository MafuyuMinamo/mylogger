# My logger

## Overview

概要

- print を使うよりも logging を使ったほうがスマートに処理できることが多いと思いますが、毎回 logging の設定をするコードをコピペするのは少し手間です。
- こういうものは自作のモジュールとしてまとめておけば便利ですよね。ということで、作りました。
- ログの中身に求められるものは、開発内容・規模・環境によって異なるようです。しかし、小規模な個人開発レベルであれば、次のような情報が付与されれば十分な気がします。

- ロガーのフォーマット（出力内容）
  - 実行日時
  - ロガーが呼ばれたソースファイルの名前（パス）と行数
  - ロガーが呼ばれた関数・メソッドの名前
  - ロガーのレベル（CRITICAL, ERROR, WARNING, INFO, DEBUG）
  - 任意のメッセージ

- 仕様的な話
  - logging root を汚さないように `logging.getLogger()` で作った枝葉で処理します。
  - コンソールへの出力、ファイルへの出力、両方に対応しています。

## Usage

使い方

### Installation

インストール方法

`pip install git+https://github.com/MafuyuMinamo/mylogger.git`

### class / method

#### class MyStreamLogger

- args
  - `set_level` (str, optional): "CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG" から選択
    - デフォルトは "DEBUG"

##### `debug`

- summary
  - ログを出力する
  - 設定レベル：DEBUG

- args
  - `msg` (Any): ログに出力する任意のメッセージ

##### `info`

- summary
  - ログを出力する
  - 設定レベル：INFO

- args
  - `msg` (Any): ログに出力する任意のメッセージ

##### `warning`

- summary
  - ログを出力する
  - 設定レベル：WARNING

- args
  - `msg` (Any): ログに出力する任意のメッセージ

##### `error`

- summary
  - ログを出力する
  - 設定レベル：ERROR

- args
  - `msg` (Any): ログに出力する任意のメッセージ

##### `critical`

- summary
  - ログを出力する
  - 設定レベル：CRITICAL

- args
  - `msg` (Any): ログに出力する任意のメッセージ

#### class MyFileLogger

- args
  - `log_file_path` (str): ログファイルのフルパス（ログの出力先）
  - `set_level` (str, optional): "CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG" から選択
    - デフォルトは "DEBUG"

- 各メソッドは `class MyStreamLogger` と同じなので割愛。
- `class MyFileLogger` の場合は、ターミナルと指定のログファイルの両方に出力される。

### Examples of use

コーディング例

```python
import os

from mylogger import MyStreamLogger, MyFileLogger


def example_streamlogger():

    sample_str = "sample"
    sample_int = 70
    sample_float = 3.14
    sample_bool = True
    sample_itr = ["a", "b", "c"]

    # * print の代替として
    print("\nAs an alternative to print.")
    log_st = MyStreamLogger()
    log_st.debug(sample_str)
    log_st.debug(sample_int)
    log_st.debug(sample_float)
    log_st.debug(sample_bool)
    log_st.debug(sample_itr)

    # * DEBUGレベルに設定した場合は、すべてのレベルが出力される
    log_st = MyStreamLogger("DEBUG")
    print("\nlevel=DEBUG: CRITICAL, ERROR, WARNING, INFO, DEBUG ")
    log_st.critical(sample_str)
    log_st.error(sample_str)
    log_st.warning(sample_str)
    log_st.info(sample_str)
    log_st.debug(sample_str)

    # * INFOレベルに設定した場合は、DEBUGレベルは出力されない
    # ? 例えば、デバッグが終わったら "DEBUG" から "INFO" に書き換えたりする
    log_st = MyStreamLogger("INFO")
    print("\nlevel=INFO: CRITICAL, ERROR, WARNING, INFO")
    log_st.critical(sample_str)
    log_st.error(sample_str)
    log_st.warning(sample_str)
    log_st.info(sample_str)
    log_st.debug(sample_str)


def example_filelogger():

    sample_str = "sample"
    sample_int = 70
    sample_float = 3.14
    sample_bool = True
    sample_itr = ["a", "b", "c"]

    td = r"C:\temp"
    log_file_path = os.path.join(td, "temp.log")
    log_fl = MyFileLogger(log_file_path, "INFO")
    log_fl.info(sample_str)
    log_fl.info(sample_int)
    log_fl.info(sample_float)
    log_fl.info(sample_bool)
    log_fl.info(sample_itr)


if __name__ == "__main__":

    example_streamlogger()
    example_filelogger()

```

コンソールの出力例

```text
As an alternative to print.
[2024-06-04 16:22:12,876] [Location >> examples_mylogger.py:17, function/method name: "example_streamlogger"] [DEBUG: Message >> sample]
[2024-06-04 16:22:12,877] [Location >> examples_mylogger.py:18, function/method name: "example_streamlogger"] [DEBUG: Message >> 70]
[2024-06-04 16:22:12,877] [Location >> examples_mylogger.py:19, function/method name: "example_streamlogger"] [DEBUG: Message >> 3.14]
[2024-06-04 16:22:12,877] [Location >> examples_mylogger.py:20, function/method name: "example_streamlogger"] [DEBUG: Message >> True]
[2024-06-04 16:22:12,877] [Location >> examples_mylogger.py:21, function/method name: "example_streamlogger"] [DEBUG: Iterator >> ['a', 'b', 'c']]

level=DEBUG: CRITICAL, ERROR, WARNING, INFO, DEBUG 
[2024-06-04 16:22:12,878] [Location >> examples_mylogger.py:26, function/method name: "example_streamlogger"] [CRITICAL: Message >> sample]       
[2024-06-04 16:22:12,878] [Location >> examples_mylogger.py:27, function/method name: "example_streamlogger"] [ERROR: Message >> sample]
[2024-06-04 16:22:12,878] [Location >> examples_mylogger.py:28, function/method name: "example_streamlogger"] [WARNING: Message >> sample]        
[2024-06-04 16:22:12,879] [Location >> examples_mylogger.py:29, function/method name: "example_streamlogger"] [INFO: Message >> sample]
[2024-06-04 16:22:12,879] [Location >> examples_mylogger.py:30, function/method name: "example_streamlogger"] [DEBUG: Message >> sample]

level=INFO: CRITICAL, ERROR, WARNING, INFO
[2024-06-04 16:22:12,879] [Location >> examples_mylogger.py:35, function/method name: "example_streamlogger"] [CRITICAL: Message >> sample]
[2024-06-04 16:22:12,880] [Location >> examples_mylogger.py:36, function/method name: "example_streamlogger"] [ERROR: Message >> sample]
[2024-06-04 16:22:12,880] [Location >> examples_mylogger.py:37, function/method name: "example_streamlogger"] [WARNING: Message >> sample]
[2024-06-04 16:22:12,880] [Location >> examples_mylogger.py:38, function/method name: "example_streamlogger"] [INFO: Message >> sample]
```

作成されたログファイルの例

```log
[2024-06-04 16:22:12,880] [Location >> c:\temp\examples_mylogger.py:53, function/method name: "example_filelogger"] [INFO: Message >> sample]
[2024-06-04 16:22:12,881] [Location >> c:\temp\examples_mylogger.py:54, function/method name: "example_filelogger"] [INFO: Message >> 70]
[2024-06-04 16:22:12,881] [Location >> c:\temp\examples_mylogger.py:55, function/method name: "example_filelogger"] [INFO: Message >> 3.14]
[2024-06-04 16:22:12,881] [Location >> c:\temp\examples_mylogger.py:56, function/method name: "example_filelogger"] [INFO: Message >> True]
[2024-06-04 16:22:12,881] [Location >> c:\temp\examples_mylogger.py:57, function/method name: "example_filelogger"] [INFO: Iterator >> ['a', 'b', 'c']]
```

### Uninstallation

アンイストール方法

`pip uninstall mylogger`

## Dependencies

依存関係の表記

- None
