from src.models.store import Store
from src.models.user import User

class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if type(name) != str or type(job) != str:
            return "Usuário não adicionado"

        user = self.search_user(name)
        if user != None:
            return "Usuário já existe"

        user = User(name, job)
        self.store.bd.append(user)

        return "Usuário adicionado!"

    def search_user(self, name):
        users = list(filter(lambda user: user.name == name, self.store.bd))
        if len(users) > 0:
            return users[0]
        return None

    def remove_user(self, name):
        if type(name) != str:
            return "Nome inválido"

        user = self.search_user(name)
        if user == None:
            return "Não existe usuário com esse nome"

        self.store.bd.remove(user)
        return "Usuário removido!"

    def update_user(self, name, job):
        if type(name) != str:
            return "Nome inválido"

        if type(job) != str:
            return "Job inválido"

        user = self.search_user(name)
        if user == None:
            return "Não existe usuário com esse nome"

        user.job = job

        return "Job de usuário atualizado"

    def get_user_by_name(self, name):
        if type(name) != str:
            return "Nome inválido"

        user = self.search_user(name)
        if user == None:
            return "Não existe usuário com esse nome"

        return user.job
