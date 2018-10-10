from alchemy import *
import alchemy

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

def get_value_by_index(data,index):
	try:
		val = str(data.get(index))
	except Exception as e:
		val = None
	finally:
		return val

loginInfo = {
		"clientId": None,
		"serverRef": None,
		"privateKey": None,
		"publicKey": None,
		"key": {
			"encKey": None,
			"macKey": None
		}
	};
connInfo = {
		"clientToken": None,
		"serverToken": None,
		"browserToken": None,
		"secret": None,
		"sharedSecret": None,
		"me": None
	};
def insert_user(obj,wid,login_info,conn_info):
	data = obj[1]
	lg = get_value_by_index(data,"lg")

	server_token = get_value_by_index(data,"serverToken")
	lc = get_value_by_index(data,"lc")
	ref = get_value_by_index(data,"ref")
	platform = get_value_by_index(data,"platform")
	battery = int(get_value_by_index(data,"battery"))
	tos = int(get_value_by_index(data,"tos"))
	secret = get_value_by_index(data,"secret")
	pushname = get_value_by_index(data,"pushname")
	plugged = bool(get_value_by_index(data,"plugged"))
	proto_version = get_value_by_index(data,"protoVersion")
	connected = bool(get_value_by_index(data,"connected"))
	browser_token =get_value_by_index(data,"browserToken")
	client_token = get_value_by_index(data,"clientToken")
	bin_version = int(get_value_by_index(data,"binVersion"))
	is_response = bool(get_value_by_index(data,"isResponse"))
	
	phone_device_model = get_value_by_index(data["phone"],"device_model")
	phone_wa_version = get_value_by_index(data["phone"],"wa_version")
	phone_mcc = int(get_value_by_index(data["phone"],"mcc"))
	phone_os_version = get_value_by_index(data["phone"],"os_version")
	phone_os_build_number =get_value_by_index(data["phone"],"os_build_number")
	phone_device_manufacturer = get_value_by_index(data["phone"],"device_manufacturer")
	phone_mnc = int(get_value_by_index(data["phone"],"mnc"))
	
	features_URL = get_value_by_index(data["features"],"URL")
	features_FLAGS = get_value_by_index(data["features"],"FLAGS")

	login_info_clientId   = get_value_by_index(login_info,"clientId")
	login_info_serverRef  = get_value_by_index(login_info,"serverRef")
	login_info_privateKey = get_value_by_index(login_info,"privateKey")
	login_info_encKey     = get_value_by_index(login_info['key'],"encKey")
	login_info_macKey     = get_value_by_index(login_info['key'],"macKey")

	conn_info_sharedSecret = get_value_by_index(conn_info,"sharedSecret")
	user = User_detail( wid , 	lg , 	server_token , 	lc , 	ref , 	platform , 	battery , 	tos , 	secret , 	pushname , 	plugged , 	proto_version , 	connected , 	browser_token , 	client_token , 	bin_version , 	is_response , 	phone_device_model , 	phone_wa_version , 	phone_mcc , 	phone_os_version , 	phone_os_build_number , 	phone_device_manufacturer , 	phone_mnc ,features_URL , 	features_FLAGS ,login_info_clientId  , 	login_info_serverRef , login_info_privateKey ,login_info_encKey ,login_info_macKey , conn_info_sharedSecret)
	print(user)

	session = Session()
	session.add(user)
	session.commit()

def insert_contact(obj,wid):
	# contacts = obj[2]
	contacts = obj
	session = Session()	

	for contact in contacts:
		contact = contact[1]
		jid = get_value_by_index(contact,"jid")
		notify = get_value_by_index(contact,"notify")
		name = get_value_by_index(contact,"name")
		short = get_value_by_index(contact,"short")
		vname = get_value_by_index(contact,"vname")
		verify = bool(get_value_by_index(contact,"verify"))
		enterprise = bool(get_value_by_index(contact,"enterprise"))
		con = alchemy.contact(wid,jid,notify,name,short,vname,verify,enterprise)
		session.add(con)
	session.commit()

def insert_chat(obj,wid):
	chats = obj[2]
	session = Session()	
	for contact in chats:
		contact = contact[1]
		jid = get_value_by_index(contact,"jid")
		old_jid = get_value_by_index(contact,"old_jid")
		count = get_value_by_index(contact,"count")
		mute = get_value_by_index(contact,"mute")
		spam = bool(get_value_by_index(contact,"spam"))
		t = get_value_by_index(contact,"t")
		message = bool(get_value_by_index(contact,"message"))
		modify_tag = get_value_by_index(contact,"modify_tag")
		name = get_value_by_index(contact,"name")
		chat = alchemy.chat(wid,jid,name,old_jid,count,mute,spam,t,message,modify_tag)
		session.add(chat)
	session.commit()



def insert_message(obj,wid):
	pass

def decode_message_media(message):
	pass

# systemctl start mariadb.service