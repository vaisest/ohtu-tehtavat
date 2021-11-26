class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetti ei ole tyyppiä int tai se on negatiivinen")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kasvatuskoko ei ole tyyppiä int tai se on negatiivinen")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukulista = [0 for _ in range(0, self.kapasiteetti)]

        self.indeksi = 0

    def kuuluu(self, n):
        for luku in self.lukulista:
            if n == luku:
                return True

        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukulista[self.indeksi] = n
            self.indeksi = self.indeksi + 1

            if self.indeksi == (len(self.lukulista) - 1):
                self.lukulista += [0 for _ in range(0, self.kasvatuskoko)]
            return True
        return False

    def poista(self, n):
        n_indeksi = -1
        for i, luku in enumerate(self.lukulista):
            if n == luku:
                n_indeksi = i

        if n_indeksi == -1:
            return False

        # otetaan siis slicellä sama lukujono, mutta poistettava n jää pois
        self.lukulista = self.lukulista[0:n_indeksi] + self.lukulista[n_indeksi + 1 :]
        self.indeksi -= 1

        return True

    def kopioi_taulukko(self, a, b):
        # tarpeeton?
        # Ei edessä alaviivaa, joten en poista
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.indeksi

    def to_int_list(self):
        return self.lukulista[0 : self.indeksi]

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()

        for luku in a.to_int_list():
            yhdiste_joukko.lisaa(luku)

        for luku in b.to_int_list():
            yhdiste_joukko.lisaa(luku)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()

        a_set = set(a.to_int_list())
        b_set = set(b.to_int_list())

        # & on leikkaus
        for luku in list(a_set & b_set):
            leikkaus_joukko.lisaa(luku)

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()

        for luku in a.to_int_list():
            erotus_joukko.lisaa(luku)

        for luku in b.to_int_list():
            erotus_joukko.poista(luku)

        return erotus_joukko

    def __str__(self):
        string_lista = [str(luku) for luku in self.to_int_list()]
        return "{" + ", ".join(string_lista) + "}"
