                          # Dokumentacja Projektu: System Zamawiania Transportu
 
## Opis wzorca Factory Method
Wzorzec Factory Method (Metoda Fabrykująca) został użyty, aby oddzielić logikę tworzenia obiektów transportu (Bike, Scooter, Taxi) od klienta. Klient używa warstwy pośredniej (usług) i nie musi wiedzieć, jak dokładnie instancjonowane są pojazdy.
 
## Opis modułów
* **customer.py**: Zawiera klasę klienta inicjującego proces zamawiania.
* **services.py**: Moduł fabryki. Definiuje wspólny interfejs usług oraz konkretne podklasy odpowiadające za zwracanie właściwych pojazdów i zarządzanie statusem dostępności.
* **transport.py**: Posiada abstrakcyjną klasę bazową pojazdu oraz klasy konkretnych środków transportu (Bike, Scooter, Taxi).
 
## Opis klas
* `Customer`: Przechowuje nazwę klienta i deleguje zlecenie do serwisów.
* `TransportServices` (oraz klasy pochodne): Szablon zawierający logikę sprawdzania dostępności (`available`) i metodę fabrykującą `create_transport()`.
* `Transport` (oraz klasy pochodne): Przechowuje dane o typie pojazdu, czasie przyjazdu i długości podróży.
 
## Instrukcja uruchomienia
1. Sklonuj repozytorium.
2. Uruchom plik `main.py` poleceniem: `python main.py`.
3. Aby uruchomić testy jednostkowe, wpisz polecenie: `python -m unittest test_main.py`.
 
## Przykłady działania programu
Po uruchomieniu `main.py` program najpierw sprawdza flagę `available`. Jeśli wynosi ona `True`, wyświetla dane pojazdu i zmienia status na `False`. Przy ponownej próbie zamówienia tego samego pojazdu, system zwraca komunikat o błędzie informujący o braku dostępności.