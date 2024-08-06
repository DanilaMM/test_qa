import csv
import datetime
import time

import pytest
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import allure

class Banking(BasePage):
    customer_login_button = (By.XPATH, "//div[@class='center']/button[@ng-click='customer()']")
    user_select = (By.XPATH, "//select[@name='userSelect']")
    button_login = (By.XPATH, "//button[text()='Login']")

    button_tranzaction = (By.XPATH, "//button[@ng-click='transactions()']")
    button_deposit = (By.XPATH, "//button[@ng-click='deposit()']")
    button_withdrawl = (By.XPATH, "//button[@ng-click='withdrawl()']")

    balance_count = (By.XPATH, '//strong[@class="ng-binding"][2]')

    input_amount = (By.XPATH, "//form/div/input")
    submit_depozit_or_withdrawl = (By.XPATH, "//form/button")


    def __init__(self, driver):
        super().__init__(driver)

    def SelectLoginAccount(self, name):
        BasePage.ClickActionClicable(self, element=self.customer_login_button)
        BasePage.ClickActionClicable(self, element=(By.XPATH, f"//select/option[text()='{name}']"))
        BasePage.ClickActionClicable(self, element=self.button_login)

    def Fibbonachi(self):
        current_date = datetime.datetime.now()
        day_of_month = current_date.day
        def fibonacci(day_of_month):
            if day_of_month <= 0:
                return 0
            elif day_of_month == 1:
                return 1
            else:
                return fibonacci(day_of_month - 1) + fibonacci(day_of_month - 2)

        result = fibonacci(day_of_month+1)
        return result

    def DepositNSum(self, amount):
        BasePage.ClickActionClicable(self, element=self.button_deposit)
        BasePage.TypeTextAction(self, element=self.input_amount, text=amount)
        BasePage.ClickActionClicable(self, element=self.submit_depozit_or_withdrawl)

    def WithdrawlNSum(self,amount):
        BasePage.ClickActionClicable(self, element=self.button_withdrawl)
        time.sleep(1)
        BasePage.TypeTextAction(self, element=self.input_amount, text=amount)
        BasePage.ClickActionClicable(self, element=self.submit_depozit_or_withdrawl)
        return BasePage.GetElementText(self, element=self.balance_count)


    def TranzactionCheckAndScv(self):
        BasePage.ClickActionClicable(self, element=self.button_tranzaction)
        keys = ["date","amount","type"]
        values = []
        for i in [1,2]:
            list = []
            for j in [1,2,3]:
                list.append(BasePage.GetElementText(self, (By.XPATH, f'//tbody/tr[{i}]/td[{j}]')))
            values.append(list)

        dictionaries = []
        for value_set in values:
            dictionary = {keys[i]: value_set[i] for i in range(len(keys))}
            dictionaries.append(dictionary)

        def create_csv_file(filename, transactions):
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Дата-времяТранзакции", "Сумма", "ТипТранзакции"])
                for transaction in transactions:
                    writer.writerow([transaction["date"], transaction["amount"], transaction["type"]])

        csv_filename = "transactions.csv"
        create_csv_file(csv_filename, dictionaries)

        with open(csv_filename, "rb") as file:
            allure.attach(file.read(), name="transactions.csv", attachment_type=allure.attachment_type.CSV)
