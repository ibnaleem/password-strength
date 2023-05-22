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
        self._count += unique_count / 2        
          
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
