import allure
import pytest
from Pages.BankingPage import Banking
import time
class TestBanking():
    @pytest.mark.test_tz
    def test_banking(self, fixtureSetup, get_env_options):
        self.driver = fixtureSetup
        self.driver.get(get_env_options['URL'])
        bn = Banking(self.driver)

        with allure.step("Выбираем user и нажимаем кнопку 'login'"):
            bn.SelectLoginAccount('Harry Potter')

        with allure.step("Находим число фиббоначи"):
            amount = bn.Fibbonachi()

        with allure.step("Вносим депозит"):
            bn.DepositNSum(amount)

        with allure.step("Вывод денег"):
            assert int(bn.WithdrawlNSum(amount)) == 0

        with allure.step("Заходим в транзакции, формируем csv отчет и добавляем в allure"):
            bn.TranzactionCheckAndScv()





