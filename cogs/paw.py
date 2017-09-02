import discord
from random import choice as randchoice
from discord.ext import commands
from .insult import Insult
import collections
from .audio import Audio
import random
from cogs.utils.dataIO import dataIO
from .utils.dataIO import fileIO
import subprocess
import os
import logging

# Uncomment following line for DEBUG logging
# logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

myName = ["paw", "小爪","大鸡吧酱","弱鸡爪","爪","爪妹"]

## Add custom replies here ##
greets = ["http://imgur.com/47vI9T5", "QwQ", "=w=" , "(:з」∠)", "=A=","http://imgur.com/Y5DMDqH", "昨天太近，明天太远，今天你有什么需要吗？"]
names = {"Dragon":"爪公","Fangzhuan":"Gay砖","Baoz":"包子","Andrew":"Andrew","Givemepaw":"假小爪","hf":"贼神","ppadante":"弱鸡嫩","Cielyc":"欧皇","illidanaire":"王总","Maxxia":"Max","Vurtune":"凯总","chopper":"Chopper"
,"Danker":"Danker","Miyano":"随老师","momotea":"momotea","Doombefall":"2k","Silentstorm":"Senpai","Mylei":"Emily","Arthies":"Zach","lm54484":"比利"}
dirty = ["penis","ass","丁丁","鸡","菊花","vagina","打飞机","下面"]
reply_to_dirty = ["太污了","有毒吧","你们太污了","不懂你们在说什么","我看不懂","你们有毒吧","...","哈?","啊?","妈个鸡","...","这帮傻屌..."]
gay = ["喜欢","爱","上","fuck","干","舔","插","打炮","gay","基","爽","操","草","艹","肏"]
reply_to_gay = ["你们这群gay","有毒吧","谁来把这人屏蔽了","...","傻逼吧","你们不要欺负我","调戏我的都是傻逼","别闹","窝要同归于尽 （举炸药包"]
suspicious = ["你们不要说我坏话","我看见了我的名字","你们在说我什么","是在叫我吗"]
who = ["gay","傻逼","汉子","妹子","丑逼","肥宅","傲娇","渣渣","女神","男神","土豪","基佬","阳痿","傻屌","武林高手","魔法少女","处男","荡妇","牛郎","AV女忧","孤儿","孙子","小屁孩","老板","大佬","穷逼","骚货","高手","交际花","单身狗"]
swear = ["傻","逼","脑残","神经","白痴","蠢","stupid","asshole","bitch","笨","呆","二","贱","sb"]
wow = ["wow","大米","魔兽","魔兽世界","公会","活动","副本","装备","橙装","地下城","raid"]
pubg = ["吃鸡","枪法","盒","跳伞","大逃杀","pubg","老阴逼","刚枪","跑毒","天命"]

feature_list = [dirty, gay, swear, wow, pubg]

replies = {"Fangzhuan":["凯总，快来把方砖屏蔽了","找你的嫩嫩去","方砖太污了","这个傻屌"],
           "ppadante": ["找你的方砖去","方砖，快来管管你的嫩嫩","不要和方砖一样污"],
           "Silentstorm":["我要看senpai打炉石","ss,你的男朋友呢","ss快打炉石","SS天梯第一了吗?"],
           "momotea":["momotea,快去打文明"]}

stories = ["你们知道公会建会成员都是谁吗？\n是Taleta(会长),Kaioolmtte,Carl,Getshot,Treebro,Joverined",
           "公会第一次组团下普通BRF,由于不够10人,只能找野人凑人数.\n第一波小怪灭了三次.\n两位野人大哥秒退，在本门口吐槽：\nYou guys raid on PEOPLE!\n后来Boss没见到，散了。",
           "公会第一次凑齐人数打本,半夜3点还没能过普通黑手.\nAeralfos太困表示坚持不住了...\n此后这人再也没上过线",
           "公会从滑大论坛招到第一名成员是Pigwannafly,后来成为了老相好.",
           "有一天，Dragon在战网好友无意看见SS在打魔兽世界.\n一顿安利之后，成功拉进了公会.\n从此公会蒸蒸日上.",
           "公会从野人招到了第一名成员是Raygulus.\n神马，你们不知道他是谁？\n把想成他是N总的初恋就好.",
           "公会成立时间是2015年6月23日.",
           "公会里招募到的唯一奥山土著人民是Zach.",
           "15年圣诞前夕决定开始正式招募野人,并在同一天，陆续招募到了小爪和Zach等。以下为招募对话:\n\"你打炉石吗\"\n\"打\"\n\"知道Silentstorm是谁吗，他在我们公会.\"\n\"卧槽,你们在哪个服务器,我来了.\"",
           "2016年1月17日,公会第一次凑齐人数开荒M.",
           "Andrew是Zach的真机(基)友.中间还隔个妹子.",
           "2000哥的名字是从一张王八的账单而来",
           "公会第一代巫妖王是战神哥，之后方砖顺利上位.",
           "有一次分配装备的时候,Dragon问Emily为什么不要披风.\nEmily说:我有更好的\n众人不信,随后一看,披风上一行小字:\nMade by Crazystorm.",
           "刚开始Emily来打团的时候还是单身,众人在teamspeak调侃ss,Dragon问了一句:开组了,你的妹子呢?\nEmily:我在呢..."]

## Add voice messages here ##
voice_greet = ["greet1","greet2"]
voice_amazed = ["amazed1","amazed2","amazed3"]
voice_angry = ["angry1","angry2","angry3","angry4","angry5","angry6"]
voice_chicken = ["chicken1","chicken2","chicken3","chicken4","chicken5","chicken6","chicken7","chicken8","chicken9"]
voice_cute = ["cute1","cute2"]
voice_dontcare = ["dontcare1"]
voice_game = ["game1","game2","game3","game4","game5","game6","game7","game8","game9","game10","game11"]
voice_laugh = ["laugh1","laugh2"]
voice_no = ["no1"]
voice_question = ["question1","question2","question3","question4","question5","question6"]
voice_raid = ["raid1","raid2","raid3","raid4","raid5","raid6","raid7"]
voice_random = ["random1","random2","random3","random4"]
voice_sad = ["sad1"]
voice_speechless = ["speechless1"]

voice_to_individual = {"Arthies":["zach1"],
                       "ppadante":["nennen1"],
                       "momotea":["momotea1"],
                       "Vurtune":["kaizong1"],
                       "Dragon":["dragon1"],
                       "Baoz":["baozi1"]}

voice_list = [voice_greet, voice_amazed, voice_angry, voice_chicken, voice_cute, voice_dontcare, voice_game,
              voice_laugh, voice_no, voice_question, voice_raid, voice_random, voice_sad, voice_speechless]
response1 = [voice_angry]
response2 = [voice_angry, voice_sad, voice_dontcare]
response3 = [voice_cute, voice_sad, voice_speechless, voice_laugh]
response4 = [voice_raid, voice_game]
response5 = [voice_chicken, voice_game]
response_list = [response1, response2, response3, response4, response5]
                       
previous = ""
reply =""
    
class Paw:
    """General commands."""
    
    def __init__(self, bot):
        self.bot = bot
        self.lick = None
        self.insult = None

    def parse_message(self, content=""):
        log.debug("Parsing message: " + content)
        feature_id = 0
        for fidx, feature in enumerate(feature_list):
            for keyidx, keyword in enumerate(feature):
                if keyword in content:
                    if feature_id == 0:
                        feature_id = fidx
                    break
        resp = random.choice(response_list[feature_id])
        resp1 = resp[random.randint(0, len(resp)-1)]
        resp2 = "lickpaw/" + resp1 + ".mp3"
        log.debug("Parsing message: respond with " + resp2)
        return resp2


    async def on_message(self, message):
        global reply
        global previous
        content = message.content
        content_all = "".join(content)
        log.debug(content_all)

        self.initImportedCogs()

        if message.author == self.bot.user:
            return

        if previous != "" and previous.author != self.bot.user:
            log.debug("Previous = " + previous.content)
            if previous.content.lower() in myName or previous.content in myName:
                content = "paw" + content
                log.debug("Name heard, query is: " + content)

        sender = message.author
        if content.startswith("-"):
            return
        if content.lower() == "hello" or content == "greet" or content == "你好":
            await self.bot.send_message(message.channel, randchoice(greets))
            await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_greet)))
        elif "有人吗" in content or "在吗" in content or "在么" in content or "有人么" in content:
            await self.bot.send_message(message.channel, "我在这")
            await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_greet)))
        elif content.lower() == "paw" or content == "小爪" or content == "大鸡吧酱" or content == "弱鸡爪" or content == "爪" or content == "爪妹" or content == "爪爪":
            if sender.name in names:
                reply += names[sender.name]
                reply += "，叫我干啥?"
                if sender.name in voice_to_individual:
                    await self.bot.send_message(message.channel, reply)
                    await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_to_individual[sender.name])))
                else:
                    await self.bot.send_message(message.channel, reply)
                    await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_greet)))
            else:
                await self.bot.send_message(message.channel, "我不认识你")
        elif content.startswith("paw") or content.startswith("小爪") or content.startswith("大鸡吧酱") or content.startswith("弱鸡爪") or content.startswith("爪"):
            badBoy = "good"
            for keyword in dirty:
                if keyword in content.lower():
                    badBoy = "dirty"
                    break
            for keyword in gay:
                if keyword in content.lower():
                    badBoy = "gay"
                    break
            for keyword in swear:
                if keyword in content.lower():
                    badBoy = "bad"
                    break
            if "奶" in content:
                await self.bot.send_message(message.channel, "奶奶奶。。。奶死你！！！")
            if "干吗" in content.lower():
                await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_random)))
            if "我要听故事" in content.lower():
                await self.bot.send_message(message.channel, randchoice(stories))
            if "声音" in content.lower():
                await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_question)))
            elif "是不是" in content.lower() or ("是" in content.lower() and ("吗" in content.lower() or "么" in content.lower())):
                if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                    reply = randchoice(list(names.values()))
                    reply += "也许是，反正我不是"
                    await self.bot.send_message(message.channel, randchoice(["不是",reply,"你才是","你在说你自己吗"]))
                else:
                    await self.bot.send_message(message.channel, randchoice(["是呀","嗯哼","是的","这都被你发现了","必须是","你才知道?"]))
            elif "会不会" in content.lower() or ("会" in content.lower() and ("吗" in content.lower() or "么" in content.lower())):
                if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                    reply = randchoice(list(names.values()))
                    reply += "应该会"
                    await self.bot.send_message(message.channel, randchoice(["不会",reply,"肯定不会"]))
                else:
                    await self.bot.send_message(message.channel, randchoice(["会","也许吧","可能会","肯定会","看情况"]))
            elif "想不想" in content.lower() or ("想" in content.lower() and ("吗" in content.lower() or "么" in content.lower())):
                if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                    reply = "我知道"
                    reply = randchoice(list(names.values()))
                    reply += "一定想"
                    await self.bot.send_message(message.channel, randchoice(["不想",reply,"没想过"]))
                else:
                    await self.bot.send_message(message.channel, randchoice(["想","(捂脸)","天天想","你猜=w="]))
            elif "谁是" in content.lower():
                    reply = randchoice(list(names.values()))
                    reply += "是"
                    await self.bot.send_message(message.channel, reply)
                    await self.lick.lick_paw(message, "lickpaw/{}.mp3".format(randchoice(voice_laugh)))
            elif "你是谁" in content:
                await self.bot.send_message(message.channel, "我是爪妹啊")
            elif "是谁" in content:
                reply += "是个"
                reply += randchoice(who)
                await self.bot.send_message(message.channel, reply)
            else:
                reply_filename = self.parse_message(content_all)
                await self.lick.lick_paw(message, reply_filename)
        elif "paw" in content.lower() or "爪" in content:
            reply_filename = self.parse_message(content_all)
            await self.lick.lick_paw(message, reply_filename)
   
        previous = message    
        reply = ""

    def initImportedCogs(self):
        if self.lick is None:
            log.info("setting lick cog")
            self.lick = self.bot.get_cog("Audio")
        if self.insult is None:
            log.info("setting insult cog")
            self.insult = self.bot.get_cog("Insult")
            
def setup(bot):
    bot.add_cog(Paw(bot))


