import os
from mega import Mega


login = os.environ.get("mega_login")
password = os.environ.get("mega_pass")

mega = Mega()

m = mega.login(login, password)

try:
    file = m.find("docs.zip")
    m.rename(file, "666.zip")
except:
    pass

file = m.upload("docs.zip")