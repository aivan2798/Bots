from breaches import breache
def start(update,context):
  worm_hole_tag=update.effective_chat.id
  print(update)
  breacher_names=update.effective_chat.first_name
  if breacher_names=none:
  context.bot.send_message(chat_id=worm_hole_tag,text="Hello  вгεанд "+breacher_names+ ".\n\n Use the command /setup_breach to generate ur space_time breaching pass or command /breach breach_pass to breach the space_time fabric to another breacher😎")

def setup_breach(update,context):
  worm_hole_tag=update.effective_chat.id
  
  breacher_names=update.effective_chat.first_name
  breacher_uname=str(worm_hole_tag)+update.effective_chat.first_name
  to_breacher="nullified"
  breache().add_breacher(breacher_uname,worm_hole_tag,breacher_names,to_breacher)
  breacher_portal_link= breache().get_breacherlink(breacher_uname)
  context.bot.send_message(chat_id=worm_hole_tag,text="вгεанд "+breacher_names+ ".\n\n ur breach ticket is 👇🏾")
  context.bot.send_message(chat_id=worm_hole_tag,text=breacher_portal_link)
  
def breach(update, context):
  worm_hole_tag=update.effective_chat.id
  breacher_names=str(worm_hole_tag)+update.effective_chat.first_name
  print(update)
  breacher_portal=context.args[0]
  breache().set_tobreacher(breacher_names,breacher_portal)
  context.bot.send_message(chat_id=worm_hole_tag,text="вгεанд "+breacher_names+ ".\n\n Breach to "+breacher_portal+" is opening.\n. 🙌🏾")
  
def breach_ping(update, context):
    msg=update.message.text
    worm_hole_tag=update.effective_chat.id
    breacher_names=str(worm_hole_tag)+update.effective_chat.first_name
    to_portal=breache().get_tobreacher(breacher_names)
    print("breacher to_portal "+to_portal)
    from_portal=breache().get_frombreacher(to_portal)
    if from_portal==breache().get_breacherlink(breacher_names):
      breach_portal=breache().get_portal(to_portal)
      context.bot.send_message(chat_id=breach_portal[0],text=msg)
    else:
       context.bot.send_message(chat_id=worm_hole_tag,text="вгεанд zero.\n\n Breach isn't opened. 🙌🏾")
    
def close_breach(update,context):
     worm_hole_tag=update.effective_chat.id
     breacher_id=str(worm_hole_tag)+update.effective_chat.first_name
     breache().close_breache(breacher_id)
     context.bot.send_message(chat_id=worm_hole_tag,text="вгεacн "+breacher_id+" \n\n closed 🙆🏾‍♂️")
     print("closed breach")
     #context.bot.send_message(chat_id=worm_hole_tag,text="вгεаcн"+breacher_id+" closed. 🙌🏾")

def show_tag(update, context):
     worm_hole_tag=update.effective_chat.id
     breacher_id=str(worm_hole_tag)+update.effective_chat.first_name
     blink=breache().get_breacherlink(breacher_id)
     context.bot.send_message(chat_id=worm_hole_tag,text="Vibe message:.\n\n Breach tag is 👇🏾")
     context.bot.send_message(chat_id=worm_hole_tag,text=blink)
     