import telegram.ext as tele
import wormholes

def vibes():
 bot_token="your_bot_token"
 worm_holes=tele.Updater(token=bot_token,use_context=True)

 viber=worm_holes.dispatcher
 worm_hole_start=tele.CommandHandler("start",wormholes.start)
 setup=tele.CommandHandler("setup_breach",wormholes.setup_breach)
 show_tag=tele.CommandHandler("show_ticket",wormholes .show_tag)
 close_breach=tele.CommandHandler("close_breach",wormholes.close_breach)
 breach=tele.CommandHandler("breach",wormholes.breach)

 breach_msg=tele.MessageHandler(tele.Filters.text & (~tele.Filters.command),wormholes.breach_ping)


 viber.add_handler(breach_msg)
 viber.add_handler(close_breach)
 viber.add_handler(show_tag)
 viber.add_handler(worm_hole_start)
 viber.add_handler(breach)
 viber.add_handler(setup)

 worm_holes.start_polling()
 
 vibes()