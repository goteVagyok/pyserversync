# pyserversync
simple gui for rsync + cronie sync scheduling

---

## must have:
### 1. ssh config file

```
Host your-server-name (eg.: myserver)
	HostName    <ip or domain of server> (eg.: 192.168.100.1 or mydomain.tld)
	Port        <port for your ssh connection> (22 by default)
	User        <name of the user you would like to connect as>
	
	# optional: private key file for secured connections
	#IdentityFile ~/.ssh/id_rsa
```

### 2. rsync and cronie on your host, rsync on your server
