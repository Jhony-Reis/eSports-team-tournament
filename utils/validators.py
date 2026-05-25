class Validators:

    @staticmethod
    def validar_email(email: str):

        return "@" in email

    @staticmethod
    def validar_nickname(nickname: str):

        return len(nickname) >= 3