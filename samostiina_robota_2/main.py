from abc import ABC, abstractmethod


class Personal(ABC):
    @abstractmethod
    def rozrahuvaty_zarplatu(self):
        pass


class Spivrobitnyk(Personal):
    __slots__ = (
        "_imya",
        "_zarobitna_plata",
        "_kilkist_vidpratsovanyh_dniv",
        "_vidsotok_bonusa",
    )

    def __init__(self, imya, zarobitna_plata, kilkist_vidpratsovanyh_dniv, vidsotok_bonusa=0):
        self.imya = imya
        self.zarobitna_plata = zarobitna_plata
        self.kilkist_vidpratsovanyh_dniv = kilkist_vidpratsovanyh_dniv
        self.vidsotok_bonusa = vidsotok_bonusa

    @property
    def imya(self):
        return self._imya

    @imya.setter
    def imya(self, value):
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        self._imya = value

    @property
    def zarobitna_plata(self):
        return self._zarobitna_plata

    @zarobitna_plata.setter
    def zarobitna_plata(self, value):
        if value < 0:
            raise ValueError("Заробітна плата не може бути від'ємною")
        self._zarobitna_plata = value

    @property
    def kilkist_vidpratsovanyh_dniv(self):
        return self._kilkist_vidpratsovanyh_dniv

    @kilkist_vidpratsovanyh_dniv.setter
    def kilkist_vidpratsovanyh_dniv(self, value):
        if value < 0 or value > 30:
            raise ValueError("Кількість відпрацьованих днів повинна бути від 0 до 30")
        self._kilkist_vidpratsovanyh_dniv = value

    @property
    def vidsotok_bonusa(self):
        return self._vidsotok_bonusa

    @vidsotok_bonusa.setter
    def vidsotok_bonusa(self, value):
        if value < 0:
            raise ValueError("Відсоток бонуса не може бути від'ємним")
        self._vidsotok_bonusa = value

    def rozrahuvaty_zarplatu(self):
        return (self.zarobitna_plata / 30) * self.kilkist_vidpratsovanyh_dniv

    def rozrahuvaty_bonus(self):
        return (self.rozrahuvaty_zarplatu() / 100) * self.vidsotok_bonusa


class Menedzher(Spivrobitnyk):
    __slots__ = ("_kilkist_pidleglyh",)

    rozmir_premii = 500

    def __init__(
        self,
        imya,
        zarobitna_plata,
        kilkist_vidpratsovanyh_dniv,
        vidsotok_bonusa=0,
        kilkist_pidleglyh=0,
    ):
        super().__init__(imya, zarobitna_plata, kilkist_vidpratsovanyh_dniv, vidsotok_bonusa)
        self.kilkist_pidleglyh = kilkist_pidleglyh

    @property
    def kilkist_pidleglyh(self):
        return self._kilkist_pidleglyh

    @kilkist_pidleglyh.setter
    def kilkist_pidleglyh(self, value):
        if value < 0:
            raise ValueError("Кількість підлеглих не може бути від'ємною")
        self._kilkist_pidleglyh = value

    def report(self):
        return f"Менеджер {self.imya} керує {self.kilkist_pidleglyh} співробітниками."

    def rozrahuvaty_bonus(self):
        osnovnyi_bonus = super().rozrahuvaty_bonus()
        premiya_za_pidleglyh = self.kilkist_pidleglyh * Menedzher.rozmir_premii

        return osnovnyi_bonus + premiya_za_pidleglyh


def pokazaty_informatsiyu(personal):
    print(f"Ім'я: {personal.imya}")
    print(f"Місячна зарплата: {personal.rozrahuvaty_zarplatu():.2f} грн")
    print(f"Бонус: {personal.rozrahuvaty_bonus():.2f} грн")

    if isinstance(personal, Menedzher):
        print(personal.report())

    print()


spysok_personalu = [
    Spivrobitnyk("Олена", 30000, 20, 10),
    Spivrobitnyk("Іван", 24000, 15, 5),
    Menedzher("Марія", 45000, 22, 12, 4),
    Menedzher("Андрій", 60000, 25, 8, 6),
]

print("Розрахунок зарплати та бонусів:")
print()

for pratsivnyk in spysok_personalu:
    pokazaty_informatsiyu(pratsivnyk)
