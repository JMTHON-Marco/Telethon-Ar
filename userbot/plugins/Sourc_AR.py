import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, catversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "I𝐐𝐓𝐇𝐎𝐍⁦♡⁩"
CAT_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/cd27beb82e7af1aff97d2.mp4"
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "❬ تـليثون الأجنبي  - Telethon-English ، 🕸  ❭"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or " ٍَ 🖤"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"———×\n"
        cat_caption += f"**{EMOJI} ❬ ٍَ أصدار النسخـة :  ِ2.0.0  ٍَ❭**\n"
        cat_caption += f"**{EMOJI}❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**\n"
        cat_caption += f"**{EMOJI} ❬ ِحسـابك  :   {mention}  ٍ**\n"
        cat_caption += f"**{EMOJI} ❬ ٰقنـاة تليـثون  :** @UUISQ  ٍَ❭\n"
        cat_caption += f"**{EMOJI} ❬ ٰمـطور السورس : ** @H_L_5 ٍَ❭\n"
        cat_caption += f"———×"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
        f"**{CUSTOM_ALIVE_TEXT}**\n"
        f"———×\n"
        f"**{EMOJI} ❬ ٍَ أصدار النسخـة :  ِ2.0.0  ٍَ❭**\n"
        f"**{EMOJI}❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**\n"
        f"**{EMOJI} ❬ ِحسـابك  :   {mention}  ٍ**\n"
        f"**{EMOJI} ❬ ٰقنـاة تليـثون  :** @UUISQ  ٍَ❭\n"
        f"**{EMOJI} ❬ ٰمـطور السورس : ** @H_L_5 ٍَ❭\n"
        f"**{EMOJI} ❬ ٰمـطور السورس : ** @H_L_5 ٍَ❭\n"
        f"———×\n"
        )


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "لم يتم تعيين قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تعمل بنجاح"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "1": "**عدد الملف :** `1`\
      \n\n  •  **الامر : **`.alive` \
      \n  •  **يفعل : **__سيتم عرض حالة البوت__\
      "
    }
)
