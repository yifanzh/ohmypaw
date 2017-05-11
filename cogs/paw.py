import discord
from random import choice as randchoice
from discord.ext import commands

greets = ["http://imgur.com/47vI9T5", "QwQ", "=w=" , "(:з」∠)", "=A=","http://imgur.com/Y5DMDqH"]
names = {"Dragon":"爪公","Fangzhuan":"Gay砖","Baoz":"包子","Andrew":"Andrew","Givemepaw":"假小爪","hf":"贼神","ppadante":"弱鸡嫩","Cielyc":"欧皇","illidanaire":"王总","Maxxia":"Max","Vurtune":"凯总","chopperdamus":"Chopper"
,"Danker":"Danker","Miyano":"随老师","momotea":"momotea","Doombefall":"2k","Silentstorm":"Senpai","Mylei":"Emily","Zillidan":"Zach"}
dirty = ["penis","ass","丁丁","鸡","菊花","vagina","打飞机","下面"]
reply_to_dirty = ["太污了","有毒吧","你们太污了","不懂你们在说什么","我看不懂","你们有毒吧","...","哈?","啊?","妈个鸡","...","这帮傻屌..."]
gay = ["喜欢","爱","上","fuck","干","舔","插","打炮","gay","基","爽"]
reply_to_gay = ["你们这群gay","有毒吧","谁来把这人屏蔽了","...","傻逼吧","你们不要欺负我","调戏我的都是傻逼","别闹"]
suspicious = ["你们不要说我坏话","我看见了我的名字","你们在说我什么","是在叫我吗"]
who = ["gay","傻逼","汉子","妹子","丑逼","肥宅","傲娇","渣渣","女神","男神","土豪","基佬","阳痿","傻屌","武林高手","魔法少女","处男","荡妇","牛郎","AV女忧","孤儿","孙子","小屁孩","老板","大佬","穷逼","骚货","高手","交际花","单身狗"]
swear = ["傻","逼","脑残","神经","白痴","蠢","stupid","asshole","bitch"]

replies = {"Fangzhuan":["凯总，快来把方砖屏蔽了","找你的嫩嫩去","方砖太污了","这个傻屌"],
           "ppadante": ["找你的方砖去","方砖，快来管管你的嫩嫩","不要和方砖一样污"],
           "Silentstorm":["我要看senpai打炉石","ss,你的男朋友呢","ss快打炉石","SS天梯第一了吗?"],
           "momotea":["momotea,快去打文明"]}

previous = ""
reply =""
         
class Paw:
    """General commands."""
    
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        global reply
        global previous
        if message.author != self.bot.user:
            sender = message.author
            if message.content.startswith("-"):
                return
            if message.content.lower() == "hello" or message.content == "greet" or message.content == "你好":
                await self.bot.send_message(message.channel, randchoice(greets))
            elif "有人吗" in message.content or "在吗" in message.content or "在么" in message.content or "有人么" in message.content:
                await self.bot.send_message(message.channel, "我在这")
                await self.bot.send_message(message.channel, randchoice(greets))
            elif message.content.lower() == "paw" or message.content == "小爪" or message.content == "大鸡吧酱" or message.content == "弱鸡爪" or message.content == "爪" or message.content == "爪妹妹" or message.content == "爪爪":
                if sender.name in names:
                    reply += names[sender.name]
                    reply += "，叫我干啥?"
                    await self.bot.send_message(message.channel, reply)
                else:
                    await self.bot.send_message(message.channel, "我不认识你")
            elif message.content.startswith("paw") or message.content.startswith("小爪") or message.content.startswith("大鸡吧酱") or message.content.startswith("弱鸡爪") or message.content.startswith("爪"):
                badBoy = "good"
                for keyword in dirty:
                    if keyword in message.content.lower():
                        badBoy = "dirty"
                        break
                for keyword in gay:
                    if keyword in message.content.lower():
                        badBoy = "gay"
                        break
                for keyword in swear:
                    if keyword in message.content.lower():
                        badBoy = "bad"
                        break
                if "是不是" in message.content.lower():
                    if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                        reply = randchoice(list(names.values()))
                        reply += "也许是，反正我不是"
                        await self.bot.send_message(message.channel, randchoice(["不是",reply,"你才是","你在说你自己吗"]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(["是呀","嗯哼","是的","这都被你发现了","必须是","你才知道?"]))
                elif "会不会" in message.content.lower():
                    if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                        reply = randchoice(list(names.values()))
                        reply += "应该会"
                        await self.bot.send_message(message.channel, randchoice(["不会",reply,"肯定不会"]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(["会","也许吧","可能会","肯定会","看情况"]))
                elif "想不想" in message.content.lower():
                    if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                        reply = "我知道"
                        reply = randchoice(list(names.values()))
                        reply += "一定想"
                        await self.bot.send_message(message.channel, randchoice(["不想",reply,"没想过"]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(["想","(捂脸)","天天想","你猜=w="]))
                elif "谁是" in message.content.lower():
                        reply = randchoice(list(names.values()))
                        reply += "是"
                        await self.bot.send_message(message.channel, reply)
                elif badBoy == "dirty":
                    if sender.name in replies:
                        await self.bot.send_message(message.channel, randchoice(replies[sender.name]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(reply_to_dirty))
                elif badBoy == "gay":
                    if sender.name in replies:
                        await self.bot.send_message(message.channel, randchoice(replies[sender.name]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(reply_to_gay))
                elif "你是谁" in message.content:
                    await self.bot.send_message(message.channel, "我是爪妹啊")
                elif "是谁" in message.content:
                    reply += "是个"
                    reply += randchoice(who)
                    await self.bot.send_message(message.channel, reply)
                elif badBoy == "good":
                    await self.bot.send_message(message.channel, randchoice(greets))
            elif previous.lower() == "paw" or previous == "小爪" or previous == "大鸡吧酱" or previous == "弱鸡爪" or previous == "爪" or previous == "爪妹妹":
                badBoy = "good"
                for keyword in dirty:
                    if keyword in message.content.lower():
                        badBoy = "dirty"
                        break
                for keyword in gay:
                    if keyword in message.content.lower():
                        badBoy = "gay"
                        break
                for keyword in swear:
                    if keyword in message.content.lower():
                        badBoy = "bad"
                        break
                if "是不是" in message.content.lower():
                    if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                        reply = randchoice(list(names.values()))
                        reply += "也许是，反正我不是"
                        await self.bot.send_message(message.channel, randchoice(["不是",reply,"你才是","你在说你自己吗"]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(["是呀","嗯哼","是的","这都被你发现了","必须是","你才知道?"]))
                elif "会不会" in message.content.lower():
                    if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                        reply = randchoice(list(names.values()))
                        reply += "应该会"
                        await self.bot.send_message(message.channel, randchoice(["不会",reply,"肯定不会"]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(["会","也许吧","可能会","肯定会","看情况"]))
                elif "想不想" in message.content.lower():
                    if badBoy == "dirty" or badBoy == "gay" or badBoy == "bad":
                        reply = "我知道"
                        reply = randchoice(list(names.values()))
                        reply += "一定想"
                        await self.bot.send_message(message.channel, randchoice(["不想",reply,"没想过"]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(["想","(捂脸)","天天想","你猜=w="]))
                elif "谁是" in message.content.lower():
                        reply = randchoice(list(names.values()))
                        reply += "是"
                        await self.bot.send_message(message.channel, reply)
                elif badBoy == "dirty":
                    if sender.name in replies:
                        await self.bot.send_message(message.channel, randchoice(replies[sender.name]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(reply_to_dirty))
                elif badBoy == "gay":
                    if sender.name in replies:
                        await self.bot.send_message(message.channel, randchoice(replies[sender.name]))
                    else:
                        await self.bot.send_message(message.channel, randchoice(reply_to_gay))
                elif "你是谁" in message.content:
                    await self.bot.send_message(message.channel, "我是爪妹啊")
                elif "是谁" in message.content:
                    reply += "是个"
                    reply += randchoice(who)
                    await self.bot.send_message(message.channel, reply)
                elif badBoy == "good":
                    await self.bot.send_message(message.channel, randchoice(greets))
            elif "paw" in message.content.lower() or "爪" in message.content:
                await self.bot.send_message(message.channel, randchoice(suspicious))
        previous = message.content
        reply = ""
            
def setup(bot):
    bot.add_cog(Paw(bot))


