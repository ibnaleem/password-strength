class Password:
    def __init__(self):
        self._is_common = False
        
        def check(self, password: str):
          if self._common_check(password):
            return "Your password is very common and was found in a database. You should generate a more secure one"
          
        def _common_check(self, password: str) -> bool:
