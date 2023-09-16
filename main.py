from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()

print(service.add_user("renatão", "development"))
print(service.add_user(None, "consultor"))
print(service.add_user("renatão", None))
print(service.add_user(0, "consultor"))
print(service.add_user("renatão", 0))

print(service.add_user("renatão", "development"))

print(service.store.bd)

print(service.remove_user("renatão"))

print(service.store.bd)