from bot.chat import check_chat
from bot.pm import check_pm
from bot.logger import add_post

import random, unidecode, sys, time, string

import vk

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def start():
    auth()
    time.sleep(0.5)
    mess_receive()
    
def auth():
    tkn = 'lol'
    session = vk.Session(access_token = tkn)
    global api
    api = vk.API(session)
    add_post('Authorized successfully')

def mess_receive():

    lastmessid = 0
    global messcnt
    global do_response
    do_response = True
    messcnt = 20

    while True:
        try:
            response = api.messages.get(count = messcnt, time_offset = 10, last_message_id = lastmessid, out = 0)
            if len(response) > 1:
                                        #util
                if response[1]['uid'] == 187906747 and 'bot_t' in response[1]['body']:
                    if response[1]['body'] == 'bot_t -h':
                        hhh_msg = '''     [Admin commands]
use 'bot_t %admin_command%' form to call admin commands\n
-h: help\n-s: stop\n-p: pause\n-r: release\n-l: leave_chat if exists or raise KeyException'''
                        api.messages.send(chat_id = response[1]['chat_id'],message = hhh_msg)
                    elif response[1]['body'] == 'bot_t -s':
                        sys.exit(0)
                    elif response[1]['body'] == 'bot_t -p':
                        add_post('#pause |\n       V')
                        do_response = False
                    elif response[1]['body'] == 'bot_t -r':
                        add_post('#release |\n         V')
                        do_response = True
                    elif response[1]['body'] == 'bot_t -l':
                        api.messages.removeChatUser(chat_id = response[1]['chat_id'],user_id = '371041508')

                if response[1]:
                    lastmessid = response[1]['mid']

                    for item in range(1, len(response)):
                        try:
                            uid = str(response[item]['uid'])
                            chatid = -1
                            try:
                                chatid = response[item]['chat_id']
                            except KeyError:
                                pass
                            if chatid == -1:
                                if uid == '187906747':
                                    add_post('> ' + response[item]['body'].translate(non_bmp_map) + ' ' + '(uid = id187906747)(admin)')
                                else:
                                    add_post('> ' + response[item]['body'].translate(non_bmp_map) + ' ' + '(uid = ' + uid + ')')
                                if do_response == True:
                                    check_pm(api,response[item])
                            else:
                                if uid == '187906747':
                                    add_post('> ' + response[item]['body'].translate(non_bmp_map) + ' ' +'(chat_id = ' + str(chatid)+ ', uid = id187906747)(admin)')
                                else:
                                    add_post('> ' + response[item]['body'].translate(non_bmp_map) + ' ' +'(chat_id = '+str(chatid)+ ', uid = ' + uid + ')')
                                if do_response == True:
                                    check_chat(api,response[item])
                        except IndexError:
                            pass
                    api.messages.markAsRead(message_ids = response[item]['mid'])

        except vk.exceptions.VkAPIError:
            pass
        except Exception:
            add_post('Runtime error')
        time.sleep(0.5)
