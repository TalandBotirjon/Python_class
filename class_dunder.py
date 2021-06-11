"""
* TalandBotirjon
* classlarni kengroq yoritish
* 11.06.2021
"""
class Shaxs():
    """Shaxs  classi """
    __num_shaxs = 0
    def __init__(self, ism, familya, password, tgyil ):
        self.ism = ism.title()
        self.familya = familya.title()
        self.password = password.upper()
        self.tgyil = tgyil
        Shaxs.__num_shaxs +=1
    def __repr__(self):
        """Shaxs opekti chaqirilganda umumiy ma'lumot qaytaradi."""
        return f"{self.ism} {self.familya} {self.tgyil}-yili tug'ilgan."

    def get_shaxs(self):
        """Shaxs haqida to'liq ma'lumot beradigan funksiya"""
        return f"{self.ism} {self.familya} {self.tgyil}-yili tug'ilgan. Password raqami: " \
               f"{self.password}"



class Talaba(Shaxs):
    """Talaba classi"""
    __num_tal = 0
    def __init__(self, ism, familya, password, tgyil, tal_ID):
        super(Talaba, self).__init__(ism, familya, password, tgyil)
        self.talID = tal_ID
        self.bosqich = 1
        Talaba.__num_tal += 1

    def set_bos(self, son):
        """Talaba bosqichini o'zgartirishga imkon beradigan funksiya """
        self.bosqich = son

    def __repr__(self):
        """Talaba obyektinni chaqirganda u haqida umumiy malumot qaytaradi."""
        return f"Talaba {self.ism.title()} {self.familya.title()}. {self.bosqich}-bosqich talabasi."

    def __lt__(self, other):
        """Talaba obyektlarini bosqichi bo'yicha katta kichikligini tekshirishga imkon beradi >>> talaba1>talaba2"""
        if isinstance(other, Talaba):
            return self.bosqich<other.bosqich

    def __eq__(self, other):
        """Talaba obyektlarini bosqichi bo'yicha tengligini tekshirishga imkon beradi >>> talaba1==talaba2"""
        if isinstance(other, Talaba):
            return self.bosqich == other.bosqich

    def get_talaba(self):
        """Talaba obyekti haqida to'liq ma'lumot qaytaradi."""
        talaba = "Talaba "
        talaba+= self.get_shaxs()
        talaba += f". Talabalik ID: {self.talID}, {self.bosqich}-bosqich talabasi."
        return talaba


class Fan():
    """Fan classi talabalarni o'z ichiga qamrab olib talabani o'chirishi ham mumkin."""
    __num__Fan = 0
    def __init__(self, fanname, fankafedra):
        self.fanname = fanname.title()
        self.fankafedra = fankafedra.title()
        self.talabalar = []
        Fan.__num__Fan += 1

    def __repr__(self):
        """Fan obyektini chaqirganimizda u haqida umumiy malumot qaytarish uchun."""
        return f"{self.fankafedra} kafedrasi {self.fanname} fani."

    def add_student(self, *Other):
        """Fan obyektiga add_student() funksiyasi orqali talaba qo'shish mumkin."""
        for other in Other:
            if isinstance(other, Talaba):
                self.talabalar.append(other)
            else:
                print("Talaba classiga oid obekt yuboring.")

    def __len__(self):
        """Fanlar obyektidagi talabalar sonini qaytaradi."""
        return len(self.talabalar)

    def __getitem__(self, item):
        """Fan obyektiga index bo'yicha murojatni taminlaydi."""
        return self.talabalar[item]

    def __setitem__(self, key, value):
        """Fan obyektidagi talabalar ro'yhatidan birorta qiymatini o'zgartirish imkonini beradi.
        Agar yangi Talaba qo'shmoqchi bo'lsangiz add_studend() methodi bor. """
        if isinstance(value, Talaba):
            self.talabalar[key] = value

    def __add__(self, *other):
        """fan obyektiga + qilib yangi talaba qo'shish uchun yordam beradigan funksiya."""
        for oth in other:
            if isinstance(oth, Talaba):
                self.talabalar.append(oth)

    def get_fan(self):
        """Fanlar obyekti ichidagi ma'lumotlarni chiqaradi."""
        return f"{self.fankafedra} kafedrasi {self.fanname} fani." \
               f"\n Talabalar: {self.talabalar}"

    @classmethod
    def get_num_fanlar(cls):
        return cls.__num__Fan


shaxs1 = Shaxs("Botirjon", "ergashov", "ab5968116",1999)
#print(shaxs1.get_shaxs())
#print(shaxs1)

talaba1= Talaba( "Botirjon", 'Ergashov', "ab5968116", 1999, 4151817 )
talaba2= Talaba( "Shaxzod", 'Ergashev', "aa5968116", 1999, 4152117 )
talaba3= Talaba( "Shermuhammad", 'Mardanov', "aa45965116", 1997, 4151805 )
talaba4= Talaba( "Kumush", 'Jumanazarova', "ab4517864", 2001, 4151819 )
talaba1.set_bos(2)
#print(talaba1.get_talaba())
#print(talaba1>talaba2)

fan1 = Fan('Dasturlash', 'Dasturiy injenering')
fan1.add_student(talaba1)
fan1.add_student(talaba3)
fan1+talaba2
fan1+talaba4

#print(fan1[:])
#print(fan1.get_fan())
