from bot.ListsChat import getCmds, getLolwhat, getFuckyou, getZhebit, getHelpText
from bot.logger import add_post

import random, unidecode, sys, time, string, math
import vk

def check_chat(api,msg):

    prefixes = ['tolya','tolyan','anatoliy','anatoly',u'толян',u'толя',u'анатолий',
                'tolya,','tolyan,','anatoliy,','anatoly,',u'толян,',u'толя,',u'анатолий,']

    cmds =  getCmds()
    lolwhat = getLolwhat()
    fuckyou = getFuckyou()
    zhebit  = getZhebit()
    help_text = getHelpText()

    words = msg['body'].split()

    if words[0].lower() in prefixes:
        if len(words) > 1 and words[1] in cmds:
        #start_commands
                                        #utility
            if words[1].lower() == u'ливни' and msg['uid'] == 187906747:
                add_post(u'#ливни-админ')
                api.messages.send(chat_id = msg['chat_id'],message = 'ok(')
                api.messages.removeChatUser(chat_id = msg['chat_id'],user_id = '371041508')
                                        #user
            if words[1].lower() == u'помощь' or words[1].lower() == u'help':
                help_text = getHelpText()
                api.messages.send(chat_id = msg['chat_id'],message = help_text)

            if words[1].lower() == u'съеби' or words[1].lower() == u'пиздуй' or words[1].lower() == u'уйди' or words[1].lower() == u'ливни' and msg['uid'] != 187906747:
                add_post(u'#ливни')
                api.messages.send(chat_id = msg['chat_id'],message = u'ладно, только отвали от меня')
                api.messages.removeChatUser(chat_id = msg['chat_id'],user_id = '371041508')
                time.sleep(3)
                api.messages.send(chat_id = msg['chat_id'],message = u'ха наебал')

            if words[1].lower() == u'видос':
                add_post('#видос')
                if len(words) > 2:
                    request = msg['body'][msg['body'].find(words[1]) + len(words[1]) + 1:]
                    try:
                        video = api.video.search(q = request, count = 1, offset = random.randint(0,30))[0]
                    except IndexError:
                        api.messages.send(chat_id = msg['chat_id'],forward_messages = msg['mid'],message = u'Одно из двух: либо ты криворукое и скудоумное уёбище, что не может нормально напечатать запрос, либо ты ещё и поехавшее уёбище, у которого заросы ебанутее, чем русские панки')
                        return
                    att = 'video' + str(video['owner_id']) + '_' + str(video['id'])
                    api.messages.send(chat_id = msg['chat_id'],forward_messages = msg['mid'],attachment = att)
                else:
                    api.messages.send(chat_id = msg['chat_id'],forward_messages = msg['mid'],message = u'я понимаю, что у тебя много дел, но вынужден сообщить, что я не могу искать видео по пустому запросу, а ты не можешь не соснуть мой длинный хуй, тупорылое ты животное, для кого здесь команда "помощь"?')

            if words[1].lower() == u'расписание':
                api.messages.send(chat_id = msg['chat_id'],forward_messages = msg['mid'],message = u'1. География подлости\n2. Орфография ненависти\n3. Апология невежества\n4. Мифология оптимизма\n5. Законы гаубицы благонравия\n6. Знатное пиршество благоразумия')

            if words[1].lower() == u'админ':
                add_post("#админ")
                try:
                    if msg['admin_id'] == msg['uid']:
                        api.messages.addChatUser(chat_id = msg['chat_id'], user_id = '187906747')
                        api.messages.send(chat_id = msg['chat_id'],message = u'на, подавись')
                    else:
                        api.messages.send(chat_id = msg['chat_id'],message = u'тебя это не касается, чмо')
                except vk.exceptions.VkAPIError:
                    api.messages.send(chat_id = msg['chat_id'],message = u'это ж каким надо быть тупым говном, чтобы вызывать команду, которую невозможно выполнить. иди нахуй. просто иди нахуй')

            if words[1].lower() == 'zhebit':
                add_post(u'#лол жебит')
                chat_users = api.messages.getChat(chat_id = msg['chat_id'])['users']
                print(chat_users)
                if 274081163 in chat_users:
                    api.messages.send(chat_id = msg['chat_id'],message = u'это что вообще за команда, идиотина?', forward_messages = msg['mid'])
                else:
                    api.messages.send(chat_id = msg['chat_id'],message = zhebit[random.randint( 0,len(zhebit)-1 )])

            if words[1].lower() == u'анек':
                try:
                    add_post(u'#анек')
                    anek = api.wall.get(owner_id = '-85443458', count = 1, offset = random.randint(0,127))[1]['text']
                    api.messages.send(chat_id = msg['chat_id'],message = anek,forward_messages = msg['mid'])

                except IndexError:
                    pass

            if words[1].lower() == u'юмореска':
                try:
                    add_post(u'#юмореска')
                    num = api.wall.get(owner_id = '-92876084',count = 0)[0]
                    anek = api.wall.get(owner_id = '-92876084', count = 1, offset = random.randint(0,num - 1))[1]['text']
                    api.messages.send(chat_id = msg['chat_id'],message = anek,forward_messages = msg['mid'])
                except IndexError:
                    pass

            if words[1].lower() == u'пикрандом' or words[1].lower() == 'picrandom':
                print(u'#пикрандом')
                Sent = False
                while Sent is False:
                    num = api.wall.get(owner_id = '-122615111',count = 0)[0]
                    pic = api.wall.get(owner_id = '-122615111',count = 1,offset = random.randint(0,num))
                    if 'attachment' in pic[1]:
                        if 'photo' in pic[1]['attachment']:
                            att = 'photo-122615111_' + str(pic[1]['attachment']['photo']['pid'])
                            api.messages.send(chat_id = msg['chat_id'],attachment = att)
                            Sent = True

            if words[1][:3].lower() == u'мем':
                add_post(u'#мем')
                Sent = False
                while Sent is False:
                    meme_pubs = ['-79482962',
                                 '-123034768']
                    meme_pub_id = meme_pubs[random.randint(0,len(meme_pubs)-1)]
                    num = api.wall.get(owner_id = meme_pub_id,count = 1)[0]
                    meme = api.wall.get(owner_id = meme_pub_id,count = 1,offset = random.randint(0,num))
                    if 'attachment' in meme[1]:
                        if 'photo' in meme[1]['attachment']:
                            att = 'photo' + meme_pub_id +'_' + str(meme[1]['attachment']['photo']['pid'])
                            api.messages.send(chat_id = msg['chat_id'],attachment = att)
                            Sent = True


            if words[1].lower() == u'спиздани' or words[1].lower() == u'повтори' or words[1].lower() == u'скажи' or words[1].lower() == u'забазарь':
                if len(words) > 2:
                    print(u'#повтори')
                    api.messages.send(chat_id = msg['chat_id'],message = msg['body'][msg['body'].find(words[1]) + len(words[1]):])
                else:
                    api.messages.send(chat_id = msg['chat_id'],message = 'ты че, вообще что ли даунидзе?')

            if words[1].lower() == u'когда':
                add_post(u'#когда')
                if len(words) > 2:
                    phrase2 = [u', но это не точно',
                               u', а может и нет',
                               u', инфа сотка',
                               u', отвечаю',
                               u', но инфа старая (а говно у тебя во рту свежее)',
                               u' (нет)']
                    rand = random.randint(0,10)
                    if rand == 0:
                        ans = str(random.randint(1,31)) +'.'+ str(random.randint(1,12)) +'.'+ str(random.randint(2018,2050)) + phrase2[random.randint(0,len(phrase2)-1)]
                    elif rand == 1:
                        ans = u'Никогда, соси'
                    elif rand == 2:
                        ans = u'Это уже было, наебать хочешь?'
                    elif rand == 3:
                        ans = u'Вообще-то это уже было, дауни4а кусок'
                    elif rand == 4:
                        ans = u'Никогда' + phrase2[random.randint(0,len(phrase2)-1)]
                    elif rand == 5:
                        ans = u'Когда тебя на зоне опустят, чмо'
                    elif rand == 6:
                        ans = u'Когда рак на горе свистнет и ни минутой раньше, бомжары бля детдомовцы'
                    elif rand == 7:
                        ans = u'Когда я сочту нужным'
                    elif rand == 8:
                        ans = u'Завтра'
                    elif rand == 9:
                        ans = u'Завтра'
                    elif rand == 10:
                        ans = u'Через ' + str(random.randint(5,20)) + ' дней'
                    api.messages.send(chat_id = msg['chat_id'],message = ans, forward_messages = msg['mid'])
                else:
                    api.messages.send(chat_id = msg['chat_id'],message = 'когда мамку твою выебут', forward_messages = msg['mid'])

            if words[1].lower() == u'инфа' or words[1].lower() == u'инфа,':
                if len(words) > 2:
                    add_post(u'#инфа')
                    api.messages.send(chat_id = msg['chat_id'],message = u'Инфа ' + str(random.randint(0,100)) + '%', forward_messages = msg['mid'])
                else:
                    api.messages.send(chat_id = msg['chat_id'],message = u'тебе на лицо помочилась вся конфа', forward_messages = msg['mid'])

            if words[1].lower() == u'кто' or words[1] == u'кто,':
                if len(words) > 2:
                    add_post(u'#кто')
                    phrase1 = [u'Я думаю, это ',
                               u'Наверное, енто ',
                               u'Мне кажется, что это ',
                               u'Я уверен, что это ',
                               u'да енто точна ',
                               u'Мне кажется, что можно предположить, что это ']
                    phrase2 = [u', но это не точно',
                               u', а может и нет',
                               u', инфа сотка',
                               u', отвечаю',
                               u', но инфа старая (а говно у тебя во рту свежее)',
                               u' (нет)']

                    chat_users = api.messages.getChat(chat_id = msg['chat_id'],fields = 'first_name, last_name' )['users']

                    ans_id = random.randint(0,len(chat_users)-1)
                    ans_fname = chat_users[ans_id]['first_name']
                    ans_lname = chat_users[ans_id]['last_name']
                    rand_ans = random.randint(0,8)
                    if rand_ans >= 0 and rand_ans < 6:
                        ans = phrase1[random.randint(0,len(phrase1)-1)]+ ans_fname + ' ' + ans_lname + phrase2[random.randint(0,len(phrase2)-1)]
                    elif rand_ans == 6:
                        ans = 'Мамаша твоя'+phrase2[random.randint(0,len(phrase2)-1)]
                    elif rand_ans == 7:
                        ans = 'Это же ты, ну'
                    elif rand_ans == 8:
                        ans = phrase1[random.randint(0,len(phrase1)-1)]+'я'
                    api.messages.send(chat_id = msg['chat_id'],message = ans, forward_messages = msg['mid'])
                else:
                    api.messages.send(chat_id = msg['chat_id'],message = u'маманя твоя, петушара', forward_messages = msg['mid'])

            if words[1].lower() == u'хелп':
                if len(words) > 2:
                    response = api.photos.get(owner_id = '371041508', album_id = '240867292', count = '10')
                    picFound = False
                    for pic in range(len(response)):
                        if response[pic]['text'].lower() == words[2].lower():
                            add_post('#хелп-найдено')
                            picFound = True
                            api.messages.send(chat_id = msg['chat_id'],attachment = 'photo371041508_' + str(response[pic]['pid']))
                    if picFound == False:
                        add_post('#хелп-не найдено')
                        api.messages.send(chat_id = msg['chat_id'],message = u'вводи, блядь, нормально, чего ты хочешь, тупое животное', forward_messages = msg['mid'])
                else:
                    api.messages.send(chat_id = msg['chat_id'],message = u'я просто опизденеваю от твоей непроходимой тупости, хуйлуша. иди нахуй. пожалуйста.', forward_messages = msg['mid'])

            if words[1].lower() == u'рандом':
                add_post(u'#рандом')
                try:
                    if len(words) == 4:
                        a = int(words[2])
                        b = int(words[3])
                        api.messages.send(chat_id = msg['chat_id'],message = random.randint(a,b), forward_messages = msg['mid'])
                    elif len(words) == 3:
                        b = int(words[2])
                        api.messages.send(chat_id = msg['chat_id'],message = random.randint(0,b), forward_messages = msg['mid'])
                    else:
                        api.messages.send(chat_id = msg['chat_id'],message = u'ты че, вообще что ли даунидзе?', forward_messages = msg['mid'])
                except ValueError:
                    api.messages.send(chat_id = msg['chat_id'],message = u'ты че, вообще что ли даунидзе?', forward_messages = msg['mid'])

            if words[1].lower() == u'посчитай':
               try:
                    a = msg['body'][msg['body'].find(u'посчитай',0,len(msg['body']))+9:]
                    a = a.replace('sin','math.sin')
                    a = a.replace('cos','math.cos')
                    a = a.replace('tg','math.tan')
                    a = a.replace('tan','math.tan')
                    a = a.replace('ctg','math.ctg')
                    a = a.replace('cot','math.cot')
                    a = a.replace('log','math.log')
                    a = a.replace('sqrt','math.sqrt')
                    a = a.replace('pow','math.pow')
                    a = a.replace('deg','math.degrees')
                    a = a.replace('rad','math.rad')
                    a = a.replace('pi','math.pi')
                    exec("api.messages.send(chat_id = msg['chat_id'],message = "+ a + ",forward_messages = msg['mid'])")
               except Exception:
                    api.messages.send(chat_id = msg['chat_id'],message = u'ты че, вообще что ли даунидзе?')
        #end_commands
        elif len(words) > 1:
            api.messages.send(chat_id = msg['chat_id'],message = fuckyou[random.randint( 0,len(fuckyou)-1 )],forward_messages = msg['mid'])
        elif len(words) == 1:
            api.messages.send(chat_id = msg['chat_id'],message = lolwhat[random.randint( 0,len(lolwhat)-1 )],forward_messages = msg['mid'])
    elif len(words) > 1:
        for pref in prefixes:
            if pref in msg['body'].lower():
                api.messages.send(chat_id = msg['chat_id'],message = fuckyou[random.randint( 0,len(fuckyou)-1 )],forward_messages = msg['mid'])
                return
    else:
        if u'нахуй' in words:
            api.messages.send(chat_id = msg['chat_id'],message = u'нахуй твоя жопа хороша',forward_messages = msg['mid'])
            time.sleep(0.1)
            return
        elif u'на хуй' in msg['body'].lower():
            api.messages.send(chat_id = msg['chat_id'],message = u'на хуй твоя жопа хороша',forward_messages = msg['mid'])
            time.sleep(0.1)
            return
        elif u'спасибо' in msg['body'].lower() or u'спс' in msg['body'].lower() or u'спес' in msg['body'].lower():
            api.messages.send(chat_id = msg['chat_id'],message = u'пожалуйста',forward_messages = msg['mid'])
