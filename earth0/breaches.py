import sqlite3
from cryptography.fernet import Fernet

class breache:
  
  def __init__(self):
    trash="hello"
    breachy=sqlite3.connect("breaches.db")
    breachy.execute("CREATE TABLE IF NOT EXISTS breach_list(ID INT IDENTITY(1000,1) PRIMARY KEY,BREACHER_ID TEXT NOT NULL,BREACHER_CHAT_ID TEXT NOT NULL,BREACHER_NAMES,BREACHER_LINK TEXT NOT NULL,TO_BREACHER TEXT NOT NULL)")
    breachy.commit()
    breachy.close()
  def getkey(self):
    file = open('vibekey.key', 'rb')  # Open the file as wb to read bytes
    key = file.read()  # The key will be type bytes
    file.close()
    return key
    
  def add_breacher(self,breacher_id,breacher_chat_id,breacher_names,to_breacher):
    breachy=sqlite3.connect("breaches.db")
    keyenc=Fernet(self.getkey())
    breacher_link_temp=keyenc.encrypt(breacher_id.encode())
    breacher_link=breacher_link_temp.decode('utf-8')
    #[0:6]
    exec_str=f"INSERT INTO breach_list (BREACHER_ID,BREACHER_CHAT_ID,BREACHER_NAMES,BREACHER_LINK,TO_BREACHER) VALUES ('{breacher_id}','{breacher_chat_id}','{breacher_names}','{breacher_link}','{to_breacher}' )"
    print(exec_str)
    breachy.execute(exec_str)
    breachy.commit()
    breachy.close()
  
  def set_tobreacher(self,breacher_id,end_breacher):
   breachy=sqlite3.connect("breaches.db")
   exec_str=f"UPDATE breach_list SET TO_BREACHER = '{end_breacher}' WHERE BREACHER_ID = '{breacher_id}'"
   print(exec_str)
   breachy.execute(exec_str)
   breachy.commit()
   breachy.close()
  
  def get_portal(self,breacher_link):
    breachy=sqlite3.connect("breaches.db")
    exec_str=f"SELECT BREACHER_CHAT_ID,BREACHER_NAMES from breach_list WHERE BREACHER_LINK = '{breacher_link}'"
 #   breachy=sqlite3.connect("breaches.db")
    exec_data=breachy.execute(exec_str).fetchone()
    breachy.commit()
    breachy.close()
    return exec_data
  
  def set_breacher_link(self,breacher_id):
    breachy=sqlite3.connect("breaches.db")
    breacher_link=""
    exec_str=f"UPDATE breach_list SET BREACHER_LINK = '{breacher_link}' WHERE BREACHER_ID = '{breacher_id}'"
    exec_data=breachy.execute(exec_str)
    breachy.close()
  
  
  def get_tobreacher(self,breacherid):
    breachy=sqlite3.connect("breaches.db")
    exec_str=f"SELECT TO_BREACHER from breach_list WHERE BREACHER_ID = '{breacherid}'"
  #  breachy=sqlite3.connect("breaches.db")
    exec_data=breachy.execute(exec_str).fetchone()
    breachy.commit()
    breachy.close()
    return exec_data[0]
    
  def get_frombreacher(self,breacherlink):
    breachy=sqlite3.connect("breaches.db")
    exec_str=f"SELECT TO_BREACHER from breach_list WHERE BREACHER_LINK = '{breacherlink}'"
   # breachy=sqlite3.connect("breaches.db")
    exec_data=breachy.execute(exec_str).fetchone()
    breachy.commit()
    breachy.close()
    return exec_data[0]
    
    
  def get_breacherlink(self,breacherid):
    breachy=sqlite3.connect("breaches.db")
    exec_str=f"SELECT BREACHER_LINK from breach_list WHERE BREACHER_ID = '{breacherid}'"
  #  breachy=sqlite3.connect("breaches.db")
    exec_data=breachy.execute(exec_str).fetchone()
    breachy.commit()
    breachy.close()
    return exec_data[0]
    
  def close_breache(self,breacherid):
    breachy=sqlite3.connect("breaches.db")
    exec_str=f"DELETE FROM breach_list WHERE BREACHER_ID = '{breacherid}'"
  #  breachy=sqlite3.connect("breaches.db")
    breachy.execute(exec_str)
    breachy.commit()
    breachy.close()