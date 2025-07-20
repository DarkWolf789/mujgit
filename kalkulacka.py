"""

class Kalkulacka:
    def secti(self,a,b):

        '''
        Metoda pro sečtení dvou čísel
        Args:
            a (int, float): První číslo.
            b (int, float): Druhé číslo.
            Returns: Vrátí výsledek sčítání

        '''
        
        return a+b

    def odecti(self,a,b):

        '''
        Metoda pro odčítání dvou čísel
        Args:
            a (int, float): První číslo.
            b (int, float): Druhé číslo.
            Returns: Vrátí výsledek odčítání

        '''
        return a-b

    def vynasob(self,a,b):

        '''
        Metoda pro násobení dvou čísel
        Args:
            a (int, float): První číslo.
            b (int, float): Druhé číslo.
            Returns: Vrátí výsledek násobení

        '''

        return a*b



    def vydel(self,a,b):

    '''
        Metoda pro dělení dvou čísel
        Args:
            a (int, float): První číslo.
            b (int, float): Druhé číslo.
            Returns: Vrátí výsledek dělení.
        Raises:
            ValueError: "Dělení nulou není povoleno".

    '''

        if b == 0:
            raise ValueError("Dělení nulou není povoleno.")
        return a / b

"""

class ValidatorHesla:

    def validuj(self, heslo):
        if len(heslo) <= 5:
            return False
        for znak in heslo:
            if '0' <= znak <= '9':
                return True
        return False
