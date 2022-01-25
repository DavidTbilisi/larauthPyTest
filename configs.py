import configparser
config = configparser.ConfigParser()
config.read('app.conf')

user = config.get("USER", 'email') 
password = config.get("USER","password")
website = config.get("WEBSITE", 'host') + ":" + config.get("WEBSITE","port")
root_dir = config.get("WEBSITE","root_dir")
mstart = config.get("MIGRATION","start")