"""
    Opiskelija lisää/poista/etsi/listaa

    On asennettava ekaksi pymongo 
    Kirjoitetaan tätä varten terminaaliin " sudo pip install pymongo " ja se hoitaa loput. 
    Löytyy tietokanta nimeltään db_students, ja on collection nimeltään student. 
"""
from pymongo import MongoClient

db = MongoClient(host='localhost', port=62091)['db_students']
table = db['student']


def AddStudent():
    hetu = int(input("Opiskelijan hetu: "))
    etunimi = input("Opiskelijan etuimi: ")
    sukunimi = input("Opiskelijan sukunimi: ")

    table.insert({"hetu": int(hetu), "etunimi": etunimi, "sukunimi": sukunimi})
    for i in table.find({"hetu": int(hetu)}):
        print(
            """ --- Opiskelija lisätty ---
                   hetu  : {}
                   etunimi      : {}
                   sukunimi   : {}""".format(i['hetu'], i['etunimi'], i['sukunimi']))


def DeleteStudent():
    hetu = int(input("Kirjoita opiskelijan hetu, joka haluat poistaa: "))

    for i in table.find({"hetu": int(hetu)}):
        print(
            """ --- Opiskelijan tiedot on poistettu. ---
               hetu  : {}
               etunimi      : {}
               sukunimi   : {}""".format(i['hetu'], i['etunimi'], i['sukunimi']))

    table.delete_one({"hetu": hetu})


def SearchStudent():
    hetu = int(input("Kirjoita opiskelijan hetu, joka haluat etsiä: "))

    table.find({"hetu": hetu})
    for i in table.find({"hetu": int(hetu)}):
        print(
            """ --- Opiskelijan tiedot löytyi. ---
                   hetu  : {}
                   etunimi      : {}
                   sukunimi   : {}""".format(i['hetu'], i['etunimi'], i['sukunimi']))


def ListStudents():
    tulos = table.find()
    for (a, i) in enumerate(tulos):
        print(
            """
                   --- {} ---
                   hetu  : {}
                   etunimi      : {}
                   sukunimi   : {} """.format(a, i['hetu'], i['etunimi'], i['sukunimi']))


def main():
    print(
        """
           Opiskelijan Rekisteröinti Järjestelmä
       
           1 - Lisää opiskelija
           2 - Etsi Opiskelijaa
           3 - Poista Opiskelija
           4 - Listaa Opiskelijoita
           """)
    valinta = int(input("Mitä Haluat Tehdä: "))
    while True:
        if valinta == 1:
            AddStudent()
            break
        if valinta == 2:
            SearchStudent()
            break
        if valinta == 3:
            DeleteStudent()
            break
        if valinta == 4:
            ListStudents()
            break


if __name__ == '__main__':
    main()
