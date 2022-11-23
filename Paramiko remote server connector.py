import warnings
from cryptography.utils import CryptographyDeprecationWarning
import os

# Подтягивает переменные окружения из .bashrc;
# get() в случае отсутствия входящих данных выводит None вместо ошибки:

SSH_HOST = os.environ.get('SSH_HOST')
SSH_USERNAME = os.environ.get('SSH_USERNAME')
SSH_PKEY = os.environ.get('SSH_PKEY')
SSH_PORT = os.environ.get('SSH_PORT')
SSH_PORT = int(SSH_PORT)

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(SSH_HOST, SSH_PORT, username=SSH_USERNAME, key_filename=SSH_PKEY)

stdin, stdout, stderr = client.exec_command('ifconfig')
for y in stdout.readlines():
    print(y)

client.close()