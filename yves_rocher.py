import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#potrzebne do przesuniecia pod element
from selenium.webdriver.common.action_chains import ActionChains


# DANE TESTOWE
imie = "Anna"
nazwisko = "Kowalska"
email= "a.kowalska@gmail.com"
haslo = "Alorax6!@"
nrtelefonu = "602550602"
plec = "kobieta"
niepoprawny_email = "a.kowalska.gmail.com"

# Szablon testu
class MojTest(unittest.TestCase):

    # setUp -> test... -> tearDown
    # Przygotowanie testu
    # Przed każdym testem
    def setUp(self):
        # print("Przygotowanie testu")
        # Tutaj otowrzymy przeglądarkę
        self.driver = webdriver.Chrome()
        # Na stronie wizzaira
        self.driver.get("https://www.yves-rocher.pl/#/")
        # Maksymalizacja okna
        self.driver.maximize_window()
        # ustaw mechanizm bezwarunkowegonrtelefonu czekania na elementy
        # na max 60 sekund
        self.driver.implicitly_wait(60)

    # Po każdym teście
    def tearDown(self):
        # print("'Sprzątanie' po teście"nrtelefonu)
        # Wyłączymy przegladarkę
        self.driver.quit()

    # Właściwe testy (metody zaczynajace się od słowa test)
    def testInvalidEmail(self):
        driver = self.driver
        # KROK 1: KLIKNIJ ZALOGUJ
        # Metody find_element_ zwracają obiekt klasy WebElement
        zaloguj_btn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div[3]/a/span')
        zaloguj_btn.click()

        # KROK 2 Kliknij Rejestracja
        rejestracja_btn = driver.find_element_by_css_selector('a[data-registration-url="/customer/register"]')
        rejestracja_btn.click()

        
        # KROK 3. Wpisz imię
        imie_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[1]/div[1]/span/input')
        imie_input.send_keys(imie)
        # KROK 4. Wpisz nazwisko
        nazwisko_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[1]/div[2]/span/input')
        nazwisko_input.send_keys(nazwisko)
        # KROK 5. Wpisz niepoprawny email
        email_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[1]/div[3]/span/input')
        email_input.send_keys(niepoprawny_email) 
        # KROK 7. Wpisz hasło
        password_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[1]/div[4]/span/input')
        password_input.send_keys(haslo)
        # KROK 6. Wpisz numer telefonu
        phone_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[1]/div[5]/span/input')
        phone_input.send_keys(nrtelefonu)
        # KROK 7. Kliknij RAkceptuj cookies
        cookies_btn = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
        cookies_btn.click()

        # KROK 8. Przewijanie strony
     
        # zgoda2_btn.location_once_scrolled_into_view
        
        element_zoom = driver.find_element_by_xpath('//*[@id="page-register-form"]/div[1]/div[3]/div[3]/div/button')
        # przesun sie pod element ktory jest na niewidocznej czesci strony 
        action = ActionChains(driver)
        action.move_to_element(element_zoom).click().perform() 

        # KROK 8. Wybierz płeć
        if plec == "kobieta":
            # Kliknij w pani
            female_label = driver.find_element_by_css_selector('input[id="female"]')                 
            #nazwisko_input.click()
            female_label.click()
        else:
            # Kliknij mezczyzna
            male_label = driver.find_element_by_css_selector('input[id="male"]')
            #imie_input.click()
            male_label.click()
        # KROK 9. Kliknij zgode 1
        zgoda1_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[3]/div[5]/span/div/label/span[3]')
        zgoda1_btn.click()
        # KROK 10. Kliknij zgode 2
        zgoda2_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[3]/div[6]/span/div/label/span[3]')
        zgoda2_btn.click()
        # KROK 11. Kliknij zaloz konto
        zaloz_konto_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div[3]/div/button')
        zaloz_konto_btn.click()

        ### UWAGA! TUTAJ BĘDZIE TEST !!! ###
        # SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # Wyszukujemy wszystkie możliwe błędy
        error_notices = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/span/div[1]/div[3]/span/span')
        # Tworzymy pustą listę na widoczne błędy
        visible_error_notices = []
        # Dla każego błędu w liście error_notices
        for error in error_notices:
        # Jeśli błąd jest widoczny
            if error.is_displayed():
        # ..dodaję tekst tego błędu do listy widocznych błędów
                visible_error_notices.append(error.text)
        # Porównuję listę widocznych błędów z oczekiwaną listą widocznych błędów
        # (Sprawdzam, czy widoczny jest tylko błąd "Nieprawidłowy adres e-mail")

        print("na stronie widnieją następujące błędy: ", visible_error_notices)
        ## PRAWDZIWY TEST - SPRAWDZENIE REZULTATU ##
        # ===================================================================================
        # "Czysty Python"
        # assert visible_error_notices == ["Proszę podać prawidłowy adres e-mail."], "Nie zgadzają się wyświetlane błędy"
        # Asercja z wykorzystaniem metody zawartej w klasie TestCase
        # self.assertListEqual(visible_error_notices, ["Proszę podać prawidłowy adres e-mail."], msg="Nie zgadzają się wyświetlane błędy")
        # ===================================================================================





        # Poczekaj ze 3 sekundy, żebym zdążył zobaczyć co się stało
        sleep(3)



# Uruchomienie testu
# Czy uruchamiamy program z tego pliku
if __name__ == "__main__":
    unittest.main(verbosity=2)