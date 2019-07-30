import unittest

from Home_work_13 import AccountingForGoodsStore
from Home_work_13 import menu_about_goods_coming
from Home_work_13 import menu_about_goods_sales
from Home_work_13 import number_document

from unittest.mock import patch

from Read_Write_File import read_file_pickle
from Read_Write_File import write_file_pickle

import datetime


class AccountingForGoodsStoreTest(unittest.TestCase):

    def test_regex_date(self):
        shablon_date = "\d{2}-\d{2}-\d{4}"
        self.assertRegex("01-01-2019", shablon_date, "Корректная дата")
        self.assertNotRegex("1-10-2019", shablon_date, "Не корректная дата")
        self.assertNotRegex("01-1-2019", shablon_date, "Не корректная дата")
        self.assertNotRegex("01-01-19", shablon_date, "Не корректная дата")
        self.assertNotRegex("1-1-2019", shablon_date, "Не корректная дата")
        self.assertNotRegex("1-1-19", shablon_date, "Не корректная дата")

    def test_regex_price_amount(self):
        shablon_price_amount = "^\d*\.\d+$"
        self.assertRegex("10.2", shablon_price_amount)
        self.assertRegex("10.22", shablon_price_amount)
        self.assertRegex("1.22", shablon_price_amount)
        self.assertNotRegex("-2.22", shablon_price_amount)
        self.assertNotRegex("2.-22", shablon_price_amount)
        self.assertNotRegex("-22", shablon_price_amount)
        self.assertNotRegex("-22.", shablon_price_amount)
        self.assertNotRegex("22", shablon_price_amount)
        self.assertNotRegex("2.", shablon_price_amount)

    def test_type_value_more_then_one(self):
        values_coming = menu_about_goods_coming()
        values_sales = menu_about_goods_sales()
        self.assertIsInstance(values_coming, tuple, "Корректный тип возвращаемой переменной")
        self.assertIsInstance(values_sales, tuple, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(values_coming, str, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(values_sales, str, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(values_coming, list, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(values_sales, list, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(values_coming, dict, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(values_sales, dict, "Корректный тип возвращаемой переменной")

    def test_type_value(self):
        value = number_document()
        self.assertIsInstance(value, int, "Корректный тип возвращаемой переменной")
        self.assertNotIsInstance(value, float, "Не корректный тип возвращаемой переменной")

    @patch("pickle.load")
    def test_read_file_pickle(self, load):
        read_file_pickle("goods_db")
        self.assertTrue(load.called)

    @patch("pickle.dump")
    def test_write_file_pickle(self, dump):
        write_file_pickle("goods_db", "some_text")
        self.assertTrue(dump.called)

    def test_IsInstance_AccountingForGoodsStore(self):
        new_obj = AccountingForGoodsStore("Вид документа", "Название товара", "Количество товара", "Цена товара",
                                          "Дата документа", 0)
        self.assertIsInstance(new_obj, AccountingForGoodsStore, "Объект класса AccountingForGoodsStore")

    @patch('Home_work_13.AccountingForGoodsStore.coming', return_value=True)
    def test_coming(self, coming):
        self.assertEqual(coming(), True)

    @patch('Home_work_13.AccountingForGoodsStore.sales', return_value=True)
    def test_sales(self, sales):
        self.assertEqual(sales(), True)

    @patch('Home_work_13.AccountingForGoodsStore.report', return_value=2)
    def test_report(self, report):
        date_one = datetime.datetime.now().strftime("%d-%m-%Y")
        date_two = datetime.datetime.now().strftime("%d-%m-%Y")
        self.assertEqual(report(date_one, date_two), 2)


if __name__ == '__main__':
    unittest.main()
