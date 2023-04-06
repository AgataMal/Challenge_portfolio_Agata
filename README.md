# Zadanie 1: Konfiguracja oprogramowania.
## Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?"
---
Podczas urlopu macierzyńskiego :family_woman_girl_boy: , podjęłam decyzję o zmianie swojej ścieżki zawodowej i obrałam kierunek IT. :smile: Na początku skoncentrowałam swoje siły na testowaniu manualnym, kończąc różne kursy i zdobywając certyfikat ISTQB. Testowanie manualne naprawdę mi się spodobało, aczkolwiek w międzyczasie zaczełam się interesować także automatyzacją testów. W związku z tym, postanowiłam poszerzeć swoją dotychczasową więdzę i pójść właśnie w tym kierunku. Jeżeli chodzi o język programowania, zaczełam od Pythona, dlatego bardzo spodobało mi się, że w Wyzwaniu będziemy używać właśnie tego języka. Liczę, że dzięki udziałowi w Wyzwaniu, zdobędę nowe umiejętności oraz usystematyzuję swoją dotychczasową wiedzę, otrzymując feedback od Mentorów (a to jest dla mnie bardzo ważne). Jestem bardzo zdeterminowana. :muscle:

# Zadanie 2:
## Podzadanie 2: Wyszukiwanie selektorów na stronie logowania.
--- 
### Lista elementów:
#### pole do wpisywania "login"
##### XPATH

```
//*[@id="login"]
//input[@id="login"]
//input[@id="login" and @type="text"]
//form//input[@id="login" and @type="text"]
```

#### pole do wpisywania "password"
##### XPATH
```
//*[@id="password"]
//input[@id="password"]
//input[@id="password" and @type="password"]
//form//input[@id="password" and @type="password"]

```
#### przycisk "SIGN IN"
##### XPATH
```
//form//button[@type="submit"]
//form//button[@type="submit" and ./span[contains(text(), SIGN-IN)]]
```
#### dropdown z wyborem języka
##### XPATH
#### link do odzyskiwania hasła "remind password"
##### XPATH


