from schema.database.data_storage import storage
from schema.user import User

storage.restart()
inst = storage.get_user_by_email(User, 'colinatjku@gmail.com')
print(inst.to_dict()) if inst else print(None)