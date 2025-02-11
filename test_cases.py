#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

    # 1. 有効な入力値
    def test_sample01(self):
        self.assertEqual(1, calc(1, 1))  # 最小の正の整数

    def test_sample02(self):
        self.assertEqual(999 * 999, calc(999, 999))  # 最大の正の整数

    def test_sample03(self):
        self.assertEqual(500 * 20, calc(500, 20))  # 任意の正の整数

    # 2. 無効な入力値
    def test_sample04(self):
        self.assertEqual(-1, calc(0, 10))  # ゼロを含む

    def test_sample05(self):
        self.assertEqual(-1, calc(-1, 5))  # 負の整数

    def test_sample06(self):
        self.assertEqual(-1, calc(0.1, 10))  # 小数

    def test_sample07(self):
        self.assertEqual(-1, calc('a', 'b'))  # 文字列

    def test_sample08(self):
        self.assertEqual(-1, calc(None, 2))  # None

    # 3. 境界値テスト
    def test_sample09(self):
        self.assertEqual(-1, calc(0, 1))  # 境界値：ゼロ

    def test_sample10(self):
        self.assertEqual(-1, calc(-1, 1))  # 境界値：負の数

    def test_sample11(self):
        self.assertEqual(-1, calc(1000, 1000))  # 上限超え

    # 4. アンダーフロー・オーバーフローの入力テスト
    def test_sample12(self):
        self.assertEqual(-1, calc(10**18, 10**18))  # 乗算が非常に大きい数

    def test_sample13(self):
        self.assertEqual(-1, calc(-10**18, 10**18))  # 乗算で極端に小さい値

    # 5. 整数でない値の入力テスト
    def test_sample14(self):
        self.assertEqual(-1, calc(0.1, 5))  # 小数を入力

    def test_sample15(self):
        self.assertEqual(-1, calc("hello", 3))  # 文字列を入力

    # 6. ヌルのインプットテスト
    def test_sample16(self):
        self.assertEqual(-1, calc(None, 2))  # None を渡す

