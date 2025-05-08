from datetime import datetime


class InscritData:
    def __init__(self, nom, email, telephone, profession, date_inscription=None):
        self.nom = nom
        self.email = email
        self.telephone = telephone
        self.profession = profession
        self.date_inscription = date_inscription or datetime.now()

    def __str__(self):
        return f"{self.nom} ({self.profession}) - {self.email}"


