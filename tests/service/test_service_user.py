from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        service = ServiceUser()
        response_assert = "Usuário adicionado!"

        response = service.add_user("renatão", "development")

        assert response_assert == response

    def test_add_user_invalid_name(self):
        service = ServiceUser()
        response_assert = "Usuário não adicionado"

        response = service.add_user(None, "development")

        assert response_assert == response

    def test_add_user_invalid_job(self):
        service = ServiceUser()
        response_assert = "Usuário não adicionado"

        response = service.add_user("renatão", None)

        assert response_assert == response

    def test_add_user_just_exist(self):
        service = ServiceUser()
        response_assert = "Usuário já existe"

        service.add_user("renatão", "development")
        response = service.add_user("renatão", "development")

        assert response_assert == response

    def test_search_user(self):
        pass

    def test_remove_user(self):
        service = ServiceUser()
        name_user = "renatão"
        response_assert = "Usuário removido!"

        service.add_user(name_user, "development")
        response = service.remove_user(name_user)

        assert response_assert == response

    def test_remove_user_name_invalid(self):
        service = ServiceUser()
        response_assert = "Nome inválido"

        response = service.remove_user(None)

        assert response_assert == response

    def test_remove_user_dont_exist(self):
        service = ServiceUser()
        response_assert = "Não existe usuário com esse nome"

        response = service.remove_user("renatão")

        assert response_assert == response

    def test_update_user(self):
        service = ServiceUser()
        name_user = "renatão"
        response_assert = "Job de usuário atualizado"

        service.add_user(name_user, "development")
        response = service.update_user(name_user, "jardineiro")

        assert response_assert == response

    def test_update_user_invalid_name(self):
        service = ServiceUser()
        response_assert = "Nome inválido"

        response = service.update_user(None, "jardineiro")

        assert response_assert == response

    def test_update_user_invalid_job(self):
        service = ServiceUser()
        response_assert = "Job inválido"

        response = service.update_user("renatão", None)

        assert response_assert == response

    def test_update_user_doesnt_exist(self):
        service = ServiceUser()
        response_assert = "Não existe usuário com esse nome"

        response = service.update_user("carina", "jardineira")

        assert response_assert == response

