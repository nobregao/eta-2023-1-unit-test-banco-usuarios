from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()

print(service.add_user("ermeson", "qa"))
print(service.add_user(None, "consultor"))
print(service.add_user("renatão", None))
print(service.add_user(0, "consultor"))
print(service.add_user("camila", 0))

print(service.add_user("carina", "development"))

print(service.store.bd)

# print(service.remove_user("carina"))
#
# print(service.store.bd)

print(service.store.bd[0].job)

print(service.update_user("renatão", "jardineiro"))

print(service.store.bd[0].job)