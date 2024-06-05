import os
import tempfile

from mylogger.mylogger import MyStreamLogger, MyFileLogger


def test_streamlogger():

    sample_str = "sample"
    sample_int = 70
    sample_float = 3.14
    sample_bool = True
    sample_itr = ["a", "b", "c"]

    # ! 目視チェック

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


def test_filelogger():

    sample_str = "sample"
    sample_int = 70
    sample_float = 3.14
    sample_bool = True
    sample_itr = ["a", "b", "c"]

    with tempfile.TemporaryDirectory() as td:
        log_file_path = os.path.join(td, "temp.log")
        log_fl = MyFileLogger(log_file_path, "INFO")
        log_fl.info(sample_str)
        log_fl.info(sample_int)
        log_fl.info(sample_float)
        log_fl.info(sample_bool)
        log_fl.info(sample_itr)

        with open(log_file_path, "r") as f:
            log_list = f.readlines()

        assert sample_str in log_list[0]
        assert str(sample_int) in log_list[1]
        assert str(sample_float) in log_list[2]
        assert str(sample_bool) in log_list[3]
        assert str(sample_itr) in log_list[4]
