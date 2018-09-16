# industrielldesign.no
Ny nettside til Leonardo, linjeforeningen for studentene ved industriell design ved NTNU i Trondheim.:boom::blue_heart:

## Oppsett for utviklere :sunglasses::

1. Installer python 3 <= 3.6
2. Installer pip3
3. Klon git-repositoren noe sted på maskina
4. Installer virtualenv
5. Sett opp et virtualenv i samme mappe som du lagret klonen i. Gjøres i terminal med `virtualenv webbaENV`
```
Nettside
  |
  |-- industrielldesign.no
  |
  |-- webbaENV // Virtualenv
  |
```
6. Aktiver `webbaENV` med kommandoen `source webbaENV/bin/activate`
7. Gå inn i mappen industrielldesign.no og kjør `pip3 install -r requirements.txt`
8. Nå kjør et par kommandoer for å sette opp database:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
9. Kjør serveren med `python manage.py runserver` :muscle:
10. Nettsiden finner du da på `localhost:8000`
