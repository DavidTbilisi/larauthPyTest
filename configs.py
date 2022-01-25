import configparser
config = configparser.ConfigParser()
config.read('app.conf')

user = config.get("USER", 'email') 
password = config.get("USER","password")
website = config.get("WEBSITE", 'host') + ":" + config.get("WEBSITE","port")
root_dir = config.get("WEBSITE","root_dir")
migration_start = config.get("MIGRATION","start")
migration_end = config.get("MIGRATION","end")
wait = int(config.get("TIMING","time"))