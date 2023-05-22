import requests
import hashlib

class Password:
    def __init__(self):
        self._is_common = False
        self._count = 0
 
    def check(self, password: str):
        if self._common_check(password):
            return "Your password is very common and was found in a database. You should generate a more secure one"
        unique_count = self._check_special_character_diversity(password)
        digit_count = self._check_digit(password)
        caseCount = self._case_count(password)
        self._count += unique_count / 2
        self._count += len(password) / 2
        self._count += digit_count / 2
        self._count += caseCount[0] / 2
        self._count += caseCount[1] / 2
        
        if self._count == 13:
            return "Your password is very strong and was not found in a database"
        elif 13 > self._count > 10:
            return "Your password is strong and was not found in a database"
        elif 10 > self._count > 8:
            return "Your password is moderate. Try using a diverse range of numbers, case letters and symbols.
        else:
            return "Your password is weak. Try using symbols, case letters and numbers
    
    def _common_check(self, password: str) -> bool:
        hash_pswd = self._hash(password)
        url = f"https://api.pwnedpasswords.com/range/{hash_pswd}"
        response = requests.get(url)

        if response.status_code == 200:
            self._is_common = True

        return self._is_common

    def _hash(self, password: str) -> str:
        h = hashlib.new('sha1')
        h.update(str(password).encode()) 
        return h.hexdigest()
        
    def _check_special_character_diversity(self, password) -> int:
        special_characters = "!@#$%^&*()_+{}[]|;:,.<>/?"
        symbols = [char for char in password if char in special_characters]
        unique_symbols_count = len(set(symbols))
        return unique_symbols_count

    def _check_digits(self, password) -> int:
      count = 0
      for i in password:
        count+=1

      return count

    def _case_count(password) -> list:
      upperCount = 0
      lowerCount = 0

      for i in password:
        if i.isupper():
          upperCount += 1

        if i.islower():
          lowerCount += 1

      return [upperCount, lowerCount]
