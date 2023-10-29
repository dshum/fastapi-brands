from sshtunnel import SSHTunnelForwarder

from lib import settings

server = SSHTunnelForwarder(
    ssh_address_or_host=settings.ssh.URL,
    ssh_username=settings.ssh.USER,
    ssh_pkey=settings.ssh.KEY,
    ssh_private_key_password=settings.ssh.SECRET,
    remote_bind_address=(settings.ssh.PRIVATE_SERVER, 5432),
    local_bind_address=("localhost", 6432)
)
