if int_old_vr < 621:
            more += MPro('در ورژن '+'6.2.1',2)
            more += '\n'
            more += MPro('اضافه شدن دستور وضعیت گروه')
            more += MPro('اضافه شدن تگ های بیشتر')
            more += MPro('افزایش قدرت عضویت اجباری')
            more += MPro('بهینه سازی و حذف شدن لایب های سنگین')
            more += MPro('رفع باگ های ریز در حذف خودکار و قابلیت سخنگو')            more += MPro('اصلاح در پک سخنگوی پیشفرض')
            more += MPro('تازه سازی وب سرویس های سرگرمی و کاربردی')
            more += '\n'
        if int_old_vr < 622:
            more += MPro('در ورژن '+'6.2.2',2)
            more += '\n'
            more += MPro('اضافه شدن لیست کلید')
            more += MPro('اضافه شدن لیست متادیتا')
            more += MPro('رفع باگ در ارسال متادیتا')
            more += MPro('قادر به ساخت دستوارت متنوع')
            more += '\n'
        if int_old_vr < 623:
            more += MPro('در ورژن '+'6.2.3',2)
            more += '\n'
            more += MPro('تغییر اسم در فایل لاگین')
            more += MPro('اضافه شدن لیست معاف')
            more += MPro('ارتقای کار با ایدی و گوید')
            more += MPro('ارتقای قابلیت تایمر')
            more += MPro('ارتقای قابلیت نجوا')
            more += MPro('اضافه شدن دستور پست')
            more += MPro('اضافه شدن قابلیت پست گذاری')
            more += MPro('اضافه شدن سیستم حفاظت از اکانت بصورت خودکار')
            more += MPro('ارتقای سیستم ضد اسپم (قفل اسپم)')
            more += MPro('ارتقای بخش سخنگوی ربات')
            more += MPro('اضافه شدن دستور Sleep')
            more += MPro('اضافه شدن باگ پروفایل')
            more += '\n'
        if int_old_vr < 624:
            more += MPro('در ورژن '+'6.2.4',2)
            more += '\n'
            more += MPro('تغییر در ساختار تایمر و ارتقای آن')
            more += MPro('امکان انتقال اطلاعات گروه به گروهای دیگر')
            more += MPro('اضافه شدن دستور گزارش')
            more += MPro('قدرت پایداری به 99.99% ارتقا یافت')
            more += '\n'
        if int_old_vr < 625:
            more += MPro('در ورژن '+'6.2.5',2)
            more += '\n'
            more += MPro('اضافه شدن سیستم سیوینگ اکانت برای جلوگیری از مسدود شدن')
            more += MPro('تنظیم حریم خصوصی از طریق پیوی بات')
            more += MPro('حداکثر قادر به فعالیت در پنج گروه میباشد')
            more += '\n'
        if int_old_vr < 626:
            more += MPro('ورژن فعلی',2)
            more += '\n'
            more += MPro('اضافه شدن تاریخ شمسی')
            more += MPro('تغییرات در بخش قابلیت ترجمه')
            more += MPro('افزایش پایداری سورس')
            more += MPro('بخش -پین دیباگ شد')
            more += MPro('اضافه شدن سخنگو باادب و بی ادب')

        more += MPro('رفع چندین باگ')
        more += MPro('بهینه سازی سورس کد')

        # more += '\n'
        # more += ""

        NOTIC = f"» ربات لوپ آپدیت شد. ⚡\n» ورژن ° {NEWVR}\n{clock}\n\n{more}\n─┅━━━♦️━━━┅─\nسایت اصلی ◆ B2n.ir/L8PaIn"
        NOTIC = NOTIC.replace('ربات','ࢪب‍‍‌ا‌‌ت')
        NOTIC = NOTIC.replace('لوپ','ل‍‌و‌‌پ')
        for gaps_active in INFOS:
            try:
                # message_sended_id = client.send_text(gaps_active,NOTIC)['message_update']['message_id']
                # client.pin_message(gaps_active,message_sended_id)
                # time.sleep(0.5)
                pass
            except:pass

        # notic_owner = Informations['notic_owner']
        # try:client.send_text(OWNER,notic_owner)
        # except:pass

    # fanctions of library

    def ExtraInfo(OBJM,INFOOBJECT,SETTING_KEYS,TimeMessages,method):
        step = PorotectMSS(SETTING_KEYS,TimeMessages,15)
        if not step:return False
        match method:
            case 'bye':num = 'خدافظی'
            case 'welcome':num = 'خوشامدگویی'
            case _:num = method
        step1 , step2 = int(SETTING_KEYS[0]) , int(SETTING_KEYS[Listset[num]])
        if step1 and step2:
            mess = make_dinamic_ans(INFOOBJECT[method],OBJM['guid_sender'],OBJM['object_guid'],OBJM['message_id'],OBJM['istimer'],OBJM['ismanagerms'],OBJM['is_reply_message'],OBJM['INFOOBJECT']['filterlist'])
            return mess
        return False
    def CheckSetting(SETTING_KEYS,method):
        step1 , step2 = int(SETTING_KEYS[0]) , int(SETTING_KEYS[Listset[method]])
        if step1 and step2:return True
        return False
    def CheckTypeGets(message,filterlist,object_guid):
        message_type , reports = message['type'] , {}
        if message_type in ListLockNames:
            pr = ListLockNames[message_type]
            reports[Listlocks[pr]] = pr
        command = False
        if 'text' in message:command = (message['text']).lower()
        if command:
            if "@" in command:reports[7] = 'ایدی'
            if '.ir' in command or 'http' in command:reports[8] = 'لینک'            xc = ''
            for x in command:
                if x in TPE:xc+=x
            for x in filterlist:
                if x in xc:
                    reports[15] = f'متن نامناسب 〔 {x} 〕'
                    break
            for x in command:
                if x in TEG:
                    reports[18] = 'انگلیسی'
                    break
            if (len(command.split('\n')) >= 25 or len(command) > 420):
                reports[20] = 'کد هنگی'
        if 'forwarded_from' in message:
            reports[9] = 'فوروارد'
        if 'metadata' in message:
            reports[19] = 'متادیتا'
        return reports

    def get_all_chats()->list:
        chats = []
        next_start_id_get_chats = True
        while next_start_id_get_chats:
            try:
                if isinstance(next_start_id_get_chats, str):
                    get_chats = client.get_chats(next_start_id_get_chats)
                else:get_chats = client.get_chats()
                chats += get_chats['chats']
                time.sleep(1)
            except:
                time.sleep(1)
                continue
            if get_chats['has_continue']:next_start_id_get_chats = get_chats['next_start_id']
            else:next_start_id_get_chats = False
        return chats
    def joining(channels,object_guid,guid_sender,ok = '',inpv = False):
        global CheckJoins
        if object_guid not in CheckJoins:CheckJoins[object_guid] = {}
        if len(channels) > 0:
            if not guid_sender in CheckJoins[object_guid]:
                CheckJoins[object_guid][guid_sender] = {}
                CheckJoins[object_guid][guid_sender]['num'] = 0
                CheckJoins[object_guid][guid_sender]['chs'] = []
            links = []
            for channel in channels:
                if channel in CheckJoins[object_guid][guid_sender]['chs']:continue
                time.sleep(0.1)
                try:
                    user = client.get_chat_info(guid_sender)['user']
                    if 'username' not in user:CheckJoins[object_guid][guid_sender]['chs'].append(channel)
                    elif client.check_join(channels[channel],guid_sender):CheckJoins[object_guid][guid_sender]['chs'].append(channel)
                    else:links.append(channel)
                except:pass
            if len(links) > 0:
                if not CheckJoins[object_guid][guid_sender]['num'] == len(links):
                    CheckJoins[object_guid][guid_sender]['num'] = len(links)
                    if inpv:mess = MPro(f"برای ادمین شدن لطفا عضو کانال/گروه های زیر شوید و سپس کد را ارسال کنید {ok}",2)+'\n'
                    else:mess = MPro(f"برای استفاده از ربات در کانال/گروه های زیر عضو شوید. {ok}",2)+'\n'
                    for link in links:mess += MPro(link)
                    return mess
                else:return False
        return True
    def Maqam(maqam:str):
        match maqam:
            case 'سازنده':return '4'
            case 'مالک':return '3'
            case 'ویژه':return '2'
            case 'ادمین':return '1'
            case _:return '0'
    def Get_tip_from_str(text:str):
        command , TIP = '' , '0'
        for line in text.split('\n'):
            cmd = 'مقام'
            if (line.strip()).startswith(cmd):
                len_cmd = len(cmd)
                cmd = '-'
                if (line[len_cmd::].strip()).startswith(cmd):
                    line = line[len_cmd::].strip()
                    len_cmd = len(cmd)
                    tip_str = line[len_cmd::].strip()
                    if tip_str.startswith('u0'):TIP = tip_str
                    else:TIP = Maqam(tip_str)
                    continue
            command += f"{line}\n"
        return {'command':command.strip(),'TIP':TIP}
    def Get_actions_from_str(text:str):
        command , actions = '' , []
        for line in text.split('\n'):
            cmd = 'دستور'
            if (line.strip()).startswith(cmd):
                len_cmd = len(cmd)
                cmd = '-'
                if (line[len_cmd::].strip()).startswith(cmd):
                    line = line[len_cmd::].strip()
                    len_cmd = len(cmd)
                    action = line[len_cmd::].strip()
                    actions.append(action)
                    continue
            command += f"{line}\n"
        return {'command':command.strip(),'actions':actions}
    def delete_messages_pro(OBJM,type_def,cmd):
        global INFOS
        cmd , target_guids , target_ids , number = str(cmd) , [] , [] , False
        cmds = cmd.split(" ")
        for step in cmds:
            if step.startswith('@'):target_ids.append(step)
            elif step.startswith('u0'):target_guids.append(step)
            else:
                try:number = int(step)
                except:pass
        for target_id in target_ids:
            result = Get_guid(target_id)
            if result[0]:
                if result[1] == 'user':
                    target_guids.append(result[0])
        if not number:return 0
        if len(target_ids) > 0:
            if not len(target_guids) > 0 :return 0
        all_deleted = 0
        info = client.get_chat_info(OBJM['object_guid'])
        if 'DeleteGlobalAllMessages' in info['chat']['access'] and 'SendMessages' in info['chat']['access']:
            send_message(OBJM,MPro(f"درحال حذف ... {OBJM['INFOOBJECT']['types']['ok']}",2),OBJM['message_id'])
            last_post_id = info['chat']['last_message']['message_id']
            next_post_id,endofloop,message_sended_id,cm,limit = False,True,False,0,0
            to_messages = 0
            while endofloop and limit < 5 and to_messages < number:
                if OBJM['object_guid'] not in INFOS or not INFOS[OBJM['object_guid']]['state']:break
                time.sleep(0.1)
                if next_post_id:
                    if next_post_id >= last_post_id:
                        limit += 1
                        time.sleep(1)
                        next_post_id = str(int(last_post_id)-1)
                        continue
                    last_post_id = next_post_id
                try:
                    posts = client.get_messages_interval(OBJM['object_guid'],last_post_id)['messages']
                    next_post_id = posts[0]['message_id']
                except:
                    limit += 1
                    time.sleep(1)
                    continue
                posts.reverse()
                gets , x = [] , 0
                for post in posts:
                    if not endofloop:break
                    post_id = post['message_id']
                    if last_post_id < post_id:continue
                    if x + all_deleted >= number:break
                    gets.append(post)
                    x += 1

                to_messages += len(gets)

                if len(gets) > 0:
                    badmes = []

                    if type_def == 'delete_messages':
                        if len(target_guids) > 0:
                            for mes in gets:
                                if 'author_object_guid' in mes:
                                    for target_guid in target_guids:
                                        if target_guid == mes['author_object_guid']:
                                            badmes.append(mes['message_id'])
                                            break
                        else:
                            for mes in gets:
                                badmes.append(mes['message_id'])

                    elif type_def == 'check_messages':
                        if len(target_guids) > 0:
                            for mes in gets:
                                if 'author_object_guid' in mes:
                                    for target_guid in target_guids:
                                        if target_guid == mes['author_object_guid']:
                                            Check = CheckTypeGets(mes,OBJM['INFOOBJECT']['filterlist'],OBJM['object_guid'])
                                            for step in Check:
                                                if int(OBJM['LOCKS_KEYS'][step]) == 0:
                                                    badmes.append(mes['message_id'])
                                                    break
                                            break
                        else:
                            for mes in gets:
                                if mes['author_object_guid'] in [Coder,OBJM['INFOOBJECT']['owner'],OWNER]:continue
                                if mes['author_object_guid'] in OBJM['INFOOBJECT']['full_admins']:continue
                                Check = CheckTypeGets(mes,OBJM['INFOOBJECT']['filterlist'],OBJM['object_guid'])
                                for step in Check:
                                    if int(OBJM['LOCKS_KEYS'][step]) == 0:
                                        badmes.append(mes['message_id'])                                        break

                    elif type_def == 'delete_edited_messages':
                        if len(target_guids) > 0:
                            for mes in gets:
                                if 'author_object_guid' in mes:
                                    for target_guid in target_guids:
                                        if target_guid == mes['author_object_guid']:
                                            if mes['is_edited']:badmes.append(mes['message_id'])
                                            break
                        else:
                            for mes in gets:
                                if mes['is_edited']:badmes.append(mes['message_id'])

                    elif type_def == 'check_edited_messages':
                        if len(target_guids) > 0:
                            for mes in gets:
                                if mes['is_edited']:
                                    if 'author_object_guid' in mes:
                                        for target_guid in target_guids:                                            if target_guid == mes['author_object_guid']:
                                                Check = CheckTypeGets(mes,OBJM['INFOOBJECT']['filterlist'],OBJM['object_guid'])
                                                for step in Check:
                                                    if int(OBJM['LOCKS_KEYS'][step]) == 0:
                                                        badmes.append(mes['message_id'])
                                                        break
                                                break
                        else:
                            for mes in gets:
                                if mes['is_edited']:
                                    if mes['author_object_guid'] in [Coder,OBJM['INFOOBJECT']['owner'],OWNER]:continue
                                    if mes['author_object_guid'] in OBJM['INFOOBJECT']['full_admins']:continue
                                    Check = CheckTypeGets(mes,OBJM['INFOOBJECT']['filterlist'],OBJM['object_guid'])
                                    for step in Check:
                                        if int(OBJM['LOCKS_KEYS'][step]) == 0:
                                            badmes.append(mes['message_id'])
                                            break

                    elif type_def == 'delete_event_messages':
                        for mes in gets:
                            if 'event_data' in mes:badmes.append(mes['message_id'])

                    else:
                        for mes in gets:
                            badmes.append(mes['message_id'])

                    if len(badmes) > 0:
                        try:
                            client.delete_messages(OBJM['object_guid'],badmes)
                            limit = 0
                        except:
                            limit += 1
                            time.sleep(1)
                            continue

                        all_deleted += len(badmes)
        else:send_message(OBJM,MPro(f"دسترسی حذف پیام ندارم. {OBJM['INFOOBJECT']['types']['ok']}",2),OBJM['message_id']);all_deleted = False
        return all_deleted

    def meta_data_text(text):
        if '&' in text:
            tags = {'1':'``','۱':'``','2':'**','۲':'**','3':'__','۳':'__','4':'~~','۴':'~~','5':'--','۵':'--','6':'@@','۶':'@@','7':'##','۷':'##'}
            for tag in tags:
                text = text.replace(f"&{tag}",tags[tag])
                text = text.replace(f"{tag}&",tags[tag])
        return text
    def text_contain_tags(text:str,object_guid,guid_sender,is_reply_message = False):
        global USERS
        owner = INFOS[object_guid]['owner']
        text = remove_ids_and_links(text=text)
        text = meta_data_text(text=text)
        if object_guid not in USERS:USERS[object_guid] = {}
        if '#u0' in text:
            for line in text.split('\n'):
                for step in line.split(' '):
                    if step.startswith('#u0'):
                        step = step[1::]
                        while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
                        if step not in USERS[object_guid]:getInfoUser(object_guid,step)
                        new_step = USERS[object_guid][step][2]
                        text = text.replace(f"#{step}",f"{new_step}").strip()

        step = 'اسم_کاربر' #name #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if guid_sender not in USERS[object_guid]:getInfoUser(object_guid,guid_sender)
            new_step = USERS[object_guid][guid_sender][2]
            text = text.replace(f"#{step}",f"{new_step}").strip()
        step = 'گوید_کاربر' #guid #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{str(guid_sender)}").strip()
        step = 'گوید_سازنده' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{str(OWNER)}").strip()
        step = 'گوید_مالک' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{str(owner)}").strip()
        step = 'گوید_ربات' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{str(GUIDME)}").strip()
        step = 'گوید_ریپلای' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if is_reply_message:
                message_info = GetInfoByMessageId(object_guid,is_reply_message)
                if message_info:
                    user_guid = GetReplyGuid(message_info)
                    if user_guid and user_guid not in USERS[object_guid]:getInfoUser(object_guid,user_guid)
                    text = text.replace(f"#{step}",f"{str(user_guid)}").strip()
            else:
                text = text.replace(f"#{step}",f"{str(guid_sender)}").strip()
        step = 'تاریخ' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            new_step = Date()
            text = text.replace(f"#{step}",f"{new_step}").strip()
        step = 'اسم_ربات' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if GUIDME not in USERS[object_guid]:getInfoUser(object_guid,GUIDME)
            new_step = USERS[object_guid][GUIDME][2]
            text = text.replace(f"#{step}",f"{new_step}").strip()
        step = 'اسم_ریپلای' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if is_reply_message:
                message_info = GetInfoByMessageId(object_guid,is_reply_message)
                if message_info:
                    user_guid = GetReplyGuid(message_info)
                    if user_guid and user_guid not in USERS[object_guid]:getInfoUser(object_guid,user_guid)
                    new_step = USERS[object_guid][user_guid][2]
                    text = text.replace(f"#{step}",f"{new_step}").strip()
            else:
                if guid_sender not in USERS[object_guid]:getInfoUser(object_guid,guid_sender)
                new_step = USERS[object_guid][guid_sender][2]
                text = text.replace(f"#{step}",f"{new_step}").strip()
        for step in ['گوید_گروه','گوید_گپ']: #staticM
            if f"#{step}" in text:
                while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
                text = text.replace(f"#{step}",f"{str(object_guid)}").strip()
        for step in ['اسم_گروه','اسم_گپ']: #static
            if f"#{step}" in text:
                while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
                new_step = INFOS[object_guid]['name']
                text = text.replace(f"#{step}",f"{new_step}").strip()
        for step in ['لینک_گروه','لینک_گپ']: #static
            if f"#{step}" in text:
                while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
                try:
                    join_link = client.get_link(object_guid)['join_link']
                    text = text.replace(f"#{step}",f"{join_link}").strip()
                except:
                    text = text.replace(f"#{step}","قادر به گرفتن لینک نیستم").strip()
        for step in ['درصد_تصادفی','درصد']: #dinamic
            if f"#{step}" in text:
                while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
                while f"#{step}" in text:
                    text = text.replace(f"#{step}",f"{str(random.randint(0,100))}",1).strip()
        for step in ['عدد_تصادفی','عدد']: #dinamic
            if f"#{step}" in text:
                while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
                while f"#{step}" in text:
                    text = text.replace(f"#{step}",f"{str(random.randint(0,9))}",1).strip()
        step = 'اسم_سازنده'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if OWNER not in USERS[object_guid]:getInfoUser(object_guid,OWNER)
            new_step = USERS[object_guid][OWNER][2]
            text = text.replace(f"#{step}",f"{new_step}").strip()
        step = 'اسم_مالک'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if owner not in USERS[object_guid]:getInfoUser(object_guid,owner)
            new_step = USERS[object_guid][owner][2]
            text = text.replace(f"#{step}",f"{new_step}").strip()
        step = 'زمان'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{Hour()}").strip()
        step = 'ساعت'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{Hour()}").strip()
        step = 'سال'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{Year()}").strip()
        step = 'هفته'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{Week()}").strip()
        step = 'ماه'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{Month()}").strip()
        step = 'روز'
        if f"#{step}" in text: #static
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{Day()}").strip()
        step = 'اسم_تصادفی'
        if f"#{step}" in text: #dinamic
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            list_guids = []
            for user_guid in USERS[object_guid]:
                try:
                    if user_guid == GUIDME:continue
                    user = USERS[object_guid][user_guid]
                    mes , war = int(user[0]) , int(user[1])
                    state = mes-war
                    if state <= 5:continue
                    list_guids.append(user_guid)
                except:pass
            if len(list_guids) > 0:
                while f"#{step}" in text:
                    user_guid = random.choice(list_guids)
                    if len(list_guids) >= 2:list_guids.remove(user_guid)                    if user_guid not in USERS[object_guid]:getInfoUser(object_guid,user_guid)
                    new_step = USERS[object_guid][user_guid][2]
                    text = text.replace(f"#{step}",f"{new_step}",1).strip()
        step = 'گوید_تصادفی'
        if f"#{step}" in text: #dinamic
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            list_guids = []
            for user_guid in USERS[object_guid]:
                try:
                    if user_guid == GUIDME:continue
                    user = USERS[object_guid][user_guid]
                    mes , war = int(user[0]) , int(user[1])
                    state = mes-war
                    if state <= 5:continue
                    list_guids.append(user_guid)
                except:pass
            if len(list_guids) > 0:
                while f"#{step}" in text:
                    user_guid = random.choice(list_guids)
                    if len(list_guids) >= 2:list_guids.remove(user_guid)                    if user_guid not in USERS[object_guid]:getInfoUser(object_guid,user_guid)
                    new_step = user_guid
                    text = text.replace(f"#{step}",f"{new_step}",1).strip()
        step = 'گوید' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            text = text.replace(f"#{step}",f"{str(guid_sender)}").strip()
        step = 'اسم' #static
        if f"#{step}" in text:
            while f"##{step}" in text:text = text.replace(f"##{step}",f"#{step}#{step}").strip()
            if guid_sender not in USERS[object_guid]:getInfoUser(object_guid,guid_sender)
            new_step = USERS[object_guid][guid_sender][2]
            text = text.replace(f"#{step}",f"{new_step}").strip()

        return text
    def get_steps(text:str)->list:
        list_steps = []
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            steps = line.split(' ')
            for step in steps:
                list_steps.append(step)
        return list_steps
    def Sorting(lst:list)->list:
        lst2 = sorted(lst, key=len)
        return lst2
    def make_dinamic_ans(text,guid_sender,object_guid,message_id,istimer,ismanagerms = True,is_reply_message = None , filterlist = [],save = True,pv = False):
        if isinstance(text,str):
            text = text_contain_tags(text=text,object_guid=object_guid,guid_sender=guid_sender,is_reply_message=is_reply_message)
            if not isinstance(text,str):return False
            if pv:object_guid = guid_sender
            if istimer:message_id = None
            list_media_tag = ['#image','#video','#voice','#audio','#gif']
            for tag in list_media_tag:
                if tag in text.lower():
                    for line in text.split('\n'):
                        for step in line.split(' '):
                            if step.startswith(tag):
                                list_infos = {'image':'png','gif':'mp4','voice':'mpeg','audio':'mp3','video':'mp4'}
                                filename = step[1::].strip()
                                tag_name = tag[1::]
                                format = list_infos[tag_name]
                                text = text.replace(step,'').strip()
                                if len(text) <= 0:text = None
                                else:
                                    for st in filterlist:
                                        if st in text:
                                            next_word = Font_close(st)
                                            text = text.replace(st,next_word)
                                    for st in LISTFILTERPRO:
                                        if st in text:
                                            next_word = Font_filter(st)
                                            text = text.replace(st,next_word)
                                if tag_name == 'gif' and filename in INLINES:
                                    ResultME = client.send_message(object_guid,INLINES[filename],text,message_id)
                                    if save:save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                    return False
                                else:
                                    if not filename.endswith(f'.{format}'):filename += f'.{format}'
                                    if os.path.isfile(f"Downloads/{filename}"):
                                        match tag_name:
                                            case 'image':
                                                ResultME = client.send_image(object_guid,f"Downloads/{filename}",message_id,text)
                                                if save:save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            case 'video':
                                                ResultME = client.send_video(object_guid,f"Downloads/{filename}",message_id,text)
                                                if save:save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            case 'voice':
                                                ResultME = client.send_voice(object_guid,f"Downloads/{filename}",message_id,text,time=1)
                                                if save:save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            case 'audio':
                                                ResultME = client.send_music(object_guid,f"Downloads/{filename}",message_id,text,time=1,performer='l‌8‌P‌B‌O‌T')
                                                if save:save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            case 'gif':
                                                ResultME = client.send_gif(object_guid,f"Downloads/{filename}",message_id,text)
                                                if save:save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                        return False
            for st in filterlist:
                if st in text:
                    next_word = Font_close(st)
                    text = text.replace(st,next_word)
            for st in LISTFILTERPRO:
                if st in text:
                    next_word = Font_filter(st)
                    text = text.replace(st,next_word)
            return text
        else:return False
    def save_info_messages(ResultME,object_guid,message_id,ismanagerms = True):
        global LSMessage,ARMessages,TimeMessages,STMessages,INFOS
        SETTING_KEYS = list(INFOS[object_guid]['setting'])
        if ResultME and ResultME != True and 'message_update' in ResultME:
            if int(SETTING_KEYS[13]):
                if len(TimeMessages) >= 20:TimeMessages.pop(0)
                TimeMessages.append(get_iran_timestamp())

            message_sended_id = ResultME['message_update']['message_id']
            if object_guid not in LSMessage:LSMessage[object_guid] = [0,1]
            LSMessage[object_guid][0] = message_sended_id
            LSMessage[object_guid][1] = message_sended_id

            if int(SETTING_KEYS[1]) and int(SETTING_KEYS[0]):
                if object_guid not in ARMessages:ARMessages[object_guid] = []
                if len(ARMessages[object_guid]) >= 50:ARMessages[object_guid].pop(0)
                ARMessages[object_guid].append(message_sended_id)

            # SAVE MS SETTING
            if ismanagerms and int(SETTING_KEYS[11]):
                if object_guid not in STMessages:STMessages[object_guid] = []
                if len(STMessages[object_guid]) >= 100:STMessages[object_guid].pop(0)
                if not message_id in STMessages[object_guid]:STMessages[object_guid].append(message_id)
                STMessages[object_guid].append(message_sended_id)

    def send_message(OBJM,text,message_id = None,metadata = True):
        if OBJM['TIP'] > 3:sleepmod = 0
        else:sleepmod = int(OBJM['SETTING_KEYS'][15])
        if sleepmod == 0 and not OBJM['silentMod']:
            # SANSOR
            for st in LISTFILTERPRO:
                if st in text:
                    next_word = Font_filter(st)
                    text = text.replace(st,next_word)
            if metadata:
                text = meta_data_text(text=text)
            text = text_make_type(text,OBJM['INFOOBJECT']['types']['type'])
            text = text_make_font(text,OBJM['INFOOBJECT']['types']['font'])
            if OBJM['istimer']:message_id = None
            ResultME = client.send_text(OBJM['object_guid'],text,message_id)
            save_info_messages(ResultME,OBJM['object_guid'],message_id,OBJM['ismanagerms'])
            global PROTECTED
            if object_guid not in PROTECTED:PROTECTED[object_guid] = 0
            else:PROTECTED[object_guid] = 0
        return True
    def send_message_limited(OBJM,text,message_id = None,metadata = True):
        if OBJM['TIP'] > 3:sleepmod = 0
        else:sleepmod = int(OBJM['SETTING_KEYS'][15])
        if sleepmod == 0 and not OBJM['silentMod']:
            # SANSOR
            for st in OBJM['INFOOBJECT']['filterlist']:
                if st in text:
                    next_word = Font_close(st)
                    text = text.replace(st,next_word)
            for st in LISTFILTERPRO:
                if st in text:
                    next_word = Font_filter(st)
                    text = text.replace(st,next_word)
            if metadata:
                text = meta_data_text(text=text)
            text = text_make_type(text,OBJM['INFOOBJECT']['types']['type'])
            text = text_make_font(text,OBJM['INFOOBJECT']['types']['font'])
            if OBJM['istimer']:message_id = None
            ResultME = client.send_text(OBJM['object_guid'],text,message_id)
            save_info_messages(ResultME,OBJM['object_guid'],message_id,OBJM['ismanagerms'])
            global PROTECTED
            if object_guid not in PROTECTED:PROTECTED[object_guid] = 0
            else:PROTECTED[object_guid] = 0
        return True

    def get_ans_from_qu_pro(client,SPEAK,update_message,OBJM,command,message_id):
        for word in SPEAK:
            if word in command and len(SPEAK[word]) > 0:
                step = random.choice(SPEAK[word])
                if 'answer' in step:answer = step['answer'];issilent = True
                else:issilent = False
                if 'actions' in step and OBJM:
                    for action in step['actions']:
                        try:
                            action = text_contain_tags(action,OBJM['object_guid'],OBJM['guid_sender'],OBJM['is_reply_message'])
                            if issilent:action = f"{action}-"
                            update_message['message']['text'] = action
                            commands_colection(client,OBJM['object_guid'],OBJM['guid_sender'],update_message,OBJM['istimer'])
                        except:pass
                if issilent and OBJM:
                    answer = make_dinamic_ans(answer,OBJM['guid_sender'],OBJM['object_guid'],OBJM['message_id'],OBJM['istimer'],OBJM['ismanagerms'],OBJM['is_reply_message'],OBJM['INFOOBJECT']['filterlist'])
                    if answer:send_message(OBJM,answer,message_id)
                if not OBJM and issilent:client.send_text(OWNER,answer,message_id)
                return True

    def get_answer(command,TIP_ANS = 0,sp_type = False):
        import requests

        step = False
        url = "https://l8p.ir/API-SPEAK/speak.php"
        if not sp_type:sp_type = typespeak

        params = {
            'maqam': TIP_ANS,
            'type_speak': sp_type,
            'command': command
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            step = response.json()['step']

        return step

    def get_default_ans_from_qu(client,TIP_ANS,update_message,OBJM,command,message_id):
        step = get_answer(command,TIP_ANS)
        if step:
            if 'answer' in step:answer = step['answer'];issilent = True
            else:issilent = False
            if 'actions' in step and OBJM:
                for action in step['actions']:
                    try:
                        action = text_contain_tags(action,OBJM['object_guid'],OBJM['guid_sender'],OBJM['is_reply_message'])
                        if issilent:action = f"{action}-"
                        update_message['message']['text'] = action
                        commands_colection(client,OBJM['object_guid'],OBJM['guid_sender'],update_message,OBJM['istimer'])
                    except:pass
            if issilent and OBJM:
                answer = make_dinamic_ans(answer,OBJM['guid_sender'],OBJM['object_guid'],OBJM['message_id'],OBJM['istimer'],OBJM['ismanagerms'],OBJM['is_reply_message'],OBJM['INFOOBJECT']['filterlist'])
                if answer:send_message(OBJM,answer,message_id)
            if not OBJM and issilent:client.send_text(OWNER,answer,message_id)
        return True

    def save_media_pro(OBJM,callback = False):
        global INLINES
        list_infos = {'عکس':{'format':'png','nick':'image'},'گیف':{'format':'mp4','nick':'gif'},'صدا':{'format':'mpeg','nick':'voice'},'ویس':{'format':'mpeg','nick':'voice'},'اهنگ':{'format':'mp3','nick':'audio'},'موزیک':{'format':'mp3','nick':'audio'},'فیلم':{'format':'mp4','nick':'video'}}
        result = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        file_inline = result.get('file_inline')
        if file_inline:type_message = file_inline.get('type')
        else:return False
        type = ListLockNames[type_message]
        if type and type in list_infos:
            format , nick = list_infos[type]['format'] , list_infos[type]['nick']
        else:return False
        try:
            if nick == 'gif':
                num = len(INLINES)+1
                result = client.download(OBJM['object_guid'],OBJM['is_reply_message'],False)
                del result['file']
                INLINES[f"{nick}{str(num)}"] = result
                UPFILES(file_inlines,INLINES)
            else:
                num = 1;fileName = f"{nick}{str(num)}.{format}"
                while os.path.isfile(f"Downloads/{fileName}"):
                    num += 1
                    fileName = f"{nick}{str(num)}.{format}"
                client.download(OBJM['object_guid'],OBJM['is_reply_message'],True,f"Downloads/{fileName}")
            if callback:return f"{nick}{str(num)}"
            else:return MPro(f"{type} با تگ #{nick}{str(num)} سیو شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        except:
            #traceback.print_exc()
            if callback:return False
            else:return MPro(f"{type} سیو نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def send_timeout_group(OBJM,option = False):
        global INFOS
        if 'timeout' in INFOS[OBJM['object_guid']] and INFOS[OBJM['object_guid']]['timeout']:
            timeout = INFOS[OBJM['object_guid']]['timeout']
            now = get_iran_timestamp()
            timeout_result = timeout-now
            result = Time_pass(timeout_result)
            if option:
                return f"{result} از شارژ گروه باقی مانده است."
            else:
                return MPro(f"{result} از شارژ گروه باقی مانده است. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:
            if option:
                return f"برای گروه شارژی تایین نشده است."
            else:
                return MPro(f"برای گروه شارژی تایین نشده است. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def delete_timeout_group(OBJM):
        global INFOS
        if 'timeout' in INFOS[OBJM['object_guid']] and INFOS[OBJM['object_guid']]['timeout']:
            INFOS[OBJM['object_guid']]['timeout'] = False
            return MPro(f"شارژ گروه حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"برای گروه شارژی تایین نشده است. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def get_my_media_pro(OBJM,type):
        global INLINES
        list_infos = {'عکس':{'format':'png','nick':'image'},'گیف':{'format':'mp4','nick':'gif'},'صدا':{'format':'mpeg','nick':'voice'},'ویس':{'format':'mpeg','nick':'voice'},'اهنگ':{'format':'mp3','nick':'audio'},'موزیک':{'format':'mp3','nick':'audio'},'فیلم':{'format':'mp4','nick':'video'}}
        if type in list_infos:
            format , nick = list_infos[type]['format'] , list_infos[type]['nick']
        else:return False
        medias = []
        if nick == 'gif':
            for key in INLINES:medias.append(key)
        else:
            files = [f for f in os.listdir("Downloads") if os.path.isfile(f"Downloads/{f}")]
            for file in files:
                if file.startswith(nick) and file.endswith(f'.{format}'):medias.append(file)

        mess = MPro(f'لیست {type}',4)
        if len(medias) > 0:
            for media in medias:
                mess += MPro(f"#{media.replace(f'.{format}','')}",2)
        else:mess = MPro(f"لیست {type} خالی میباشد. {OBJM['INFOOBJECT']['types']['ok']}")
        return mess
    def delete_all_media_pro(OBJM,type):
        global INLINES
        list_infos = {'عکس':{'format':'png','nick':'image'},'گیف':{'format':'mp4','nick':'gif'},'صدا':{'format':'mpeg','nick':'voice'},'ویس':{'format':'mpeg','nick':'voice'},'اهنگ':{'format':'mp3','nick':'audio'},'موزیک':{'format':'mp3','nick':'audio'},'فیلم':{'format':'mp4','nick':'video'}}
        if type in list_infos:
            format , nick = list_infos[type]['format'] , list_infos[type]['nick']
        else:return False
        medias = []
        if nick == 'gif':
            INLINES = {}
            UPFILES(file_inlines,INLINES)
        else:
            files = [f for f in os.listdir("Downloads") if os.path.isfile(f"Downloads/{f}")]
            for file in files:
                if file.startswith(nick) and file.endswith(f'.{format}'):medias.append(file)
            for media in medias:
                try:os.remove(f"Downloads/{media}")
                except:pass
        return MPro(f"لیست {type} پاکسازی شد. {OBJM['INFOOBJECT']['types']['ok']}")

    def notif_messages(update):
        global USERS,INFOS
        if 'show_notifications' in update:
            for notif_messsage in update['show_notifications']:
                try:
                    if notif_messsage['notification_id'].startswith('n_g0'):
                        message_data = notif_messsage.get('message_data')
                        title = notif_messsage.get('title')
                        text = notif_messsage.get('text').split(':')
                        user_firstname = None
                        if len(text) >= 2:user_firstname = text[0]
                        object_guid = message_data.get('object_guid')
                        guid_sender = message_data.get('sender_guid')
                        if guid_sender and object_guid and user_firstname:
                            if object_guid in INFOS:
                                if object_guid not in USERS:USERS[object_guid] = {}
                                if guid_sender not in USERS[object_guid]:
                                    USERS[object_guid][guid_sender] = [0,0,user_firstname,'ناشناس']
                                else:
                                    last_up_name = USERS[object_guid][guid_sender][2]
                                    if last_up_name == 'اراذل' or last_up_name == 'بدون لقب':
                                        USERS[object_guid][guid_sender][2] = user_firstname
                except:
                    #traceback.print_exc()
                    pass

    def send_tas(OBJM):
        match random.randint(1,6):
            case 1:return "⬤"
            case 2:return "⬤ ⬤"
            case 3:return "⬤ ⬤\n  ⬤"
            case 4:return "⬤ ⬤\n⬤ ⬤"
            case 5:return "⬤ ⬤\n  ⬤\n⬤ ⬤"
            case 6:return "⬤ ⬤\n⬤ ⬤\n⬤ ⬤"
    def send_version(OBJM):
        global NEWVR
        return f"v{str(NEWVR)}"
    def get_info_user_1(OBJM):
        global USERS

        rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,OBJM['guid_sender'])
        if OBJM['guid_sender'] not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],OBJM['guid_sender'])
        return MPro(f"مقام 〔 {rank} 〕",4)+formInfo(USERS[OBJM['object_guid']][OBJM['guid_sender']])
    def get_link_gap(OBJM):
        result = False
        try:result = client.get_link(OBJM['object_guid'])
        except:pass
        if result:return MPro(f"لینک دعوت گپ 〔 {OBJM['INFOOBJECT']['name']} 〕 : \n"+result['join_link'],2)
        else:return MPro(f"لینک دعوت رو نمیتونم بگیرم.{OBJM['INFOOBJECT']['types']['ok']}",2)
    def get_full_date(OBJM):
        return FormDate(requests.get(url = "https://one-api.ir/time/?token=833942:64919956105c3&action=timestamp&timestamp="+str(get_iran_timestamp())+"&timezone='Asia/Tehran'", timeout=30).json())
    def get_clock(OBJM):
        return f"» {Hour()} ⌯ {Week()} {OBJM['INFOOBJECT']['types']['ok']}"
    def get_mention_malek(OBJM):
        if OBJM['INFOOBJECT']['owner'] not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],OBJM['INFOOBJECT']['owner'])
        return MPro(f"@@〔 {USERS[OBJM['object_guid']][OBJM['INFOOBJECT']['owner']][2]} 〕@@({OBJM['INFOOBJECT']['owner']})",1)
    def get_guid_group(OBJM):
        return MPro(f"گوید گروه : ``{str(OBJM['object_guid'])}``",1)
    def send_seckeh(OBJM):
        if random.randint(1,2) == 1:return '⦿ #شیر ⦿'
        else:return '⊝ #خط ⊝'
    def send_api_jock(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/jock/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return f"⌯ #JOCK\n\n{data['result']['QU']}"
    def send_api_chalesh(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/chalesh/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return data['result']['QU']
    def send_api_bio(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/bio/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return  f"⌯ #BIO\n\n{data['result']['QU']}"
    def send_api_fact(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/fact/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return f"⌯ #FACT\n\n{data['result']['QU']}"
    def send_api_etraf(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/etraf/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return f"⌯ #ETRAF\n\n{data['result']['QU']}"
    def send_api_danestani(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/dnstni/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return f"⌯ #DANESTANI\n\n{data['result']['QU']}"
    def send_api_dastan(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/story/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return f"⌯ #STORY\n\n{data['result']['QU']}"
    def send_api_textmod(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/text/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:return f"⌯ #TEXT\n\n{data['result']['QU']}"
    def send_api_gang(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = ((requests.get("https://haji-api.ir/gang/", timeout=30)).content).decode("utf-8")
        return f"⌯ #GANG\n\n{data}"
    def send_api_angizeshi(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = (requests.get("https://haji-api.ir/angizeshi/", timeout=30).content).decode("utf-8")
        return f"⌯ #ANGIZESHI\n\n{data}"
    def send_api_zekr(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get("https://haji-api.ir/zekr", timeout=30).json()
        if data['ok']:return "⌯ #ZEKR\n\n"+MPro(data['Result']['zekr'])+MPro(data['Result']['persian'])+MPro(data['Result']['info'])
    def send_api_fal(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get(url = "https://l8p.ir/API/index-api.php/fal/?key=34613461&chat_id="+object_guid+"&user_id="+guid_sender, timeout=30).json()
        if data['status'] == 200:
            title = Font_shec(data['result']['title'])
            mess = f"⌯ #FAL\n\n𝗧𝗜𝗧𝗟𝗘 »\n{MPro(title,4)}\n𝗥𝗛𝗬𝗠𝗘 »\n"
            lines = data['result']['rhyme'].split('\n')
            for line in lines:mess += MPro(line)
            mess += "\n\n𝗠𝗘𝗔𝗡𝗜𝗡𝗚 »\n\n"+MPro(data['result']['meaning'])
            return mess
    def send_nickname_me(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['message_id'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
            nickname = USERS[OBJM['object_guid']][user_guid][2]
            if len(nickname) <= 0:nickname = 'بدون لقب'
            return MPro(f"لقبت : {nickname}")
    def send_asl_me(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['message_id'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
            asl = USERS[OBJM['object_guid']][user_guid][3]
            if len(asl) <= 0:asl = 'بدون اصل'
            return MPro(f"اصلت : {asl}")
    def send_maqam_me(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['message_id'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,user_guid)
                return MPro(f"مقامت : {rank}")
    def send_guid_me(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['message_id'])
        if message_info:
            return MPro(f"گویدت : ``{GetReplyGuid(message_info)}``",1)
    def send_media_welcom(OBJM):
        return OBJM['INFOOBJECT']['welcome']
    def send_media_bye(OBJM):
        return OBJM['INFOOBJECT']['bye']
    def send_banner(OBJM):
        mess = OBJM['INFOOBJECT']['baner']
        if len(mess) == 0:return MPro(f"بنری ثبت نشده است.{OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return remove_ids_and_links(mess)
    def send_rules(OBJM):
        return make_dinamic_ans(OBJM['INFOOBJECT']['rols'],OBJM['guid_sender'],OBJM['object_guid'],OBJM['message_id'],OBJM['istimer'],OBJM['ismanagerms'],OBJM['is_reply_message'],OBJM['INFOOBJECT']['filterlist'])
    def send_limites(OBJM):
        mess = MPro("محدودیت 〔 💀 〕",4)+MPro("ارسال موارد زیر ممنوع است. 〔 قفل 🚫 〕\n",2)
        locks_warning = list(OBJM['INFOOBJECT']['locks_warning'])
        locks_warning_show = list(OBJM['INFOOBJECT']['locks_warning_show'])
        locks_ban = list(OBJM['INFOOBJECT']['locks_ban'])
        for lock in Listlocks:
            key = Listlocks[lock]
            if int(OBJM['LOCKS_KEYS'][key]) == 0:
                ison,isshow = '',''
                if locks_ban[key] == '0':ison = '🟢'
                if locks_warning_show[key] == '0':isshow = '🔇'
                mess += MPro(f"{lock} 〔 {locks_warning[key]} 〕 {ison}{isshow}")
        mess += '\n'
        mess += MPro(f"تعداد اخطار : {str(OBJM['INFOOBJECT']['warnning'])}\n",2)+MPro("دستورات زیر خاموش است. 〔 خاموش 💤 〕\n",2)
        empty = True
        for lock in ListKeys_Names:
            res , name = '' , ListKeys_Names[lock]
            try:
                if int(OBJM['ORDERS_KEYS'][lock]) == 0:
                    empty = False
                    mess += MPro(name)
            except:pass
        if empty:mess += MPro("هیچ دستوری خاموش نیست")
        return mess
    def send_maqam_maker(OBJM):
        if OWNER not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],OWNER)
        return MPro(f"@@〔 {USERS[OBJM['object_guid']][OWNER][2]} 〕@@({OWNER})",1)                                                             
    def send_api_profile(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        try:
            url = (requests.get("https://api-free.ir/api/prof.php", timeout=30).json())['result'][0]
            response = requests.get(url, timeout=30)
            name_file = f'prof_{str(get_iran_timestamp())}.png'
            with open(name_file, "wb") as file:
                file.write(response.content)
            try:
                ResultME = client.send_image(OBJM['object_guid'],name_file,OBJM['message_id'])
                save_info_messages(ResultME,OBJM['object_guid'],OBJM['message_id'],OBJM['ismanagerms'])
            except:pass
            os.remove(name_file)
        except:pass
    def send_api_background(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        try:
            url = random.choice((requests.get("https://api-free.ir/api/background.php", timeout=30).json())['result'])
            response = requests.get(url, timeout=30)
            name_file = f'prof_{str(get_iran_timestamp())}.png'
            with open(name_file, "wb") as file:
                file.write(response.content)
            try:
                ResultME = client.send_image(OBJM['object_guid'],name_file,OBJM['message_id'])
                save_info_messages(ResultME,OBJM['object_guid'],OBJM['message_id'],OBJM['ismanagerms'])
            except:pass
            os.remove(name_file)
        except:pass
    def send_api_procsy(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = requests.get("https://api-free.ir/api/proxy.php", timeout=30).json()
        if data['ok']:
            form,m = '',0
            for url in data['result']:
                if m>20:break
                form += f"@@PROXI{str(m)}@@({url}) ⌯ "
                m += 1
            return f"⌯ #PROXIS\n\n{form}"
    def send_api_photography(OBJM):
        try:
            response = requests.get("http://haji-api.ir/photography/", timeout=30)
            name_file = f'photography_{str(get_iran_timestamp())}.png'
            with open(name_file, "wb") as file:
                file.write(response.content)
            try:
                ResultME = client.send_image(OBJM['object_guid'],name_file,OBJM['message_id'])
                save_info_messages(ResultME,OBJM['object_guid'],OBJM['message_id'],OBJM['ismanagerms'])
            except:pass
            os.remove(name_file)
        except:pass
    def send_api_arz(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        try:
            data = requests.get("https://haji-api.ir/exchange-rate/", timeout=30).json()
            if data['ok']:
                results , mess = data['Results'] , ''
                for info in results:
                    rate = results[info]['Average']
                    mess += MPro(f"{RATES[info]} : {rate}",2)
                if len(mess) > 0:return f"⌯ #CURRENCY\n\n{mess}"
        except:pass
    def send_api_deghat(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = ((requests.get("https://haji-api.ir/deghat", timeout=30)).content).decode("utf-8")
        return f"⌯ #DEGHAT\n\n{data}"
    def send_api_hagh(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        data = ((requests.get("https://haji-api.ir/ketab/", timeout=30)).content).decode("utf-8")
        return f"⌯ #HAGH\n\n{data}"
    def send_api_fal_hafez(OBJM):
        global limitAPI
        if object_guid not in limitAPI:limitAPI[object_guid] = 0

        limitAPI[object_guid] += 1
        if limitAPI[object_guid] >= 6:
            return

        try:
            url = (requests.get("https://api-free.ir/api/fal", timeout=30).json())['result']
            response = requests.get(url, timeout=30)
            name_file = f'fal_hafez_{str(get_iran_timestamp())}.png'
            with open(name_file, "wb") as file:
                file.write(response.content)
            try:
                ResultME = client.send_image(OBJM['object_guid'],name_file,OBJM['message_id'])
                save_info_messages(ResultME,OBJM['object_guid'],OBJM['message_id'],OBJM['ismanagerms'])
            except:pass
            os.remove(name_file)
        except:pass
    def send_random_number(OBJM):
        return f"°•{str(random.randint(1,1000))}"
    def send_count_messages_me(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['message_id'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
            return MPro(f"تعداد پیامت : {str(USERS[OBJM['object_guid']][user_guid][0])}")
    def send_count_warnning_me(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['message_id'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
            countwr = USERS[OBJM['object_guid']][user_guid][1]
            return MPro(f"تعداد اخطارت : {str(USERS[OBJM['object_guid']][user_guid][1])}")
    def send_api_pnp(OBJM):
        data = requests.get(f"https://haji-api.ir/jok/?q=51&page={str(random.randint(1,47))}", timeout=30).json()
        if data['ok']:
            rand = random.randint(1,int(len(data['results']))-1)
            return f"⌯ #P N P\n\n{data['results'][str(rand)]}"

    def send_text_keshideh(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:mess = Font_kesh(message_info['text'])
        return mess
    def send_text_lash(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:mess = Font_lash(message_info['text'])
        return mess
    def send_text_shekasteh(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:mess = Font_shec(message_info['text'])
        return mess
    def send_your_laqab(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                nickname = USERS[OBJM['object_guid']][user_guid][2]
                if len(nickname) <= 0:nickname = 'بدون لقب'
                mess = MPro(f"لقبش : {nickname}")
        return mess
    def send_your_asl(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                infouser = USERS[OBJM['object_guid']][user_guid][3]
                if len(infouser) <= 0:infouser = 'بدون اصل'
                mess = MPro(f"اصلش : {infouser}")
        else:mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        return mess
    def send_your_maqam(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,user_guid)
                mess = MPro(f"مقامش : {rank}")
        return mess
    def send_your_guid(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:mess = MPro(f"گویدش : ``{user_guid}``",1)
        return mess
    def send_your_info(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,user_guid)
                mess = MPro(f"مقام 〔 {rank} 〕",4)
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                mess += formInfo(USERS[OBJM['object_guid']][user_guid])
        return mess
    def send_your_count_messages(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                countms = USERS[OBJM['object_guid']][user_guid][0]
                mess = MPro(f"تعداد پیامش : {str(countms)}")
        return mess
    def send_your_count_warnings(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        mess = MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
        if message_info:
            mess = MPro(f"کاربر شناسایی نشد.{OBJM['INFOOBJECT']['types']['ok']}",2)
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                countwr = USERS[OBJM['object_guid']][user_guid][1]
                mess = MPro(f"تعداد اخطارش : {str(countwr)}")
        return mess
    def message_length(OBJM):
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:return MPro(f"طول پیام : {str(len(message_info['text']))}")
        return MPro(f"روی پیام پاک شده ریپلای زدی.{OBJM['INFOOBJECT']['types']['ok']}",2)
    def message_infos(OBJM):
        message = client.get_messages_by_id(OBJM['object_guid'],[OBJM['is_reply_message']])
        return json.dumps(message)
    def install_pro_libs(OBJM):
        client.send_text(OBJM['object_guid'],MPro(f"در حال نصب لایب ها... {OBJM['INFOOBJECT']['types']['ok']}",2),OBJM['message_id'])
        install_auto(['jdatetime','Pillow','moviepy'])
        try:import jdatetime
        except:import datetime as jdatetime
        return MPro(f"لایب ها نصب شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def make_voice_call(OBJM):
        global INFOS
        mess = MPro(f"ویسکال ایجاد شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        try:
            result = client.create_voice_chat(OBJM['object_guid'])
            if result['status'] == 'VoiceChatExist':
                mess = MPro(f"ویسکال ایجاد شده است. {OBJM['INFOOBJECT']['types']['ok']}",4)
                mess += MPro(f"عنوان : {str(result['exist_group_voice_chat']['title'])}")
                mess += MPro(f"تعداد افراد : {str(result['exist_group_voice_chat']['participant_count'])}")
            else:INFOS[OBJM['object_guid']]['voice_call'] += 1
        except:mess = MPro(f"کال ایجاد نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        return mess
    def send_full_info_me(OBJM):
        rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,OBJM['guid_sender'])
        mess = MPro(f"مقام 〔 {rank} 〕",4)
        user = client.get_chat_info(OBJM['guid_sender'])['user']
        mess += manage_info(user)
        if OBJM['guid_sender'] not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],OBJM['guid_sender'])
        mess += formInfo(USERS[OBJM['object_guid']][OBJM['guid_sender']])
        mess += f"\n{MPro(OBJM['guid_sender'])}\n─┅━━━━━━━┅─"
        if 'bio' in user:
            mess += f"\n\n{user['bio']}"
        return mess
    def send_setting_commands(OBJM):
        mess = MPro("تنظیم 〔 💎 〕",4)
        list_texts = Sorting(["تنظیم فونت","تنظیم شکل","تنظیم خوشامدگویی","تنظیم خدافظی","تنظیم قوانین","تنظیم بنر"])
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def send_status_commands(OBJM):
        mess = MPro("امار 〔 📌 〕",4)
        list_texts = Sorting(["امار گپ","وضعیت گپ","گزارشات","محدودیت","امار اعضا","امار کل"])
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def send_reset_commands(OBJM):
        list_texts = Sorting(["ریست دستورات","ریست قفل","ریست داشبورد","ریست قوانین","ریست خدافظی","ریست خوشامدگویی","ریست بنر","ریست کلید","ریست گپ","ریست شکل","ریست فونت","ریست علامت","ریست تنظیمات"])
        mess = MPro("ریست 〔 👾 〕",4)
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def send_games_commands(OBJM):
        mess = MPro("سرگرمی 〔 ⚡ 〕",4)
        list_texts = Sorting(["چالش","جوک","بیو","فال","فکت","اعتراف","دانستنی","گنگ","ذکر","انگیزشی","فتوگرافی","پ ن پ","پروفایل","والپیپر","فال حافظ","حق","دقت","تکست","تاس","سکه","عدد شانسی"])
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def send_panel_setting(OBJM):
        mess = MPro("تنظیمات 〔 💠 〕",4)
        list_texts = Sorting(["داشبورد","امار","سرگرمی","هوش مصنوعی","تنظیم","ریست","دستورات"])
        # list_texts = Sorting(["مدیریت قفل ها","امار","سرگرمی","هوش مصنوعی","تنظیم","ریست","دستورات"])
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def send_reports_gap(OBJM):
        mess = MPro("گزارشات 〔 📊 〕",4)
        reports , empty = OBJM['INFOOBJECT']['type_messages'] , True
        for report in reports:
            empty = False
            mess += MPro(f"{report} : {reports[report]}")
        if empty:
            mess += MPro("هیچ دیتایی شناسایی نشده است.")
        return mess
    def send_dashboard(OBJM):
        mess = MPro("داشبورد 〔 🛠️ 〕",4)+MPro(f"زمان : {Date()}\n")
        for lock in Listset:
            res = ''
            if int(OBJM['SETTING_KEYS'][Listset[lock]]) == 0:res = '〔 خاموش 〕'
            mess += MPro(f"{lock} {res}")
        mess += '\n'
        mess += MPro(f"تعداد اخطار : {str(OBJM['INFOOBJECT']['warnning'])}")
        return mess
    def send_list_lists(OBJM):
        mess = MPro("لیست ها 〔 📑 〕",4)
        list_texts = Sorting(["لیست دستورات","لیست قفل","لیست ویژه","لیست ادمین","لیست سکوت","لیست معاف","لیست فیلتر","لیست کلمات","لیست عضویت","لیست یادداشت","لیست کیل","لیست کلید","لیست متادیتا"])
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def send_status_gap(OBJM):
        global USERS
        mess = MPro(f"امار گروه 〔 {str(OBJM['INFOOBJECT']['name'])} 〕",4)
        def myFunc(e):return e['mes']
        listMems , allMes = [] , 0
        list_users = USERS[OBJM['object_guid']]
        for mems in list_users:
            allMes += int(list_users[mems][0])
            listMems.append({'mes':int(list_users[mems][0]),'name':str(list_users[mems][2]),'guid':str(mems)})
        now = f"{Date()} {Hour()}"
        time_oj = jdatetime.datetime.fromtimestamp(int(OBJM['INFOOBJECT']['date']))
        mess += MPro(f"شروع فعایت : {str(time_oj)}")
        mess += MPro(f"زمان : {str(now)}\n")
        mess += MPro(f"تعداد کل پیام ثبت شده : {str(OBJM['INFOOBJECT']['messages'])}")
        mess += MPro(f"تعداد کل پیام مجاز : {str(allMes)}")
        mess += MPro(f"تعداد جوین شده : {str(OBJM['INFOOBJECT']['join'])}")
        mess += MPro(f"تعداد افزوده شده : {str(OBJM['INFOOBJECT']['add'])}")
        mess += MPro(f"تعداد لفت داده : {str(OBJM['INFOOBJECT']['left'])}")
        mess += MPro(f"تعداد بن شده : {str(OBJM['INFOOBJECT']['ban'])}")        mess += MPro(f"تعداد ویسکال : {str(OBJM['INFOOBJECT']['voice_call'])}\n")
        mess += 'به ترتیب تعداد پیام ها  ━━━━━━━━┅─\n\n'
        listMems.sort(reverse=True,key=myFunc)
        limit = 1
        cups = {1:'🥇',2:'🥈',3:'🥉'}
        for member in listMems:
            if limit > 20:break
            rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,member['guid'],True)
            countms , nickname , guid = member['mes'] , member['name'] , member['guid']
            if nickname == 'بدون لقب' or nickname == 'اراذل':
                getInfoUser(OBJM['object_guid'],guid,list_users[guid][3])
                nickname = list_users[guid][2]
            if rank and len(rank) > 0:rank = f" - {rank}"
            if limit in cups:
                mess += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank} - {cups[limit]}\n"
            else:
                mess += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank}\n"
            limit += 1
        return mess
    def send_all_gap_status(OBJM):
        global USERS
        mess = MPro(f"وضعیت گروه 〔 {str(OBJM['INFOOBJECT']['name'])}  ",4)
        def myFunc(e):return e['mes']
        listMems , allMes = [] , 0
        list_users = USERS[OBJM['object_guid']]
        for mems in list_users:
            allMes += int(list_users[mems][0])
            listMems.append({'mes':int(list_users[mems][0]),'name':str(list_users[mems][2]),'guid':str(mems)})
        listMems.sort(reverse=True,key=myFunc)
        count_full_admins , count_admins , count_members , limit = 0 , 0 , 0 , 1
        count_all = len(listMems)
        for member in listMems:
            rank = validatUser(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,member['guid'])
            match rank:
                case 2:count_full_admins += 1
                case 1:count_admins += 1
            count_members += 1
            limit += 1

        now = f"{Date()} {Hour()}"
        time_oj = jdatetime.datetime.fromtimestamp(int(OBJM['INFOOBJECT']['date']))
        time_pass_activity = get_iran_timestamp()-int(OBJM['INFOOBJECT']['date'])
        mess += MPro(f"شروع فعایت : {str(time_oj)}")
        mess += MPro(f"زمان : {str(now)}")
        mess += MPro(send_timeout_group(OBJM,True))
        mess += MPro(f"مدت زمان فعالیت : {str(Time_pass(time_pass_activity))}")
        mess += '\n'
        mess += MPro(f"تعداد کل پیام ثبت شده : {str(OBJM['INFOOBJECT']['messages'])}")
        mess += MPro(f"تعداد کل پیام مجاز : {str(allMes)}")
        mess += MPro(f"تعداد جوین شده : {str(OBJM['INFOOBJECT']['join'])}")
        mess += MPro(f"تعداد افزوده شده : {str(OBJM['INFOOBJECT']['add'])}")
        mess += MPro(f"تعداد لفت داده : {str(OBJM['INFOOBJECT']['left'])}")
        mess += MPro(f"تعداد بن شده : {str(OBJM['INFOOBJECT']['ban'])}")        mess += MPro(f"تعداد ویسکال : {str(OBJM['INFOOBJECT']['voice_call'])}\n")
        mess += MPro(f"تعداد کاربران ویژه : {str(count_full_admins)}")
        mess += MPro(f"تعداد ادمین ها : {str(count_admins)}")
        mess += MPro(f"تعداد کاربران فعال : {str(count_members)}")
        mess += "\n"
        mess += 'برترین افراد ━━━━━━━━┅─\n\n'
        limit = 1
        cups = {1:'🥇',2:'🥈',3:'🥉'}
        for member in listMems:
            if limit > 3:break
            rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,member['guid'],True)
            countms , nickname , guid = member['mes'] , member['name'] , member['guid']
            if nickname == 'بدون لقب' or nickname == 'اراذل':
                getInfoUser(OBJM['object_guid'],guid,list_users[guid][3])
                nickname = list_users[guid][2]
            if rank and len(rank) > 0:rank = f" - {rank}"
            if limit in cups:
                mess += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank} - {cups[limit]}\n"
            else:
                mess += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank}\n"
            limit += 1
        return mess
    def send_status_users(OBJM):
        global USERS
        mess = MPro(f"امار اعضا 〔 {str(OBJM['INFOOBJECT']['name'])} 〕",4)

        def myFunc(e):return e['mes']
        listMems , allMes = [] , 0
        list_users = USERS[OBJM['object_guid']]
        for mems in list_users:
            allMes += int(list_users[mems][0])
            listMems.append({'mes':int(list_users[mems][0]),'name':str(list_users[mems][2]),'guid':str(mems)})
        mess += MPro(f"تعداد کل پیام ثبت شده : {str(OBJM['INFOOBJECT']['messages'])}")
        mess += MPro(f"تعداد کل پیام مجاز : {str(allMes)}\n")
        mess += 'به ترتیب تعداد پیام ها  ━━━━━━━━┅─\n\n'
        listMems.sort(reverse=True,key=myFunc)
        limit = 1
        cups = {1:'🥇',2:'🥈',3:'🥉'}
        for member in listMems:
            if limit > 100:break
            rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,member['guid'],True)
            countms , nickname , guid = member['mes'] , member['name'] , member['guid']
            if nickname == 'بدون لقب' or nickname == 'اراذل':
                getInfoUser(OBJM['object_guid'],guid,list_users[guid][3])
                time.sleep(0.5)
                nickname = list_users[guid][2]
            if rank and len(rank) > 0:rank = f" - {rank}"
            if limit in cups:
                mess += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank} - {cups[limit]}\n"
            else:
                mess += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank}\n"
            limit += 1
        return mess
    def send_status_all(OBJM):
        mess = MPro(f"امار کل 〔 {str(OBJM['INFOOBJECT']['name'])} 〕",4)
        def myFunc(e):return e['mes']
        listMems , allMes = [] , 0
        list_users = USERS[OBJM['object_guid']]
        for mems in list_users:
            allMes += int(list_users[mems][0])
            listMems.append({'mes':int(list_users[mems][0]),'name':str(list_users[mems][2]),'guid':str(mems)})
        mess += MPro(f"تعداد کل پیام ثبت شده : {str(OBJM['INFOOBJECT']['messages'])}")
        mess += MPro(f"تعداد کل پیام مجاز : {str(allMes)}")
        listMems.sort(reverse=True,key=myFunc)
        count_full_admins , count_admins , count_members , limit = 0 , 0 , 0 , 1
        count_all , manage_list = len(listMems) , ''
        for member in listMems:
            rank = validatUser(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,member['guid'])
            match rank:
                case 4:rank = 'سازنده 💀‍👑‍'
                case 3:rank = 'مالک ‍👑‍'
                case 2:
                    rank = 'ادمین ویژه ⭐'
                    count_full_admins += 1
                case 1:
                    rank = 'ادمین ✨'
                    count_admins += 1
                case _:rank = ''
            count_members += 1
            countms,nickname = member['mes'], member['name']
            if rank and len(rank) > 0:rank = f" - {rank}"
            manage_list += f"{str(limit)}.کاربر {nickname} با {str(countms)}{rank}\n"
            limit += 1

        mess += MPro(f"تعداد کاربران ویژه : {str(count_full_admins)}")
        mess += MPro(f"تعداد ادمین ها : {str(count_admins)}")
        mess += MPro(f"تعداد کاربران : {str(count_members)}")
        mess += MPro(f"تعداد کل : {str(count_all)}")
        caption = MPro(f"تعداد کاربران ویژه : {str(count_full_admins)}")        caption += MPro(f"تعداد ادمین ها : {str(count_admins)}")
        caption += MPro(f"تعداد کاربران : {str(count_members)}")
        caption += MPro(f"تعداد کل : {str(count_all)}")
        mess += '\nتعداد پیام ها  ━━━━━━━━┅─\n\n'
        mess += manage_list
        listMembers = 'listMembers.txt'
        with open(listMembers, "w" ,encoding="utf-8") as file:
            file.write(mess)
        client.send_file(OBJM['object_guid'],listMembers,OBJM['message_id'],caption)
    def arange_list_words(OBJM = None):
        global SPEAKX
        def myFunc(e):return len(e)
        for TIP in SPEAKX:
            SPEAK = SPEAKX[TIP]
            listManage = []
            for key in SPEAK:listManage.append(key)
            listManage.sort(reverse=True,key=myFunc)
            NSPEAK = {}
            for newkey in listManage:
                NSPEAK[newkey] = SPEAK[newkey]
            SPEAKX[TIP] = NSPEAK
        UPFILES(file_speakx,SPEAKX)
        if OBJM:return MPro(f"جملات ربات مرتب سازی شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_banner_gap(OBJM):
        global INFOS
        mess = OBJM['INFOOBJECT']['baner']
        if len(mess) == 0:mess = MPro(f"بنری ثبت نشده است.{OBJM['INFOOBJECT']['types']['ok']}",2)
        else:
            mess = MPro(f"بنر حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            INFOS[OBJM['object_guid']]['baner'] = ''
        return mess
    def send_ai_commands(OBJM):
        mess = MPro("هوش مصنوعی 💎",4)
        list_texts = Sorting(["پرسش سوال","ساخت عکس","ساخت لوگو","تبدیل متن به ویس","تبدیل متن به عکس"])
        for text in list_texts:
            mess += MPro(text,1)
        return mess
    def reset_timer_commands(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['AUTOS'] = []
        return MPro(f"لیست تایمر پاکسازی شد.{OBJM['INFOOBJECT']['types']['ok']}",2)
    def optimizing_source(OBJM):
        global USERS
        Alls , User , nums , deleting = 0 ,0 , 10 , []
        for user_guid in USERS[OBJM['object_guid']]:
            try:
                if user_guid == GUIDME:continue
                user = USERS[OBJM['object_guid']][user_guid]
                mes,war = user[0],user[1]
                state = mes-war
                if (state <= nums):
                    Alls += mes
                    User += 1
                    deleting.append(user_guid)
            except:pass
        for user_guid in deleting:
            USERS[OBJM['object_guid']].pop(user_guid)
        with open(file_users, "w") as outfile:
            json.dump(USERS, outfile)
        JoindUsers[OBJM['object_guid']] = []
        mess = MPro(f"کاربران با تعداد پیام کمتر از {str(nums)} از حافظه پاک شد. \nدر مجموع {str(Alls)} پیام و {str(User)} کاربر پاک شده است.{OBJM['INFOOBJECT']['types']['ok']}",2)
        return mess
    def reset_locks(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][18]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['locks'] = "1"*35
            return MPro(f"قفل ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def close_all_looks(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][18]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['locks'] = "0"*35
            return MPro(f"قفل ها بسته شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def open_all_looks(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][18]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['locks'] = "1"*35
            return MPro(f"قفل ها باز شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_commands(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][17]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['keys'] = "1"*90
            return MPro(f"دستورات ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def open_all_commands(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][17]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['keys'] = "1"*90
            return MPro(f"دستورات باز شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def close_all_commands(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][17]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['keys'] = "0"*90
            return MPro(f"دستورات بسته شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_rules(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['rols'] = "📜 قوانین گپ 〔 #اسم_گروه  〕 به شرح زیر میباشد.\n\n» احترام به کاربران\n» احترام به عقاید و فرهنگ ها\n» ارسال نکردن تبلیغات\n» ممبر دزدی نکردن\n» اسپم و محتوای نامناسب ارسال نکردن"
        return MPro(f"قوانین ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)

    def reset_main_keys(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['main_keys'] = ['ربات']
        return MPro(f"کلید ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_media_bye(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['bye'] = '🤲'
        return MPro(f"خدافظی ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_media_welcome(OBJM):
        INFOS[OBJM['object_guid']]['welcome'] = "+ به گپ 〔 #اسم_گروه   خوش آمدی عزیزم 💎✨\n- بمونی برامون +×)\n\n⏰ - » #زمان\n📆 - » #تاریخ"
        return MPro(f"خوشامدگویی ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_banner(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['banner'] = ''
        return MPro(f"بنر ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_symbol(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['types']['ok'] = '↺'
        return MPro(f"علامت ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_font_text(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['types']['font'] = 'natual'
        return MPro(f"قفل ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_shape_text(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['types']['type'] = 'natual'
        return MPro(f"شکل ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_dashboard(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][16]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['setting'] = "1"*35
            return MPro(f"داشبورد ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def open_dashboard(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][16]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['setting'] = "1"*35
            return MPro(f"داشبورد باز شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def close_dashboard(OBJM):
        global INFOS
        isok = True
        if OBJM['TIP'] <= 3 and int(OBJM['SETTING_KEYS'][16]) == 0:isok = False
        if isok:
            INFOS[OBJM['object_guid']]['setting'] = "0"*35
            return MPro(f"داشبورد بسته شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"دسترسی ندارید. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_setting(OBJM):
        global INFOS
        try:
            group_title = client.get_chat_info(OBJM['object_guid'])['group']['group_title']
            INFOS[OBJM['object_guid']]['name'] = group_title
        except:pass
        INFOS[OBJM['object_guid']]['welcome'] = "+ به گپ 〔 #اسم_گروه   خوش آمدی عزیزم 💎✨\n- بمونی برامون +×)\n\n⏰ - » #زمان\n📆 - » #تاریخ"
        INFOS[OBJM['object_guid']]['bye'] = '🤲'
        INFOS[OBJM['object_guid']]['rols'] = "📜 قوانین گپ 〔 #اسم_گروه  〕 به شرح زیر میباشد.\n\n» احترام به کاربران\n» احترام به عقاید و فرهنگ ها\n» ارسال نکردن تبلیغات\n» ممبر دزدی نکردن\n» اسپم و محتوای نامناسب ارسال نکردن"
        INFOS[OBJM['object_guid']]['setting'] = "1"*35
        INFOS[OBJM['object_guid']]['keys'] = "1"*90
        INFOS[OBJM['object_guid']]['locks'] = "1"*35
        INFOS[OBJM['object_guid']]['types']['ok'] = '↺'
        INFOS[OBJM['object_guid']]['types']['font'] = 'natual'
        INFOS[OBJM['object_guid']]['types']['type'] = 'natual'
        return MPro(f"تنظیمات ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def send_list_fulladmins(OBJM):
        mess , empty = MPro(f"لیست ویژه 〔 ⭐ 〕",4) , True
        for prs in OBJM['INFOOBJECT']['full_admins']:
            mess += MPro(f"کاربر {OBJM['INFOOBJECT']['full_admins'][prs]}")
            empty = False
        if empty:mess += MPro("لیست مدیران ویژه خالی میباشد.")
        return mess
    def send_list_silents(OBJM):
        mess , empty = MPro("لیست سکوت 〔 🔕 〕",4) , True
        for prs in OBJM['INFOOBJECT']['silent_list']:
            mess += MPro(f"کاربر {OBJM['INFOOBJECT']['silent_list'][prs]}")
            empty = False
        if empty:mess += MPro("لیست سکوت خالی میباشد.")
        return mess
    def send_list_exempts(OBJM):
        mess , empty = MPro("لیست معاف 〔 ❇️ 〕",4) , True
        for prs in OBJM['INFOOBJECT']['exempt_list']:
            mess += MPro(f"کاربر {OBJM['INFOOBJECT']['exempt_list'][prs]}")
            empty = False
        if empty:mess += MPro("لیست معاف خالی میباشد.")
        return mess
    def send_list_kills(OBJM):
        mess , empty = MPro("لیست کیل 〔 ☠️ 〕",4) , True
        for prs in OBJM['INFOOBJECT']['black_list']:
            state = OBJM['INFOOBJECT']['black_list'][prs][1]
            name = OBJM['INFOOBJECT']['black_list'][prs][0]
            if state == 1:state = '🫀'
            else:state = '💀'
            mess += MPro(f"کاربر {name} -{state}")
            empty = False
        if empty:mess += MPro("لیست کیل خالی میباشد.")
        return mess
    def send_list_filters(OBJM):
        mess , empty = MPro("لیست فیلتر 〔 📛 〕",4) , True
        for word in OBJM['INFOOBJECT']['filterlist']:
            word = Font_filter(word)
            mess += MPro(f"کلمه {word}")
            empty = False
        if empty:mess += MPro("لیست فیلتر خالی میباشد.")
        return mess
    def send_list_metadata(OBJM):
        mess = MPro("لیست متادیتا 〔 ❤️‍🔥 〕",4)
        mess += MPro(f"۱&متن تکی&۱")
        mess += MPro(f"۲&متن برجسته&۲")
        mess += MPro(f"۳&متن کج شده&۳")
        mess += MPro(f"۴&متن خط خورده&۴")
        mess += MPro(f"۵&متن زیر خط&۵")
        mess += MPro(f"۶&متن لینک دار&۶(لینک یا گوید)")
        mess += MPro(f"۷&متن اسپویلر&۷")
        return mess
    def send_list_keys(OBJM):
        mess , empty = MPro("لیست کلید 〔 🔑 〕",4) , True
        for word in OBJM['INFOOBJECT']['main_keys']:
            mess += MPro(f"کلمه {word}")
            empty = False
        if empty:mess += MPro("لیست کلید خالی میباشد.")
        return mess
    def send_list_admins(OBJM):
        mess , empty = MPro("لیست ادمین 〔 ✨ 〕",4) , True
        for prs in OBJM['INFOOBJECT']['admins']:
            mess += MPro(f"کاربر {OBJM['INFOOBJECT']['admins'][prs]}")
            empty = False
        if empty:mess += MPro("لیست ادمین ها خالی میباشد.")
        return mess
    def send_list_locks(OBJM):
        mess = MPro("لیست قفل 〔 🔓 ‍〕",4)
        locks_warning = list(OBJM['INFOOBJECT']['locks_warning'])
        locks_warning_show = list(OBJM['INFOOBJECT']['locks_warning_show'])
        locks_ban = list(OBJM['INFOOBJECT']['locks_ban'])
        for lock in Listlocks:
            key , res = Listlocks[lock] , ''
            if int(OBJM['LOCKS_KEYS'][key]) == 0:
                ison , isshow = '' , ''
                if locks_ban[key] == '0':ison = '🟢'
                if locks_warning_show[key] == '0':isshow = '🔇'
                res = f"〔 {locks_warning[key]} 〕 {ison}{isshow}"
            mess += MPro(f"{lock} {res}")
        return mess
    def send_list_joining(OBJM):
        mess = MPro("لیست عضویت 〔 ⚜️ ‍〕",4)
        channels = OBJM['INFOOBJECT']['channels']
        if len(channels) == 0:
            mess += MPro("لیست عضویت خالی میباشد.")
        else:
            for channel in channels:mess += MPro(channel)
        return mess
    def send_list_notes(OBJM):
        mess = MPro("لیست یادداشت 〔 💬 ‍〕 ",4)
        year,month,week,day,hour = Year(),Month(),Week(),Day(),Hour()
        mess += MPro(f"تاریخ : {hour} ⌯ {week} ⌯ {year}-{month}-{day}",2)
        mess += '\n─┅━━━━━━━┅─\n'
        rems = OBJM['INFOOBJECT']['remmember']
        if len(rems) == 0:mess += MPro("لیست یادداشت خالی میباشد.")
        else:
            m = 0
            for rem in rems:
                rem_text,rem_date = rem['text'],rem['date']
                year,month,week,day,hour = Year(rem_date),Month(rem_date),Week(rem_date),Day(rem_date),Hour(rem_date)
                time_pass = get_iran_timestamp()-rem_date
                str_time_pass = Time_pass(time_pass)
                mess += MPro(f"کد〔{str(m)}〕⌯ {str_time_pass} پیش")
                mess += MPro(f"{hour} ⌯ {week} ⌯ {year}-{month}-{day}")
                mess += MPro(rem_text)
                mess += '\n'
                m += 1
        return mess
    def send_list_timer(OBJM):
        mess , empty = MPro("لیست تایمر 〔 ⏰ 〕",4) , True
        m = 0
        for step in OBJM['INFOOBJECT']['AUTOS']:
            empty = False
            mess += MPro(f"کد〔{str(m)}〕")
            if 'is_loop' in step and not step['is_loop']:
                loop_mung , loop_mung_use = step['loop_mung'] , step['loop_mung_use']
                is_loop = f' ⌯ {loop_mung_use} ⇐ {loop_mung}'
            else:is_loop = ' ⌯ ↻'
            if step['TYPE'] == 'intime':
                hour = str(step['INTIME']['hour'])
                minute = str(step['INTIME']['minute'])
                mess += MPro(f"تایمر : {hour}:{minute} {is_loop}")
            elif step['TYPE'] == 'pertime':
                per = int(step['PERTIME']['per'])
                mess += MPro(f"تایمر : {Time_pass(per)} {is_loop}")
            coms = ''
            first_cmd = True
            for com in step['COMMANDS']:
                if first_cmd:
                    first_cmd = False
                    coms += com
                    continue
                coms += f" > {com}"
            mess += MPro(f"دستورات : {coms}\n")
            m += 1
        if empty:mess += MPro("دستوری تایمر بندی نشده است.")
        return mess
    def update_list_admins(OBJM):
        global INFOS
        has_continue , next_start_id , count , ADMINS = True , None , 0 , {}
        mess = MPro(f"درحال اپدیت...{OBJM['INFOOBJECT']['types']['ok']}",2)
        send_message(OBJM,mess,OBJM['message_id'])
        while has_continue:
            if OBJM['object_guid'] not in INFOS or not INFOS[OBJM['object_guid']]['state']:break
            result = client.get_admin_members(OBJM['object_guid'],next_start_id)
            time.sleep(0.2)
            has_continue = result['has_continue']
            if 'next_start_id' in result:next_start_id = result['next_start_id']
            for admin in result['in_chat_members']:
                count += 1
                if 'first_name' in admin:ADMINS[admin['member_guid']] = admin['first_name']
                else:ADMINS[admin['member_guid']] = 'بدون نام'

        INFOS[OBJM['object_guid']]['admins'] = ADMINS
        UPFILES(file_infos,INFOS)
        if count == 0:mess = MPro(f"لیست ادمین خالی است. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:mess = MPro(f"لیست ادمین اپدیت شد\nتعداد ادمین ها : {str(count)}",2)
        return mess
    def delete_managing_messages(OBJM):
        global STMessages
        if len(STMessages[OBJM['object_guid']]) > 0:
            messages_id , m = [] , 0
            for msid in STMessages[OBJM['object_guid']]:
                if m < 20:
                    messages_id.append(msid)
                    m += 1
                    continue
                m = 0
                try:client.delete_messages(OBJM['object_guid'],messages_id)
                except:pass
                messages_id = []
            if len(messages_id) > 0:
                try:client.delete_messages(OBJM['object_guid'],messages_id)
                except:pass
            STMessages[OBJM['object_guid']] = []
        return MPro(f"پیام مدیریتی حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def delete_robot_messages(OBJM):
        global ARMessages
        if len(ARMessages[OBJM['object_guid']]) > 0:
            client.delete_messages(OBJM['object_guid'],ARMessages[OBJM['object_guid']])
            ARMessages[OBJM['object_guid']] = []
        return MPro(f"پیام ربات حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def recheck_joining(OBJM):
        global CheckJoins
        if OBJM['object_guid'] not in CheckJoins:CheckJoins[OBJM['object_guid']] = {}
        else:CheckJoins[OBJM['object_guid']] = {}
        return MPro(f"عضویت مجدد بررسی میشود. {OBJM['INFOOBJECT']['types']['ok']}",2)

    def ban_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['admins']:return MPro(f"ایشون ادمین است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:
                    resetUser(user_guid,OBJM['object_guid'])
                    client.ban_member(OBJM['object_guid'],user_guid)
                except:pass
                INFOS[OBJM['object_guid']]['ban'] += 1
                first_name = check_name(OBJM['object_guid'],user_guid)
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) بن شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def pin_message_reply(OBJM):
        try:
            client.pin_message(OBJM['object_guid'],OBJM['is_reply_message'])
            return MPro(f"پین شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        except:return MPro(f"پین نمیتونم کنم. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_admin_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['admins']:return MPro(f"ایشون ادمین است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:client.set_admin(OBJM['object_guid'],user_guid,[],random.choice(BoxEmoji))
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                INFOS[OBJM['object_guid']]['admins'][user_guid] = first_name
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) ادمین شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def unadd_admin_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid  not in OBJM['INFOOBJECT']['admins']:return MPro(f"ایشون ادمین نیست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:client.unset_admin(OBJM['object_guid'],user_guid)
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                INFOS[OBJM['object_guid']]['admins'].pop(user_guid)
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) برکنار شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_silent_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['admins']:return MPro(f"ایشون ادمین است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                if user_guid in INFOS[OBJM['object_guid']]['silent_list']:
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) در لیست سکوت بود. {OBJM['INFOOBJECT']['types']['ok']}",2)
                else:
                    first_name = check_name(OBJM['object_guid'],user_guid)
                    INFOS[OBJM['object_guid']]['silent_list'][user_guid] = first_name
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) به لیست سکوت اضافه شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_exempt_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                first_name = check_name(OBJM['object_guid'],user_guid)
                if user_guid in INFOS[OBJM['object_guid']]['exempt_list']:
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) در لیست معاف بود. {OBJM['INFOOBJECT']['types']['ok']}",2)
                else:
                    INFOS[OBJM['object_guid']]['exempt_list'][user_guid] = first_name
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) به لیست معاف اضافه شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_kill_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['admins']:return MPro(f"ایشون ادمین است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                if user_guid in INFOS[OBJM['object_guid']]['black_list']:
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) در لیست کیل بود. {OBJM['INFOOBJECT']['types']['ok']}",2)
                else:
                    first_name = check_name(OBJM['object_guid'],user_guid)
                    INFOS[OBJM['object_guid']]['black_list'][user_guid] = [first_name,1]
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) به لیست کیل اضافه شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def give_warning_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                isadmin = False
                if user_guid in OBJM['INFOOBJECT']['admins']:isadmin = True
                count = INFOS[OBJM['object_guid']]['warnning']
                first_name = check_name(OBJM['object_guid'],user_guid)
                pscount = USERS[OBJM['object_guid']][user_guid][1]
                pscount += 1
                if pscount >= count:
                        if isadmin:
                            INFOS[OBJM['object_guid']]['admins'].pop(user_guid)
                            try:client.unset_admin(OBJM['object_guid'],user_guid)
                            except:pass
                        else:
                            USERS[OBJM['object_guid']][user_guid][1] = pscount
                            INFOS[OBJM['object_guid']]['ban'] += 1
                            try:
                                reply_message_banded_id = client.ban_member(OBJM['object_guid'],user_guid)['data']['chat_update']['chat']['last_message']['message_id']
                                resetUser(user_guid,OBJM['object_guid'])                                if int(OBJM['SETTING_KEYS'][8]):mess = INFOS[OBJM['object_guid']]['bye']
                            except:pass
                        if pscount == count:
                            try:
                                if int(OBJM['SETTING_KEYS'][6]):
                                        if isadmin:mess = MPro(f"کاربر @@ {first_name} @@({user_guid})〔{str(pscount)}/{str(count)}〕⚠️",2)
                                        else:mess = MPro(f"کاربر @@ {first_name} @@({user_guid})〔{str(pscount)}/{str(count)}〕🚫",2)
                            except:pass
                else:
                    USERS[OBJM['object_guid']][user_guid][1] = pscount
                    try:
                        if int(OBJM['SETTING_KEYS'][6]):
                            mess = MPro(f"کاربر @@ {first_name} @@({user_guid})〔{str(pscount)}/{str(count)}〕⚠️",2)
                    except:pass
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
        return mess
    def get_status_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                rank = formrank(Coder,OBJM['INFOOBJECT']['admins'],OBJM['INFOOBJECT']['full_admins'],OBJM['INFOOBJECT']['owner'],OWNER,user_guid)
                mess = MPro(f"مقام 〔 {rank} 〕",4)
                user = client.get_chat_info(user_guid)['user']
                mess += manage_info(user)
                if user_guid not in USERS[OBJM['object_guid']]:getInfoUser(OBJM['object_guid'],user_guid)
                mess += formInfo(USERS[OBJM['object_guid']][user_guid])
                mess += f"\n{MPro(user_guid)}\n─┅━━━━━━━┅─"
                if 'bio' in user:
                    mess += f"\n\n{user['bio']}"
                return mess
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def unban_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                try:
                    resetUser(user_guid,OBJM['object_guid'])
                    client.unban_member(OBJM['object_guid'],user_guid)
                except:return MPro(f"رفع محدودیت نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
                first_name = check_name(OBJM['object_guid'],user_guid)
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) رفع محدودیت شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_warning_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)                      
            if user_guid:
                resetUser(user_guid,OBJM['object_guid'])
                first_name = check_name(OBJM['object_guid'],user_guid)
                return MPro(f"اخطار @@ {first_name} @@({user_guid}) حدف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_silent_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                first_name = check_name(OBJM['object_guid'],user_guid)
                if user_guid in INFOS[OBJM['object_guid']]['silent_list']:
                    INFOS[OBJM['object_guid']]['silent_list'].pop(user_guid)
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) از لیست سکوت حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
                else:return MPro(f"کاربر @@ {first_name} @@({user_guid}) در لیست سکوت یافت نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_exempt_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                first_name = check_name(OBJM['object_guid'],user_guid)
                if user_guid in INFOS[OBJM['object_guid']]['exempt_list']:
                    INFOS[OBJM['object_guid']]['exempt_list'].pop(user_guid)
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) از لیست معاف حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
                else:return MPro(f"کاربر @@ {first_name} @@({user_guid}) در لیست معاف یافت نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_kill_user_reply(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                first_name = check_name(OBJM['object_guid'],user_guid)
                if user_guid in INFOS[OBJM['object_guid']]['black_list']:
                    INFOS[OBJM['object_guid']]['black_list'].pop(user_guid)
                    return MPro(f"کاربر @@ {first_name} @@({user_guid}) از لیست کیل حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
                else:return MPro(f"کاربر @@ {first_name} @@({user_guid}) در لیست کیل یافت نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_nickname_user_reply(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:USERS[OBJM['object_guid']][user_guid] = [0,0,message_info['text'],'ناشناس']
                else:USERS[OBJM['object_guid']][user_guid][2] = message_info['text']
                return MPro(f"لقب ثبت شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_nickname_user_reply(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:USERS[OBJM['object_guid']][user_guid] = [0,0,'بدون لقب','ناشناس']
                else:USERS[OBJM['object_guid']][user_guid][2] = 'بدون لقب'
                return MPro(f"لقب حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def update_group(OBJM):
        global INFOS
        group_title = client.get_chat_info(OBJM['object_guid'])['group']['group_title']
        INFOS[OBJM['object_guid']]['name'] = group_title
        return MPro(f"اطلاعات گروه اپدیت شد. {OBJM['INFOOBJECT']['types']['ok']}",2)

    def add_info_user_reply(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:USERS[OBJM['object_guid']][user_guid] = [0,0,'بدون لقب',message_info['text']]
                else:USERS[OBJM['object_guid']][user_guid][3] = message_info['text']
                return MPro(f"اصل ثبت شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def remove_info_user_reply(OBJM):
        global USERS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid:
                if user_guid not in USERS[OBJM['object_guid']]:USERS[OBJM['object_guid']][user_guid] = [0,0,'بدون لقب','ناشناس']
                else:USERS[OBJM['object_guid']][user_guid][3] = 'ناشناس'                return MPro(f"اصل حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def set_welcome_message_reply(OBJM):
        global INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            tag_media = ''
            result = save_media_pro(OBJM,True)
            if result:tag_media = f"#{result}"
            INFOS[OBJM['object_guid']]['welcome'] = (f"{message_info['text']} {tag_media}").strip()
            return MPro(f"خوشامدگویی تنظیم شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def set_bye_message_reply(OBJM):
        global INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            tag_media = ''
            result = save_media_pro(OBJM,True)
            if result:tag_media = f"#{result}"
            INFOS[OBJM['object_guid']]['bye'] = (f"{message_info['text']} {tag_media}").strip()
            return MPro(f"خدافظی تنظیم شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def set_rules_group_reply(OBJM):
        global INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            tag_media = ''
            result = save_media_pro(OBJM,True)
            if result:tag_media = f"#{result}"
            INFOS[OBJM['object_guid']]['rols'] = (f"{message_info['text']} {tag_media}").strip()
            return MPro(f"قوانین تنظیم شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_banner_reply(OBJM):
        global INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            INFOS[OBJM['object_guid']]['baner'] = message_info['text']
            return MPro(f"بنر تنظیم شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)

    def left_form_group(OBJM):
        leave_from_group(client,OBJM['object_guid'])
        time.sleep(0.2)
        try:client.send_text(OBJM['guid_sender'],MPro(f"لفت دادم. {OBJM['INFOOBJECT']['types']['ok']}",2))
        except:pass
        return False
    def reset_bot_group(OBJM):
        global INFOS,USERS,SPEAKX,LSMessage,ARMessages,STMessages,Spam,JoindUsers,CheckJoins
        if OBJM['object_guid'] in INFOS:INFOS.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in USERS:USERS.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in LSMessage:LSMessage.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in ARMessages:ARMessages.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in STMessages:STMessages.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in Spam:Spam.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in JoindUsers:JoindUsers.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in CheckJoins:CheckJoins.pop(OBJM['object_guid'])

        UPFILES(file_infos,INFOS)
        UPFILES(file_users,USERS)
        UPFILES(file_speakx,SPEAKX)
        client.send_text(OBJM['object_guid'],MPro(f"تمام اطلاعات ربات پاک شد. {OBJM['INFOOBJECT']['types']['ok']}",2),OBJM['message_id'])
        return False
    def reset_info_group(OBJM):
        global INFOS,LSMessage,ARMessages,STMessages,Spam,JoindUsers,CheckJoins
        if OBJM['object_guid'] in INFOS:INFOS.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in LSMessage:LSMessage.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in ARMessages:ARMessages.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in STMessages:STMessages.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in Spam:Spam.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in JoindUsers:JoindUsers.pop(OBJM['object_guid'])
        if OBJM['object_guid'] in CheckJoins:CheckJoins.pop(OBJM['object_guid'])

        UPFILES(file_infos,INFOS)
        client.send_text(OBJM['object_guid'],MPro(f"تمام اطلاعات گروه پاک شد. {OBJM['INFOOBJECT']['types']['ok']}",2),OBJM['message_id'])
        return False
    def reset_users_group(OBJM):
        global USERS
        USERS[OBJM['object_guid']] = {}
        UPFILES(file_users,USERS)
        return MPro(f"تمام امار گروه ریست شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def reset_words(OBJM):
        global SPEAKX
        SPEAKX = {}
        UPFILES(file_speakx,SPEAKX)
        return MPro(f"کلمات سخنگوی شخصی حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def send_reset_bot_group_message(OBJM):
        return MPro("🛑 درصورت ریست کردن ربات تمام اطلاعات ربات ( امار گپ و اطلاعات گپ ) پاک خواهد شد!\n\nاگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.\n",2)+MPro("``RESETBOT ``")
    def send_reset_info_group_message(OBJM):
        return MPro("🛑 اگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.\n",2)+MPro("``RESETINFO ``")
    def send_reset_users_group_message(OBJM):
        return MPro("🛑 اگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.\n",2)+MPro("``RESETUSERS ``")
    def send_reset_words_message(OBJM):
        return MPro("🛑 درصورت ریست کردن کلمات تمام کلمات سخنگو شخصی پاک خواهد شد!\n\nاگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.\n",2)+MPro("``RESETWORDS ``")
    def send_list_words(OBJM):
        mess = MPro("لیست کلمات",4)
        caption , nkeys , nans = mess , 0 , 0
        for TIP_ANS in SPEAKX:
            SPEAK = SPEAKX[TIP_ANS]
            rank = Rank_user(TIP_ANS,OBJM)
            for word in SPEAK:
                nkeys += 1
                nans += int(len(SPEAK[word]))
                empty = False
                mess += '\n'
                if TIP_ANS.startswith('u0'):
                    mess += MPro(f"{word} - @@{rank}@@({TIP_ANS})",2)
                else:
                    mess += MPro(f"{word} - {rank}",2)
                mess += '\n'
                for step in SPEAK[word]:
                    if 'answer' in step:
                        mess += MPro(step['answer'])
                    if 'actions' in step:
                        form_actions = ''
                        for action in step['actions']:
                            if len(form_actions) > 0:form_actions += f" - {action}"
                            else:form_actions += f"{action}"
                        if len(form_actions) > 0:
                            mess += MPro(form_actions,4)
                mess += '\n'

        caption += MPro(f"کلیدواژه : 〔 {str(nkeys)} 〕",1)
        caption += MPro(f"جواب : 〔 {str(nans)} 〕",1)
        lword = 'listWords.txt'
        with open(lword, "w" ,encoding="utf-8") as file:
            file.write(mess)
        try:client.send_file(OBJM['object_guid'],lword,OBJM['message_id'],caption)
        except:return MPro(f"ظاهرا همچین فایلی وجود ندارد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def send_file_words(OBJM):
        try:client.send_file(OBJM['object_guid'],file_speakx,OBJM['message_id'],'فایل کلمات شخصی')
        except:return MPro(f"ظاهرا همچین فایلی وجود ندارد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def send_file_users(OBJM):
        try:client.send_file(OBJM['object_guid'],file_users,OBJM['message_id'],'فایل امار')
        except:return MPro(f"ظاهرا همچین فایلی وجود ندارد {OBJM['INFOOBJECT']['types']['ok']}",2)
    def send_file_infos(OBJM):
        try:client.send_file(OBJM['object_guid'],file_infos,OBJM['message_id'],'فایل گروه')
        except:return MPro(f"ظاهرا همچین فایلی وجود ندارد {OBJM['INFOOBJECT']['types']['ok']}",2)
    def deleting_fulladmins_group(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['full_admins'] = {}
        return MPro(f"لیست ویژه پاکسازی شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def deleting_blacklist_group(OBJM):
        global INFOS
        has_continue , next_start_id = True , None
        mess = MPro(f"درحال پاکسازی... {OBJM['INFOOBJECT']['types']['ok']}",2)
        send_message(OBJM,mess,OBJM['message_id'])
        listBannded , count = [] , 0
        while has_continue:
            if OBJM['object_guid'] not in INFOS or not INFOS[OBJM['object_guid']]['state']:break
            result = client.get_banned_members(OBJM['object_guid'],next_start_id)
            time.sleep(0.2)
            listBannded = result['in_chat_members']
            for x in listBannded:
                member_guid = x['member_guid']
                try:
                    resetUser(member_guid,OBJM['object_guid'])
                    client.unban_member(OBJM['object_guid'],member_guid)                except:pass
            count += len(listBannded)
            listBannded , has_continue = [] , result['has_continue']
            if 'next_start_id' in result:next_start_id = result['next_start_id']

        if count == 0:return MPro(f"لیست سیاه خالی است. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"لیست سیاه پاکسازی شد\nتعداد پاک شده : {str(count)}",2)
    def updat_data_bot(OBJM = None):
        global INFOS,USERS,SPEAKX
        UPFILES(file_infos,INFOS)
        UPFILES(file_users,USERS)
        UPFILES(file_speakx,SPEAKX)
        if OBJM:return MPro(f"دیتا سیو شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def backup_data_bot(OBJM = None):
        global INFOS,USERS,SPEAKX
        UPFILES('backup_INFOS.json',INFOS)
        UPFILES('backup_USERS.json',USERS)
        UPFILES('backup_SPEAKX.json',SPEAKX)
        if OBJM:return MPro(f"بکاپ از فایل ها گرفته شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def list_media_form(OBJM):
        mess = MPro("لیست رسانه",4)
        mess += MPro('لیست گیف',2)
        mess += MPro('لیست ویس',2)
        mess += MPro('لیست اهنگ',2)
        mess += MPro('لیست عکس',2)
        mess += MPro('لیست فیلم',2)
        return mess
    def list_tag_form(OBJM):
        mess = MPro("لیست تگ ها",4)

        mess += MPro('#اسم_کاربر'+' / '+'#اسم',2)
        mess += MPro('#اسم_گروه'+' / '+'#اسم_گپ',2)
        mess += MPro('#اسم_ریپلای',2)
        mess += MPro('#اسم_ربات',2)
        mess += MPro('#اسم_سازنده',2)
        mess += MPro('#اسم_مالک',2)
        mess += MPro('#اسم_تصادفی',2)
        mess += MPro('#لینک_گروه'+' / '+'#لینک_گپ',2)
        mess += MPro('#گوید_کاربر'+' / '+'#گوید',2)
        mess += MPro('#گوید_گروه'+' / '+'#گوید_گپ',2)
        mess += MPro('#گوید_ریپلای',2)
        mess += MPro('#گوید_ربات',2)
        mess += MPro('#گوید_سازنده',2)
        mess += MPro('#گوید_مالک',2)
        mess += MPro('#گوید_تصادفی',2)
        mess += MPro('#عدد_تصادفی'+' / '+'#عدد',2)
        mess += MPro('#درصد_تصادفی'+' / '+'#درصد',2)
        mess += MPro('#تاریخ',2)
        mess += MPro('#ساعت',2)
        mess += MPro('#سال',2)
        mess += MPro('#هفته',2)
        mess += MPro('#ماه',2)
        mess += MPro('# user_guid',2)
        return mess
    def delete_shap_end_orders(OBJM):
        global INFOS
        INFOS[OBJM['object_guid']]['types']['ok'] = ''
        return MPro(f"علامت حذف شد.",2)
    def add_fulladmin_form_goldadmin(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"شما مالک من هستید. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:
                    resetUser(user_guid,OBJM['object_guid'])
                    client.set_admin(OBJM['object_guid'],user_guid,[],random.choice(BoxEmoji))
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                INFOS[OBJM['object_guid']]['full_admins'][user_guid] = first_name
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) ادمین ویژه شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def unadmin_user_form_goldadmin(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"شما مالک من هستید. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid not in OBJM['INFOOBJECT']['full_admins'] and user_guid not in OBJM['INFOOBJECT']['admins']:return MPro(f"مقامی ندارد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:client.unset_admin(OBJM['object_guid'],user_guid)
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                if user_guid in OBJM['INFOOBJECT']['full_admins']:INFOS[OBJM['object_guid']]['full_admins'].pop(user_guid)
                if user_guid in OBJM['INFOOBJECT']['admins']:INFOS[OBJM['object_guid']]['admins'].pop(user_guid)
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) برکنار شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def deleting_all_warnings(OBJM):
        global USERS
        for user_guid in USERS[OBJM['object_guid']]:
            USERS[OBJM['object_guid']][user_guid][1] = 0
        return MPro(f"تمام اخطار های کاربران حذف شد. {OBJM['INFOOBJECT']['types']['ok']}",2)

    def add_fulladmin_form_owner(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"ایشون سازنده من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"ایشون مالک من هست. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid == GUIDME:return MPro(f"ایشون من هستم. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid in OBJM['INFOOBJECT']['full_admins']:return MPro(f"ایشون ادمین ویژه است. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:client.set_admin(OBJM['object_guid'],user_guid,[],random.choice(BoxEmoji))
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                INFOS[OBJM['object_guid']]['full_admins'][user_guid] = first_name
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) ادمین ویژه شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def add_goldadmin_from_owner(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"شما سازنده من هستید. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:client.set_admin(OBJM['object_guid'],user_guid,[],random.choice(BoxEmoji))
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                INFOS[OBJM['object_guid']]['owner'] = user_guid
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) مالک شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)
    def unadmin_user_form_owner(OBJM):
        global USERS,INFOS
        message_info = GetInfoByMessageId(OBJM['object_guid'],OBJM['is_reply_message'])
        if message_info:
            user_guid = GetReplyGuid(message_info)
            if user_guid == OWNER:return MPro(f"شما سازنده من هستید. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid not in OBJM['INFOOBJECT']['full_admins'] and user_guid not in OBJM['INFOOBJECT']['admins'] and not user_guid == OBJM['INFOOBJECT']['owner']:return MPro(f"مقامی ندارد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            elif user_guid:
                try:client.unset_admin(OBJM['object_guid'],user_guid)
                except:pass
                first_name = check_name(OBJM['object_guid'],user_guid)
                if user_guid == OBJM['INFOOBJECT']['owner']:INFOS[OBJM['object_guid']]['owner'] = OWNER
                if user_guid in OBJM['INFOOBJECT']['full_admins']:INFOS[OBJM['object_guid']]['full_admins'].pop(user_guid)
                if user_guid in OBJM['INFOOBJECT']['admins']:INFOS[OBJM['object_guid']]['admins'].pop(user_guid)
                return MPro(f"کاربر @@ {first_name} @@({user_guid}) برکنار شد. {OBJM['INFOOBJECT']['types']['ok']}",2)
            else:return MPro(f"کاربر شناسایی نشد. {OBJM['INFOOBJECT']['types']['ok']}",2)
        else:return MPro(f"روی پیام پاک شده ریپلای زدی. {OBJM['INFOOBJECT']['types']['ok']}",2)

    def sum_tuples(tuple1,tuple2):
        list_1 , list_2 = list(tuple1) , list(tuple2)
        for step in list_2:
            if step not in list_1:list_1.append(step)
        return tuple(list_1)
    def sum_dictionary(list1,list2):
        for command in list2:
            if command not in list1:list1[command] = list2[command]
        return list1
    def insert_keys_in_tuple(dics:list):
        new = []
        for dic in dics:
            for step in dic:new.append(step)
        return tuple(new)

    list_command_owner_reply = {
        'ویژه':add_fulladmin_form_owner,'مالک':add_goldadmin_from_owner,'برکناری':unadmin_user_form_owner
    }

    list_command_owner = {
        'لفت':left_form_group,'RESETBOT':reset_bot_group,'RESETINFO':reset_info_group,
        'RESETUSERS':reset_users_group,'RESETWORDS':reset_words,'ریست ربات':send_reset_bot_group_message,
        'بازنشانی ربات':send_reset_bot_group_message,'ریست گپ':send_reset_info_group_message,
        'بازنشانی گپ':send_reset_info_group_message,'ریست گروه':send_reset_info_group_message,
        'بازنشانی گروه':send_reset_info_group_message,'ریست امار':send_reset_users_group_message,
        'بازنشانی امار':send_reset_users_group_message,'ریست کلمات':send_reset_words_message,
        'بازنشانی کلمات':send_reset_words_message,'لیست کلمات':send_list_words,'فایل کلمات':send_file_words,
        'بکاپ کلمات':send_file_words,'فایل امار':send_file_users,'بکاپ امار':send_file_users,
        'فایل گپ':send_file_infos,'بکاپ گپ':send_file_infos,'فایل گروه':send_file_infos,
        'بکاپ گروه':send_file_infos,'اپدیت دیتا':updat_data_bot,'دیتا سیو':updat_data_bot,'بکاپ دیتا':backup_data_bot,
        'لیست رسانه':list_media_form,'لیست مدیا':list_media_form,'سیو':save_media_pro,
        'حذف شارژ گروه':delete_timeout_group,'ریست تنظیمات':reset_setting
    }

    list_command_goldadmin_reply = {
        'ویژه':add_fulladmin_form_goldadmin,'برکناری':unadmin_user_form_goldadmin
    }

    list_command_goldadmin = {
        'پاکسازی لیست ویژه':deleting_fulladmins_group,'پاکسازی لیست سیاه':deleting_blacklist_group,'پاکسازی لیست بن':deleting_blacklist_group,
        'حذف تمام اخطارها':deleting_all_warnings,'حذف تمام اخطار ها':deleting_all_warnings,'شارژ گروه':send_timeout_group
    }

    list_command_fulladmins_reply = {
        'بن':ban_user_reply,'پین':pin_message_reply,'ارتقا':add_admin_reply,'برکناری':unadd_admin_reply,'سکوت':add_silent_user_reply,'معاف':add_exempt_user_reply,'کیل':add_kill_user_reply,
        'اخطار':give_warning_user_reply,'امار':get_status_user_reply,'رفع محدودیت':unban_user_reply,'حذف اخطار':remove_warning_user_reply,
        'حذف سکوت':remove_silent_user_reply,'حذف معاف':remove_exempt_user_reply,'حذف کیل':remove_kill_user_reply,'تنظیم خوشامدگویی':set_welcome_message_reply,'طول پیام':message_length,
        'تنظیم خدافظی':set_bye_message_reply,'تنظیم قوانین':set_rules_group_reply,'تنظیم لقب':add_nickname_user_reply,'تنظیم اصل':add_info_user_reply,'Info':message_infos,
        'ثبت لقب':add_nickname_user_reply,'ثبت اصل':add_info_user_reply,'حذف لقب':remove_nickname_user_reply,'حذف اصل':remove_info_user_reply,'تنظیم بنر':add_banner_reply
    }

    list_command_fulladmins = {
        'کال':make_voice_call,'ویسکال':make_voice_call,'امارم':send_full_info_me,'تنظیم':send_setting_commands,'امار':send_status_commands,
        'ریست':send_reset_commands,'سرگرمی':send_games_commands,'تنظیمات':send_panel_setting,'پنل':send_panel_setting,'گزارشات':send_reports_gap,'نصب کتابخونه':install_pro_libs,
        'داشبورد':send_dashboard,'لیست':send_list_lists,'امار گپ':send_status_gap,'امار گروه':send_status_gap,'امار اعضا':send_status_users,'امار کل':send_status_all,'نصب کتابخونه ها':install_pro_libs,
        'مرتب سازی':arange_list_words,'حذف بنر':remove_banner_gap,'هوش مصنوعی':send_ai_commands,'پاکسازی تایمر':reset_timer_commands,'نصب لایب ها':install_pro_libs,'نصب لایب':install_pro_libs,
        'بهینه سازی':optimizing_source,'ریست داشبورد':reset_dashboard,'ریست قفل':reset_locks,'ریست قفل ها':reset_locks,'ریست دستورات':reset_commands,'ریست قوانین':reset_rules,
        'ریست خدافظی':reset_media_bye,'ریست خوشامدگویی':reset_media_welcome,'ریست بنر':reset_banner,'ریست علامت':reset_symbol,'ریست فونت':reset_font_text,'ریست کلید':reset_main_keys,
        'ریست شکل':reset_shape_text,'لیست ویژه':send_list_fulladmins,'لیست سکوت':send_list_silents,'لیست معاف':send_list_exempts,'لیست کیل':send_list_kills,'لیست کلید':send_list_keys,'ریست لیست کلید':reset_main_keys,        'لیست فیلتر':send_list_filters,'لیست متادیتا':send_list_metadata,'لیست ادمین':send_list_admins,'لیست قفل':send_list_locks,'لیست عضویت':send_list_joining,'لیست یادداشت':send_list_notes,
        'لیست تایمر':send_list_timer,'اپدیت لیست ادمین':update_list_admins,'حذف پیام مدیریتی':delete_managing_messages,'حذف پیام ربات':delete_robot_messages,
        'بررسی مجدد عضویت':recheck_joining,'بررسی عضویت مجدد':recheck_joining,'اپدیت گروه':update_group,'باز کردن قفل ها' :open_all_looks,'بستن قفل ها' :close_all_looks,'باز کردن دستورات':open_all_commands,
        'بستن دستورات':close_all_commands,'باز کردن داشبورد':open_dashboard,'بستن داشبورد':close_dashboard,'لیست تگ':list_tag_form,'لیست تگ ها':list_tag_form,
        'حذف علامت':delete_shap_end_orders,'وضعیت گروه':send_all_gap_status,'وضعیت گپ':send_all_gap_status
    }

    list_command_users_reply = {
        'کشیده':send_text_keshideh,'لش':send_text_lash,'شکسته':send_text_shekasteh,'لقب':send_your_laqab,'لقبش':send_your_laqab,
        'اصل':send_your_asl,'اصلش':send_your_asl,'مقام':send_your_maqam,'مقامش':send_your_maqam,'گوید':send_your_guid,
        'گویدش':send_your_guid,'اینفو':send_your_info,'امار':send_your_info,'امارش':send_your_info,'اینفوش':send_your_info,
        'تعداد پیام':send_your_count_messages,'تعداد پیامش':send_your_count_messages,'تعداد اخطار':send_your_count_warnings,'تعداد اخطارش':send_your_count_warnings
    }

    list_command_users = {
        'اینفو':get_info_user_1,'اینفوم':get_info_user_1,'امارم':get_info_user_1,'امار':get_info_user_1,'تاس':send_tas,'ورژن':send_version,
        'نسخه':send_version,'لینک':get_link_gap,'تاریخ':get_full_date,'تقویم':get_full_date,'ساعت':get_clock,'مالک':get_mention_malek,
        'گوید گپ':get_guid_group,'گوید گروه':get_guid_group,'سکه':send_seckeh,'جوک':send_api_jock,'چالش':send_api_chalesh,'بیو':send_api_bio,'فکت':send_api_fact,
        'اعتراف':send_api_etraf,'دانستنی':send_api_danestani,'داستان':send_api_dastan,'تکست':send_api_textmod,'گنگ':send_api_gang,
        'انگیزشی':send_api_angizeshi,'ذکر':send_api_zekr,'فال':send_api_fal,'لقب':send_nickname_me,'اصل':send_asl_me,'اصلم':send_asl_me,
        'مقام':send_maqam_me,'مقامم':send_maqam_me,'گوید':send_guid_me,'گویدم':send_guid_me,'خوشامدگویی':send_media_welcom,'خدافظی':send_media_bye,
        'بنر':send_banner,'قوانین':send_rules,'محدودیت':send_limites,'سازنده':send_maqam_maker,'پروفایل':send_api_profile,'بکگراند':send_api_background,
        'والپیپر':send_api_background,'پروکسی':send_api_procsy,'فتوگرافی':send_api_photography,'ارز':send_api_arz,'دقت':send_api_deghat,'حق':send_api_hagh,
        'فال حافظ':send_api_fal_hafez,'عدد شانسی':send_random_number,'تعداد پیام':send_count_messages_me,'تعداد اخطار':send_count_warnning_me,
        'تعداد پیامم':send_count_messages_me,'تعداد اخطارم':send_count_warnning_me,'پ ن پ':send_api_pnp
    }

    list_filter_metadata = ('لیست متادیتا')

    list_command_users_all = insert_keys_in_tuple([list_command_users,list_command_users_reply])
    list_command_users_reply_keys = insert_keys_in_tuple([list_command_users_reply])
    list_command_users_keys = insert_keys_in_tuple([list_command_users])    list_command_fulladmins_reply_keys = insert_keys_in_tuple([list_command_fulladmins_reply])
    list_command_fulladmins_keys = insert_keys_in_tuple([list_command_fulladmins])
    list_command_goldadmin_reply_keys = insert_keys_in_tuple([list_command_goldadmin_reply])
    list_command_goldadmin_keys = insert_keys_in_tuple([list_command_goldadmin])
    list_command_owner_reply_keys = insert_keys_in_tuple([list_command_owner_reply])
    list_command_owner_keys = insert_keys_in_tuple([list_command_owner])    list_command_goldadmin = sum_dictionary(list_command_goldadmin,list_command_fulladmins)
    list_command_goldadmin_reply = sum_dictionary(list_command_goldadmin_reply,list_command_fulladmins_reply)
    list_command_goldadmin_keys = sum_tuples(list_command_goldadmin_keys,list_command_fulladmins_keys)
    list_command_goldadmin_reply_keys = sum_tuples(list_command_goldadmin_reply_keys,list_command_fulladmins_reply_keys)
    list_command_owner = sum_dictionary(list_command_owner,list_command_goldadmin)
    list_command_owner_reply = sum_dictionary(list_command_owner_reply,list_command_goldadmin_reply)
    list_command_owner_keys = sum_tuples(list_command_owner_keys,list_command_goldadmin_keys)
    list_command_owner_reply_keys = sum_tuples(list_command_owner_reply_keys,list_command_goldadmin_reply_keys)
    list_command_owner = sum_dictionary(list_command_owner,list_command_users)
    list_command_owner_reply = sum_dictionary(list_command_owner_reply,list_command_users_reply)
    list_command_owner_keys = sum_tuples(list_command_owner_keys,list_command_users_keys)
    list_command_owner_reply_keys = sum_tuples(list_command_owner_reply_keys,list_command_users_reply_keys)

    def commands_colection(client,object_guid,guid_sender,update_message,istimer = False):
        try:
            global INFOS,USERS,OWNER,SPEAKX,PROTECTED,Spam,LSMessage,ARMessages,STMessages,CheckJoins,JoindUsers,TimeMessages,limitAPI,typespeak
            message_info = update_message.get('message')
            message_type = message_info.get('type')
            command = message_info.get('text')

            if istimer:
                is_reply_message , message_id , event_data , metadata = None , None , None , None
                is_forward = False
            else:
                is_reply_message = message_info.get('reply_to_message_id')
                message_id = update_message.get('message_id')
                event_data = message_info.get('event_data')
                metadata = message_info.get('metadata')
                is_forward = message_info.get('forwarded_from')

            if 'file_inline' in message_info:message_type = message_info.get('file_inline').get('type')

            if event_data:
                event_type = event_data.get('type')
                if not guid_sender:
                    performer_object = event_data.get('performer_object')
                    if performer_object:guid_sender = performer_object.get('object_guid')

            if command:
                lower_command = command.lower()
                if command.endswith('-'):command , silentMod = command[:-1].strip() , True
                else:silentMod = False
                if command.endswith('+'):command = f"{command[:-1].strip()}-"
                command = command.replace('آ','ا')
                if '&' in command:
                    tags = {'1':'``','2':'**','_':'__','3':'~~','4':'--','5':'##','6':'@@'}
                    for tag in tags:
                        command = command.replace(f"&{tag}",tags[tag])
                wordCount = command.count(" ")
                command = supper_command(command)
            else:lower_command , silentMod = False , False

            ResultME,ismanagerms = False,True

            #GET GAP INFO
            INFOOBJECT = INFOS[object_guid]

            HOWNER , FULL_ADMINS , ADMINS , ST , SETTING_KEYS , LOCKS_KEYS , FILTERLIST = INFOOBJECT['owner'] , INFOOBJECT['full_admins'] , INFOOBJECT['admins'] , INFOOBJECT['types'] , list(INFOOBJECT['setting']) , list(INFOOBJECT['locks']) , INFOOBJECT['filterlist']

            ORDERS_KEYS = list(INFOOBJECT['keys'])

            # VALIDATE USER
            if guid_sender == Coder:TIP = 4
            elif guid_sender == OWNER:TIP = 4
            elif guid_sender == HOWNER:TIP = 3
            elif guid_sender in FULL_ADMINS:TIP = 2
            elif guid_sender in ADMINS:TIP = 1
            else:TIP = 0

            dopin = False
            if TIP >= 2 and command:
                if "-پین" in command:
                    dopin = True
                    command = command.replace("-پین",'').strip()
                if "+پین" in command:
                    command = command.replace("+پین","-پین").strip()

            OBJM = {
                'INFOOBJECT': INFOOBJECT,
                'guid_sender': guid_sender,
                'object_guid': object_guid,
                'message_id': message_id,
                'LOCKS_KEYS': LOCKS_KEYS,
                'SETTING_KEYS': SETTING_KEYS,
                'ORDERS_KEYS': ORDERS_KEYS,
                'is_reply_message': is_reply_message,
                'ismanagerms': ismanagerms,
                'istimer': istimer,
                'silentMod': silentMod,
                'TIP':TIP
            }

            # IS ACTIVE OR NOT
            if TIP >= 3:
                if command:
                    match command:
                        case 'غیر فعال' | 'غیرفعال':
                            if INFOOBJECT['state']:
                                send_message(OBJM,'ربات غیرفعال شد.',message_id)
                                INFOOBJECT['state'] = False
                                UPFILES(file_infos,INFOS)
                                return True
                            else:
                                send_message(OBJM,'ربات از قبل غیرفعال بود.',message_id)
                                return True
                        case 'فعال':
                            if not object_guid in USERS:USERS[object_guid] = {}
                            if not INFOOBJECT['state']:
                                send_message(OBJM,'ربات فعال شد.',message_id)
                                INFOS[object_guid]['state'] = True
                                UPFILES(file_infos,INFOS)
                                return True
                            elif INFOOBJECT['state']:
                                send_message(OBJM,'ربات از قبل فعال بود.',message_id)
                                return True

                    if not INFOOBJECT['state']:return True

                    if lower_command.startswith('multi commands'):
                        commands = command.replace('multi commands','').strip()
                        commands = commands.replace('Multi commands','').strip()
                        commands = commands.replace('آ','ا')
                        commands = commands.split('\n')
                        multi_commands = []
                        for cmd in commands:
                            multi_commands.append(f"{cmd} -")
                        for command in multi_commands:
                            update_message['message']['text'] = command
                            commands_colection(client,object_guid,guid_sender,update_message,True)
                        mess = MPro(f"دستورات اجرا شد. {ST['ok']}",2)
                        send_message(OBJM,mess,message_id)
                        return True

            if not INFOOBJECT['state']:return True

            isok = True

            #KILL LIST
            if guid_sender in INFOOBJECT['black_list'] and TIP <= 1:
                client.ban_member(object_guid,guid_sender)
                INFOOBJECT['black_list'][guid_sender][1] = 0
                first_name = INFOOBJECT['black_list'][guid_sender][0]
                mess = MPro(f"کاربر @@ {first_name} @@({guid_sender}) کیل شد. {ST['ok']}",2)
                ResultME = send_message(OBJM,mess,message_id)
                isok = False

            # CHECK DATA TYPE AND DELETE BAD MESSAGE AND SAVE REPORTS AND IF IS LINK CONTINIO
            if TIP <= 1:
                # CHECK DATA TYPE
                reports = {}

                if is_forward:reports[9] = 'فوروارد'
                if command:
                    if '.ir' in lower_command or 'http' in lower_command:reports[8] = 'لینک'
                    if "@" in command:reports[7] = 'ایدی'
                    xc = ''
                    for x in command:
                        if x in TPE:xc+=x
                    for x in FILTERLIST:
                        if x in xc:
                            reports[15] = f'متن نامناسب 〔 {x} 〕'
                            break
                    for x in TEGX:
                        if x in lower_command:
                            reports[18] = 'انگلیسی'
                            break
                    if (len(command.split('\n')) >= 25 or len(command) > 420):
                        reports[20] = 'کد هنگی'
                if metadata:reports[19] = 'متادیتا'
                if message_type in ListLockNames:
                    pr = ListLockNames[message_type]
                    reports[Listlocks[pr]] = pr
                if event_data and event_type == "JoinedGroupByLink":
                    if guid_sender in JoindUsers[object_guid]:reports[17] = 'جوین تکراری'
                    else:JoindUsers[object_guid].append(guid_sender)
                if int(INFOOBJECT['locks'][16]) == 0 and not event_data:                    isspam = False
                    if not object_guid in Spam:Spam[object_guid] = []
                    if len(Spam[object_guid]) >= 10:Spam[object_guid].pop(0)
                    if command:message_spam = command
                    else:message_spam = message_type
                    Spam[object_guid].append([guid_sender,message_spam,get_iran_timestamp()])
                    if command and (len(command.split('\n')) >= 7 or len(command) > 420):reports[16],isspam= 'اسپم 〔 ارسال پیام بلند 〕',True
                    lastnum = int(len(Spam[object_guid]))
                    if lastnum >= 10 and not isspam:
                        lastone = Spam[object_guid][lastnum-1]
                        firstone = Spam[object_guid][0]
                        limit_mes = lastnum*2
                        during_time = lastone[2]-firstone[2]
                        if during_time <= limit_mes:
                            sensetif = 1
                            check_mses = []
                            for step in Spam[object_guid]:check_mses.append(step[1])
                            ls_check_ms = lastone[1]
                            for check_ms in check_mses:
                                if check_ms == ls_check_ms:sensetif += 1                                if sensetif >= lastnum-5:
                                    reports[16],isspam = 'اسپم 〔 ارسال پیام تکراری 〕',True
                                    break
                            if not isspam:
                                sens = 1
                                for step in Spam[object_guid]:
                                    if step[0] == lastone[0]:sens += 1
                                    if sens >= lastnum:
                                        reports[16],isspam = 'اسپم 〔 ارسال پیام رگباری 〕',True
                                        break
                        else:
                            sensetif , check_mses = 1 , []
                            for step in Spam[object_guid]:check_mses.append(step[1])
                            ls_check_ms = lastone[1]
                            for check_ms in check_mses:
                                if check_ms == ls_check_ms:sensetif += 1                                if sensetif >= lastnum-5:
                                    reports[16],isspam = 'اسپم 〔 ارسال پیام تکراری 〕',True
                                    break

                if guid_sender not in INFOOBJECT['exempt_list']:
                    # DELETE MESSAGE
                    for step in reports:
                        if int(LOCKS_KEYS[step]) == 0:
                            warning_type = reports[step]
                            locks_warning = list(INFOOBJECT['locks_warning'])
                            locks_ban = list(INFOOBJECT['locks_ban'])
                            locks_warning_show = list(INFOOBJECT['locks_warning_show'])
                            if int(SETTING_KEYS[5]) and int(locks_ban[step]):
                                if guid_sender not in USERS[object_guid]:USERS[object_guid][guid_sender] = [0,0,'اراذل','ناشناس']
                                count = int(locks_warning[step])
                                pscount = USERS[object_guid][guid_sender][1]+1
                                if pscount >= count:
                                        if TIP >= 1:
                                            try:client.unset_admin(object_guid,guid_sender)
                                            except:pass
                                            if guid_sender in INFOOBJECT['admins']:INFOS[object_guid]['admins'].pop(guid_sender)
                                        else:
                                            try:
                                                reply_message_banded_id = client.ban_member(object_guid,guid_sender)['data']['chat_update']['chat']['last_message']['message_id']
                                                if int(SETTING_KEYS[8]):                                                    step = PorotectMSS(SETTING_KEYS,TimeMessages,5)
                                                    if step:ResultME = send_message(OBJM,INFOOBJECT['bye'],reply_message_banded_id)
                                            except:pass
                                            resetUser(guid_sender,object_guid)
                                            USERS[object_guid][guid_sender][1] = pscount
                                            INFOS[object_guid]['ban'] += 1
                                        if pscount == count:
                                            try:
                                                if int(SETTING_KEYS[6]) and int(locks_warning_show[step]):
                                                    step = PorotectMSS(SETTING_KEYS,TimeMessages,5)
                                                    if step:
                                                        if TIP >= 1:ResultME = send_message_limited(OBJM,f"**{warning_type}** @@ممنوع است. @@({guid_sender})〔{str(pscount)}/{str(count)}〕⚠️",message_id)
                                                        else:ResultME = send_message_limited(OBJM,f"**{warning_type}** @@ممنوع است. @@({guid_sender})〔{str(pscount)}/{str(count)}〕🚫",message_id)
                                            except:pass
                                else:
                                    try:
                                        if int(SETTING_KEYS[6]) and int(locks_warning_show[step]):
                                            step = PorotectMSS(SETTING_KEYS,TimeMessages,5)
                                            if step:ResultME = send_message_limited(OBJM,f"**{warning_type}** @@ممنوع است. @@({guid_sender})〔{str(pscount)}/{str(count)}〕⚠️",message_id)
                                    except:pass
                                    USERS[object_guid][guid_sender][1] = pscount
                            try:client.delete_messages(object_guid,[message_id])
                            except:pass
                            isok = False
                            break

                # SAVE REPORTS
                for step in reports:
                    if ListLocks_R[step] in INFOOBJECT['type_messages']:INFOS[object_guid]['type_messages'][ListLocks_R[step]] += 1
                    else:INFOS[object_guid]['type_messages'][ListLocks_R[step]] = 1

            # IF IS NOT GOOD MS SO CONTINUE
            if not isok:return True

            # BLACKLIST
            if guid_sender in INFOOBJECT['silent_list'] and TIP <= 1:
                client.delete_messages(object_guid,[message_id])
                return True

            # EVENT DATA
            if event_data and not ResultME:
                match event_type:
                    case 'LeaveGroup':
                        INFOS[object_guid]['left'] += 1
                        result = ExtraInfo(OBJM,INFOOBJECT,SETTING_KEYS,TimeMessages,"bye")
                        if result:
                            ResultME = send_message(OBJM,result,message_id)
                    case 'JoinedGroupByLink':
                        INFOS[object_guid]['join'] += 1
                        result = ExtraInfo(OBJM,INFOOBJECT,SETTING_KEYS,TimeMessages,"welcome")
                        if result:
                            ResultME = send_message(OBJM,result,message_id)
                    case 'AddedGroupMembers':
                        INFOS[object_guid]['add'] += 1
                        result = ExtraInfo(OBJM,INFOOBJECT,SETTING_KEYS,TimeMessages,"welcome")
                        if result:
                            ResultME = send_message(OBJM,result,message_id)
                    case 'RemoveGroupMembers':
                        INFOS[object_guid]['ban'] += 1
                        result = ExtraInfo(OBJM,INFOOBJECT,SETTING_KEYS,TimeMessages,"bye")
                        if result:
                            ResultME = send_message(OBJM,result,message_id)
                        resetUser(guid_sender,object_guid)
                    case 'CreateGroupVoiceChat':
                        INFOS[object_guid]['voice_call'] += 1
                        result = CheckSetting(SETTING_KEYS,'اعلان')

                        if result:ResultME = send_message(OBJM,MPro(f"@@[ ویس کال ایجاد شد. ]@@({guid_sender})",2),message_id)
                    case 'StopGroupVoiceChat':
                        result = CheckSetting(SETTING_KEYS,'اعلان')
                        if result:ResultME = send_message(OBJM,MPro(f"@@[ ویس کال قطع شد. ]@@({guid_sender})",2),message_id)
                    case 'TitleUpdate':
                        INFOS[object_guid]['name'] = event_data['title']                        result = CheckSetting(SETTING_KEYS,'اعلان')
                        if result:ResultME = send_message(OBJM,MPro(f"@@[ اسم گروه اپدیت شد. ]@@({guid_sender})",2),message_id)
                    case 'PhotoUpdate':
                        result = CheckSetting(SETTING_KEYS,'اعلان')
                        if result:ResultME = send_message(OBJM,MPro(f"@@[ عکس گروه اپدیت شد. ]@@({guid_sender})",2),message_id)
                guid_sender = False
                command = False
                if int(SETTING_KEYS[12]) == 0:client.delete_messages(object_guid,[message_id])

            #COMMANDS
            if command:
                if not ResultME and wordCount <= 5:
                    # FOR OWNER
                    if TIP == 4 and not ResultME:
                        # static order
                        if is_reply_message and command in list_command_owner_reply_keys:
                            text = list_command_owner_reply[command](OBJM)
                            if text:send_message(OBJM=OBJM,text=text,message_id=message_id)
                            ResultME = True
                        elif command in list_command_owner_keys:
                            if command in list_filter_metadata:metadata = False
                            else:metadata = True
                            text = list_command_owner[command](OBJM)
                            if text:send_message(OBJM=OBJM,text=text,message_id=message_id,metadata=metadata)
                            elif text is False:return
                            ResultME = True
                        else:
                            if is_reply_message:
                                match wordCount:
                                    case 1:
                                        if command.startswith('تبدیل '):                                            type_result = command.replace('تبدیل','').strip()
                                            list_infos = {'عکس':{'format':'png','nick':'image'},'گیف':{'format':'mp4','nick':'gif'},'صدا':{'format':'mpeg','nick':'voice'},'ویس':{'format':'mpeg','nick':'voice'},'اهنگ':{'format':'mp3','nick':'audio'},'موزیک':{'format':'mp3','nick':'audio'},'فیلم':{'format':'mp4','nick':'video'}}
                                            if type_result in list_infos:
                                                format = list_infos[type_result]['format']
                                                nick = list_infos[type_result]['nick']
                                                filename = f"{nick}_{str(get_iran_timestamp())}.{format}"
                                                client.download(object_guid,is_reply_message,True,f"Downloads/{filename}")
                                                if os.path.isfile(f"Downloads/{filename}"):
                                                    try:
                                                        match nick:
                                                            case 'image':
                                                                ResultME = client.send_image(object_guid,f"Downloads/{filename}",message_id)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'video':
                                                                ResultME = client.send_video(object_guid,f"Downloads/{filename}",message_id)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'voice':
                                                                ResultME = client.send_voice(object_guid,f"Downloads/{filename}",message_id,time=1)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'audio':
                                                                ResultME = client.send_music(object_guid,f"Downloads/{filename}",message_id,time=1,performer='l‌8‌P‌B‌O‌T')
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'gif':
                                                                ResultME = client.send_gif(object_guid,f"Downloads/{filename}",message_id)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                        ResultME = True
                                                    except:ResultME = send_message(OBJM,MPro(f"عملیات ناموفق بود. {ST['ok']}",2),message_id)
                                                try:os.remove(f"Downloads/{filename}")
                                                except:pass
                            else:
                                match wordCount:
                                    case 1:
                                        if command.startswith('برکناری @'):
                                            command = command.replace('برکناری','').strip()
                                            reply_message_guid = False
                                            try:reply_message_guid = client.get_chat_info_by_username(command)['user']['user_guid']
                                            except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)

                                            if reply_message_guid:
                                                if reply_message_guid == OWNER:mess = MPro(f"شما سازنده من هستید.{ST['ok']}",2)
                                                elif reply_message_guid not in FULL_ADMINS and reply_message_guid not in ADMINS and not reply_message_guid == HOWNER:
                                                    mess = MPro(f"مقامی ندارد.{ST['ok']}",2)
                                                else:
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) برکنار شد. {ST['ok']}",2)
                                                    if reply_message_guid == HOWNER:INFOS[object_guid]['owner'] = OWNER
                                                    if reply_message_guid in FULL_ADMINS:INFOS[object_guid]['full_admins'].pop(reply_message_guid)
                                                    if reply_message_guid in ADMINS:INFOS[object_guid]['admins'].pop(reply_message_guid)
                                                    try:client.unset_admin(object_guid,reply_message_guid)
                                                    except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('برکناری u0'):
                                            command = command.replace('برکناری','').strip()
                                            reply_message_guid = False
                                            try:reply_message_guid = client.get_chat_info(command)['user']['user_guid']
                                            except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)

                                            if reply_message_guid:
                                                if reply_message_guid == OWNER:mess = MPro(f"شما سازنده من هستید.{ST['ok']}",2)
                                                elif reply_message_guid not in FULL_ADMINS and reply_message_guid not in ADMINS and not reply_message_guid == HOWNER:
                                                    mess = MPro(f"مقامی ندارد.{ST['ok']}",2)
                                                else:
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) برکنار شد. {ST['ok']}",2)
                                                    if reply_message_guid == HOWNER:INFOS[object_guid]['owner'] = OWNER
                                                    if reply_message_guid in FULL_ADMINS:INFOS[object_guid]['full_admins'].pop(reply_message_guid)
                                                    if reply_message_guid in ADMINS:INFOS[object_guid]['admins'].pop(reply_message_guid)
                                                    try:client.unset_admin(object_guid,reply_message_guid)
                                                    except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('ویژه @'):
                                            command = command.replace('ویژه','').strip()
                                            try:reply_message_guid = client.get_chat_info_by_username(command)['user']['user_guid']
                                            except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)

                                            if reply_message_guid:
                                                if reply_message_guid == OWNER:mess = MPro(f"شما سازنده من هستید.{ST['ok']}",2)
                                                elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                                elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                                else:
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    INFOS[object_guid]['full_admins'][reply_message_guid] = first_name
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) ادمین ویژه شد. {ST['ok']}",2)
                                                    try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                                    except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('ویژه u0'):
                                            command = command.replace('ویژه','').strip()
                                            reply_message_guid = False
                                            try:reply_message_guid = client.get_chat_info(command)['user']['user_guid']
                                            except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                            if reply_message_guid:
                                                if reply_message_guid == OWNER:mess = MPro(f"شما سازنده من هستید.{ST['ok']}",2)
                                                elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                                elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                                else:
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    INFOS[object_guid]['full_admins'][reply_message_guid] = first_name
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) ادمین ویژه شد. {ST['ok']}",2)
                                                    try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                                    except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('مالک @'):
                                            command = command.replace('مالک','').strip()
                                            reply_message_guid = False
                                            try:reply_message_guid = client.get_chat_info_by_username(command)['user']['user_guid']
                                            except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                            if reply_message_guid:
                                                if reply_message_guid == OWNER:mess = MPro(f"شما سازنده من هستید.{ST['ok']}",2)
                                                else:
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    INFOS[object_guid]['owner'] = reply_message_guid
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) مالک شد. {ST['ok']}",2)
                                                    try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                                    except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('مالک u0'):
                                            command = command.replace('مالک','').strip()
                                            reply_message_guid = False
                                            try:reply_message_guid = client.get_chat_info(command)['user']['user_guid']
                                            except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)

                                            if reply_message_guid:
                                                if reply_message_guid == OWNER:mess = MPro(f"شما سازنده من هستید.{ST['ok']}",2)
                                                else:
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    INFOS[object_guid]['owner'] = reply_message_guid
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) مالک شد. {ST['ok']}",2)
                                                    try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                                    except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('عضویت '):
                                            command = command.replace('عضویت','').strip()
                                            channel_guid = False
                                            if command.startswith('@'):
                                                try:channel_guid = client.get_chat_info_by_username(command)['channel']['channel_guid']
                                                except:pass
                                            elif command.startswith('https://'):
                                                try:
                                                    get_info = client.get_chat_preview(command)
                                                    if 'group' in get_info:
                                                        channel_guid = get_info['group']['group_guid']
                                                    elif 'channel' in get_info:
                                                        channel_guid = get_info['channel']['channel_guid']
                                                except:pass
                                            if channel_guid:
                                                INFOS[object_guid]['channels'][command] = channel_guid
                                                mess = MPro(f"به لیست عضویت اضافه شد. {ST['ok']}",2)
                                            else:mess = MPro(f"نامعتبر است. {ST['ok']}",2)
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('افزودن @'):
                                            mess = MPro(f"کاربر یافت نشد. {ST['ok']}",2)
                                            command = command.replace('افزودن','').strip()
                                            reply_message_guid = getinfos(command)
                                            if reply_message_guid:
                                                mess = MPro(f"بیش از حد مجاز. {ST['ok']}",2)
                                                try:
                                                    client.add_member(object_guid,[reply_message_guid])
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) افزوده شد. {ST['ok']}",2)
                                                except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('افزودن u0'):
                                            mess = MPro(f"کاربر یافت نشد. {ST['ok']}",2)
                                            command = command.replace('افزودن','')
                                            reply_message_guid = getinfos(command,False)
                                            if reply_message_guid:
                                                mess = MPro(f"بیش از حد مجاز. {ST['ok']}",2)
                                                try:
                                                    client.add_member(object_guid,[reply_message_guid])
                                                    first_name = check_name(object_guid,reply_message_guid)
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) افزوده شد. {ST['ok']}",2)
                                                except:pass
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('رسانه '):
                                            command = command.replace('#','')
                                            filename = command.replace('رسانه','').strip()
                                            list_media_tag = ['image','video','voice','audio','gif']
                                            tag_name = False
                                            for tag in list_media_tag:
                                                if filename.startswith(tag):tag_name = tag;break
                                            if tag_name:
                                                list_infos = {'image':'png','gif':'mp4','voice':'mpeg','audio':'mp3','video':'mp4'}
                                                format = list_infos[tag_name]
                                                text = f"رسانه #{filename}"
                                                if tag_name == 'gif' and filename in INLINES:
                                                    ResultME = client.send_message(object_guid,INLINES[filename],text,message_id)
                                                else:
                                                    if not filename.endswith(f'.{format}'):filename += f'.{format}'
                                                    if os.path.isfile(f"Downloads/{filename}"):
                                                        match tag_name:
                                                            case 'image':
                                                                ResultME = client.send_image(object_guid,f"Downloads/{filename}",message_id,text)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'video':
                                                                ResultME = client.send_video(object_guid,f"Downloads/{filename}",message_id,text)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'voice':
                                                                ResultME = client.send_voice(object_guid,f"Downloads/{filename}",message_id,text,time=1)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'audio':
                                                                ResultME = client.send_music(object_guid,f"Downloads/{filename}",message_id,text,time=1,performer='l‌8‌P‌B‌O‌T')
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                            case 'gif':
                                                                ResultME = client.send_gif(object_guid,f"Downloads/{filename}",message_id,text)
                                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                        ResultME = True
                                        elif command.startswith('جوین '):
                                            command = command.replace('جوین','').strip()
                                            mess = False
                                            if command.startswith("https://rubika.ir/joing/"):
                                                mess = MPro(f"لینک گروه نامعتبر است. {ST['ok']}",2)
                                                try:
                                                    if client.join_chat(command)['is_valid']:
                                                        mess = MPro(f"عضو گروه شدم. {ST['ok']}",2)
                                                except:pass
                                            elif command.startswith("https://rubika.ir/joinc/"):
                                                mess = MPro(f"لینک کانال نامعتبر است. 🚫{ST['ok']}",2)
                                                try:
                                                    if client.join_chat(command)['is_valid']:
                                                        mess = MPro(f"عضو کانال شدم. {ST['ok']}",2)
                                                except:pass
                                            elif command.startswith("@"):
                                                result = client.get_chat_info_by_username(command)
                                                if 'channel' in result:
                                                    direction_guid = result['channel']['channel_guid']
                                                    mess = MPro(f"ایدی کانال نامعتبر است. 🚫{ST['ok']}",2)
                                                    try:
                                                        client.join_chat(direction_guid)['chat_update']['object_guid']
                                                        mess = MPro(f"عضو کانال شدم. {ST['ok']}",2)
                                                    except:pass
                                            if mess:ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('لفت '):                                            UPFILES(file_infos,INFOS)
                                            UPFILES(file_users,USERS)
                                            UPFILES(file_speakx,SPEAKX)
                                            link = command.replace('لفت',"").strip()
                                            if len(link) > 0:
                                                mess , chat_guid = 'نامعتبر است. 🚫' , None
                                                if link.startswith("https://rubika.ir/"):
                                                    try:
                                                        get_info = client.get_chat_preview(link)
                                                        if 'group' in get_info:
                                                            chat_guid = get_info['group']['group_guid']
                                                        elif 'channel' in get_info:
                                                            chat_guid = get_info['channel']['channel_guid']
                                                    except:pass
                                                elif link.startswith('g0'):chat_guid = link
                                                elif link.startswith('c0'):chat_guid = link
                                                elif link.startswith('@'):
                                                    try:chat_guid = client.get_chat_info_by_username(link)['channel']['channel_guid']
                                                    except:pass
                                                if chat_guid:
                                                    mess = 'لفت دادم. '
                                                    leave_from_group(client,chat_guid)
                                                ResultME = send_message(OBJM,mess,message_id)
                                    case 2:
                                        if command.startswith('حذف عضویت '):
                                            command = command.replace('حذف عضویت','').strip()
                                            mess = MPro(f"در لیست عضویت قرار ندارد. {ST['ok']}",2)
                                            if command in INFOS[object_guid]['channels']:
                                                INFOS[object_guid]['channels'].pop(command)
                                                mess = MPro(f"از لیست عضویت حذف شد. {ST['ok']}",2)
                                            ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('پاکسازی لیست '):
                                            media = command.replace('پاکسازی لیست','').strip()
                                            result = delete_all_media_pro(OBJM,media)
                                            if result:ResultME = send_message(OBJM,result,message_id)
                                        elif command.startswith('حذف رسانه '):
                                            command = command.replace('#','')
                                            filename = command.replace('حذف رسانه','').strip()
                                            list_media_tag = ['image','video','voice','audio','gif']
                                            tag_name = False
                                            for tag in list_media_tag:
                                                if filename.startswith(tag):tag_name = tag;break
                                            if tag_name:
                                                mess =  MPro(f"تگ #{str(filename)} موجود نیست. {ST['ok']}",2)
                                                list_infos = {'image':'png','gif':'mp4','voice':'mpeg','audio':'mp3','video':'mp4'}
                                                format = list_infos[tag_name]
                                                if tag_name == 'gif' and filename in INLINES:
                                                    del INLINES[filename]
                                                    mess =  MPro(f"تگ #{str(filename)} حذف شد. {ST['ok']}",2)
                                                else:
                                                    tag_file = filename
                                                    if not filename.endswith(f'.{format}'):filename += f'.{format}'
                                                    if os.path.isfile(f"Downloads/{filename}"):
                                                        os.remove(f"Downloads/{filename}")
                                                        mess =  MPro(f"تگ #{str(tag_file)} حذف شد. {ST['ok']}",2)
                                                ResultME = send_message(OBJM,mess,message_id)
                                        elif command.startswith('شارژ گروه ') or command.startswith('تنظیم شارژ '):
                                            new_timeout = command.replace('شارژ گروه','').strip()
                                            new_timeout = new_timeout.replace('تنظیم شارژ','').strip()
                                            try:new_timeout = int(new_timeout)*86400
                                            except:new_timeout = False
                                            if new_timeout:
                                                if 'timeout' not in INFOS[object_guid]:INFOS[object_guid]['timeout'] = False
                                                timeout = INFOS[object_guid]['timeout']
                                                if not timeout:timeout = get_iran_timestamp()
                                                result_timeout = timeout+new_timeout
                                                INFOS[object_guid]['timeout'] = result_timeout
                                                time_now = get_iran_timestamp()
                                                mess = MPro(f"{Time_pass(new_timeout)} به شارژ گروه اضافه شد. {ST['ok']}",2)
                                                mess += MPro(f"شارژ گروه : {Time_pass(result_timeout-time_now)}")
                                                ResultME = send_message(OBJM,mess,message_id)

                    # FOR GOLD
                    elif TIP == 3 and not ResultME:
                        # static order
                        if is_reply_message and command in list_command_goldadmin_reply_keys:
                            text = list_command_goldadmin_reply[command](OBJM)
                            if text:send_message(OBJM=OBJM,text=text,message_id=message_id)
                            ResultME = True
                        elif command in list_command_goldadmin_keys:
                            if command in list_filter_metadata:metadata = False
                            else:metadata = True
                            text = list_command_goldadmin[command](OBJM)                            if text:send_message(OBJM=OBJM,text=text,message_id=message_id,metadata=metadata)
                            ResultME = True
                        else:
                            if command.startswith('برکناری @'):
                                command = command.replace('برکناری','').strip()
                                reply_message_guid = False
                                try:reply_message_guid = client.get_chat_info_by_username(command)['user']['user_guid']
                                except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)

                                if reply_message_guid:
                                    if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من است.{ST['ok']}",2)
                                    elif reply_message_guid == HOWNER:mess = MPro(f"شما مالک من هستید.{ST['ok']}",2)
                                    elif reply_message_guid not in FULL_ADMINS and reply_message_guid not in ADMINS:mess = MPro(f"مقامی ندارد.{ST['ok']}",2)
                                    else:
                                        first_name = check_name(object_guid,reply_message_guid)
                                        mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) برکنار شد. {ST['ok']}",2)
                                        if reply_message_guid == HOWNER:INFOS[object_guid]['owner'] = OWNER
                                        if reply_message_guid in FULL_ADMINS:INFOS[object_guid]['full_admins'].pop(reply_message_guid)
                                        if reply_message_guid in ADMINS:INFOS[object_guid]['admins'].pop(reply_message_guid)
                                        try:client.unset_admin(object_guid,reply_message_guid)
                                        except:pass
                                ResultME = send_message(OBJM,mess,message_id)
                            elif command.startswith('برکناری u0'):
                                command = command.replace('برکناری','').strip()
                                reply_message_guid = False
                                try:reply_message_guid = client.get_chat_info(command)['user']['user_guid']
                                except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)

                                if reply_message_guid:
                                    if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من است.{ST['ok']}",2)
                                    elif reply_message_guid == HOWNER:mess = MPro(f"شما مالک من هستید.{ST['ok']}",2)
                                    elif reply_message_guid not in FULL_ADMINS and reply_message_guid not in ADMINS:
                                        mess = MPro(f"مقامی ندارد.{ST['ok']}",2)
                                    else:
                                        first_name = check_name(object_guid,reply_message_guid)
                                        mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) برکنار شد. {ST['ok']}",2)
                                        if reply_message_guid == HOWNER:INFOS[object_guid]['owner'] = OWNER
                                        if reply_message_guid in FULL_ADMINS:INFOS[object_guid]['full_admins'].pop(reply_message_guid)
                                        if reply_message_guid in ADMINS:INFOS[object_guid]['admins'].pop(reply_message_guid)
                                        try:client.unset_admin(object_guid,reply_message_guid)
                                        except:pass
                                ResultME = send_message(OBJM,mess,message_id)
                            elif command.startswith('ویژه @'):
                                command = command.replace('ویژه','').strip()
                                try:reply_message_guid = client.get_chat_info_by_username(command)['user']['user_guid']
                                except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                if reply_message_guid:
                                    if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من است.{ST['ok']}",2)
                                    elif reply_message_guid == HOWNER:mess = MPro(f"شما مالک من هستید.{ST['ok']}",2)
                                    elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                    else:
                                        first_name = check_name(object_guid,reply_message_guid)
                                        INFOS[object_guid]['full_admins'][reply_message_guid] = first_name
                                        mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) ادمین ویژه شد. {ST['ok']}",2)
                                        try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                        except:pass
                                ResultME = send_message(OBJM,mess,message_id)
                            elif command.startswith('ویژه u0'):
                                command = command.replace('ویژه','').strip()
                                reply_message_guid = False
                                try:reply_message_guid = client.get_chat_info(command)['user']['user_guid']
                                except:mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                if reply_message_guid:
                                    if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من است.{ST['ok']}",2)
                                    elif reply_message_guid == HOWNER:mess = MPro(f"شما مالک من هستید.{ST['ok']}",2)
                                    elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                    else:
                                        first_name = check_name(object_guid,reply_message_guid)
                                        INFOS[object_guid]['full_admins'][reply_message_guid] = first_name
                                        mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) ادمین ویژه شد. {ST['ok']}",2)
                                        try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                        except:pass
                                ResultME = send_message(OBJM,mess,message_id)

                    # FOR FULLADMINS
                    elif TIP == 2 and not ResultME:
                        # static order
                        if is_reply_message and command in list_command_fulladmins_reply_keys:
                            text = list_command_fulladmins_reply[command](OBJM)
                            if text:send_message(OBJM=OBJM,text=text,message_id=message_id)
                            ResultME = True
                        elif command in list_command_fulladmins_keys:
                            if command in list_filter_metadata:metadata = False
                            else:metadata = True
                            text = list_command_fulladmins[command](OBJM)
                            if text:send_message(OBJM=OBJM,text=text,message_id=message_id,metadata=metadata)
                            ResultME = True

                    # same for all fulladmins up...
                    if TIP >= 2 and not ResultME:
                        if is_reply_message:
                            if wordCount >= 2:
                                if command.startswith('تنظیم لقب ') or command.startswith('ثبت لقب '):
                                    info = command.replace('تنظیم لقب','').strip()
                                    info = info.replace('ثبت لقب','').strip()
                                    reply_message = GetInfoByMessageId(object_guid,is_reply_message)
                                    mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                    if reply_message:
                                        reply_message_guid = GetReplyGuid(reply_message)
                                        if reply_message_guid:
                                            if reply_message_guid not in USERS[object_guid]:USERS[object_guid][reply_message_guid] = [0,0,info,'ناشناس']
                                            else:USERS[object_guid][reply_message_guid][2] = info
                                            mess = MPro(f"لقب تنظیم شد. {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)
                                elif command.startswith('تنظیم اصل ') or command.startswith('ثبت اصل '):
                                    info = command.replace('ثبت اصل','').strip()
                                    info = info.replace('تنظیم اصل','').strip()
                                    reply_message = GetInfoByMessageId(object_guid,is_reply_message)
                                    mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                    if reply_message:
                                        reply_message_guid = GetReplyGuid(reply_message)
                                        if reply_message_guid:
                                            if reply_message_guid not in USERS[object_guid]:getInfoUser(object_guid,reply_message_guid,info)
                                            else:USERS[object_guid][reply_message_guid][3] = info
                                            mess = MPro(f"اصل تنظیم شد. {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)
                        else:
                            match wordCount:
                                case 1:
                                    if command.startswith('یادداشت '):
                                        num = command.replace('یادداشت','').strip()
                                        try:num = int(num)
                                        except:num = 0
                                        try:rem = INFOS[object_guid]['remmember'][num]
                                        except:rem = False
                                        if not rem:
                                            mess = MPro(f"یادداشت موجود نمیباشد.{ST['ok']}",2)
                                            ResultME = send_message(OBJM,mess,message_id)
                                        else:
                                            mess = MPro("یادداشت 〔 💬 ‍  ",4)
                                            year,month,week,day,hour = Year(),Month(),Week(),Day(),Hour()
                                            mess += MPro(f"تاریخ : {hour} ⌯ {week} ⌯ {year}-{month}-{day}",2)
                                            mess += '\n─┅━━━━━━━┅─\n'
                                            rem_text,rem_date = rem['text'],rem['date']
                                            year,month,week,day,hour = Year(rem_date),Month(rem_date),Week(rem_date),Day(rem_date),Hour(rem_date)
                                            time_pass = get_iran_timestamp()-rem_date
                                            str_time_pass = Time_pass(time_pass)
                                            mess += MPro(f"کد〔{str(num)}〕⌯ {str_time_pass} پیش")
                                            mess += MPro(f"{hour} ⌯ {week} ⌯ {year}-{month}-{day}")
                                            mess += MPro(rem_text)
                                            mess += '\n'
                                            ResultME = send_message(OBJM,mess,message_id)
                                    elif command.startswith('پاسخدهی '):                                        num = command.replace('پاسخدهی','').strip()
                                        try:num = int(num)
                                        except:num = 0
                                        num = 3600 if num > 3600 else num
                                        num = 0 if num < 0 else num
                                        client.edit_group_info(object_guid=object_guid,slow_mode=num)
                                        ResultME = send_message(OBJM,MPro(f"پاسخدهی {str(num)} ثانیه تنظیم شد. {ST['ok']}",2),message_id)
                                    elif command.startswith('لیست'):
                                        media = command.replace('لیست','').strip()
                                        result = get_my_media_pro(OBJM,media)
                                        if result:ResultME = send_message(OBJM,result,message_id)
                                    elif command.startswith('Sleep'):
                                        sleepcmd = command.replace('Sleep','').strip()
                                        if sleepcmd.isnumeric():sleepcmd = int(sleepcmd)
                                        else:sleepcmd = 10
                                        if sleepcmd > 60:sleepcmd = 60
                                        elif sleepcmd < 0:sleepcmd = 1
                                        mess = MPro(f"sleeping mode {str(sleepcmd)} {ST['ok']}",2)
                                        try:ResultME = send_message(OBJM,mess,message_id)
                                        except:pass
                                        time.sleep(int(sleepcmd))
                                case 2:
                                    if command.startswith('بهینه سازی '):
                                        lims = command.replace('بهینه سازی','').strip()
                                        iscount = False
                                        try:
                                            nums = int(lims)
                                            if nums < 0:nums = 10
                                            iscount = True
                                        except:pass
                                        if iscount:
                                            deleting = []
                                            Alls,User = 0,0
                                            for user_guid in USERS[object_guid]:
                                                try:
                                                    if user_guid == GUIDME:continue
                                                    user = USERS[object_guid][user_guid]
                                                    mes,war = user[0],user[1]
                                                    state = mes-war
                                                    if state <= nums:
                                                        Alls += mes
                                                        User += 1
                                                        deleting.append(user_guid)
                                                except:pass
                                            for user_guid in deleting:USERS[object_guid].pop(user_guid)
                                            with open(file_users, "w") as outfile:
                                                json.dump(USERS, outfile)
                                            JoindUsers[object_guid] = []                                            mess = MPro(f"کاربران با تعداد پیام کمتر از {str(nums)} از حافظه پاک شد. {ST['ok']}\nدر مجموع {str(Alls)} پیام و {str(User)} کاربر پاک شده است.{ST['ok']}",2)
                                            ResultME = send_message(OBJM,mess,message_id)
                                            Alls,deleting = 0,[]
                                    elif command.startswith('حذف یادداشت '):
                                        num = command.replace('حذف یادداشت','').strip()
                                        try:num = int(num)
                                        except:num = 0
                                        mess = MPro(f"از لیست یادداشت حذف شد. {ST['ok']}",2)
                                        try:INFOS[object_guid]['remmember'].pop(num)
                                        except:mess = MPro(f"در لیست یادداشت موجود نیست. {ST['ok']}",2)
                                        ResultME = send_message(OBJM,mess,message_id)
                                    elif command.startswith('حذف تایمر '):
                                        num = command.replace('حذف تایمر','').strip()
                                        try:num = int(num)
                                        except:num = 0
                                        mess = MPro(f"از لیست تایمر حذف شد. {ST['ok']}",2)
                                        endlen = len(INFOS[object_guid]['AUTOS'])-1
                                        if endlen >= num:
                                            INFOS[object_guid]['AUTOS'].pop(num)
                                        else:mess = MPro(f"در لیست تایمر موجود نیست. {ST['ok']}",2)
                                        ResultME = send_message(OBJM,mess,message_id)
                                    elif command.startswith('پاکسازی لیست '):
                                        xcomand = command.replace('پاکسازی لیست','').strip()
                                        isok = False
                                        match xcomand:
                                            case 'سکوت':
                                                INFOS[object_guid]['silent_list'] , isok = {} , True
                                            case 'معاف':
                                                INFOS[object_guid]['exempt_list'] , isok = {} , True
                                            case 'کیل':
                                                INFOS[object_guid]['black_list'] , isok = {} , True
                                            case 'فیلتر':
                                                INFOS[object_guid]['filterlist'] , isok = [] , True
                                            case 'کلید':
                                                INFOS[object_guid]['main_keys'] , isok = [] , True
                                            case 'تایمر':
                                                INFOS[object_guid]['AUTOS'] , isok = [] , True
                                            case 'ادمین':
                                                ADMINS = {}
                                                has_continue , next_start_id = True , None
                                                count = 0
                                                mess = MPro(f"درحال پاکسازی...{ST['ok']}",2)
                                                ResultME = send_message(OBJM,mess,message_id)
                                                while has_continue:
                                                    time.sleep(0.2)
                                                    result = client.get_admin_members(object_guid,next_start_id)
                                                    has_continue = result['has_continue']
                                                    if 'next_start_id' in result:next_start_id = result['next_start_id']                        
                                                    for admin in result['in_chat_members']:
                                                        member_guid = admin['member_guid']
                                                        if not (member_guid == OWNER or member_guid == HOWNER or member_guid == GUIDME or member_guid in FULL_ADMINS):
                                                            try:client.unset_admin(object_guid,member_guid)
                                                            except:pass
                                                    count += len(result['in_chat_members'])
                                                INFOS[object_guid]['admins'] = {}
                                                UPFILES(file_infos,INFOS)
                                                if count == 0:mess = MPro(f"لیست ادمین خالی است {ST['ok']}",2)
                                                else:mess = MPro(f"لیست ادمین پاکسازی شد. {ST['ok']}\nتعداد برکناری ها : {str(count)}",2)
                                                ResultME = send_message(OBJM,mess,message_id)
                                            case 'عضویت':
                                                INFOS[object_guid]['channels'] , isok = {} , True
                                            case 'یادداشت':
                                                INFOS[object_guid]['remmember'] , isok = [] , True
                                        if isok:ResultME = send_message(OBJM,MPro(f"لیست {xcomand} پاکسازی شد. {ST['ok']}",2),message_id)
                            if not ResultME and wordCount > 0:
                                mess = False
                                if wordCount <= 2:
                                    if 'https://rubika.ir/joing/' not in command and 'https://rubika.ir/joinc/' not in command:
                                        command = command.replace('https://rubika.ir/','@')
                                    if command.startswith('بن @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('بن','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  in ADMINS:mess = MPro(f"ایشون ادمین است.{ST['ok']}",2)
                                            else:
                                                INFOS[object_guid]['ban'] += 1
                                                first_name = check_name(object_guid,reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) بن شد. {ST['ok']}",2)
                                                try:
                                                    client.ban_member(object_guid,reply_message_guid)
                                                    resetUser(reply_message_guid,object_guid)
                                                except:pass
                                    elif command.startswith('بن u0'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('بن','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  in ADMINS:mess = MPro(f"ایشون ادمین است.{ST['ok']}",2)
                                            else:
                                                INFOS[object_guid]['ban'] += 1
                                                first_name = check_name(object_guid,reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) بن شد. {ST['ok']}",2)
                                                try:
                                                    client.ban_member(object_guid,reply_message_guid)
                                                    resetUser(reply_message_guid,object_guid)
                                                except:pass
                                    elif command.startswith('سکوت @'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('سکوت','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  in ADMINS:mess = MPro(f"ایشون ادمین است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                if reply_message_guid in INFOS[object_guid]['silent_list']:
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست سکوت بود. {ST['ok']}",2)
                                                else:
                                                    INFOS[object_guid]['silent_list'][reply_message_guid] = first_name
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) به لیست سکوت اضافه شد. {ST['ok']}",2)
                                    elif command.startswith('معاف @'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('معاف','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                if reply_message_guid in INFOS[object_guid]['exempt_list']:
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست معاف بود. {ST['ok']}",2)
                                                else:
                                                    INFOS[object_guid]['exempt_list'][reply_message_guid] = first_name
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) به لیست معاف اضافه شد. {ST['ok']}",2)
                                    elif command.startswith('سکوت u0'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('سکوت','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  in ADMINS:mess = MPro(f"ایشون ادمین است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                if reply_message_guid in INFOS[object_guid]['silent_list']:
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست سکوت بود. {ST['ok']}",2)
                                                else:
                                                    INFOS[object_guid]['silent_list'][reply_message_guid] = first_name
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) به لیست سکوت اضافه شد. {ST['ok']}",2)
                                    elif command.startswith('معاف u0'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('معاف','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                if reply_message_guid in INFOS[object_guid]['exempt_list']:
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست معاف بود. {ST['ok']}",2)
                                                else:
                                                    INFOS[object_guid]['exempt_list'][reply_message_guid] = first_name
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) به لیست معاف اضافه شد. {ST['ok']}",2)
                                    elif command.startswith('حذف سکوت @'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('حذف سکوت','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            if reply_message_guid in INFOS[object_guid]['silent_list']:
                                                INFOS[object_guid]['silent_list'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) از لیست سکوت حذف شد. {ST['ok']}",2)                                            else:mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست سکوت یافت نشد. {ST['ok']}",2)
                                    elif command.startswith('حذف معاف @'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('حذف معاف','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            if reply_message_guid in INFOS[object_guid]['exempt_list']:
                                                INFOS[object_guid]['exempt_list'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) از لیست معاف حذف شد. {ST['ok']}",2)                                            else:mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست معاف یافت نشد. {ST['ok']}",2)
                                    elif command.startswith('حذف سکوت u0'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('حذف سکوت','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            if reply_message_guid in INFOS[object_guid]['silent_list']:
                                                INFOS[object_guid]['silent_list'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) از لیست سکوت حذف شد. {ST['ok']}",2)                                            else:mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست سکوت یافت نشد. {ST['ok']}",2)
                                    elif command.startswith('حذف معاف u0'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('حذف معاف','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            if reply_message_guid in INFOS[object_guid]['exempt_list']:
                                                INFOS[object_guid]['exempt_list'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) از لیست معاف حذف شد. {ST['ok']}",2)                                            else:mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست معاف یافت نشد. {ST['ok']}",2)

                                    elif command.startswith('کیل @'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('کیل','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هست.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هست.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  in ADMINS:mess = MPro(f"ایشون ادمین است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                if reply_message_guid in INFOS[object_guid]['black_list']:
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست کیل بود. {ST['ok']}",2)                                                else:
                                                    INFOS[object_guid]['black_list'][reply_message_guid] = [first_name,1]
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) به لیست کیل اضافه شد. {ST['ok']}",2)
                                    elif command.startswith('کیل u0'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('کیل','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  in ADMINS:mess = MPro(f"ایشون ادمین است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                if reply_message_guid in INFOS[object_guid]['black_list']:
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست کیل بود. {ST['ok']}",2)                                                else:
                                                    INFOS[object_guid]['black_list'][reply_message_guid] = [first_name,1]
                                                    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) به لیست کیل اضافه شد. {ST['ok']}",2)
                                    elif command.startswith('حذف کیل @'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('حذف کیل','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            if reply_message_guid in INFOS[object_guid]['black_list']:
                                                INFOS[object_guid]['black_list'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) از لیست کیل حذف شد. {ST['ok']}",2)
                                            else:mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست کیل یافت نشد. {ST['ok']}",2)
                                    elif command.startswith('حذف کیل u0'):
                                        mess = MPro(f"کاربر شناسایی نشد.{ST['ok']}",2)
                                        command = command.replace('حذف کیل','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            if reply_message_guid in INFOS[object_guid]['black_list']:
                                                INFOS[object_guid]['black_list'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) از لیست کیل حذف شد. {ST['ok']}",2)
                                            else:mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) در لیست کیل یافت نشد. {ST['ok']}",2)

                                    elif command.startswith('برکناری @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('برکناری','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  not in ADMINS:mess = MPro(f"ایشون ادمین نیست.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                INFOS[object_guid]['admins'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) برکنار شد. {ST['ok']}",2)
                                                try:client.unset_admin(object_guid,reply_message_guid)
                                                except:pass
                                    elif command.startswith('برکناری u0'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('برکناری','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            elif reply_message_guid  not in ADMINS:mess = MPro(f"ایشون ادمین نیست.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                INFOS[object_guid]['admins'].pop(reply_message_guid)
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) برکنار شد. {ST['ok']}",2)
                                                try:client.unset_admin(object_guid,reply_message_guid)
                                                except:pass
                                    elif command.startswith('ارتقا @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('ارتقا','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                INFOS[object_guid]['admins'][reply_message_guid] = first_name
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) ادمین شد. {ST['ok']}",2)
                                                try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                                except:pass
                                    elif command.startswith('ارتقا u0'):                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('ارتقا','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            else:
                                                first_name = check_name(object_guid,reply_message_guid)
                                                INFOS[object_guid]['admins'][reply_message_guid] = first_name
                                                mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) ادمین شد. {ST['ok']}",2)
                                                try:client.set_admin(object_guid,reply_message_guid,[],random.choice(BoxEmoji))
                                                except:pass
                                    elif command.startswith('رفع محدودیت @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('رفع محدودیت','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) رفع محدودیت شد. {ST['ok']}",2)
                                            try:
                                                resetUser(reply_message_guid,object_guid)
                                                client.unban_member(object_guid,reply_message_guid)
                                            except:pass
                                    elif command.startswith('رفع محدودیت u0'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('رفع محدودیت','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid}) رفع محدودیت شد. {ST['ok']}",2)
                                            try:
                                                resetUser(reply_message_guid,object_guid)
                                                client.unban_member(object_guid,reply_message_guid)
                                            except:pass
                                    elif command.startswith('اخطار @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('اخطار','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            else:
                                                count = INFOS[object_guid]['warnning']
                                                first_name = check_name(object_guid,reply_message_guid)
                                                pscount = USERS[object_guid][reply_message_guid][1]
                                                isadmin = False
                                                if reply_message_guid in ADMINS:
                                                    isadmin = True
                                                pscount += 1
                                                if pscount >= count:
                                                        if isadmin:
                                                            INFOS[object_guid]['admins'].pop(reply_message_guid)
                                                            try:client.unset_admin(object_guid,reply_message_guid)
                                                            except:pass
                                                        else:
                                                            USERS[object_guid][reply_message_guid][1] = pscount
                                                            INFOS[object_guid]['ban'] += 1
                                                            try:
                                                                reply_message_banded_id = client.ban_member(object_guid,reply_message_guid)['data']['chat_update']['chat']['last_message']['message_id']
                                                                resetUser(reply_message_guid,object_guid)
                                                                if int(SETTING_KEYS[8]):mess = INFOS[object_guid]['bye']
                                                            except:pass
                                                        if pscount == count:
                                                            try:
                                                                if int(SETTING_KEYS[6]):
if isadmin:
    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid})〔{str(pscount)}/{str(count)}〕⚠️",2)
else:
    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid})〔{str(pscount)}/{str(count)}〕🚫",2)
                                                            except:pass
                                                else:
                                                    USERS[object_guid][reply_message_guid][1] = pscount
                                                    try:
                                                        if int(SETTING_KEYS[6]):
                                                            mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid})〔{str(pscount)}/{str(count)}〕⚠️",2)
                                                    except:pass
                                    elif command.startswith('اخطار u0'):                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('اخطار','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            if reply_message_guid == OWNER:mess = MPro(f"ایشون سازنده من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == HOWNER:mess = MPro(f"ایشون مالک من هستید.{ST['ok']}",2)
                                            elif reply_message_guid == GUIDME:mess = MPro(f"ایشون من هستم.{ST['ok']}",2)
                                            elif reply_message_guid in FULL_ADMINS:mess = MPro(f"ایشون ادمین ویژه است.{ST['ok']}",2)
                                            else:
                                                count = INFOS[object_guid]['warnning']
                                                first_name = check_name(object_guid,reply_message_guid)
                                                pscount = USERS[object_guid][reply_message_guid][1]
                                                isadmin = False
                                                if reply_message_guid in ADMINS:
                                                    isadmin = True
                                                pscount += 1
                                                if pscount >= count:
                                                        if isadmin:
                                                            INFOS[object_guid]['admins'].pop(reply_message_guid)
                                                            try:client.unset_admin(object_guid,reply_message_guid)
                                                            except:pass
                                                        else:
                                                            USERS[object_guid][reply_message_guid][1] = pscount
                                                            INFOS[object_guid]['ban'] += 1
                                                            try:
                                                                result = client.ban_member(object_guid,reply_message_guid)
                                                                resetUser(reply_message_guid,object_guid)
                                                                if int(SETTING_KEYS[8]):
                                                                    mess = INFOS[object_guid]['bye']
                                                                    reply_message_banded_id = result['data']['chat_update']['chat']['last_message']['message_id']
                                                            except:pass
                                                        if pscount == count:
                                                            try:
                                                                if int(SETTING_KEYS[6]):
if isadmin:
    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid})〔{str(pscount)}/{str(count)}〕⚠️",2)
else:
    mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid})〔{str(pscount)}/{str(count)}〕🚫",2)
                                                            except:pass
                                                else:
                                                    USERS[object_guid][reply_message_guid][1] = pscount
                                                    try:
                                                        if int(SETTING_KEYS[6]):
                                                            mess = MPro(f"کاربر @@ {first_name} @@({reply_message_guid})〔{str(pscount)}/{str(count)}〕⚠️",2)
                                                    except:pass
                                    elif command.startswith('حذف اخطار @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('حذف اخطار','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            resetUser(reply_message_guid,object_guid)
                                            mess = MPro(f"اخطار @@ {first_name} @@({reply_message_guid}) حدف شد. "+ST['ok'],2)
                                    elif command.startswith('حذف اخطار u0'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('حذف اخطار','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            first_name = check_name(object_guid,reply_message_guid)
                                            resetUser(reply_message_guid,object_guid)
                                            mess = MPro(f"اخطار @@ {first_name} @@({reply_message_guid}) حدف شد. "+ST['ok'],2)
                                    elif command.startswith('امار @'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('امار','')
                                        reply_message_guid = getinfos(command)
                                        if reply_message_guid:
                                            rank = formrank(Coder,ADMINS,FULL_ADMINS,HOWNER,OWNER,reply_message_guid)
                                            mess = MPro(f"مقام 〔 {rank} 〕",4)
                                            user = client.get_chat_info(reply_message_guid)['user']
                                            mess += manage_info(user)
                                            if reply_message_guid not in USERS[object_guid]:getInfoUser(object_guid,reply_message_guid)
                                            mess += formInfo(USERS[object_guid][reply_message_guid])
                                            mess += '\n'
                                            mess += MPro(reply_message_guid)
                                            mess += '\n─┅━━━━━━━┅─'
                                            if 'bio' in user:
                                                bio = user['bio']
                                                mess += "\n\n"+bio
                                    elif command.startswith('امار u0'):
                                        mess = MPro(f"کاربر یافت نشد.{ST['ok']}",2)
                                        command = command.replace('امار','')
                                        reply_message_guid = getinfos(command,False)
                                        if reply_message_guid:
                                            rank = formrank(Coder,ADMINS,FULL_ADMINS,HOWNER,OWNER,reply_message_guid)
                                            mess = MPro(f"مقام 〔 {rank} 〕",4)
                                            user = client.get_chat_info(reply_message_guid)['user']
                                            mess += manage_info(user)
                                            if reply_message_guid not in USERS[object_guid]:getInfoUser(object_guid,reply_message_guid)
                                            mess += formInfo(USERS[object_guid][reply_message_guid])
                                            mess += '\n'
                                            mess += MPro(reply_message_guid)
                                            mess += '\n─┅━━━━━━━┅─'
                                            if 'bio' in user:
                                                bio = user['bio']
                                                mess += "\n\n"+bio      

                                    elif command.startswith('کرونا '):
                                        locat = command.replace('کرونا ','').strip()
                                        result = requests.get(url ="https://one-api.ir/corona/?token=833942:64919956105c3", timeout=30).json()
                                        if result['status'] == 200:
                                            mess = MPro(f"کشور مورد نظر یافت نشد.{ST['ok']}",2)
                                            entries , isok = result['result']['entries'] , False
                                            for mins in Countris:
                                                for min in mins:
                                                    if locat == min:
                                                        isok = True
                                                        break
                                                if isok:
                                                    pname = mins[0]
                                                    ename = mins[1]
                                                    for num in entries:
                                                        if 'country' in num:
                                                            name = num['country']
                                                            if name == pname:
                                                                country = num
                                                                Name_continent = country['continent']
                                                                Name_country = country['country']
                                                                cases = country['cases']
                                                                deaths = country['deaths']
                                                                recovered = country['recovered']

                                                                Name_continentF = ''
                                                                if Name_continent == 'Asia':Name_continentF = 'اسیا'
                                                                elif Name_continent == 'Africa':Name_continentF = 'افریقا'
                                                                elif Name_continent == 'Europe':Name_continentF = 'اروپا'
                                                                elif Name_continent == 'North America':Name_continentF = 'امریکای شمالی'
                                                                elif Name_continent == 'South America':Name_continentF = 'امریکای جنوبی'
                                                                elif Name_continent == 'Australia':Name_continentF = 'استرالیا'
                                                                elif Name_continent == 'Antarctica':Name_continentF = 'جنوبگان'
                                                                elif Name_continent == 'Oceania':Name_continentF = 'اقیانوسیه'

                                                                mess = "⌯ #ᑕOᖇOᑎᗩ\n\n"
                                                                mess += "𝗖𝗼𝗻𝘁𝗶𝗻𝗲𝗻𝘁 » "+Name_continent+" ⌯ "+Name_continentF+"\n"
                                                                mess += "𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » "+Name_country+" ⌯ "+ename+"\n\n"
                                                                mess += "𝗖𝗮𝘀𝗲𝘀 » "+cases+" "+"مورد"+"\n"
                                                                mess += "𝗗𝗲𝗮𝘁𝗵𝘀 » "+deaths+" "+"فوت شده"+"\n"
                                                                mess += "𝗥𝗲𝗰𝗼𝘃𝗲𝗿𝗱 » "+recovered+" "+"بهبود یافته"+"\n"
                                                                break
                                                    break
                                    elif command.startswith('وضعیت '):
                                        locat = command.replace('وضعیت','').strip()
                                        cities = [['Tehran','تهران'],['Tabriz','تبریز','اذربایجان شرقی','اذربایجان شرقی'],['Urmia','ارومیه','اذربایجان غربی','اذربایجان غربی'],['Ardabil','اردبیل'],['Isfahan','اصفهان'],['Karaj','کرج','البرز'],['Ilam','ایلام'],['Bushehr','بوشهر'],['Shahre-Kord','شهرکرد','چهارمحال و بختیاری','چهارمحال'],['Birjand','بیرجند','خراسان جنوبی'],['Mashhad','مشهد','خراسان رضوی'],['Bojnord','بجنورد','خراسان شمالی'],['Ahvaz','اهواز','خوزستان'],['Zanjan','زنجان'],['Semnan','سمنان'],['Zahedan','زاهدان','سیستان و بلوچستان','سیستان'],['Shiraz','شیراز','فارس'],['Qazvin','قزوین'],['Qom','قم'],['Sanandaj','کردستان','سنندج'],['Kerman','کرمان'],['Kermanshah','کرمانشاه'],['Yasuj','یاسوج','کهگیلویه و بویراحمد','کهگیلویه'],['Gorgan','گلستان','گرگان'],['Rasht','گیلان','رشت'],['Khorramabad','لرستان','خرم‌اباد','خرم‌اباد'],['Sari','مازندران','ساری'],['Arak','اراک','مرکزی'],['Bandar-Abbas','هرمزگان','بندرعباس'],['Hamadan','همدان'],['Yazd','یزد']]
                                        elocat = False
                                        mess = False
                                        for city in cities:
                                            for step in city:
                                                if step == locat:
                                                    elocat = city[0]
                                                    plocat = city[1]
                                                    break
                                            mess = MPro(f"شهر مورد نظر یافت نشد.{ST['ok']}",2)
                                            if elocat:
                                                response = requests.get(url ="http://dorweb.ir/api/weather/"+elocat, timeout=30).json()
                                                mess = MPro(f"خطایی رخ داد.{ST['ok']}",2)
                                                if not response['IsOK']:break

                                                result = response['Result']
                                                location = result['location']
                                                province , city = location['province']['caption'] , location['city']['caption']
                                                weather = result['weather']
                                                persian_dt , descriptionF , descriptionE , temp_min , temp_max , humidity , windSpeed = weather['persian_dt'] , weather['description'] , str(weather['main']) , str(weather['temp_min']) , str(weather['temp_max']) , str(weather['humidity']) , str(weather['wind']['speed'])
                                                temp_max , temp_min , humidity , windSpeed= temp_max+"°C" , temp_min+"°C" , humidity+" %" , windSpeed+" km/h"

                                                mess = "⌯ #ᗯᗴᗩTᕼᗴᖇ\n\n"
                                                mess += f"𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻 » {province} / {city}\n"
                                                mess += f"𝗗𝗮𝘁𝗲 » {persian_dt}\n\n"
                                                mess += f"{descriptionE} ⌯ {descriptionF}\n"
                                                mess += f"𝗧𝗲𝗺𝗽 » {temp_max} / {temp_min}\n"
                                                mess += f"𝗛𝘂𝗺𝗶𝗱𝗶𝘁𝘆 » {humidity}\n"
                                                mess += f"𝗪𝗶𝗻𝗱 𝗦𝗽𝗲𝗲𝗱 » {windSpeed}\n"
                                                break

                                if not mess and wordCount <= 4:
                                    cmd,cmdx,order = False,False,False
                                    cmds_on = ('باز','روشن','ازاد','فعال','وصل')
                                    cmds_off = ('بسته','خاموش','قفل','غیرفعال','قطع')
                                    for cmd_on in cmds_on:
                                        if cmd_on in command:
                                            cmd , cmdx , Vb = command.replace(cmd_on,'') , cmd_on , True
                                    for cmd_off in cmds_off:
                                        if cmd_off in command:
                                            cmd , cmdx , Vb = command.replace(cmd_off,'') , cmd_off , False

                                    if cmd and cmd.startswith('دستور '):cmd , order = cmd.replace('دستور','') , True

                                    if cmd:
                                        cmd = cmd.strip()
                                        if cmd in Listkeys and order:
                                            isok = True
                                            if TIP <= 3 and int(SETTING_KEYS[17]) == 0:isok = False
                                            if isok:
                                                key = int(Listkeys[cmd])                                                ORDERS_KEYS[key] = str(int(Vb))
                                                INFOS[object_guid]['keys'] = ''.join(ORDERS_KEYS)
                                                mess = MPro(f"دستور {cmd} {cmdx} است. {ST['ok']}",2)
                                        elif not order:
                                            match cmd:
                                                case 'کال' | 'ویسکال':
                                                    if Vb:
                                                        mess = MPro(f"ویسکال ایجاد شد. {ST['ok']}",2)
                                                        try:
                                                            result = client.create_voice_chat(object_guid)
                                                            if result['status'] == 'VoiceChatExist':
                                                                countMember = result['exist_group_voice_chat']['participant_count']
                                                                title = result['exist_group_voice_chat']['title']
                                                                mess = MPro(f"ویسکال ایجاد شده است. {ST['ok']}",4)
                                                                mess += MPro(f"عنوان : {title}")
                                                                mess += MPro(f"تعداد افراد : {str(countMember)}")
                                                            else:INFOS[object_guid]['voice_call'] += 1
                                                        except:mess = MPro(f"کال ایجاد نشد.{ST['ok']}",2)
                                                    else:
                                                        mess = MPro(f"کال قطع شد. {ST['ok']}",2)
                                                        try:
                                                            result = client.get_chat_info(object_guid)
                                                            if 'group_voice_chat_id' in result['chat']:
                                                                group_voice_chat_id = result['chat']['group_voice_chat_id']
                                                                client.discard_voice_chat(object_guid,group_voice_chat_id)
                                                        except:mess = MPro(f"کال قطع نشد. {ST['ok']}",2)
                                                case 'ضدفش' | 'ضد فش':
                                                    if Vb:
                                                        words = ['کص','کوبص','کوص','کون','کیر','ممه','لخت','برهنه','سکس','جنده','گایید','گاید','پورن','گوه','sex','xnxx','porn']
                                                        for word in words:
                                                            if word not in INFOS[object_guid]['filterlist']:
                                                                INFOS[object_guid]['filterlist'].append(word)
                                                        keys = list(INFOS[object_guid]['locks'])
                                                        key = int(15)
                                                        keys[key] = '0'
                                                        INFOS[object_guid]['locks'] = ''.join(keys)
                                                    else:
                                                        keys = list(INFOS[object_guid]['locks'])
                                                        key = int(15)
                                                        keys[key] = '1'
                                                        INFOS[object_guid]['locks'] = ''.join(keys)
                                                    mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                case "سرگرمی":
                                                    if TIP >= 4:
                                                        steps = ['تاس', 'عدد شانسی', 'سکه', 'جوک', 'چالش', 'بیو', 'فکت', 'اعتراف', 'دانستنی', 'داستان', 'تکست', 'گنگ', 'فونت', 'فال حافظ', 'پروفایل', 'بکگراند', 'انگیزشی', 'ذکر', 'والپیپر', 'پروکسی', 'فتوگرافی', 'دقت', 'حق', 'پ ن پ', 'ویس', '/', 'ویس زن', 'ویس مرد', 'ساخت عکس', 'لوگو', 'عکس', 'لوگو3', 'لوگو2', '//', 'سخنگو', 'ترجمه', 'افکت', 'اسم', 'ارز']
                                                        for step in steps:
                                                            key = int(Listkeys[step])
                                                            ORDERS_KEYS[key] = str(int(Vb))
                                                        INFOS[object_guid]['keys'] = ''.join(ORDERS_KEYS)
                                                        mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                    else:mess = MPro(f"دسترسی تغییر آن را ندارید. {ST['ok']}",2)
                                                case "سخنگو با ادب" | "سخنگو باادب" | "سخنگو بی ادب" | "سخنگو بی‌ادب":
                                                    if TIP >= 4:
                                                        if cmd == "سخنگو بی ادب" or cmd == "سخنگو بی‌ادب":
                                                            if Vb:
                                                                handle_text_file(text_input='rude')
                                                                typespeak = 'rude'
                                                            else:
                                                                handle_text_file(text_input='polit')
                                                                typespeak = 'polit'
                                                        else:
                                                            if Vb:
                                                                handle_text_file(text_input='polit')
                                                                typespeak = 'polit'
                                                            else:
                                                                handle_text_file(text_input='rude')
                                                                typespeak = 'rude'
                                                        mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                    else:mess = MPro(f"دسترسی تغییر آن را ندارید. {ST['ok']}",2)
                                                case "افزودن عضو":
                                                    Set_group_default_access(object_guid,"AddMember",Vb)
                                                    mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                case "مشاهده مدیر" | "مشاهده مدیران":
                                                    Set_group_default_access(object_guid,"ViewAdmins",Vb)
                                                    mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                case "مشاهده اعضا":
                                                    Set_group_default_access(object_guid,"ViewMembers",Vb)
                                                    mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                case 'گپ' | 'گروه':
                                                    Set_group_default_access(object_guid,"SendMessages",Vb)
                                                    mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                case _:
                                                    steps = cmd.split(' ')
                                                    if cmd in Listlocks:                                                        isok = True
                                                        if TIP <= 3 and int(SETTING_KEYS[18]) == 0:isok = False
                                                        if isok:
                                                            key = int(Listlocks[cmd])
                                                            LOCKS_KEYS[key] = str(int(Vb))
                                                            INFOS[object_guid]['locks'] = ''.join(LOCKS_KEYS)
                                                            mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                    elif cmd in Listset:                                                        isok = True
                                                        if TIP <= 3 and int(SETTING_KEYS[16]) == 0:isok = False
                                                        if isok:
                                                            if cmd == 'تنظیم دستورات':
                                                                if TIP <= 2:
                                                                    isok = False
                                                                    mess = MPro(f"دسترسی تغییر آن را ندارید. {ST['ok']}",2)
                                                            elif cmd == 'تنظیم محدودیت':
                                                                if TIP <= 2:
                                                                    isok = False
                                                                    mess = MPro(f"دسترسی تغییر آن را ندارید. {ST['ok']}",2)

                                                            if isok:
                                                                key = int(Listset[cmd])
                                                                SETTING_KEYS[key] = str(int(Vb))
                                                                INFOS[object_guid]['setting'] = ''.join(SETTING_KEYS)
                                                                mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)

                                                                # EXTRA
                                                                if cmd == 'حذف خودکار':
                                                                    if int(Vb) == 1:
timer = 60
commands_auto = ['حذف پیام مدیریتی'+'-']
new = []
for step in INFOS[object_guid]['AUTOS']:
    if len(commands_auto) > 0:
        commands_new = []
        for cm_auto_saved in step['COMMANDS']:
            deleted = False
            for cm_auto in commands_auto:
                if cm_auto == cm_auto_saved:
                    deleted = True
            if deleted:continue
            commands_new.append(cm_auto_saved)
        if len(commands_new) <= 0:continue
        step['COMMANDS'] = commands_new
    else:
        if step['PERTIME']['per'] == timer:
            continue
    new.append(step)
INFOS[object_guid]['AUTOS'] = new
time_come = get_iran_timestamp()
STEP = {}
STEP['TYPE'] = 'pertime'
STEP['PERTIME'] = {}
STEP['PERTIME']['old'] = time_come
STEP['PERTIME']['per'] = timer
STEP['COMMANDS'] = commands_auto
STEP['GUID_SENDER'] = guid_sender
INFOS[object_guid]['AUTOS'].append(STEP)
                                                                    elif int(Vb) == 0:
STMessages[object_guid] = []
timer = 60
commands_auto = ['حذف پیام مدیریتی'+'-']
new = []
for step in INFOS[object_guid]['AUTOS']:
    if len(commands_auto) > 0:
        commands_new = []
        for cm_auto_saved in step['COMMANDS']:
            deleted = False
            for cm_auto in commands_auto:
                if cm_auto == cm_auto_saved:
                    deleted = True
            if deleted:continue
            commands_new.append(cm_auto_saved)
        if len(commands_new) <= 0:continue
        step['COMMANDS'] = commands_new
    else:
        if step['PERTIME']['per'] == timer:
            continue
    new.append(step)
INFOS[object_guid]['AUTOS'] = new
                                                                elif cmd == 'ضد تبچی' and Vb:
                                                                    # close group
                                                                    try:Set_group_default_access(object_guid,"SendMessages",False)
ResultME = send_message(OBJM,MPro(f"گپ بسته شد. {ST['ok']}",2),message_id)
                                                                    except:ResultME = send_message(OBJM,MPro(f"گپ بسته نشد. {ST['ok']}",2),message_id)
                                                                    nxx = ''
                                                                    y = 3
                                                                    x = 0
                                                                    while x < len(object_guid):
nxx += object_guid[x:x+y:y]
x += y
                                                                    # send message for adding
                                                                    extra = MPro(f"برای چت کردن باید اد بشی. {ST['ok']}",2)
                                                                    extra += MPro(f"کد زیر رو پی ویم ارسال کن تا ادمینت کنم. {ST['ok']}",2)
                                                                    extra += '\n'
                                                                    extra += MPro(f"#{nxx}")
                                                                    message_sended_id = client.send_text(object_guid,extra)['message_update']['message_id']
                                                                    # pin message
                                                                    client.pin_message(object_guid,message_sended_id)
                                                                    ResultME = send_message(OBJM,MPro(f"پیام پین شد. {ST['ok']}",2),message_sended_id)
                                                                elif cmd == 'ضد تبچی' and not Vb:
                                                                    try:Set_group_default_access(object_guid,"SendMessages",True)
ResultME = send_message(OBJM,MPro(f"گپ باز شد. {ST['ok']}",2),message_id)
                                                                    except:ResultME = send_message(OBJM,MPro(f"گپ باز نشد. {ST['ok']}",2),message_id)
                                                                elif cmd == 'عضویت اجباری' and Vb:
                                                                    if len(INFOS[object_guid]['channels']) == 0:
extra = MPro(f"عزیزم لطفا چنل یا گروهی تعریف کن تا کاربرارو مجبور به عضو شدن کنم. {ST['ok']}")
extra += MPro(f"و توجه داشته باش که من باید در این چنل یا گروه ها ادمین باشم تا بتونم چک کنم. {ST['ok']}")
extra += '\n'
extra += MPro(f"عضویت @example",2)
extra += MPro(f"عضویت اجباری روشن / خاموش ",2)
extra += MPro(f"لیست عضویت ",2)
extra += MPro(f"پاکسازی لیست عضویت",2)
extra += MPro(f"بررسی مجدد عضویت",2)
client.send_text(object_guid,extra,message_id)
                                                                elif cmd == 'سخنگو' and not Vb:
                                                                    ARMessages[object_guid] = []
                                                                elif cmd == 'ربات' and not Vb:
                                                                    ARMessages[object_guid] = []


                                                    elif len(steps) >= 1:
                                                        isban = steps[0]                                                        order = cmd.replace(isban,'').strip()
                                                        if isban == 'بن':
                                                            if order in Listlocks:
                                                                locks_ban = list(INFOS[object_guid]['locks_ban'])
                                                                locks_ban[Listlocks[order]] = str(int(Vb))
                                                                INFOS[object_guid]['locks_ban'] = ''.join(locks_ban)
                                                                mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)
                                                        elif isban == "اخطار":
                                                            if order in Listlocks:
                                                                locks_warning_show = list(INFOS[object_guid]['locks_warning_show'])
                                                                locks_warning_show[Listlocks[order]] = str(int(Vb))
                                                                INFOS[object_guid]['locks_warning_show'] = ''.join(locks_warning_show)
                                                                mess = MPro(f"{cmd} {cmdx} است. {ST['ok']}",2)

                                if command.startswith('تنظیم ') and wordCount <= 4 and not mess:
                                    xcomand = command.replace('تنظیم','').strip()
                                    if xcomand.startswith('اخطار'):
                                        isok = False
                                        zcomand = xcomand.replace('اخطار','').strip()
                                        spaces = zcomand.split(' ')
                                        if len(spaces) > 1:spaces.reverse()
                                        count = spaces[0]
                                        order = zcomand.replace(count,'').strip()
                                        iscount = False
                                        try:count,iscount = int(count),True
                                        except:pass
                                        if iscount:
                                            if len(order) > 0:
                                                if order in Listlocks:
                                                    key_order = Listlocks[order]
                                                    locks_warning = list(INFOS[object_guid]['locks_warning'])
                                                    if count >= 10:count = 9
                                                    elif count <= 0:count = 0
                                                    locks_warning[key_order] = str(count)
                                                    INFOS[object_guid]['locks_warning'],isok = ''.join(locks_warning),True
                                                else:mess = MPro(f"قفل مورد نظر یافت نشد.{ST['ok']}",2)
                                            else:
                                                if count > 100:count = 100
                                                elif count <= 0:count = 0
                                                INFOS[object_guid]['warnning'],isok = count,True
                                        if isok:mess = MPro(f"{xcomand} تنظیم شد. {ST['ok']}",2)
                                    elif xcomand.startswith('فونت'):
                                        zcomand = xcomand.replace('فونت','').strip()
                                        if zcomand in Fonts_text:
                                            zcomand = Fonts_text[zcomand]
                                            INFOS[object_guid]['types']['font'] = zcomand
                                            mess = MPro(f"{xcomand} تنظیم شد. {ST['ok']}",2)
                                        else:mess = MPro(f" فونت موردنظر یافت نشد. {ST['ok']}",2)
                                    elif xcomand.startswith('شکل'):
                                        zcomand = xcomand.replace('شکل','').strip()
                                        if zcomand in Types_text:
                                            zcomand = Types_text[zcomand]
                                            INFOS[object_guid]['types']['type'] = zcomand
                                            mess = MPro(f"{xcomand} تنظیم شد. {ST['ok']}",2)
                                        else:mess = MPro(f" شکل موردنظر یافت نشد. {ST['ok']}",2)
                                    elif xcomand.startswith('علامت'):
                                        zcomand = xcomand.replace('علامت','').strip()
                                        INFOS[object_guid]['types']['ok'] = zcomand.strip()[0:4]
                                        mess = MPro(f"{xcomand} تنظیم شد. {ST['ok']}",2)

                                if mess:ResultME = send_message(OBJM,mess,message_id)

                    # FOR ADMINS AND MEMBERS
                    if is_reply_message and not ResultME and command in list_command_users_reply_keys:
                        if TIP >= 4:step1,step2,step3 = 1,1,True
                        else:step3 , step2 , step1 = PorotectMSS(SETTING_KEYS,TimeMessages,5) , int(ORDERS_KEYS[Listkeys[command]]) , int(SETTING_KEYS[0])
                        if step1 and step2 and step3:
                            # CHECK JOINING
                            if TIP <= 3 and int(SETTING_KEYS[14]):
                                isok = joining(INFOOBJECT['channels'],object_guid,guid_sender,ST['ok'])
                                if isok and isok is not True:ResultME = send_message(OBJM,isok,message_id)
                                elif isok is False:ResultME = True
                            # FOR MEMBERS
                            if not ResultME:
                                text = list_command_users_reply[command](OBJM)
                                if text:send_message(OBJM=OBJM,text=text,message_id=message_id)
                                ResultME = True
                    elif not ResultME and command in list_command_users_keys:
                        if TIP >= 4:step1,step2,step3 = 1,1,True
                        else:step3 , step2 , step1 = PorotectMSS(SETTING_KEYS,TimeMessages,5) , int(ORDERS_KEYS[Listkeys[command]]) , int(SETTING_KEYS[0])
                        if step1 and step2 and step3:
                            # CHECK JOINING
                            if TIP <= 3 and int(SETTING_KEYS[14]):
                                isok = joining(INFOOBJECT['channels'],object_guid,guid_sender,ST['ok'])
                                if isok and isok is not True:ResultME = send_message(OBJM,isok,message_id)
                                elif isok is False:ResultME = True
                            # FOR MEMBERS
                            if not ResultME:
                                text = list_command_users[command](OBJM)                                if text:send_message(OBJM=OBJM,text=text,message_id=message_id)
                                ResultME = True

                # for fulladmins up - reply
                if TIP >= 2 and not ResultME and is_reply_message:
                    # CHECK JOINING
                    if TIP <= 3 and int(SETTING_KEYS[14]):
                        isok = joining(INFOOBJECT['channels'],object_guid,guid_sender,ST['ok'])
                        if isok and isok is not True:ResultME = send_message(OBJM,isok,message_id)
                        elif isok is False:ResultME = True
                    if not ResultME:
                        match command:
                            case '/':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['/']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess = steps['text']
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            baner = INFOS[object_guid]['baner']
                                            ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                            try:mess = (requests.get(f"https://api-free.ir/api/chat.php?text={QUS}", timeout=30).json())['result']
                                            except:pass
                                    ResultME = send_message_limited(OBJM,"**"+mess+"**",is_reply_message)
                            case '//':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['//']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess = steps['text']
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            baner = INFOS[object_guid]['baner']
                                            ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                            try:mess = (requests.get(f"https://api-free.ir/api/chat2.php?text={QUS}", timeout=30).json())['result']
                                            except:pass
                                    ResultME = send_message_limited(OBJM,"**"+mess+"**",is_reply_message)
                            case 'ویس زن':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ویس زن']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess,sended = steps['text'],False
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            baner = INFOS[object_guid]['baner']
                                            ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                            name_file = f'voice_{str(get_iran_timestamp())}.mp3'
                                            voice_AI(QUS,'DilaraNeural',name_file)
                                            text = MPro(f"متن شما : {QUS}",4)
                                            try:
                                                ResultME,sended = client.send_voice(object_guid,name_file,message_id,file_name=name_file,text=text),True
                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            except :pass
                                            os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                            case 'ویس مرد':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ویس مرد']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess,sended = steps['text'],False
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            baner = INFOS[object_guid]['baner']
                                            ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                            name_file = f'voice_{str(get_iran_timestamp())}.mp3'
                                            voice_AI(QUS,'FaridNeural',name_file)
                                            text = MPro(f"متن شما : {QUS}",4)
                                            try:
                                                ResultME,sended = client.send_voice(object_guid,name_file,message_id,file_name=name_file,text=text),True
                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            except:pass
                                            os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                            case 'لوگو2':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['لوگو2']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess,sended = steps['text'],False
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            if object_guid not in limitAPI:limitAPI[object_guid] = 0
                                            limitAPI[object_guid] += 1
                                            if limitAPI[object_guid] < 6:
                                                mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                                baner = INFOS[object_guid]['baner']
                                                ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                                if not is_english_text(QUS):
                                                    QUS = Translater(text=QUS,to_lang='en')
                                                urls = (requests.get("https://api-free.ir/api/Logo-top.php?page=90&text="+QUS, timeout=30).json())['result']
                                                rand = random.randint(0,len(urls)-1)
                                                url = urls[rand].replace(';','&')
                                                response = requests.get(url)
                                                name_file = f'logo2_{str(get_iran_timestamp())}.png'
                                                with open(name_file, "wb") as file:
                                                    file.write(response.content)
                                                    file.close()
                                                text = MPro(f"متن شما : {QUS}",4)
                                                try:
                                                    ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                                    save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                except:pass
                                                os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                            case 'لوگو':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['لوگو']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess,sended = steps['text'],False
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            baner = INFOS[object_guid]['baner']
                                            ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                            rand = str(random.randint(1,100))
                                            if not is_english_text(QUS):                                                QUS = Translater(text=QUS,to_lang='en')
                                            result = requests.get("http://api2.haji-api.ir/ephoto360?type=text&id="+rand+"&text="+QUS, timeout=30)
                                            name_file = f'logo_{str(get_iran_timestamp())}.png'
                                            with open(name_file, "wb") as file:
                                                file.write(result.content)
                                                file.close()
                                            text = MPro(f"متن شما : {QUS}",4)
                                            try:
                                                ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            except:pass
                                            os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                            case 'عکس':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['عکس']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess,sended = steps['text'],False
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            if object_guid not in limitAPI:limitAPI[object_guid] = 0
                                            limitAPI[object_guid] += 1
                                            if limitAPI[object_guid] < 6:
                                                mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                                baner = INFOS[object_guid]['baner']
                                                ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                                if not is_english_text(QUS):
                                                    QUS = Translater(text=QUS,to_lang='en')
                                                urls = (requests.get("https://haji-api.ir/prompts/?text="+QUS, timeout=30).json())['result']
                                                rand = random.randint(0,len(urls)-1)
                                                response = requests.get(urls[rand], timeout=30)
                                                name_file = f'photoAi_{str(get_iran_timestamp())}.png'
                                                with open(name_file, "wb") as file:
                                                    file.write(response.content)
                                                    file.close()
                                                text = MPro(f"متن شما : {QUS}",4)
                                                try:
                                                    ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                                    save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                except:pass
                                                os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                            case 'ساخت عکس':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ساخت عکس']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess,sended = steps['text'],False
                                    if steps['ok']:
                                        QUS = steps['text']
                                        if len(QUS) > 0:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            baner = INFOS[object_guid]['baner']
                                            ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                            if not is_english_text(QUS):                                                QUS = Translater(text=QUS,to_lang='en')
                                            data = requests.get(f"https://api-free.ir/api/img.php?text={QUS}&v=3.5", timeout=30).json()
                                            response = requests.get(random.choice(data['result']), timeout=30)
                                            name_file = f'photoAi_{str(get_iran_timestamp())}.png'
                                            with open(name_file, "wb") as file:
                                                file.write(response.content)
                                                file.close()
                                            text = MPro(f"متن شما : {QUS}",4)
                                            try:
                                                ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                                save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                            except:pass
                                            os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                            case 'حذف فیلتر':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['حذف فیلتر']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess = steps['text']
                                    if steps['ok']:
                                        reply_message_text = steps['text']
                                        if reply_message_text in INFOS[object_guid]['filterlist']:
                                            INFOS[object_guid]['filterlist'].remove(reply_message_text)
                                            mess = MPro(f"کلمه {reply_message_text} از لیست فیلتر حذف شد. {ST['ok']}",2)
                                        else:mess = MPro(f"کلمه {reply_message_text} در لیست فیلتر یافت نشد. {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)
                            case 'حذف کلید':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['حذف کلید']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess = steps['text']
                                    if steps['ok']:
                                        reply_message_text = steps['text']
                                        if reply_message_text in INFOS[object_guid]['main_keys']:
                                            INFOS[object_guid]['main_keys'].remove(reply_message_text)
                                            mess = MPro(f"کلمه {reply_message_text} از لیست کلید حذف شد. {ST['ok']}",2)
                                        else:mess = MPro(f"کلمه {reply_message_text} در لیست کلید یافت نشد. {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)
                            case 'فیلتر':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['فیلتر']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess = steps['text']
                                    if steps['ok']:
                                        reply_message_text = steps['text']
                                        if reply_message_text in INFOS[object_guid]['filterlist']:
                                            mess = MPro(f"کلمه {Font_filter(reply_message_text)} در لیست فیلتر بود. {ST['ok']}",2)
                                        else:
                                            INFOS[object_guid]['filterlist'].append(reply_message_text)
                                            mess = MPro(f"کلمه {Font_filter(reply_message_text)} فیلتر شد. {ST['ok']}",2)
                                    ResultME = send_message_limited(OBJM,mess,message_id)
                            case 'فونت':
                                isok = 1
                                if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['فونت']])
                                if isok:
                                    steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                    mess = steps['text']
                                    if steps['ok']:
                                        text = steps['text']
                                        if not is_english_text(text):
                                            text = Translater(text=text,to_lang='en')
                                        if len(text) > 0:
                                            rand = False
                                            if len(text) > 10:rand = True
                                            result = Fontmaker(text)
                                            mess = MPro(f"〔 فونت 〕",4)                                            if rand:
                                                num = int(random.randint(0,int(len(result))-1))
                                                mess += MPro(result[num])
                                            else:
                                                for font in result:mess += MPro(font)
                                    ResultME = send_message(OBJM,mess,message_id)
                            case 'افکت':
                                ResultME = send_message(OBJM,MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),message_id)
                            case _:
                                if command.startswith('ترجمه'):
                                    isok = 1
                                    if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ترجمه']])
                                    if isok:
                                        steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                        mess = steps['text']
                                        if steps['ok']:
                                            mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                            text = steps['text']
                                            steps = command.replace('ترجمه','').strip()
                                            target = False
                                            if len(steps) > 0:
                                                steps = steps.split(' ')                                                len_steps = len(steps)
                                                target = steps[len_steps-1]
                                            name_target = False
                                            for box_lang in Box_langs:
                                                if name_target:break
                                                for bx in box_lang:
                                                    if target == bx:
                                                        target = box_lang[2]
                                                        name_target = box_lang[0]
                                                        break
                                            if not target:target = 'fa'
                                            if not name_target:
                                                for box_lang in Box_langs:
                                                    if name_target:break                                                    for bx in box_lang:
                                                        if target == bx:                                                            name_target = box_lang[0]
                                                            break

                                            local = Detect_lang(text)
                                            name_local = False
                                            for box_lang in Box_langs:
                                                if name_local:break
                                                for bx in box_lang:
                                                    if local == bx:
                                                        name_local = box_lang[0]
                                                        break
                                            if not name_local:name_local = 'نامشخص'
                                            if name_target:
                                                try:
                                                    result = Translater(text=text,to_lang=target,from_lang=local)
                                                    mess = MPro(f"زبان اصلی : {name_local}",2)
                                                    mess += MPro(result,2)
                                                except:pass
                                            else:mess = MPro(f"زبان مورد نظر یافت نشد. {ST['ok']}",2)
                                        ResultME = send_message_limited(OBJM,mess,message_id)
                                elif command.startswith('ویس'):
                                    isok = 1
                                    if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ویس']])
                                    if isok:
                                        steps = get_reply_text(OBJM,object_guid,is_reply_message)
                                        mess = steps['text']
                                        if steps['ok']:
                                            mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                            text = steps['text']
                                            steps = command.replace('ویس','').strip()
                                            target = False
                                            if len(steps) > 0:
                                                steps = steps.split(' ')                                                len_steps = len(steps)
                                                target = steps[len_steps-1]
                                            name_target = False
                                            for box_lang in Box_langs:
                                                if name_target:break
                                                for bx in box_lang:
                                                    if target == bx:
                                                        target = box_lang[2]
                                                        name_target = box_lang[0]
                                                        break
                                            if not target:target = Detect_lang(text)
                                            if not name_target:
                                                for box_lang in Box_langs:
                                                    if name_target:break                                                    for bx in box_lang:
                                                        if target == bx:                                                            name_target = box_lang[0]
                                                            break

                                            local = Detect_lang(text)
                                            name_local = False
                                            for box_lang in Box_langs:
                                                if name_local:break
                                                for bx in box_lang:
                                                    if local == bx:
                                                        name_local = box_lang[0]
                                                        break
                                            if not name_local:name_local = 'نامشخص'
                                            if name_target:
                                                try:
                                                    result = Translater(text=text,to_lang=target,from_lang=local)
                                                    text = MPro(f"زبان اصلی : {name_local}",2)
                                                    text += MPro(result,2)
                                                    audio = Voice_google(text=result, lang=target)
                                                    name_file = f'transVoice_{str(get_iran_timestamp())}.mp3'
                                                    audio.save(name_file)
                                                    try:
                                                        ResultME,sended = client.send_voice(object_guid,name_file,message_id,file_name=name_file,text=text),True
                                                        save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                                    except:pass
                                                    os.remove(name_file)                                                except:pass
                                            else:mess = MPro(f"زبان مورد نظر یافت نشد. {ST['ok']}",2)
                                        if not sended:ResultME = send_message(OBJM,mess,message_id)

                # for all... - reply
                if not ResultME and is_reply_message:
                    # CHECK JOINING
                    if TIP <= 3 and int(SETTING_KEYS[14]):
                        isok = joining(INFOOBJECT['channels'],object_guid,guid_sender,ST['ok'])
                        if isok and isok is not True:ResultME = send_message(OBJM,isok,message_id)
                        elif isok is False:ResultME = True
                    if not ResultME:
                        if command.startswith('گزارش'):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['گزارش']])
                            if isok:
                                mess = MPro(f"کاربر شناسایی نشد. {ST['ok']}",2)
                                reply_message = GetInfoByMessageId(object_guid,is_reply_message)
                                if reply_message:
                                    global reaporter_limit
                                    if object_guid not in reaporter_limit:reaporter_limit[object_guid] = {}
                                    if guid_sender not in reaporter_limit[object_guid]:reaporter_limit[object_guid][guid_sender] = 0
                                    if reaporter_limit[object_guid][guid_sender] >= 2:mess = MPro(f"بیش از حد مجاز {ST['ok']}",2)
                                    else:
                                        reaporter_limit[object_guid][guid_sender] += 1
                                        reply_message_guid = GetReplyGuid(reply_message)
                                        reaporter_message = command.replace('گزارش','',1).strip()
                                        reaport_message = ''
                                        if 'text' in reply_message:
                                            reaport_message = reply_message['text']
                                        reaport_sender_info = client.get_chat_info(guid_sender)['user']
                                        time.sleep(0.25)
                                        reaport_user_info = client.get_chat_info(reply_message_guid)['user']
                                        reaport_text = MPro('گزارش ارسالی ‼️',4)
                                        reaport_text += MPro('مشخصات گزارش کننده - 👨🏻‍💻')
                                        reaport_text += manage_info(reaport_sender_info)
                                        reaport_text += MPro(f'گوید : {guid_sender}')
                                        reaport_text += MPro(f'توضیحات : {reaporter_message}')
                                        reaport_text += '\n'
                                        reaport_text += MPro('مشخصات فرد گزارش شده - 🔻')
                                        reaport_text += manage_info(reaport_user_info)
                                        reaport_text += MPro(f'گوید : {reply_message_guid}')
                                        reaport_text += MPro(f'پیام گزارش شده  : {reaport_message}')
                                        client.send_text(HOWNER,reaport_text)
                                        time.sleep(0.25)
                                        mess = MPro(f"گزارش ارسال شد. {ST['ok']}",2)
                                ResultME = send_message_limited(OBJM,mess,message_id)

                # for fulladmins up - reply
                if TIP >= 2 and not ResultME and ((is_reply_message and is_reply_message in ARMessages[object_guid]) or (not is_reply_message)):                    # CHECK JOINING
                    if TIP <= 3 and int(SETTING_KEYS[14]):
                        isok = joining(INFOOBJECT['channels'],object_guid,guid_sender,ST['ok'])
                        if isok and isok is not True:ResultME = send_message(OBJM,isok,message_id)
                        elif isok is False:ResultME = True
                    if not ResultME:
                        if command.find(' !!') >= 0:
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['سخنگو']])
                            if isok:
                                sended,key,ans = False,False,[]
                                result = Get_tip_from_str(command)
                                command = result['command']
                                TIP_ANS = result['TIP']
                                steps = command.split(' !!')
                                for step in steps:
                                    step = step.strip()
                                    if len(step) > 0:
                                        if not key:key = step
                                        else:ans.append(step)
                                if not TIP_ANS in SPEAKX:SPEAKX[TIP_ANS] = {}
                                SPEAK = SPEAKX[TIP_ANS]
                                if len(ans) <= 0:
                                    if key in SPEAK:
                                        cnt = str(len(SPEAK[key]))
                                        SPEAKX[TIP_ANS].pop(key)
                                        mess = f"{str(cnt)} کلمه و کلیدواژه 〔 {key} 〕 حذف شد. "
                                        sended = True
                                else:
                                    if key in SPEAK:
                                        cnt = 0
                                        for de in ans:
                                            for step in SPEAK[key]:
                                                if 'answer' in step and step['answer'] == de:
                                                    SPEAKX[TIP_ANS][key].remove(step)
                                                    cnt +=1
                                        if cnt != 0:
                                            mess = f"{str(cnt)} کلمه از کلیدواژه  〔 {key} 〕 حذف شد. "
                                            sended = True
                                if sended:
                                    UPFILES(file_speakx,SPEAKX)
                                    ResultME = send_message_limited(OBJM,mess,message_id)
                        elif command.startswith('! '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['سخنگو']])
                            if isok:
                                mess = MPro(f"〔 جملات مورد نظر 〕",1)
                                empty = True
                                search = command.replace('!','').strip()                                for TIP_ANS in SPEAKX:
                                    SPEAK = SPEAKX[TIP_ANS]
                                    rank = Rank_user(TIP_ANS,OBJM)
                                    for word in SPEAK:
                                        if word in search:
                                            empty = False
                                            mess += '\n'
                                            if TIP_ANS.startswith('u0'):                                                mess += MPro(f"{word} - @@{rank}@@({TIP_ANS})",2)
                                            else:
                                                mess += MPro(f"{word} - {rank}",2)
                                            mess += '\n'
                                            for step in SPEAK[word]:
                                                if 'answer' in step:
                                                    mess += MPro(step['answer'])
                                                if 'actions' in step:
                                                    form_actions = ''
                                                    first_cmd = True
                                                    for action in step['actions']:
                                                        if first_cmd:
                                                            first_cmd = False
                                                            form_actions += action
                                                            continue
                                                        form_actions += f" > {action}"
                                                    if len(form_actions) > 0:
                                                        mess += MPro(form_actions,4)
                                            mess += '\n'

                                if empty:mess = MPro(f"لغتی پیدا نشد.{ST['ok']}",2)
                                ResultME = send_message_limited(OBJM,mess,message_id,False)
                        elif command.find(' !') >= 0:
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['سخنگو']])
                            if isok:
                                result = Get_tip_from_str(command)
                                command = result['command']
                                TIP_ANS = result['TIP']
                                result = Get_actions_from_str(command)
                                command = result['command']
                                actions = result['actions']
                                steps = command.split('!')
                                iskey,isadded = False,False
                                if not TIP_ANS in SPEAKX:SPEAKX[TIP_ANS] = {}
                                SPEAK = SPEAKX[TIP_ANS]
                                for step in steps:
                                    if len(step) <= 0:continue
                                    if not iskey:
                                        key,iskey = step,True
                                        key = key.replace('آ','ا').strip()
                                    else:
                                        step = step.replace('آ','ا').strip()
                                        if not key in SPEAK:SPEAKX[TIP_ANS][key] = []
                                        child = {}
                                        if len(step) > 0:child['answer'] = step
                                        if len(actions) > 0:child['actions'] = actions
                                        SPEAKX[TIP_ANS][key].append(child)
                                        isadded = True
                                if not isadded and len(actions) > 0 and iskey:
                                    if not key in SPEAK:SPEAKX[TIP_ANS][key] = []
                                    child = {}
                                    child['actions'] = actions
                                    SPEAKX[TIP_ANS][key].append(child)
                                    isadded = True
                                if isadded:
                                    UPFILES(file_speakx,SPEAKX)
                                    mess = MPro(f"یاد گرفتم. {ST['ok']}",2)
                                    ResultME = send_message_limited(OBJM,mess,message_id)
                                    arange_list_words()

                        elif command.startswith('//') and len(command) > 1:
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['//']])
                            if isok:
                                QUS = command.replace('//','').strip()
                                if len(QUS) > 0:
                                    mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                    baner = INFOS[object_guid]['baner']
                                    ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                    try:mess = (requests.get(f"https://api-free.ir/api/chat2.php?text={QUS}", timeout=30).json())['result']
                                    except:pass
                                    ResultME = send_message_limited(OBJM,"**"+mess+"**",message_id)
                        elif command.startswith('/') and len(command) > 1:
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['/']])
                            if isok:
                                QUS = command.replace('/','').strip()
                                if len(QUS) > 0:
                                    mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                    baner = INFOS[object_guid]['baner']
                                    ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                    try:mess = (requests.get(f"https://api-free.ir/api/chat.php?text={QUS}", timeout=30).json())['result']
                                    except:pass
                                    ResultME = send_message_limited(OBJM,"**"+mess+"**",message_id)
                        elif command.startswith('ثبت یادداشت'):
                            command = command.replace('ثبت یادداشت','').strip()
                            if len(command) > 0:
                                INFOS[object_guid]['remmember'].append({'text':command,'date':get_iran_timestamp()})
                                mess = MPro(f"به لیست یادداشت اضافه شد. {ST['ok']}",2)
                                ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('ویس زن '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ویس زن']])
                            if isok:
                                QUS = command.replace('ویس زن','').strip()
                                if len(QUS) > 0:
                                    mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                    baner = INFOS[object_guid]['baner']
                                    ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                    name_file = f'voice_{str(get_iran_timestamp())}.mp3'
                                    voice_AI(QUS,'DilaraNeural',name_file)
                                    text = MPro(f"متن شما : {QUS}",4)
                                    try:
                                        ResultME,sended = client.send_voice(object_guid,name_file,message_id,file_name=name_file,text=text),True                                        save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                    except:pass
                                    os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('ویس مرد '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ویس مرد']])
                            if isok:
                                QUS = command.replace('ویس مرد','').strip()
                                if len(QUS) > 0:
                                    mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                    baner = INFOS[object_guid]['baner']
                                    ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                    name_file = f'voice_{str(get_iran_timestamp())}.mp3'
                                    voice_AI(QUS,'FaridNeural',name_file)
                                    text = MPro(f"متن شما : {QUS}",4)
                                    try:
                                        ResultME,sended = client.send_voice(object_guid,name_file,message_id,file_name=name_file,text=text),True                                        save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                    except:pass
                                    os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('ویس '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ویس']])
                            if isok:
                                mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                text = command.replace('ویس','').strip()                                local = Detect_lang(text)
                                name_target = False
                                for box_lang in Box_langs:
                                    if name_target:break
                                    for bx in box_lang:
                                        if local == bx:name_target = box_lang[0]
                                if not name_target:name_target = 'نامشخص'
                                try:
                                    audio = Voice_google(text=text, lang=local)
                                    name_file = f'voice_{str(get_iran_timestamp())}.mp3'
                                    audio.save(name_file)
                                    text = MPro(f"متن شما : {text} ({name_target})",4)
                                    try:
                                        ResultME,sended = client.send_voice(object_guid,name_file,message_id,file_name=name_file,text=text),True                                        save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                    except:pass
                                    os.remove(name_file)
                                except:pass
                            if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('لوگو2 '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['لوگو2']])
                            if isok:
                                QUS = command.replace('لوگو2','').strip()
                                if len(QUS) > 0:
                                    if object_guid not in limitAPI:limitAPI[object_guid] = 0
                                    limitAPI[object_guid] += 1
                                    if limitAPI[object_guid] < 6:
                                        mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                        baner = INFOS[object_guid]['baner']
                                        ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                        if not is_english_text(QUS):
                                            QUS = Translater(text=QUS,to_lang='en')
                                        urls = (requests.get("https://api-free.ir/api/Logo-top.php?page=90&text="+QUS, timeout=30).json())['result']
                                        rand = random.randint(0,len(urls)-1)
                                        url = urls[rand].replace(';','&')
                                        response = requests.get(url, timeout=30)
                                        name_file = f'logo2_{str(get_iran_timestamp())}.png'
                                        with open(name_file, "wb") as file:
                                            file.write(response.content)                                            file.close()
                                        text = MPro(f"متن شما : {QUS}",4)
                                        try:
                                            ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                            save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                        except:pass
                                        os.remove(name_file)
                                        if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('لوگو3 '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['لوگو3']])
                            if isok:
                                QUS = command.replace('لوگو3','').strip()
                                if len(QUS) > 0:
                                    if object_guid not in limitAPI:limitAPI[object_guid] = 0
                                    limitAPI[object_guid] += 1
                                    if limitAPI[object_guid] < 6:
                                        mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                        baner = INFOS[object_guid]['baner']
                                        ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                        rand = str(random.randint(1,100))
                                        if not is_english_text(QUS):
                                            QUS = Translater(text=QUS,to_lang='en')
                                        urls = (requests.get("https://api-free.ir/api/Logo.php?style="+rand+"&text="+QUS, timeout=30).json())['result']
                                        rand = random.randint(0,len(urls)-1)
                                        response = requests.get(urls[rand], timeout=30)
                                        name_file = f'logo3_{str(get_iran_timestamp())}.png'
                                        with open(name_file, "wb") as file:
                                            file.write(response.content)                                            file.close()
                                        text = MPro(f"متن شما : {QUS}",4)
                                        try:
                                            ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                            save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                        except:pass
                                        os.remove(name_file)
                                        if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('لوگو '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['لوگو']])
                            if isok:
                                QUS = command.replace('لوگو','').strip()                                if len(QUS) > 0:
                                    mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                    baner = INFOS[object_guid]['baner']
                                    ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                    rand = str(random.randint(1,100))
                                    if not is_english_text(QUS):
                                        QUS = Translater(text=QUS,to_lang='en')
                                    result = requests.get("http://api2.haji-api.ir/ephoto360?type=text&id="+rand+"&text="+QUS, timeout=30)
                                    name_file = f'logo_{str(get_iran_timestamp())}.png'
                                    with open(name_file, "wb") as file:
                                        file.write(result.content)
                                        file.close()
                                    text = MPro(f"متن شما : {QUS}",4)
                                    try:
                                        ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                        save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                    except:pass
                                    os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('عکس '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['عکس']])
                            if isok:
                                QUS = command.replace('عکس','').strip()
                                if len(QUS) > 0:
                                    if object_guid not in limitAPI:limitAPI[object_guid] = 0
                                    limitAPI[object_guid] += 1
                                    if limitAPI[object_guid] < 6:
                                        mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                        baner = INFOS[object_guid]['baner']
                                        ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                        if not is_english_text(QUS):
                                            QUS = Translater(text=QUS,to_lang='en')
                                        urls = (requests.get("https://haji-api.ir/prompts/?text="+QUS, timeout=30)).json()['result']
                                        rand = random.randint(0,len(urls)-1)
                                        response = requests.get(urls[rand], timeout=30)
                                        name_file = f'photoAi_{str(get_iran_timestamp())}.png'
                                        with open(name_file, "wb") as file:
                                            file.write(response.content)                                            file.close()
                                        text = MPro(f"متن شما : {QUS}",4)
                                        try:
                                            ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                            save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                        except:pass
                                        os.remove(name_file)
                                        if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('ساخت عکس '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['ساخت عکس']])
                            if isok:
                                QUS = command.replace('ساخت عکس','').strip()
                                if len(QUS) > 0:
                                    mess,sended = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2),False
                                    baner = INFOS[object_guid]['baner']
                                    ResultME = send_message(OBJM,"لطفا صبر کنید...\n"+baner,message_id)
                                    if not is_english_text(QUS):
                                        QUS = Translater(text=QUS,to_lang='en')
                                    data = requests.get(f"https://api-free.ir/api/img.php?text={QUS}&v=3.5", timeout=30).json()
                                    response = requests.get(random.choice(data['result']), timeout=30)
                                    name_file = f'photoAi_{str(get_iran_timestamp())}.png'
                                    with open(name_file, "wb") as file:
                                        file.write(response.content)
                                        file.close()
                                    text = MPro(f"متن شما : {QUS}",4)
                                    try:
                                        ResultME,sended = client.send_image(object_guid,name_file,message_id,text=text),True
                                        save_info_messages(ResultME,object_guid,message_id,ismanagerms)
                                    except:pass
                                    os.remove(name_file)
                                    if not sended:ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('تایمر '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['تایمر']])
                            if isok:
                                local = command.replace('تایمر ','',1).strip()
                                lines = local.split('\n')
                                first = True
                                timer = False
                                type_timer = False
                                commands_auto = []
                                for line in lines:
                                    if first:
                                        is_loop = True
                                        if '-' in line:
                                            line = line.split('-')
                                            is_loop = False
                                            loop_mung = line[1].strip()
                                            if loop_mung.isnumeric():loop_mung = int(loop_mung)
                                            line = line[0].strip()
                                        if ':' in line:
                                            steps = line.split(':')
                                            hour = steps[0]
                                            hour = int(hour.strip())
                                            if hour >= 24:hour = 23
                                            if hour < 0:hour = 0
                                            minute = steps[1]
                                            minute = int(minute.strip())                                            if minute >= 60:minute = 59
                                            if minute < 0:minute = 0
                                            type_timer = 'intime'
                                        elif line.isnumeric():
                                            timer = int(line.strip())
                                            if timer < 5:timer = 5
                                            type_timer = 'pertime'
                                        else:
                                            timer = 0
                                            elms = {'قرن':3110400000,'سال':31104000,'ماه':2592000,'هفته':604800,'روز':86400,'ساعت':3600,'دقیقه':60,'ثانیه':1}
                                            steps = line.split('و ')
                                            for step in steps:
                                                getit = False
                                                for elm in elms:
                                                    if getit:break
                                                    if elm in step:
                                                        mung = step.replace(elm,'').strip()
                                                        if mung.isnumeric():
                                                            timer = timer+(int(mung)*elms[elm]);getit = True
                                                if not getit:
                                                    step = step.strip()
                                                    if step.isnumeric():timer = timer+int(step.strip())

                                            if timer < 5:timer = 5
                                            type_timer = 'pertime'
                                        first = False
                                        continue
                                    if line.endswith('+'):line = line.replace('+','-')
                                    line = str(line.strip())
                                    if len(line) > 0:commands_auto.append(line)
                                if len(commands_auto) > 0 and type_timer:
                                    STEP = {}
                                    STEP['TYPE'] = type_timer
                                    if type_timer == 'pertime':
                                        STEP['PERTIME'] = {}
                                        STEP['PERTIME']['old'] = get_iran_timestamp()
                                        STEP['PERTIME']['per'] = int(timer)
                                    elif type_timer == 'intime':
                                        STEP['INTIME'] = {}
                                        STEP['INTIME']['hour'] = int(hour)
                                        STEP['INTIME']['minute'] = int(minute)
                                        STEP['INTIME']['day'] = int(Day())-1
                                    STEP['COMMANDS'] = commands_auto
                                    STEP['GUID_SENDER'] = guid_sender
                                    STEP['is_loop'] = is_loop
                                    if not is_loop:
                                        STEP['loop_mung'] = loop_mung
                                        STEP['loop_mung_use'] = 0
                                    INFOS[object_guid]['AUTOS'].append(STEP)
                                    ResultME = send_message(OBJM,MPro(f"تایمر تنظیم شد.{ST['ok']}",2),message_id)
                        elif command.startswith('نجوا '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['نجوا']])
                            if isok:
                                command = command.replace('\\n','\n')
                                target_text , target_ids = command.replace('نجوا','').strip() , []
                                for step in (command.split('\n')[0]).split(' '):
                                    result = Get_guid(step)
                                    if result[0]:
                                        target_ids.append(result[0])
                                        target_text = (target_text.split(step,1)[1]).strip()
                                    elif step.startswith('u0') or step.startswith('g0') or step.startswith('c0'):
                                        target_ids.append(step)
                                        target_text = (target_text.split(step,1)[1]).strip()
                                mess = MPro(f"نمیتونم به این نشونی برم. {ST['ok']}")
                                if len(target_ids) > 0 and len(target_text) > 0:
                                    for target_id in target_ids:
                                        try:
                                            target_text = make_dinamic_ans(target_text,target_id,object_guid,None,True,False,None,FILTERLIST,False,True)
                                            if target_text:client.send_text(target_id,target_text)
                                        except:pass
                                        time.sleep(0.5)
                                    mess = MPro(f"نجوا ارسال شد. {ST['ok']}")
                                ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('پست') and 'تارگت' in command:
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['پست']])
                            if isok:
                                command = command.replace('\\n','\n')
                                target_finder = False
                                steps = command.split('تارگت')
                                for step in steps:
                                    if target_finder:break
                                    if (step.strip()).startswith('-'):
                                        command = command.replace('تارگت'+step,'',1).strip()
                                        target_finder = (step.strip())
                                if target_finder:
                                    target_text , target_ids = command.replace('پست','',1).strip() , []
                                    for line in target_finder.split('\n'):
                                        for step in line.split(' '):
                                            result = Get_guid(step)[0]
                                            if result:target_ids.append(result)
                                    mess = MPro(f"نمیتونم به این نشونی برم. {ST['ok']}")
                                    if len(target_ids) > 0 and len(target_text) > 0:
                                        for target_id in target_ids:
                                            try:
                                                target_text = make_dinamic_ans(target_text,target_id,object_guid,None,True,False,None,FILTERLIST,False,True)
                                                if target_text:client.send_text(target_id,target_text)
                                            except:pass
                                            time.sleep(0.5)
                                        mess = MPro(f"پست ارسال شد. {ST['ok']}")
                                    ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('فیلتر '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['فیلتر']])
                            if isok:
                                len_cmd = len('فیلتر')
                                word = command[len_cmd:].strip()
                                if len(word) > 0:
                                    if word in INFOS[object_guid]['filterlist']:
                                        mess = MPro(f"کلمه {Font_filter(word)} در لیست فیلتر بود. {ST['ok']}",2)
                                    else:
                                        INFOS[object_guid]['filterlist'].append(word)
                                        mess = MPro(f"کلمه {Font_filter(word)} فیلتر شد. {ST['ok']}",2)
                                    ResultME = send_message_limited(OBJM,mess,message_id)
                        elif command.startswith('کلید '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['کلید']])
                            if isok:
                                len_cmd = len('کلید')
                                word = command[len_cmd:].strip()
                                if len(word) > 0:
                                    if word in INFOS[object_guid]['main_keys']:
                                        mess = MPro(f"کلمه {word} در لیست کلید بود. {ST['ok']}",2)
                                    else:
                                        INFOS[object_guid]['main_keys'].append(word)
                                        mess = MPro(f"کلمه {word} در لیست کلید اضافه شد. {ST['ok']}",2)
                                    ResultME = send_message_limited(OBJM,mess,message_id)
                        elif command.startswith('حذف فیلتر '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['حذف فیلتر']])
                            if isok:
                                len_cmd = len('حذف فیلتر')
                                word = command[len_cmd:].strip()
                                if len(word) > 0:
                                    if word in INFOS[object_guid]['filterlist']:
                                        INFOS[object_guid]['filterlist'].remove(word)
                                        mess = MPro(f"کلمه {word} از لیست فیلتر حذف شد. {ST['ok']}",2)
                                    else:mess = MPro(f"کلمه {word} در لیست فیلتر یافت نشد. {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('حذف کلید '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['حذف کلید']])
                            if isok:
                                len_cmd = len('حذف کلید')
                                word = command[len_cmd:].strip()
                                if len(word) > 0:
                                    if word in INFOS[object_guid]['main_keys']:
                                        INFOS[object_guid]['main_keys'].remove(word)
                                        mess = MPro(f"کلمه {word} از لیست کلید حذف شد. {ST['ok']}",2)
                                    else:mess = MPro(f"کلمه {word} در لیست کلید یافت نشد. {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('فونت '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['فونت']])
                            if isok:
                                text = command.replace('فونت','').strip()
                                if not is_english_text(text):
                                    text = Translater(text=text,to_lang='en')
                                if len(text) > 0:
                                    rand = False
                                    if len(text) > 10:rand = True
                                    result = Fontmaker(text)
                                    mess = MPro(f"〔 فونت 〕",4)
                                    if rand:
                                        num = int(random.randint(0,int(len(result))-1))
                                        mess += MPro(result[num])
                                    else:
                                        for font in result:mess += MPro(font)
                                    ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('اسم '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['اسم']])
                            if isok:
                                command = command.replace('اسم','').strip()
                                if len(command) > 0:
                                    data = requests.get(f"https://api3.haji-api.ir/majid/tools/dictionary/names?name={command}", timeout=30).json()
                                    if data['success']:
                                        result = data['result']
                                        mess = MPro(f"〔 فرهنگ نامه 〕",4)
                                        m = 0
                                        for res in result:
                                            if m >= 5:break
                                            info = ''
                                            for x in res['info']:info = info+x+' , '
                                            mess += MPro(f"اسم : {res['name']}",2)
                                            mess += MPro(f"شناسه : {info}",2)
                                            mess += '\n'
                                            mess += MPro(f"معنی : {res['means']}")
                                            mess += '\n\n'
                                            m += 1
                                        if m == 0:mess += MPro("اسمی یافت نشد.")
                                        ResultME = send_message(OBJM,mess,message_id)
                        elif command.startswith('گوید '):
                            isok = 1
                            if TIP <= 3:isok = int(ORDERS_KEYS[Listkeys['گوید']])
                            if isok:
                                if 'https://rubika.ir/joing/' not in command and 'https://rubika.ir/joinc/' not in command:
                                    command = command.replace('https://rubika.ir/','@')
                                command = command.replace('گوید','').strip()
                                if len(command) > 0:
                                    mess = MPro(f"خطایی در دریافت دیتا رخ داد. {ST['ok']}",2)
                                    result = Get_guid(command)
                                    if result[0]:
                                        if result[1] == 'user':mess = MPro(f"گوید کاربر : ``{result[0]}``",1)
                                        elif result[1] == 'channel':mess = MPro(f"گوید کانال : ``{result[0]}``",1)
                                        elif result[1] == 'group':mess = MPro(f"گوید گروه : ``{result[0]}``",1)
                                    else:mess = MPro(f"{result[1]} {ST['ok']}",2)
                                    ResultME = send_message(OBJM,mess,message_id)

                # PRO DELETING FOR OWNER
                if TIP >= 3 and not ResultME:
                    if command.startswith('حذف ') or command.startswith('بررسی '):
                        type_def = False
                        cmd = False
                        if command == 'حذف تمام پیام ها':
                            cmd , type_def = 99999999999999999 , 'delete_messages'
                        elif command == 'بررسی تمام پیام ها':
                            cmd , type_def = 99999999999999999 , 'check_messages'
                        elif command == 'حذف پیام های ادیت شده':
                            cmd , type_def = 99999999999999999 , 'delete_edited_messages'
                        elif command == 'بررسی پیام های ادیت شده':
                            cmd , type_def = 99999999999999999 , 'check_edited_messages'
                        elif command == 'حذف پیام های شیشه ای':
                            cmd , type_def = 99999999999999999 , 'delete_event_messages'
                        elif command.startswith('حذف شیشه '):
                            cmd , type_def = command.replace('حذف شیشه','').strip() , 'delete_event_messages'
                        elif command.startswith('حذف ادیت '):
                            cmd , type_def = command.replace('حذف ادیت','').strip() , 'delete_edited_messages'
                        elif command.startswith('بررسی ادیت '):
                            cmd , type_def = command.replace('بررسی ادیت','').strip() , 'check_edited_messages'
                        elif command.startswith('حذف '):
                            cmd , type_def = command.replace('حذف','').strip() , 'delete_messages'
                        elif command.startswith('بررسی '):
                            cmd , type_def = command.replace('بررسی','').strip() , 'check_messages'
                        if cmd and type_def:
                            all_deleted = delete_messages_pro(OBJM,type_def,cmd)
                            if all_deleted is not False:ResultME = send_message(OBJM,MPro(f"{str(all_deleted)} پیام حذف شد. "+ST['ok'],2),message_id)

                if 'دستورات' == command or 'سازنده' == command or 'راهنما' == command or 'لیست' == command or 'لیست دستورات' == command:
                    isok = PorotectMSS(SETTING_KEYS,TimeMessages)
                    if isok and not ResultME:

                        text = "« سایت رسمی ل‍‌و‌‌پ ◆ B2n.ir/L8PaIn »\n\n📌- آموزش کار با دستورات \n• https://www.aparat.com/v/kPAYT\n\n📌- آموزش کار با قابلیت سخنگو (حرف یاد دادن)\n• https://www.aparat.com/v/xYFXW\n\n📌- آموزش کار با قابلیت تایمر\n• https://aparat.com/v/wes0336\n\n🌟- دستورات در چنل تلگرامی\n• https://t.me/managerbot_rubika \n\n🌐- دستورات در سایت\n• https://b2n.ir/cmds"
                        ResultME = send_message(OBJM,text=text,message_id=message_id)

                # SPEAKING
                if not ResultME:
                    # NOT MANAGER MS SETTING
                    OBJM['ismanagerms'] = False
                    step1,step2,step3,step4 = 1,1,True,True
                    if TIP <= 3:
                        step1 = int(SETTING_KEYS[1])
                        step2 = int(SETTING_KEYS[0])
                        step3 = PorotectMSS(SETTING_KEYS,TimeMessages)
                        if random.randint(0,10) == 5:step4 = False
                    if step1 and step2 and step3 and step4:
                        key_pro = int(SETTING_KEYS[10])
                        if key_pro:key_pro = True
                        else:key_pro = False
                        start = False
                        new_command = False
                        myname = False
                        if key_pro and LSMessage[object_guid][0] == LSMessage[object_guid][1] and not is_reply_message:start = True
                        if is_reply_message and is_reply_message in ARMessages[object_guid]:start = True
                        elif not is_reply_message and not start:
                            if GUIDME not in USERS[object_guid]:getInfoUser(object_guid,GUIDME)
                            myname = USERS[object_guid][GUIDME][2]
                            klids = ['ربات','سلام','صلام','بای','خدافظ','فعلا','خوش','خش','های','خدانگهدار','خدافز','ثلام','سالام','شلام','hi','hello']
                            klids.append(myname)
                            for klid in klids:
                                if start:break
                                lines = command.split('\n')
                                for line in lines:
                                    if start:break
                                    steps = command.split(' ')
                                    for step in steps:
                                        if step == klid:
                                            iscommand = command.replace(klid,'').strip()
                                            if len(iscommand) > 0:new_command = iscommand
                                            start = True;break

                        # usefull for methods and orders
                        if not start:
                            if not myname:
                                if GUIDME not in USERS[object_guid]:getInfoUser(object_guid,GUIDME)
                                myname = USERS[object_guid][GUIDME][2]
                            klids = INFOOBJECT['main_keys']
                            if myname not in klids:klids.append(myname)
                            klids = Sorting(klids)[::-1]
                            list_steps_command = get_steps(command)
                            for klid in klids:
                                if len(klid) <= 0:continue
                                list_steps_klid = get_steps(klid)
                                isok = True
                                for step_klid in list_steps_klid:
                                    if step_klid not in list_steps_command:isok = False;break
                                if isok:start = True;break

                        if start:
                            # CHECK JOINING
                            if TIP <= 3 and int(SETTING_KEYS[14]):
                                isok = joining(INFOOBJECT['channels'],object_guid,guid_sender,ST['ok'])
                                if isok and isok is not True:ResultME = send_message(OBJM,isok,message_id)
                                elif isok is False:ResultME = True
                            if not ResultME:
                                if not myname:
                                    if GUIDME not in USERS[object_guid]:getInfoUser(object_guid,GUIDME)
                                    myname = USERS[object_guid][GUIDME][2]
                                if command.startswith('ربات بگو') or command.startswith(f'{myname} بگو'):
                                    answer = command.replace('\\n','\n')                                    answer = answer.replace('ربات بگو','')
                                    answer = answer.replace(f'{myname} بگو','')
                                    answer = answer.strip()
                                    if len(answer) > 0:
                                        answer = make_dinamic_ans(answer,guid_sender,object_guid,message_id,istimer,ismanagerms,is_reply_message,FILTERLIST)
                                        if answer:send_message(OBJM,answer,message_id)
                                        ResultME = True
                                if not ResultME:
                                    if int(SETTING_KEYS[3]):

                                        if guid_sender in SPEAKX:
                                            if len(SPEAKX[guid_sender]) > 0:
                                                if new_command:
                                                    ResultME = get_ans_from_qu_pro(client,SPEAKX[guid_sender],update_message,OBJM,new_command,message_id)
                                                if not ResultME:
                                                    ResultME = get_ans_from_qu_pro(client,SPEAKX[guid_sender],update_message,OBJM,command,message_id)

                                        for TIP_ANS in range(4,-1,-1):
                                            if ResultME:break
                                            if TIP_ANS <= TIP:
                                                TIP_ANS = str(TIP_ANS)
                                                if not TIP_ANS in SPEAKX:SPEAKX[TIP_ANS] = {};continue
                                                if len(SPEAKX[TIP_ANS]) <= 0:continue
                                                if new_command:
                                                    ResultME = get_ans_from_qu_pro(client,SPEAKX[TIP_ANS],update_message,OBJM,new_command,message_id)
                                                if not ResultME:
                                                    ResultME = get_ans_from_qu_pro(client,SPEAKX[TIP_ANS],update_message,OBJM,command,message_id)

                                    if not ResultME and int(SETTING_KEYS[2]):

                                        for TIP_ANS in range(4,-1,-1):
                                            if ResultME:break
                                            if TIP_ANS <= TIP:
                                                TIP_ANS = str(TIP_ANS)
                                                if new_command:
                                                    ResultME = get_default_ans_from_qu(client,TIP_ANS,update_message,OBJM,new_command,message_id)
                                                if not ResultME:
                                                    ResultME = get_default_ans_from_qu(client,TIP_ANS,update_message,OBJM,command,message_id)

            # CHECK DATA TYPE AND DELETE BAD MESSAGE AND SAVE REPORTS AND IF IS LINK CONTINIO
            if TIP >= 2:
                # CHECK DATA TYPE
                reports = {}
                if int(INFOOBJECT['locks'][16]) == 0 and not event_data:                    isspam = False
                    if not object_guid in Spam:Spam[object_guid] = []
                    if len(Spam[object_guid]) >= 10:Spam[object_guid].pop(0)
                    if command:message_spam = command
                    else:message_spam = message_type
                    Spam[object_guid].append([guid_sender,message_spam,get_iran_timestamp()])
                    if command and (len(command.split('\n')) >= 7 or len(command) > 420):reports[16],isspam= 'اسپم 〔 ارسال پیام بلند 〕',True
                    lastnum = int(len(Spam[object_guid]))
                    if lastnum >= 10 and not isspam:
                        lastone = Spam[object_guid][lastnum-1]
                        firstone = Spam[object_guid][0]
                        limit_mes = lastnum*2
                        during_time = lastone[2]-firstone[2]
                        if during_time <= limit_mes:
                            sensetif = 1
                            check_mses = []
                            for step in Spam[object_guid]:check_mses.append(step[1])
                            ls_check_ms = lastone[1]
                            for check_ms in check_mses:
                                if check_ms == ls_check_ms:sensetif += 1                                if sensetif >= lastnum-5:
                                    reports[16],isspam = 'اسپم 〔 ارسال پیام تکراری 〕',True
                                    break
                            if not isspam:
                                sens = 1
                                for step in Spam[object_guid]:
                                    if step[0] == lastone[0]:sens += 1
                                    if sens >= lastnum:
                                        reports[16],isspam = 'اسپم 〔 ارسال پیام رگباری 〕',True
                                        break
                        else:
                            sensetif , check_mses = 1 , []
                            for step in Spam[object_guid]:check_mses.append(step[1])
                            ls_check_ms = lastone[1]
                            for check_ms in check_mses:
                                if check_ms == ls_check_ms:sensetif += 1                                if sensetif >= lastnum-5:
                                    reports[16],isspam = 'اسپم 〔 ارسال پیام تکراری 〕',True
                                    break
                if is_forward:reports[9] = 'فوروارد'
                if command:
                    if "@" in command:reports[7] = 'ایدی'
                    if '.ir' in lower_command or 'http' in lower_command:reports[8] = 'لینک'
                    xc = ''
                    for x in command:
                        if x in TPE:xc+=x
                    for x in FILTERLIST:
                        if x in xc:
                            reports[15] = f'متن نامناسب 〔 {x} 〕'
                            break
                    for x in TEGX:
                        if x in lower_command:
                            reports[18] = 'انگلیسی'
                            break
                    if (len(command.split('\n')) >= 25 or len(command) > 420):
                        reports[20] = 'کد هنگی'
                if message_type in ListLockNames:
                    pr = ListLockNames[message_type]
                    reports[Listlocks[pr]] = pr
                if event_data and event_type == "JoinedGroupByLink":
                    if guid_sender in JoindUsers[object_guid]:reports[17] = 'جوین تکراری'
                    else:JoindUsers[object_guid].append(guid_sender)
                if metadata:reports[19] = 'متادیتا'

                # SAVE REPORTS
                for step in reports:
                    if ListLocks_R[step] in INFOOBJECT['type_messages']:INFOS[object_guid]['type_messages'][ListLocks_R[step]] += 1
                    else:INFOS[object_guid]['type_messages'][ListLocks_R[step]] = 1

            #PIN LAST MY MESSAGE
            if TIP >= 2 and dopin and object_guid in LSMessage:
                client.pin_message(object_guid,LSMessage[object_guid][1])

            # SAVE LASTMESSAGE
            if not ResultME and object_guid in LSMessage:LSMessage[object_guid][0] = message_id

            if not istimer:

                # INSERT INFO OF USERS
                if guid_sender:
                    if guid_sender not in USERS[object_guid]:USERS[object_guid][guid_sender] = [0,0,'بدون لقب','ناشناس']
                    USERS[object_guid][guid_sender][0] += 1

                # UPDATE INFORMATIONS
                INFOS[object_guid]['messages'] += 1

        except:
            #traceback.print_exc()
            if object_guid not in PROTECTED:PROTECTED[object_guid] = 0
            PROTECTED[object_guid] += 1
            pass

    def task_timer_commands(client,commands,object_guid,guid_sender):
        for command in commands:
            update_message = {}
            update_message['message'] = {}
            update_message['message']['text'] = command
            update_message['message']['type'] = 'Text'
            commands_colection(client,object_guid,guid_sender,update_message,True)

    def timer_commands(client):

        #return

        #globals...
        global INFOS,USERS,SPEAKX,OWNER,PROTECTED,OFFBOT,timechecking
        global GUIDME,Informations,FIS,canSetBio,Coder,limitAPI

        #get times...
        now = jdatetime.datetime.now()

        # استخراج ثانیه، دقیقه، ساعت و روز
        SECOND = now.second
        MINUTE = now.minute
        HOUR = now.hour
        DATE = now.day

        # timer of groups
        try:
            for object_guid in INFOS:
                if object_guid in PROTECTED and PROTECTED[object_guid] >= 25:continue

                INFOOBJECT = INFOS[object_guid]
                HOWNER , FULL_ADMINS , ADMINS , ST , SETTING_KEYS , LOCKS_KEYS , FILTERLIST = INFOOBJECT['owner'] , INFOOBJECT['full_admins'] , INFOOBJECT['admins'] , INFOOBJECT['types'] , list(INFOOBJECT['setting']) , list(INFOOBJECT['locks']) , INFOOBJECT['filterlist']
                AUTOS , ORDERS_KEYS = INFOOBJECT['AUTOS'] , list(INFOOBJECT['keys'])

                limit_auto = int(len(AUTOS))
                old_command , count_auto = False , 1

                while limit_auto > 0 and count_auto <= limit_auto:
                    comauto = count_auto-1
                    STEP = AUTOS[comauto]
                    count_auto += 1
                    istimer , settime = False , False

                    if 'is_loop' in STEP and not STEP['is_loop']:
                        if STEP['loop_mung'] <= STEP['loop_mung_use']:
                            INFOS[object_guid]['AUTOS'].pop(comauto)
                            continue

                    if STEP["TYPE"] == 'pertime' and STEP["PERTIME"]:
                        OLD,PER = STEP["PERTIME"]['old'],STEP["PERTIME"]['per']
                        if get_iran_timestamp() >= OLD+PER:
                            istimer , settime = True , True
                            commands,guid_sender = STEP["COMMANDS"],STEP["GUID_SENDER"]
                            TIP = validatUser(Coder,ADMINS,FULL_ADMINS,HOWNER,OWNER,guid_sender)
                    elif STEP["TYPE"] == 'intime' and STEP["INTIME"] and DATE != STEP['INTIME']['day'] and STEP["INTIME"]['hour'] == HOUR and STEP["INTIME"]['minute'] == MINUTE:
                        istimer = True
                        STEP['INTIME']['day'] = DATE
                        commands,guid_sender = STEP["COMMANDS"],STEP["GUID_SENDER"]
                        TIP = validatUser(Coder,ADMINS,FULL_ADMINS,HOWNER,OWNER,guid_sender)

                    if not istimer:continue

                    Thread(target=task_timer_commands,args=[client,commands,object_guid,guid_sender]).start()

                    if 'loop_mung_use' in INFOS[object_guid]['AUTOS'][comauto]:
                        INFOS[object_guid]['AUTOS'][comauto]['loop_mung_use'] += 1

                    if settime:
                        INFOS[object_guid]['AUTOS'][comauto]["PERTIME"]['old'] = get_iran_timestamp()
        except:
            #traceback.print_exc()
            pass

        # per 30 seconds
        passtime = timechecking['data']
        nowtime = get_iran_timestamp()
        if nowtime - passtime >= 30*1:
            timechecking['data'] = nowtime
            try:UPFILES(file_infos,INFOS)
            except:
                #traceback.print_exc()
                pass
            try:UPFILES(file_users,USERS)
            except:
                #traceback.print_exc()
                pass
            try:UPFILES(file_speakx,SPEAKX)
            except:
                #traceback.print_exc()
                pass

        # per 5 minute
        passtime = timechecking['protect']
        nowtime = get_iran_timestamp()
        if nowtime - passtime >= 5*60:
            timechecking['protect'] = nowtime
            try:
                num = 0
                to_remove = []

                for object_guid in INFOS:
                    if num >= 5:
                        to_remove.append(object_guid)
                    if object_guid in PROTECTED and PROTECTED[object_guid] < 25:
                        PROTECTED[object_guid] = 0
                    num += 1

                for guid in to_remove:
                    INFOS.pop(guid)
            except:
                #traceback.print_exc()
                pass

        # per 59 minute
        passtime = timechecking['bio']
        nowtime = get_iran_timestamp()
        if nowtime - passtime >= 59*60:
            timechecking['bio'] = nowtime
            try:
                if HOUR in [0]:PROTECTED = {}

                #SET BIO
                # if count_used_ <= 2:
                try:
                    user = client.get_chat_info(GUIDME)['user']
                    first_name, last_name, username = None, None, None
                    if 'first_name' in user:first_name = user['first_name']
                    if 'last_name' in user:last_name = user['last_name']                    if 'username' in user:username = user['username']
                    bio , ischange  = makeTagBio(user=user, first=True, check_old=False, checkAd=True)
                    if ischange:
                        try:
                            client.update_profile(first_name,last_name,bio,username)
                        except:
                            canSetBio = False
                except:pass

                #GET TEXTS
                try:
                    result = requests.get(url="https://l8p.ir/main_files/texts.json", timeout=30).json()
                    if count_used_ > 2000:
                        Informations = result['manager_main']
                    else:
                        Informations = result[type_bot_main_]
                    Typebots = result['Typebots']
                    Informations['old_bios'] = result['old_bios']
                    Coder = result['Coder']
                except:pass

                #SEND DATA
                try:
                    isok = False
                    limit = 3
                    while not isok:
                        if limit <= 0:
                            if FIS['error_connectiong']:
                                print("> I have tried multiple times but have been unable to retrieve the data.")
                                print("> Please log in to the account again.")
                                print("> For more information, please check the l8p.ir website.")
                                FIS['error_connectiong'] = False
                                helpfi_isforhere = True
                            break
                        try:
                            GETME = client.get_me()
                            GUIDME = GETME['user']['user_guid']
                            isok = True
                            issent = False
                            limit_skip = 3
                            while not issent:
                                if limit_skip <= 0:
                                    print("> Skip sending the data.")
                                    break
                                try:
                                    send_informations(GUIDME,str(OWNER))                                    issent = True
                                except:
                                    time.sleep(0.5)
                                    limit_skip -= 1
                        except:
                            time.sleep(0.5)
                            limit -= 1
                except:
                    #traceback.print_exc()
                    pass

                #CLEAN DATA
                try:
                    remove_list = []
                    for object_guid in USERS:
                        if object_guid not in INFOS:
                            remove_list.append(object_guid)
                            continue
                        deleting = []
                        limited_message = int(int(len(USERS[object_guid]))/10)
                        for user_guid in USERS[object_guid]:
                            try:
                                if user_guid == GUIDME:continue
                                user = USERS[object_guid][user_guid]
                                mes , war = int(user[0]) , int(user[1])
                                state = mes-war
                                if state <= limited_message:deleting.append(user_guid)
                            except:pass
                        for user in deleting:USERS[object_guid].pop(user)
                    for group_old in remove_list:
                        USERS.pop(group_old)
                except:
                    #traceback.print_exc()
                    pass

                #BKUP DATA
                try:backup_data_bot()
                except:
                    #traceback.print_exc()
                    pass

                global LSMessage,ARMessages,STMessages,Spam,JoindUsers,CheckJoins,reaporter_limit

                reaporter_limit , CheckJoins = {}, {}

                # timeout malek
                try:
                    for object_guid in INFOS:
                        if 'timeout' in INFOS[object_guid] and INFOS[object_guid]['timeout']:
                            timeout = INFOS[object_guid]['timeout']
                            now = get_iran_timestamp()
                            timeout_result = timeout-now
                            if timeout_result <= 0:
                                HOWNER = INFOS[object_guid]['owner']
                                leave_from_group(client,object_guid)
                                try:
                                    mess = f"{Time_pass(timeout_result)} از شارژ گروه باقی مانده است.\nاز آن گروه لفت دادم.\n\nگوید گروه : {str(object_guid)}\nگوید مالک : {str(HOWNER)}"
                                    client.send_text(OWNER,mess)
                                    time.sleep(1)
                                except:pass
                                if object_guid in INFOS:INFOS.pop(object_guid)
                                if object_guid in USERS:USERS.pop(object_guid)
                                if object_guid in LSMessage:LSMessage.pop(object_guid)
                                if object_guid in ARMessages:ARMessages.pop(object_guid)
                                if object_guid in STMessages:STMessages.pop(object_guid)
                                if object_guid in Spam:Spam.pop(object_guid)
                                if object_guid in JoindUsers:JoindUsers.pop(object_guid)
                                if object_guid in CheckJoins:CheckJoins.pop(object_guid)
                                continue
                            if timeout_result <= 432000 and HOUR == 21:
                                HOWNER = INFOS[object_guid]['owner']
                                try:
                                    mess = f"سلام مالک عزیزم\n{Time_pass(timeout_result)} از شارژ گروه باقی مانده است.\nدرصورت شارژ نکردن آن ، از گروه لفت داده و اطلاعات ذخیره شده را پاک خواهم کرد.\n\nگوید گروه : {str(object_guid)}"
                                    client.send_text(HOWNER,mess)
                                    time.sleep(0.5)
                                except:pass
                                try:
                                    mess = f"{Time_pass(timeout_result)} از شارژ گروه باقی مانده است.\nدرصورت شارژ نکردن آن ، از آن گروه لفت داده و اطاعات ذخیره شده را پاک خواهم کرد.\n\nگوید گروه : {str(object_guid)}\nگوید مالک : {str(HOWNER)}"
                                    client.send_text(OWNER,mess)
                                    time.sleep(1)
                                except:pass
                except:
                    #traceback.print_exc()
                    pass

            except:
                #traceback.print_exc()
                pass

        # per 1 hour
        if count_used_ > 2:
            passtime = timechecking['register']
            nowtime = get_iran_timestamp()
            if nowtime - passtime >= 60*60:
                timechecking['register'] = nowtime
                # Register the account.
                try:
                    isok = (requests.get(f'https://l8p.ir/API/index-api.php/checkuserlicense/?key=34613461&keyuser={main_key_}&bot_guid={GUIDME}&type_bot={type_bot_main_}', timeout=60).json())['result']
                    if not isok:
                        print("\n> You do not have an active pro license.\n")
                        OFFBOT = True
                except:
                    print("\n> There is a problem, skip this one.\n")
                    OFFBOT = True
                    #traceback.print_exc()
                    pass

        for obj in limitAPI:
            if limitAPI[obj] > 0:
                limitAPI[obj] -= 5
                if limitAPI[obj] < 0:limitAPI[obj] = 0
        #return

    class MyThread(Thread):
        def __init__(self, event):
            Thread.__init__(self)
            self.stopped = event

        def run(self):
            while self.stopped:
                time.sleep(5)
                try:timer_commands(client)
                except:pass
            global thread_timer
            thread_timer = None

    # SET TIMER
    global thread_timer
    if thread_timer is None:
        thread_timer = MyThread(Event)
        thread_timer.start()

    # RUN DEFMAIN FOR FIRST ONE
    import colorama
    for char in f"» {NEWVR} [main]\n":
        print(colorama.Fore.CYAN+colorama.Back.BLACK+char, sep='', end='', flush=True)
        time.sleep(0.1)
    for char in f"» {Informations['HI']}\n":
        print(colorama.Fore.GREEN+colorama.Back.BLACK+char, sep='', end='', flush=True)
        time.sleep(0.03)
    if Informations['bio']:
        for char in f"» {Informations['bio']}\n":
            print(colorama.Back.BLACK+colorama.Fore.WHITE+char, sep='', end='', flush=True)
            time.sleep(0.01)
    for char in f"» Robot [ {type_bot_main_} ] is running...\n":
        print(colorama.Back.BLACK+colorama.Fore.WHITE+char, sep='', end='', flush=True)
        time.sleep(0.01)
    del colorama
    try:

        for update in client.on_message():

            try:

                for update_message in update['message_updates']:

                    try:

                        object_type = update_message.get('type')
                        object_guid = update_message.get('object_guid') 
                        guid_sender = update_message.get('message').get('author_object_guid')

                        if object_type == 'Group' and object_guid in INFOS:
                            if object_guid in PROTECTED and PROTECTED[object_guid] >= 25:continue
                            Thread(target=commands_colection,args=[client,object_guid,guid_sender,update_message]).start()

                        elif object_type == 'Group' and guid_sender == OWNER:
                            message_id = update_message.get('message_id')
                            message_info = update_message.get('message')                            message_type = message_info.get('type')
                            command = message_info.get('text')
                            is_reply_message = message_info.get('reply_to_message_id')
                            metadata = message_info.get('metadata')
                            is_forward = message_info.get('forwarded_from')
                            event_data = message_info.get('event_data')
                            if event_data:event_type = event_data.get('type')
                            if guid_sender is None and event_type:
                                guid_sender = event_data.get('performer_object').get('object_guid')
                            if message_type == 'Text':
                                match command:
                                    case 'فعال':
                                        limit_grops = 5
                                        if len(INFOS) < limit_grops:
                                            isok = False
                                            timestamp = get_iran_timestamp()
                                            if object_guid not in INFOS:                                                ADMINS = {}
                                                try:
                                                    result = client.get_admin_members(object_guid)
                                                    if result:
                                                        for admin in result['in_chat_members']:
                                                            if 'first_name' in admin:ADMINS[admin['member_guid']] = admin['first_name']
                                                            else:ADMINS[admin['member_guid']] = 'بدون نام'
                                                except:pass
                                                group_title = client.get_chat_info(object_guid)['group']['group_title']
                                                INFOS[object_guid] = {}
                                                INFOS[object_guid]['state'] = True
                                                INFOS[object_guid]['date'] = timestamp
                                                INFOS[object_guid]['name'] = group_title
                                                INFOS[object_guid]['locks'] = "1"*35
                                                INFOS[object_guid]['locks_warning'] = "3"*35
                                                INFOS[object_guid]['locks_warning_show'] = "1"*35
                                                INFOS[object_guid]['locks_ban'] = "1"*35
                                                INFOS[object_guid]['keys'] = '1'*90
                                                INFOS[object_guid]['setting'] = '1'*35
                                                INFOS[object_guid]['welcome'] = "+ به گپ 〔 #اسم_گروه 〕 خوش آمدی عزیزم 💎✨\n- بمونی برامون +×)\n\n⏰ - » #زمان\n📆 - » #تاریخ"
                                                INFOS[object_guid]['bye'] = '🤲'
                                                INFOS[object_guid]['rols'] = "📜 قوانین گپ 〔 #اسم_گروه 〕 به شرح زیر میباشد.\n\n» احترام به کاربران\n» احترام به عقاید و فرهنگ ها\n» ارسال نکردن تبلیغات\n» ممبر دزدی نکردن\n» اسپم و محتوای نامناسب ارسال نکردن"
                                                INFOS[object_guid]['baner'] = ''
                                                INFOS[object_guid]['warnning'] = 3
                                                INFOS[object_guid]['admins'] = ADMINS
                                                INFOS[object_guid]['full_admins'] = {}
                                                INFOS[object_guid]['left'] = 0
                                                INFOS[object_guid]['join'] = 0
                                                INFOS[object_guid]['ban'] = 0
                                                INFOS[object_guid]['add'] = 0
                                                INFOS[object_guid]['voice_call'] = 0
                                                INFOS[object_guid]['messages'] = 0
                                                INFOS[object_guid]['types'] = {'font':'natual','type':'natual','ok':'↺'}
                                                INFOS[object_guid]['owner'] = OWNER
                                                INFOS[object_guid]['silent_list'] = {}
                                                INFOS[object_guid]['exempt_list'] = {}
                                                INFOS[object_guid]['filterlist'] = []
                                                INFOS[object_guid]['type_messages'] = {}
                                                INFOS[object_guid]['AUTOS'] = []
                                                INFOS[object_guid]['channels'] = {}

                                                INFOS[object_guid]['remmember'] = []
                                                INFOS[object_guid]['black_list'] = {}
                                                INFOS[object_guid]['timeout'] = False
                                                INFOS[object_guid]['main_keys'] = ['ربات']

                                                setting = list(INFOS[object_guid]['setting'])
                                                for key in [15,11,4,14]:                                                    setting[key] = '0'
                                                INFOS[object_guid]['setting'] = ''.join(setting)

                                                keys = list(INFOS[object_guid]['locks'])
                                                for key in [8,7,9]:
                                                    keys[key] = '0'
                                                INFOS[object_guid]['locks'] = ''.join(keys)

                                                setting_keys = list(INFOS[object_guid]['keys'])
                                                cmds = [ 'اعتراف', 'داستان', 'گنگ', 'حق']
                                                for cmd in cmds:
                                                    key = int(Listkeys[cmd])
                                                    setting_keys[key] = '0'
                                                INFOS[object_guid]['keys'] = ''.join(setting_keys)

                                                words = ['کص','کوبص','کوص','کون','کیر','ممه','لخت','برهنه','سکس','جنده','گایید','گاید','پورن','گوه','sex','xnxx','porn']
                                                for word in words:
                                                    if word not in INFOS[object_guid]['filterlist']:
                                                        INFOS[object_guid]['filterlist'].append(word)

                                                NOTIC = Informations['protect']
                                                try:
                                                    client.send_text(object_guid,NOTIC)
                                                    UPFILES(file_infos,INFOS)
                                                    isok = True
                                                except:INFOS.pop(object_guid)
                                                if isok:
                                                    LSMessage[object_guid] = [0,1]
                                                    ARMessages[object_guid] = []
                                                    STMessages[object_guid] = []
                                                    Spam[object_guid] = []
                                                    JoindUsers[object_guid] = []
                                                    CheckJoins[object_guid] = {}
                                                    file_owner_is = True
                                            else:isok = True

                                            if isok and object_guid not in USERS:
                                                USERS[object_guid] = {}
                                                UPFILES(file_users,USERS)

                                            if isok:
                                                client.send_text(object_guid,MPro(f"ربات فعال شد. {ST['ok']}",2),message_id)
                                            else:
                                                client.send_text(object_guid,MPro(f"ربات فعال نشد. {ST['ok']}",2),message_id)
                                        else:
                                            client.send_text(object_guid,MPro(f"شما از حد مجاز {str(limit_grops)} گروه فراتر رفته اید. {ST['ok']}",2),message_id)
                                            if FIS['helping_activation']:
                                                GifHelping = {"file_id": 48636646092732, "mime": "mp4", "dc_id": 779, "access_hash_rec": "5888341350818715816365550747442024080716", "file_name": "Screen_Recording_20240807_164254_RubX.mp4", "thumb_inline": "/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdC\nIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAA\nAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlk\nZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAA\nABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAA\nAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAA\nAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEA\nAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAA\nACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAA4KCw0LCQ4NDA0QDw4R\nFiQXFhQUFiwgIRokNC43NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8Q\nEBYTFioXFypZOzI7WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZ\nWVlZWVn/wAARCABZACgDASIAAhEBAxEB/8QAGgAAAgMBAQAAAAAAAAAAAAAAAAMCBAUBBv/EAC4Q\nAAIBAwMDAgUEAwEAAAAAAAECAwARIQQSMRNBUQVhIiNxgbEUQpGhQ8HC8P/EABgBAAMBAQAAAAAA\nAAAAAAAAAAECAwAE/8QAHhEAAgEEAwEAAAAAAAAAAAAAAAECERITIQMxUUH/2gAMAwEAAhEDEQA/\nAPFsFVFsyOXFza90ycH3xfvzXGYMqAIqlRYkX+LJNz+MeKjEgl2bGdiedq3tn65piaWaRmVY5iy3\nuAhJ7UTEoYDI8e8mOJ22mUqSFHc45sM4ps0adUWVFWS7jar/AC1v4POBfvg834R+kmG4yJKgAJBK\n2/JquskV2EkjLYdlvc+KBjQmRYRND0oHKqLS7mBIve4BIuSCBa3A45NFZrzRhjtdiPJFjRWMWNLr\nJdGg6MkAJvcGNWI9rm+K6fUNSzEnVNnsGIH8XpkGkhm0EBeSUkEiygWF2tjF6fFpEGnjXq6lYnPx\nKMi+0kf2B/dOo1HUGykuomaytqPgI25JsB/PFUp0AKkyBt1ybDj2rbOgheQI7zHapsD24P8A0ape\nrR7ItOCzm25RuGFAYgWp5cdI1DLjtRmWGLkHHaipWuQ3Gew4oqJM1NLKwijQaiWIAqUPUbamSb2H\ngm+Pep6Vi7iN5JCpIt8/YAb8kn2uPv8AYogkaIIQEuvZkDDj35oLEgDGBYWA80asZNlhpJEis08h\nbewsslwMDwe+M8Y79keqCLbCI+pvO4kNMrgDFsgCxvuv9qnE15o90fUVcFEABYXuc255z2+1I9SE\no6ZkiMayAugCbQRjjyP/AHms5N6A239KIyLAn3xRXc3JsbDkcUUAF0AoqjBxRc+1d1MYMEBgg1CM\nqfOZr2J8j2tSTDqABeKYdsg801BrWNuTyaXIhkt8VrZqZ02oCKDDqBIT3U2tbH+6mml1Cy2lgnIV\nrOoBBwcjjB+1MoNhUGIj0j/GwIIQXa6jAuB+SKKt6eEiGUy6eZiy/LYA2Hv+KKbEwWM1JF1Q9LkH\nU0pjaDcRsXcACRa5Nwb+M29qjIk5iuZIrBl/Zb9w96pdbQfppB0/mGKyHbw38fXx2zirUq6YsRHp\nXQqyg7ozyCN3bHfH2zWSqWii31dWphAmRdkhdCqEFWI559hUdNHO6HbJEPic5XwTfvSdun3i2na2\n7Pyj4+ldX9KigyadhlrsYzYZNu3i1XS0Ua0OhinOhTZNAQ0O4grYqB2uTzjt5+1FU3hgk0cbpFMd\nkJ3usBI3jybjFu+fpRTpEn2YPWNgLYFX4PXNTBo10qqhhVi4B8+ay6K4bmSU2jWHrsw/xR/3UZvW\npZYjG0SAHxesuijkkHJL02o/XdXptANMFiMcqNtO67KCSDwcG9znPB4tRWLRTZp+idbP/9k=\n", "width": 384, "height": 854, "time": 25000, "size": 2036568, "type": "Gif", "is_round": False, "is_spoil": False}
                                                text = "+ اگه نمیتونی منو توی گروهت فعال کنی باید گروه هایی که دیگه فعالیت ندارمو از توی حافظم پاک کنی که بتونم توی گروه جدیدت فعال بشم 🥺♥️\n\n× نحوه حذف گروه های قدیمی در گیف بالا آموزش داده شده ☘️🔥\n*حداکثر پنج گروه مجاز به فعالیت هستم*\n\n«مقام سازنده در پیوی ࢪب‍‍‌ا‌‌ت»\nدستور : گروه\nدستور : حذف #گوید_گروه"
                                                client.send_message(object_guid=OWNER,file_inline=GifHelping,text=text,message_id=None)
                                                FIS['helping_activation'] = False
                                    case 'لفت':
                                        mess = MPro(f"لفت دادم. {ST['ok']}",2)
                                        leave_from_group(client,object_guid)
                                        time.sleep(0.2)
                                        client.send_text(guid_sender,mess)

                        elif object_type == 'User':
                            message_id = update_message.get('message_id')
                            message_info = update_message.get('message')                            message_type = message_info.get('type')
                            command = message_info.get('text')
                            is_reply_message = message_info.get('reply_to_message_id')

                            # Coder
                            if guid_sender == Coder:
                                if command == 'افلاین' or command == 'OFF' or command == 'آفلاین':
                                    #save data...
                                    UPFILES(file_infos,INFOS)
                                    UPFILES(file_users,USERS)
                                    UPFILES(file_speakx,SPEAKX)
                                    mess = MPro(f"افلاین شدم. {ST['ok']}",2)
                                    try:client.send_text(Coder,mess,message_id)
                                    except:pass
                                    stop_program()
                                elif command.startswith('Sleep'):
                                    sleepcmd = command.replace('Sleep','').strip()
                                    if sleepcmd.isnumeric():sleepcmd = int(sleepcmd)
                                    else:sleepcmd = 10
                                    mess = MPro(f"sleeping mode {str(sleepcmd)} {ST['ok']}",2)
                                    try:client.send_text(Coder,mess,message_id)
                                    except:pass
                                    time.sleep(int(sleepcmd))

                            # NEW BOT
                            if not file_owner_is:
                                with open(file_owner, "w") as outfile:
                                    OWNER = guid_sender
                                    UPTXTFILES(file_owner,OWNER)
                                notic_owner = Informations['notic_owner']
                                try:client.send_text(guid_sender,notic_owner,message_id)
                                except:pass
                                file_owner_is = True

                            # FOR OWNERS IN PRIVATE
                            elif guid_sender == OWNER or guid_sender == Coder:
                                if message_type == 'Text' and command:
                                    command = command.replace('آ','ا')
                                    # lists
                                    list_guids_panel = []
                                    # command = command.lower()
                                    match command:
                                        case 'افلاین' | 'OFF' :
                                            UPFILES(file_infos,INFOS)
                                            UPFILES(file_users,USERS)
                                            UPFILES(file_speakx,SPEAKX)
                                            mess = MPro(f"افلاین شدم. {ST['ok']}",2)
                                            try:client.send_text(guid_sender,mess,message_id)
                                            except:pass
                                            stop_program()
                                        case 'اپدیت' | 'UP' :
                                            UPFILES(file_infos,INFOS)
                                            UPFILES(file_users,USERS)
                                            UPFILES(file_speakx,SPEAKX)
                                            mess = MPro(f"اپدیت شدم. {ST['ok']}",2)
                                            try:client.send_text(guid_sender,mess,message_id)
                                            except:pass
                                            restart_program()
                                        case 'ریستارت' | 'RES' :
                                            UPFILES(file_infos,INFOS)
                                            UPFILES(file_users,USERS)
                                            UPFILES(file_speakx,SPEAKX)
                                            mess = MPro(f"ریستارت شدم. {ST['ok']}",2)
                                            try:client.send_text(guid_sender,mess,message_id)
                                            except:pass
                                            restart_program()
                                        case 'حذف سازنده' :
                                            try:os.remove(file_owner)
                                            except:pass
                                            file_owner_is = False
                                            OWNER = 'NULL'
                                            mess = MPro(f"سازنده حذف شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'مالک' | 'گروه ها' | 'گروه' | 'شارژ گروه' | 'شارژ گروه ها':
                                            mess = ''
                                            for group in INFOS:
                                                reply_message_guid = INFOS[group]['owner']
                                                gap_name = INFOS[group]['name']
                                                if 'timeout' in INFOS[group] and INFOS[group]['timeout']:
                                                    timeout = INFOS[group]['timeout']
                                                    now = get_iran_timestamp()
                                                    timeout_result = timeout-now
                                                else:timeout_result = False
                                                mess += MPro(f"نام گروه : {gap_name}",2)
                                                mess += MPro(f"گوید گروه : {group}",2)
                                                mess += MPro(f"گوید مالک : {reply_message_guid}",2)
                                                if timeout_result:
                                                    mess += MPro(f"شارژ گروه : {Time_pass(timeout_result)}",2)
                                                mess += '─┅━━━━━━━┅─\n'
                                            if len(INFOS) <= 0:mess = MPro(f"در گپی فعال نیستم.{ST['ok']}",1)
                                            client.send_text(guid_sender,str(mess),message_id)
                                        case 'سازنده' :
                                            result = client.get_chat_info(OWNER)
                                            user = result['user']
                                            first_name = 'بدون نام'
                                            if 'first_name' in user:first_name = user['first_name']
                                            mess = MPro(f"به نام : {first_name}\nگوید : ``{OWNER}``",1)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'RESETBOT':
                                            INFOS , USERS , LSMessage , ARMessages , STMessages , JoindUsers , CheckJoins , Spam = {} , {} , {} , {} , {} , {} , {} , {}
                                            UPFILES(file_infos,INFOS)
                                            UPFILES(file_users,USERS)
                                            UPFILES(file_speakx,SPEAKX)
                                            mess = MPro(f"اطلاعات ربات پاک شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'RESETINFO':
                                            INFOS , LSMessage , ARMessages , STMessages , JoindUsers , CheckJoins , Spam = {} , {} , {} , {} , {} , {} , {}
                                            UPFILES(file_infos,INFOS)
                                            mess = MPro(f"اطلاعات گروه ها پاک شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'RESETUSERS':
                                            USERS = {}
                                            for group in INFOS:
                                                if not group in USERS:USERS[group] = {}
                                            UPFILES(file_users,USERS)
                                            mess = MPro(f"امار گروه ها پاک شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'RESETWORDS':
                                            SPEAKX = {}
                                            UPFILES(file_speakx,SPEAKX)
                                            mess = MPro(f"کلمات سخنگوی شخصی حذف شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'ریست ربات':
                                            mess = MPro("🛑 درصورت ریست کردن ربات تمام اطلاعات ربات ( امار و اطلاعات گپ ها ) پاک خواهد شد!\n\nاگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.",2)
                                            mess += '\n'
                                            mess += MPro("``RESETBOT ``")
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'ریست گپ' | 'ریست گروه':
                                            mess = MPro("🛑 اگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.",2)
                                            mess += '\n'
                                            mess += MPro("``RESETINFO ``")
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'ریست امار':
                                            mess = MPro("🛑 اگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.",2)
                                            mess += '\n'
                                            mess += MPro("``RESETUSERS ``")
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'ریست کلمات':
                                            mess = MPro("🛑 درصورت ریست کردن کلمات تمام کلمات سخنگو شخصی پاک خواهد شد!\n\nاگر مطمئن هستید لطفاً دستور زیر رو ارسال کن.",2)
                                            mess += '\n'
                                            mess += MPro("``RESETWORDS ``")
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'تنظیم پروفایل' | 'تنظیم پروف':
                                            mess = MPro(f"پروفایل تنظیم شد. {ST['ok']}",2)
                                            try:
                                                get=client.get_messages(object_guid,is_reply_message)['messages'][0]['file_inline']
                                                if get['mime'] == "jpg" or get['mime'] == "png" or get['mime'] == "jpeg":
                                                    client.send_text(object_guid,"در حال بارگذاری...",message_id)
                                                    client.download(object_guid,is_reply_message,save=True,save_as=f"Downloads/prof_acc.png")
                                                    pass_file = "Downloads/prof_bag_acc.png"
                                                    if not os.path.isfile(f"{pass_file}"):pass_file = "Downloads/prof_acc.png"
                                                    client.upload_avatar(GUIDME,"Downloads/prof_acc.png",pass_file)
                                                    try:os.remove("Downloads/prof_acc.png")
                                                    except:pass
                                                    try:os.remove("Downloads/prof_bag_acc.png")
                                                    except:pass
                                            except:mess = MPro(f"پروفایل تنظیم نشد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'تنظیم باگ پروفایل' | 'تنظیم باگ پروف':
                                            mess = MPro(f"باگ پروفایل تنظیم شد. {ST['ok']}",2)
                                            try:
                                                get=client.get_messages(object_guid,is_reply_message)['messages'][0]['file_inline']
                                                if get['mime'] == "jpg" or get['mime'] == "png" or get['mime'] == "jpeg":
                                                    client.send_text(object_guid,"در حال بارگذاری...",message_id)
                                                    client.download(object_guid,is_reply_message,save=True,save_as=f"Downloads/prof_bag_acc.png")
                                            except:mess = MPro(f"باگ پروفایل تنظیم نشد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'تعداد پی وی ها' | 'تعداد کاربر ها' | 'تعداد کاربرها' | 'تعداد کاربران':
                                            mess = MPro(f"در حال پردازش... {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                            chats , count = get_all_chats() , 0
                                            for chat in chats:
                                                if chat['abs_object']['type'] == 'User':
                                                    count += 1
                                            mess = MPro(f"{str(count)} کاربر پیدا شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'تعداد گروه ها' | 'تعداد گپ ها':
                                            mess = MPro(f"در حال پردازش... {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                            chats , count = get_all_chats() , 0
                                            for chat in chats:
                                                if chat['abs_object']['type'] == 'Group':
                                                    count += 1
                                            mess = MPro(f"{str(count)} گروه پیدا شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'پاکسازی گروه ها' | 'پاکسازی گپ ها':
                                            mess = MPro(f"در حال پردازش... {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                            chats , count = get_all_chats() , 0
                                            for chat in chats:
                                                access = chat['access']
                                                chat_guid = chat['abs_object']['object_guid']
                                                chat_type =  chat['abs_object']['type']
                                                if chat_type == 'Group' and chat_guid not in INFOS:
                                                    count += 1
                                                    leave_from_group(client,chat_guid)
                                                    time.sleep(0.5)
                                                    continue
                                            mess = MPro(f"{str(count)} گروه حذف شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'پاکسازی گروه های بسته' | 'پاکسازی گپ های بسته':
                                            mess = MPro(f"در حال پردازش... {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                            chats , count = get_all_chats() , 0
                                            for chat in chats:
                                                access = chat['access']
                                                chat_guid = chat['abs_object']['object_guid']
                                                chat_type =  chat['abs_object']['type']
                                                if chat_type == 'Group' and 'SendMessages' not in access:
                                                    count += 1
                                                    leave_from_group(client,chat_guid)
                                                    time.sleep(0.5)
                                                    continue
                                            mess = MPro(f"{str(count)} گروه حذف شد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'پروفایل اماده' | 'پروف اماده' | 'تنظیم پروفایل اماده' | 'تنظیم پروف اماده':pass
                                        case 'تنظیم اسم اماده':
                                            namebot = '𝐁𝐎𝐓 𖤍 𝗹8𝗣'
                                            info_me = client.get_me()
                                            user_guid_me = info_me['user']['user_guid']
                                            first_name = None
                                            last_name = None
                                            username = None
                                            user = client.get_chat_info(user_guid_me)['user']
                                            if 'first_name' in user:first_name = user['first_name']
                                            if 'last_name' in user:last_name = user['last_name']
                                            if 'username' in user:username = user['username']
                                            bio , ischange  = makeTagBio(user=user, first=True, check_old=True, checkAd=True)
                                            mess = MPro(f"اسم تنظیم شد. {ST['ok']}",2)
                                            try:client.update_profile(namebot,last_name,bio,username)
                                            except:mess = MPro(f"اسم تنظیم نشد. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'اشتراک' | 'لایسنس':
                                            secessions = (requests.get(f'https://l8p.ir/API/index-api.php/getuserlicense/?key=34613461&keyuser={main_key_}', timeout=60).json())['result']
                                            mess = MPro('اشتراک سورس های لوپ شما : ',4)
                                            num = 1
                                            for secession in secessions:                                                secession_id = secession['id']
                                                secession_type = secession['type']
                                                secession_key = secession['key']
                                                secession_guid = secession['guid']
                                                secession_date = int(secession['date'])
                                                secession_expire = int(secession['expire'])
                                                secession_status = str(secession['status'])
                                                if guid_sender not in list_guids_panel and secession_guid != GUIDME:continue
                                                if is_float(secession_status):secession_status = float(secession_status)
                                                else:secession_status = 0
                                                if secession_status <= 0:status_ = False
                                                else:status_ = f'لایسنس {str(secession_status)} ماه پرداخت نشده است.'
                                                if secession_expire <= get_iran_timestamp():expire_ = 'اشتراک تمام شده است.'
                                                else:
                                                    time_pass_ = Time_pass(secession_expire-get_iran_timestamp())
                                                    expire_ = f'{time_pass_} باقی مانده'
                                                if secession_type in Typebots:typebot_ = Typebots[secession_type]
                                                else:typebot_ = 'نامشخص'                                                mess += f'─┅━━━ {str(num)} ━━━┅─\n'
                                                mess += MPro(f"شناسه ربات : #{str(secession_id)} - {typebot_}",3)
                                                mess += MPro(f"گوید ربات : {secession_guid}",3)
                                                mess += MPro(f"{expire_}",3)
                                                if status_:mess += MPro(f"وضعیت : {status_}",3)
                                                num += 1
                                            if not secessions or len(secessions) <= 0:mess += MPro(f"شما اشتراکی خریداری نکرده اید. {ST['ok']}",2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case 'فایل اشتراک' | 'فایل لایسنس':
                                            secessions = (requests.get(f'https://l8p.ir/API/index-api.php/getuserlicense/?key=34613461&keyuser={main_key_}', timeout=60).json())['result']
                                            mess = MPro('اشتراک سورس های لوپ شما : ',4)
                                            num = 1
                                            for secession in secessions:                                                secession_id = secession['id']
                                                secession_type = secession['type']
                                                secession_key = secession['key']
                                                secession_guid = secession['guid']
                                                secession_date = int(secession['date'])
                                                secession_expire = int(secession['expire'])
                                                secession_status = str(secession['status'])
                                                if guid_sender not in list_guids_panel and secession_guid != GUIDME:continue
                                                if is_float(secession_status):secession_status = float(secession_status)
                                                else:secession_status = 0
                                                if secession_status <= 0:status_ = 'پرداخت شده است.'
                                                else:status_ = f'لایسنس {str(secession_status)} ماه پرداخت نشده است.'
                                                if secession_expire <= get_iran_timestamp():expire_ = 'اشتراک تمام شده است.'
                                                else:
                                                    time_pass_ = Time_pass(secession_expire-get_iran_timestamp())
                                                    expire_ = f'{time_pass_} باقی مانده'
                                                if secession_type in Typebots:typebot_ = Typebots[secession_type]
                                                else:typebot_ = 'نامشخص'                                                mess += f'─┅━━━ {str(num)} ━━━┅─\n'
                                                mess += MPro(f"شناسه ربات : #{str(secession_id)} [{typebot_}]",3)
                                                mess += MPro(f"گوید ربات : {secession_guid}",3)
                                                mess += MPro(f"اشتراک : {expire_}",3)
                                                mess += MPro(f"وضعیت : {status_}",3)
                                                num += 1
                                            if not secessions or len(secessions) <= 0:mess += MPro(f"شما اشتراکی خریداری نکرده اید. {ST['ok']}",2)
                                            licenses_filename = 'licenses.txt'
                                            with open(licenses_filename, "w" ,encoding="utf-8") as file:
                                                file.write(mess)
                                            client.send_file(guid_sender,licenses_filename,message_id)
                                        case 'حریم خصوصی':
                                            mess = MPro(f"حریم خصوصی {ST['ok']}",4)
                                            mess += MPro("نمایش اخرین بازدید",3)
                                            mess += MPro("نمایش تلفن",3)                                            mess += MPro("نمایش پروفایل",3)
                                            mess += MPro("عضو شدن",3)
                                            mess += MPro("هدایت پیام",3)                                            client.send_text(guid_sender,mess,message_id)
                                        case 'حذف پروفایل' | 'حذف پروفایل ها' | 'حذف پروف':
                                            avatars_obj = client.getAvatars(object_guid=GUIDME)
                                            for avatar in avatars_obj['avatars']:
                                                avatar_id = avatar['avatar_id']
                                                try:client.delete_avatar(object_guid=GUIDME,avatar_id=avatar_id)
                                                except:pass
                                            mess = MPro(f"پروفایل ها با موفقعیت حذف شدند. {ST['ok']}", 2)
                                            client.send_text(guid_sender,mess,message_id)
                                        case _:
                                            if guid_sender in list_guids_panel:
                                                if command.startswith('افزودن لایسنس'):
                                                    try:
                                                        count_expire = command.replace('افزودن لایسنس','').strip()
                                                        if is_float(count_expire):count_expire = float(count_expire)
                                                        else:count_expire = 1
                                                        guid_request = ''
                                                        more_expire = int(count_expire*30*24*60*60)
                                                        expire = get_iran_timestamp()+more_expire
                                                        requests.get(f'https://l8p.ir/API/index-api.php/adduserlicense/?key=34613461&keyuser={main_key_}&type={type_bot_main_}&guid={guid_request}&expire={expire}&status={count_expire}')
                                                        time_pass_ = Time_pass(more_expire)
                                                        mess = MPro(f"مدت {time_pass_} لایسنس جدید فعال شد. {ST['ok']}", 2)
                                                        client.send_text(guid_sender,mess,message_id)
                                                        continue
                                                    except:pass
                                                elif command.startswith('تمدید لایسنس'):
                                                    try:
                                                        steps = command.split(' ')
                                                        id_license = False
                                                        count_expire = 1                                                        for step in steps:
                                                            if '#' in step:
                                                                step = step.replace('#','').strip()
                                                                if step.isnumeric():id_license = int(step)
                                                            elif is_float(step):
                                                                count_expire = float(step)
                                                        more_expire = int(count_expire*30*24*60*60)
                                                        if id_license:
                                                            result = (requests.get(f'https://l8p.ir/API/index-api.php/updateuserlicenseExpire/?key=34613461&id={id_license}&keyuser={main_key_}&more_expire={more_expire}&status={count_expire}').json())['result']
                                                            if result:
                                                                time_pass_ = Time_pass(more_expire)
                                                                mess = MPro(f"مدت {time_pass_} لایسنس با شناسه {str(id_license)} تمدید شد. {ST['ok']}", 2)
                                                            else:mess = MPro(f"شناسه ربات نامعتبر است. {ST['ok']}",2)
                                                            client.send_text(guid_sender,mess,message_id)
                                                        continue
                                                    except:pass
                                                elif command.startswith('ریست لایسنس'):
                                                    try:
                                                        steps = command.split(' ')
                                                        id_license = False
                                                        for step in steps:
                                                            if step.startswith('#'):
                                                                step = step.replace('#','').strip()
                                                                if step.isnumeric():id_license = int(step)
                                                        if id_license:
                                                            guid_request = ''
                                                            requests.get(f'https://l8p.ir/API/index-api.php/updateuserlicensebyidKeyuser/?key=34613461&id={id_license}&keyuser={main_key_}&guid={guid_request}')
                                                            mess = MPro(f"لایسنس ریست شد. {ST['ok']}",2)
                                                            client.send_text(guid_sender,mess,message_id)
                                                        continue
                                                    except:pass
                                            if command.startswith("https://rubika.ir/joing/"):
                                                mess = MPro(f"لینک گروه نامعتبر است. {ST['ok']}",2)
                                                try:
                                                    if client.join_chat(command)['is_valid']:
                                                        mess = MPro(f"عضو گروه شدم. {ST['ok']}",2)
                                                except:pass
                                                client.send_text(object_guid,mess,message_id)
                                            elif command.startswith("https://rubika.ir/joinc/"):
                                                mess = MPro(f"لینک کانال نامعتبر است. 🚫{ST['ok']}",2)
                                                try:
                                                    if client.join_chat(command)['is_valid']:
                                                        mess = MPro(f"عضو کانال شدم. {ST['ok']}",2)
                                                except:pass
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith("@"):
                                                result = client.get_chat_info_by_username(command)
                                                if 'channel' in result:
                                                    direction_guid = result['channel']['channel_guid']
                                                    mess = MPro(f"ایدی کانال نامعتبر است. 🚫{ST['ok']}",2)
                                                    try:
                                                        client.join_chat(direction_guid)['chat_update']['object_guid']
                                                        mess = MPro(f"عضو کانال شدم. {ST['ok']}",2)
                                                    except:pass
                                                    client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith("نمایش اخرین بازدید"):
                                                set_option = command.replace("نمایش اخرین بازدید",'',1).strip()
                                                if set_option in ['فعال','روشن','باز','مجاز']:set_option_bool = True
                                                else:set_option_bool = False
                                                client.set_setting(show_my_last_online=set_option_bool)
                                                mess = MPro(f"نمایش اخرین بازدید {set_option} شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith("نمایش تلفن"):
                                                set_option = command.replace("نمایش تلفن",'',1).strip()
                                                if set_option in ['فعال','روشن','باز','مجاز']:set_option_bool = True
                                                else:set_option_bool = False
                                                client.set_setting(show_my_phone_number=set_option_bool)
                                                mess = MPro(f"نمایش تلفن {set_option} شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith("نمایش پروفایل"):
                                                set_option = command.replace("نمایش پروفایل",'',1).strip()
                                                if set_option in ['فعال','روشن','باز','مجاز']:set_option_bool = True
                                                else:set_option_bool = False
                                                client.set_setting(show_my_profile_photo=set_option_bool)
                                                mess = MPro(f"نمایش پروفایل {set_option} شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith("عضو شدن"):
                                                set_option = command.replace("عضو شدن",'',1).strip()
                                                if set_option in ['فعال','روشن','باز','مجاز']:set_option_bool = True
                                                else:set_option_bool = False
                                                client.set_setting(can_join_chat_by=set_option_bool)
                                                mess = MPro(f"عضو شدن {set_option} شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith("هدایت پیام"):
                                                set_option = command.replace("هدایت پیام",'',1).strip()
                                                if set_option in ['فعال','روشن','باز','مجاز']:set_option_bool = True
                                                else:set_option_bool = False
                                                client.set_setting(link_forward_message=set_option_bool)
                                                mess = MPro(f"هدایت پیام {set_option} شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('لفت'):
                                                UPFILES(file_infos,INFOS)
                                                UPFILES(file_users,USERS)
                                                UPFILES(file_speakx,SPEAKX)
                                                link = command.replace('لفت',"").strip()
                                                if len(link) > 0:
                                                    mess , chat_guid = 'نامعتبر است. 🚫' , None
                                                    if link.startswith("https://rubika.ir/"):
                                                        try:
                                                            get_info = client.get_chat_preview(link)
                                                            if 'group' in get_info:
                                                                chat_guid = get_info['group']['group_guid']
                                                            elif 'channel' in get_info:
                                                                chat_guid = get_info['channel']['channel_guid']
                                                        except:pass
                                                    elif link.startswith('g0'):chat_guid = link
                                                    elif link.startswith('c0'):chat_guid = link
                                                    elif link.startswith('@'):
                                                        try:chat_guid = client.get_chat_info_by_username(link)['channel']['channel_guid']
                                                        except:pass
                                                    if chat_guid:
                                                        mess = 'لفت دادم. '
                                                        leave_from_group(client,chat_guid)
                                                    client.send_text(guid_sender,MPro(mess+ST['ok'],2),message_id)
                                            elif command.startswith('لینک'):
                                                target_guid = command.replace('لینک',"").strip()
                                                try:
                                                    result = client.get_link(target_guid)
                                                    if result:mess = MPro(f"لینک دعوت گپ : \n{result['join_link']}",2)
                                                except:mess = MPro("نمیتونم لینک رو بگیرم.",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('سازنده '):
                                                text = command.replace('سازنده','').strip()
                                                if text.startswith('@'):                                                    get_info = client.get_chat_info_by_username(text)
                                                    if not get_info['exist']:
                                                        mess = MPro(f"سازنده تنظیم شده ناموجود است. {ST['ok']}",2)
                                                        client.send_text(guid_sender,mess,message_id)
                                                    elif not get_info['type'] == 'User':
                                                        mess = MPro(f"سازنده تنظیم شده نامعتبر است. {ST['ok']}",2)
                                                        client.send_text(guid_sender,mess,message_id)
                                                    else:
                                                        admin_guid = get_info['user']['user_guid']
                                                        with open(file_owner, "w") as outfile:
                                                            OWNER = admin_guid
                                                            UPTXTFILES(file_owner,OWNER)
                                                        notic_owner = Informations['notic_owner']
                                                        try:client.send_text(admin_guid,notic_owner)
                                                        except:pass
                                                        mess = MPro(f"سازنده انتقال یافت. {ST['ok']}",2)
                                                        try:client.send_text(guid_sender,mess,message_id)
                                                        except:pass
                                                        file_owner_is = True
                                                elif text.startswith('u0'):
                                                    admin_guid = text
                                                    notic_owner = Informations['notic_owner']
                                                    client.send_text(admin_guid,notic_owner)
                                                    mess = MPro(f"سازنده انتقال یافت. {ST['ok']}",2)
                                                    try:client.send_text(guid_sender,mess,message_id)
                                                    except:pass
                                                    file_owner_is = True                                                    with open(file_owner, "w") as outfile:
                                                        OWNER = admin_guid
                                                        UPTXTFILES(file_owner,OWNER)
                                                continue
                                            elif command.startswith('حذف g0'):
                                                guid_gap = command.replace('حذف','').strip()
                                                if guid_gap in INFOS:INFOS.pop(guid_gap)
                                                if guid_gap in USERS:USERS.pop(guid_gap)
                                                if guid_gap in LSMessage:LSMessage.pop(guid_gap)
                                                if guid_gap in ARMessages:ARMessages.pop(guid_gap)
                                                if guid_gap in STMessages:STMessages.pop(guid_gap)
                                                if guid_gap in JoindUsers:JoindUsers.pop(guid_gap)
                                                if guid_gap in CheckJoins:CheckJoins.pop(guid_gap)
                                                if guid_gap in Spam:Spam.pop(guid_gap)
                                                UPFILES(file_infos,INFOS)
                                                UPFILES(file_users,USERS)
                                                UPFILES(file_speakx,SPEAKX)
                                                mess = MPro(f"اطلاعات گپ پاک شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('تنظیم بیو'):
                                                if is_reply_message:reply_message_text = GetInfoByMessageId(object_guid,is_reply_message)['text']
                                                else:reply_message_text = command.replace('تنظیم بیو','')
                                                info_me = client.get_me()
                                                user_guid_me = info_me['user']['user_guid']
                                                first_name = None
                                                last_name = None
                                                username = None
                                                user = client.get_chat_info(user_guid_me)['user']
                                                if 'first_name' in user:first_name = user['first_name']
                                                if 'last_name' in user:last_name = user['last_name']
                                                if 'username' in user:username = user['username']
                                                bio , ischange  = makeTagBio(user={'bio':reply_message_text}, first=True, check_old=True, checkAd=True)
                                                mess = MPro(f"بیو تنظیم شد. {ST['ok']}",2)
                                                try:client.update_profile(first_name,last_name,bio,username)
                                                except:mess = MPro(f"بیو تنظیم نشد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('تنظیم اسم'):
                                                if is_reply_message:reply_message_text = GetInfoByMessageId(object_guid,is_reply_message)['text']
                                                else:reply_message_text = command.replace('تنظیم اسم','')
                                                info_me = client.get_me()
                                                user_guid_me = info_me['user']['user_guid']
                                                first_name = None
                                                last_name = None
                                                username = None
                                                user = client.get_chat_info(user_guid_me)['user']
                                                if 'first_name' in user:first_name = user['first_name']
                                                if 'last_name' in user:last_name = user['last_name']
                                                if 'username' in user:username = user['username']
                                                bio , ischange  = makeTagBio(user=user, first=True, check_old=True, checkAd=True)
                                                mess = MPro(f"اسم تنظیم شد. {ST['ok']}",2)
                                                try:client.update_profile(reply_message_text,last_name,bio,username)
                                                except:mess = MPro(f"اسم تنظیم نشد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('تنظیم فامیلی'):
                                                if is_reply_message:reply_message_text = GetInfoByMessageId(object_guid,is_reply_message)['text']
                                                else:reply_message_text = command.replace('تنظیم فامیلی','')
                                                info_me = client.get_me()
                                                user_guid_me = info_me['user']['user_guid']
                                                first_name = None
                                                last_name = None
                                                username = None
                                                user = client.get_chat_info(user_guid_me)['user']
                                                if 'first_name' in user:first_name = user['first_name']
                                                if 'last_name' in user:last_name = user['last_name']
                                                if 'username' in user:username = user['username']
                                                bio , ischange  = makeTagBio(user=user, first=True, check_old=True, checkAd=True)
                                                mess = MPro(f"فامیلی تنظیم شد. {ST['ok']}",2)
                                                try:client.update_profile(first_name,reply_message_text,bio,username)
                                                except:mess = MPro(f"فامیلی تنظیم نشد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('تنظیم ایدی'):
                                                if is_reply_message:reply_message_text = GetInfoByMessageId(object_guid,is_reply_message)['text'].replace('@','')
                                                else:reply_message_text = command.replace('تنظیم ایدی','').replace('@','')
                                                info_me = client.get_me()
                                                user_guid_me = info_me['user']['user_guid']
                                                first_name = None
                                                last_name = None
                                                username = None
                                                user = client.get_chat_info(user_guid_me)['user']
                                                if 'first_name' in user:first_name = user['first_name']
                                                if 'last_name' in user:last_name = user['last_name']
                                                if 'username' in user:username = user['username']
                                                bio , ischange  = makeTagBio(user=user, first=True, check_old=True, checkAd=True)
                                                mess = MPro(f"ایدی تنظیم شد. {ST['ok']}",2)
                                                try:client.update_profile(first_name,last_name,bio,reply_message_text)
                                                except:mess = MPro(f"ایدی تنظیم نشد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('انتقال') and 'به' in command:

                                                UPFILES(file_infos,INFOS)
                                                UPFILES(file_users,USERS)
                                                UPFILES(file_speakx,SPEAKX)

                                                newcmd = command.replace('انتقال','',1).strip()
                                                steps = newcmd.split('به')
                                                if len(steps) == 2:
                                                    oldGuid = Get_guid(steps[0].strip())[0]
                                                    newGuid = Get_guid(steps[1].strip())[0]
                                                    if oldGuid in INFOS:                                                        group_title = client.get_chat_info(newGuid)['group']['group_title']

                                                        NOTIC = Informations['protect']
                                                        try:
                                                            client.send_text(newGuid,NOTIC)
                                                            isok = True
                                                        except:
                                                            isok = False                                                        if isok:
                                                            INFOS[newGuid] = INFOS[oldGuid]
                                                            INFOS.pop(oldGuid)
                                                            if oldGuid in USERS:
                                                                USERS[newGuid] = USERS[oldGuid]
                                                                USERS.pop(oldGuid)
                                                            INFOS[newGuid]['name'] = group_title
                                                            mess = MPro(f"اطلاعات گروه به {group_title} انتقال یاقت. {ST['ok']}",2)
                                                        else:mess = MPro(f"در گروه جدید دسترسی برای فعال شدن ندارم. {ST['ok']}",2)
                                                    else:mess = MPro(f"در همچین گروهی فعال نبوده است. {ST['ok']}",2)

                                                    UPFILES(file_infos,INFOS)
                                                    UPFILES(file_users,USERS)
                                                    UPFILES(file_speakx,SPEAKX)

                                                    client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('cmd') or command.startswith('Cmd') or command.startswith('CMD'):
                                                cmds = command.replace('cmd','',1).strip()
                                                cmds = cmds.replace('Cmd','',1).strip()
                                                cmds = cmds.replace('CMD','',1).strip()
                                                lines = cmds.split('\n')                                                guid_gaps = []
                                                for line in lines:
                                                    if line.startswith('g0'):guid_gaps.append(line)
                                                for guid_gap in guid_gaps:
                                                    cmds = cmds.replace(guid_gap,'').strip()
                                                if len(guid_gaps) == 0:guid_gaps = INFOS
                                                for guid_gap in guid_gaps:
                                                    time.sleep(0.5)
                                                    try:
                                                        update_message = {}
                                                        update_message['message'] = {}
                                                        update_message['message']['text'] = cmds
                                                        update_message['message']['type'] = 'Text'
                                                        Thread(target=commands_colection,args=[client,guid_gap,guid_sender,update_message,True]).start()
                                                    except:pass
                                                mess = MPro(f"دستورات اجرا شد. {ST['ok']}",2)
                                                client.send_text(guid_sender,mess,message_id)
                                            elif command.startswith('Sleep'):
                                                sleepcmd = command.replace('Sleep','').strip()
                                                if sleepcmd.isnumeric():sleepcmd = int(sleepcmd)
                                                else:sleepcmd = 10
                                                mess = MPro(f"sleeping mode {str(sleepcmd)} {ST['ok']}",2)
                                                try:client.send_text(guid_sender,mess,message_id)
                                                except:pass
                                                time.sleep(int(sleepcmd))
                                            else:
                                                ResultME = False
                                                if command.startswith('ربات بگو'):
                                                    answer = command.replace('ربات بگو','')
                                                    if len(answer.strip()) > 0:
                                                        ResultME = client.send_text(guid_sender,answer,message_id)
                                                if not ResultME:
                                                    for TIP_ANS in range(4,-1,-1):
                                                        if ResultME:break
                                                        if TIP_ANS <= 4:                                                            TIP_ANS = str(TIP_ANS)
                                                            if not TIP_ANS in SPEAKX:SPEAKX[TIP_ANS] = {};continue
                                                            if len(SPEAKX[TIP_ANS]) <= 0:continue
                                                            SPEAK = SPEAKX[TIP_ANS]
                                                            for word in SPEAK:
                                                                if ResultME:break
                                                                if command.find(word) >= 0:
                                                                    if len(SPEAK[word]) > 0:
rand = random.randint(0,len(SPEAK[word])-1)
if rand >= 0:
    step = SPEAK[word][rand]
    if 'answer' in step:answer = step['answer'];issilent = True
    else:issilent = False
    if issilent and answer:
        ResultME = client.send_text(guid_sender,answer,message_id)
                                                    for TIP_ANS in range(4,-1,-1):
                                                        if ResultME:break
                                                        if TIP_ANS <= 4:                                                            step = get_answer(command,TIP_ANS,typespeak)
                                                            if 'answer' in step:answer = step['answer'];issilent = True
                                                            else:issilent = False
                                                            if issilent and answer:
                                                                ResultME = client.send_text(guid_sender,answer,message_id)

                            # FOR MEMBERS
                            else:
                                group_guids = {}
                                for group_guid in INFOS:
                                    nxx = ''
                                    y,x = 3,0
                                    while x < len(group_guid):
                                        nxx += group_guid[x:x+y:y]
                                        x += y
                                    group_guids[nxx] = group_guid
                                if command:
                                    for key in group_guids:
                                        if key in command:
                                            target_group = group_guids[key]
                                            SETTING_KEYS = list(INFOS[target_group]['setting'])
                                            if int(SETTING_KEYS[4]):
                                                HOWNER = INFOS[target_group]['owner']
                                                FULL_ADMINS = INFOS[target_group]['full_admins']
                                                ADMINS = INFOS[target_group]['admins']
                                                ST = INFOS[target_group]['types']
                                                channels = INFOS[target_group]['channels']
                                                if not (guid_sender == GUIDME or guid_sender in FULL_ADMINS or guid_sender in ADMINS or guid_sender == HOWNER or guid_sender == OWNER):
                                                    ResultME = False
                                                    if int(SETTING_KEYS[14]):
                                                        isok = joining(channels,target_group,guid_sender,ST['ok'],True)
                                                        if isok and isok is not True:ResultME = client.send_text(guid_sender,isok,message_id)
                                                        elif isok is False:ResultME = True
                                                    if not ResultME:
                                                        try:client.set_admin(target_group,guid_sender,[],random.choice(BoxEmoji))
                                                        except:pass
                                                        if target_group not in USERS:USERS[target_group] = {}
                                                        if guid_sender not in USERS[target_group]:getInfoUser(target_group,guid_sender)
                                                        first_name = USERS[target_group][guid_sender][2]
                                                        mess = MPro(f"کاربر @@ {first_name} @@({guid_sender}) ادمین شد. {ST['ok']}",2)
                                                        INFOS[target_group]['admins'][guid_sender] = first_name
                                                        client.send_text(target_group,mess)
                                                        baner = INFOS[target_group]['baner']
                                                        client.send_text(guid_sender,MPro(f"اد شدی. {ST['ok']}",2)+baner,message_id)

                    except:
                        #traceback.print_exc()
                        pass

                Thread(target=notif_messages,args=[update]).start()
                if OFFBOT or not canSetBio:stop_program()

            except:
                #traceback.print_exc()
                pass

    except:
        #traceback.print_exc()
        pass

limit_sleep = 1
while True:
    if limit_sleep >= 10:
        print('> sleeping 180s ...')
        time.sleep(180)
        limit_sleep = 1

    try:
        time_start = get_iran_timestamp()
        result = main()
    except:
        #traceback.print_exc()
        pass

    time.sleep(limit_sleep*2)
    print(f'> sleep for {limit_sleep*2}s " -d {get_iran_timestamp()-time_start}s')
    if get_iran_timestamp()-time_start < 60:limit_sleep += 1
    else:limit_sleep = 1
فایل ذخیره شد: bot_decode.py

[Program finished]
