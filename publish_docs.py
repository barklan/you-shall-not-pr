import os
from mega import Mega


login = os.environ.get("mega_login")
password = os.environ.get("mega_pass")

mega = Mega()

m = mega.login(login, password)

# file = m.find('index.html')
# m.rename(file, 'my_file.doc')

file = m.upload("zipped.zip")