from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        service = ServiceUser()
        response_assert = "Usuário adicionado!"

        response = service.add_user("renatão", "development")

        assert response_assert == response

    def test_add_user_invalid_name(self):
        service = ServiceUser()
        response_assert = "Usuário adicionado!"

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
