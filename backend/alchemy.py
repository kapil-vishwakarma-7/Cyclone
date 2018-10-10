from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Text, Boolean

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost/whatsapp', echo=True)



class User_detail(Base):
	__tablename__ = 'user_detail'
	wid = Column(String(30), primary_key=True)
	lg = Column(String(5))

	serverToken = Column(String(100))
	lc =Column(String(5))
	ref = Column(String(70))
	platform = Column(String(30))
	battery = Column(Integer)
	tos = Column(Integer)
	secret = Column(String(200))
	pushname = Column(String(100))
	plugged = Column(Boolean)
	protoVersion = Column(String(10))
	connected = Column(Boolean)
	browserToken =Column(String(200)) 
	clientToken = Column(String(60))
	binVersion = Column(Integer)
	isResponse = Column(Boolean)
	
	phone_device_model = Column(String(20))
	phone_wa_version = Column(String(10))
	phone_mcc = Column(Integer)
	phone_os_version = Column(String(10))
	phone_os_build_number =Column(String(10))
	phone_device_manufacturer = Column(String(30))
	phone_mnc = Column(Integer)
	
	features_URL = Column(String(30))
	features_FLAGS = Column(String(30))

	login_info_clientId  =Column(String(50))
	login_info_serverRef = Column(String(200))
	login_info_privateKey = Column(String(100))
	login_info_encKey = Column(String(100))
	login_info_macKey = Column(String(100))

	conn_info_sharedSecret = Column(String(200))

	def __init__(self, wid , 	lg , 	serverToken , 	lc , 	ref , 	platform , 	battery , 	tos , 	secret , 	pushname , 	plugged , 	protoVersion , 	connected , 	browserToken , 	clientToken , 	binVersion , 	isResponse , 	phone_device_model , 	phone_wa_version , 	phone_mcc , 	phone_os_version , 	phone_os_build_number , 	phone_device_manufacturer , 	phone_mnc ,features_URL , 	features_FLAGS ,login_info_clientId  , 	login_info_serverRef , login_info_privateKey ,login_info_encKey ,login_info_macKey , conn_info_sharedSecret):
		self.wid = wid 
		self.lg = 	lg 
		self.serverToken = 	serverToken 
		self.lc = 	lc 
		self.ref = 	ref 
		self.platform = 	platform 
		self.battery = 	battery 
		self.tos = 	tos 
		self.secret = 	secret 
		self.pushname = 	pushname 
		self.plugged = 	plugged 
		self.protoVersion = 	protoVersion 
		self.connected = 	connected 
		self.browserToken = 	browserToken 
		self.clientToken = 	clientToken 
		self.binVersion = 	binVersion 
		self.isResponse = 	isResponse 
		self.phone_device_model = 	phone_device_model 
		self.phone_wa_version = 	phone_wa_version 
		self.phone_mcc = 	phone_mcc 
		self.phone_os_version = 	phone_os_version 
		self.phone_os_build_number = 	phone_os_build_number 
		self.phone_device_manufacturer = 	phone_device_manufacturer 
		self.phone_mnc = 	phone_mnc 
		self.features_URL = 	features_URL 
		self.features_FLAGS = 	features_FLAGS 
		self.login_info_clientId = 	login_info_clientId  
		self.login_info_serverRef = 	login_info_serverRef 
		self.login_info_privateKey = 	login_info_privateKey 
		self.login_info_encKey = 	login_info_encKey 
		self.login_info_macKey = 	login_info_macKey 
		self.conn_info_sharedSecret = 	conn_info_sharedSecret 



class contact(Base):
	__tablename__ = 'contact'
	id = Column(Integer,primary_key=True)
	wid = Column(String(30))
	jid = Column(String(30))
	notify = Column(String(100))
	name = Column(String(100))
	short = Column(String(100))
	vname = Column(String(100))
	verify = Column(Boolean)
	enterprise = Column(Boolean)

	def __init__(self,wid,jid,notify,name,short,vname,verify,enterprise):
		self.wid = wid
		self.jid =jid 
		self.notify =notify 
		self.name =name 
		self.short = short
		self.vname = vname
		self.verify =verify 
		self.enterprise =enterprise


class chat(Base):
	__tablename__ = 'chat'
	id = Column(Integer, primary_key=True)
	wid = Column(String(30))
	jid = Column(String(30))
	old_jid = Column(String(30))
	count = Column(String(30))
	mute = Column(String(20))
	spam = Column(Boolean)
	t = Column(String(10))
	message = Column(Boolean)
	modify_tag = Column(String(20))
	name = Column(String(100))

	def __init__(self,wid,jid,name,old_jid,count,mute,spam,t,message,modify_tag):
		self.wid =wid 
		self.jid = jid
		self.name =name 
		self.old_jid =old_jid 
		self.count =count 
		self.mute =mute 
		self.spam =spam 
		self.t = t
		self.message =message 
		self.modify_tag =modify_tag


class message(Base):
	__tablename__ = 'message'
	msg_id = Column(String(30),primary_key=True)
	wid = Column(String(30))
	remote_jid = Column(String(30))
	from_me = Column(Boolean)
	m_timestampe = Column(Boolean)
	status = Column(String(20))
	chat_type = Column(String(20))
	message_type = Column(String(20))
	context_participant = Column(String(30))
	context_stanza_id = Column(String(30))

Base.metadata.create_all(engine)