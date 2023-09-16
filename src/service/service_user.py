from src.models.store import Store
from src.models.user import User

class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if type(name) != str or type(job) != str:
            return "Usuário não adicionado"

        ja_existe = len(self.search_user(name)) > 0
        if ja_existe:
            return "Usuário não adicionado"

        user = User(name, job)
        self.store.bd.append(user)

        return "Usuário adicionado!"

    def search_user(self, name):
        return list(filter(lambda user: user.name == name, self.store.bd))

    def remove_user(self, name):
        if type(name) != str:
            return "Nome inválido"

        listUser = self.search_user(name)
        if len(listUser) == 0:
            return "Não existe usuário com esse nome"

        user = listUser[0]
        self.store.bd.remove(user)
        return "Usuário removido!"

    def update_user(self, name, job): #atualizando job
        if type(name) != str:
            return "Nome inválido"

        if type(job) != str:
            return "Job inválido"

        user = self.search_user(name)[0]
        return user.job

    def get_user_by_name(self, name):
        if type(name) != str:
            return "Nome inválido"

        listUser = self.search_user(name)
        if len(listUser) == 0:
            return "Não existe usuário com esse nome"

        user = listUser[0]
        return user.job
