#!/usr/bin/env python3
class WZMLStyle:
    #  async def start(client, message) ---> __main__.py
    ST_BN1_NAME = "Owner"
    ST_BN1_URL = "https://t.me/V_Sbotmaker"
    ST_BN2_NAME = "Updates"
    ST_BN2_URL = "https://t.me/Animeworld_zone"
    ST_MSG = """<b><i>ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ᴍɪʀʀᴏʀ ᴀʟʟ ʏᴏᴜʀ ʟɪɴᴋs|ғɪʟᴇs|ᴛᴏʀʀᴇɴᴛs ᴛᴏ ɢᴏᴏɢʟᴇ ᴅʀɪᴠᴇ ᴏʀ ᴀɴʏ ʀᴄʟᴏɴᴇ ᴄʟᴏᴜᴅ ᴏʀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴏʀ ᴛᴏ ᴅᴅʟ sᴇʀᴠᴇʀs.</i></b>
<b><i>ᴛʏᴘᴇ {help_command} ᴛᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs</i></b>"""
    ST_BOTPM = """<b><i>ɴᴏᴡ, ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ᴀʟʟ ʏᴏᴜʀ ғɪʟᴇs ᴀɴᴅ ʟɪɴᴋs ʜᴇʀᴇ. sᴛᴀʀᴛ ᴜsɪɴɢ ...</i></b>"""
    ST_UNAUTH = """<b><i>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀ! ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ WZML-X ᴍɪʀʀᴏʀ-ʟᴇᴇᴄʜ ʙᴏᴛ</i></b>"""
    OWN_TOKEN_GENERATE = (
        """<b><i>ᴛᴇᴍᴘᴏʀᴀʀʏ ᴛᴏᴋᴇɴ ɪs ɴᴏᴛ ʏᴏᴜʀs!</i></b>\n\n<b><i>ᴋɪɴᴅʟʏ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ.</i></b>"""
    )
    USED_TOKEN = (
        """<b><i>ᴛᴇᴍᴘᴏʀᴀʀʏ ᴛᴏᴋᴇɴ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ!</i></b>\n\n<b><i>ᴋɪɴᴅʟʏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ɴᴇᴡ ᴏɴᴇ.</i></b>"""
    )
    LOGGED_PASSWORD = """<b><i>ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ʟᴏɢɢᴇᴅ ɪɴ ᴠɪᴀ ᴘᴀssᴡᴏʀᴅ</i></b>\n\n<b><i>ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴀᴄᴄᴇᴘᴛ ᴛᴇᴍᴘ ᴛᴏᴋᴇɴs.</i></b>"""
    ACTIVATE_BUTTON = "<b><i>ᴀᴄᴛɪᴠᴀᴛᴇ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴛᴏᴋᴇɴ</i></b>"
    TOKEN_MSG = """<b><i><u>ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛᴇᴍᴘᴏʀᴀʀʏ ʟᴏɢɪɴ ᴛᴏᴋᴇɴ!</u></i></b>
<b><i>ᴛᴇᴍᴘ ᴛᴏᴋᴇɴ:</i></b> <code>{token}</code>
<b><i>ᴠᴀʟɪᴅɪᴛʏ:</i></b> {validity}"""
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = "<b><i>✅️ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅</i></b>"
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = "<b><i>ᴀʟʀᴇᴀᴅʏ ʙᴏᴛ ʟᴏɢɪɴ ɪɴ!</i></b>"
    INVALID_PASS = "<b><i>ɪɴᴠᴀʟɪᴅ ᴘᴀssᴡᴏʀᴅ!</i></b>\n\n<b><i>ᴋɪɴᴅʟʏ ᴘᴜᴛ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴘᴀssᴡᴏʀᴅ.</i></b>"
    PASS_LOGGED = "<b><i>ʙᴏᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟᴏɢɪɴ sᴜᴄᴄᴇssғᴜʟʟʏ!</i></b>"
    LOGIN_USED = "<b><i>ʙᴏᴛ ʟᴏɢɪɴ ᴜsᴀɢᴇ:</i></b>\n\n<code>/cmd [password]</code>"
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = "<b><i>📑 ʟᴏɢ ᴅɪsᴘʟᴀʏ</i></b>"
    WEB_PASTE_BT = "<b><i>📨 ᴡᴇʙ ᴘᴀsᴛᴇ (SB)</i></b>"
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = "<b><i>ʙᴀsɪᴄ</i></b>"
    USER_BT = "<b><i>ᴜsᴇʀs</i></b>"
    MICS_BT = "<b><i>ᴍɪᴄs</i></b>"
    O_S_BT = "<b><i>ᴏᴡɴᴇʀ & sᴜᴅᴏs</i></b>"
    CLOSE_BT = "<b><i>ᴄʟᴏsᴇ</i></b>"
    HELP_HEADER = "<b><i>㊂ ʜᴇʟᴘ ɢᴜɪᴅᴇ ᴍᴇɴᴜ!</i></b>\n\n<b><i>ɴᴏᴛᴇ: ᴄʟɪᴄᴋ ᴏɴ ᴀɴʏ ᴄᴍᴅ ᴛᴏ sᴇᴇ ᴍᴏʀᴇ ᴍɪɴᴏʀ ᴅᴇᴛᴀɪʟs.</i></b>"

    # async def stats(client, message):
    BOT_STATS = """<b><i>⌬ ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs :</i></b>
┖ <b><i>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :</i></b> {bot_uptime}

<b><i>┎ ʀᴀᴍ ( ᴍᴇᴍᴏʀʏ ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b><i>ᴜ :</i></b> {ram_u} | <b><i>ғ :</i></b> {ram_f} | <b><i>ᴛ :</i></b> {ram_t}

<b><i>┎ sᴡᴀᴘ ᴍᴇᴍᴏʀʏ :</i></b>
┃ {swap_bar} {swap}%
┖ <b><i>ᴜ :</i></b> {swap_u} | <b><i>ғ :</i></b> {swap_f} | <b><i>ᴛ :</i></b> {swap_t}

<b><i>┎ ᴅɪsᴋ :</i></b>
┃ {disk_bar} {disk}%
┃ <b><i>ᴛᴏᴛᴀʟ ᴅɪsᴋ ʀᴇᴀᴅ :</i></b> {disk_read}
┃ <b><i>ᴛᴏᴛᴀʟ ᴅɪsᴋ ᴡʀɪᴛᴇ :</i></b> {disk_write}
┖ <b><i>ᴜ :</i></b> {disk_u} | <b><i>ғ :</i></b> {disk_f} | <b><i>ᴛ :</i></b> {disk_t}
    """
    SYS_STATS = """<blockquote><b><i>⌬ ᴏs sʏsᴛᴇᴍ :</i></b>
┠ <b><i>ᴏs ᴜᴘᴛɪᴍᴇ :</i></b> {os_uptime}
┠ <b><i>ᴏs ᴠᴇʀsɪᴏɴ :</i></b> {os_version}
┖ <b><i>ᴏs ᴀʀᴄʜ :</i></b> {os_arch}</blockquote>

<blockquote><b><i>⌬ ɴᴇᴛᴡᴏʀᴋ sᴛᴀᴛs :</i></b>
┠ <b><i>ᴜᴘʟᴏᴀᴅ ᴅᴀᴛᴀ:</i></b> {up_data}
┠ <b><i>ᴅᴏᴡɴʟᴏᴀᴅ ᴅᴀᴛᴀ:</i></b> {dl_data}
┠ <b><i>ᴘᴋᴛs sᴇɴᴛ:</i></b> {pkt_sent}k
┠ <b><i>ᴘᴋᴛs ʀᴇᴄᴇɪᴠᴇᴅ:</i></b> {pkt_recv}k
┖ <b><i>ᴛᴏᴛᴀʟ ɪ/ᴏ ᴅᴀᴛᴀ:</i></b> {tl_data}</blockquote>

<blockquote><b><i>┎ ᴄᴘᴜ :</i></b>
┃ {cpu_bar} {cpu}%
┠ <b><i>ᴄᴘᴜ ғʀᴇQᴜᴇɴᴄʏ :</i></b> {cpu_freq}
┠ <b><i>sʏsᴛᴇᴍ ᴀᴠɢ ʟᴏᴀᴅ :</i></b> {sys_load}
┠ <b><i>ᴘ-ᴄᴏʀᴇ(s) :</i></b> {p_core} | <b><i>ᴠ-ᴄᴏʀᴇ(s) :</i></b> {v_core}
┠ <b><i>ᴛᴏᴛᴀʟ ᴄᴏʀᴇ(s) :</i></b> {total_core}
┖ <b><i>ᴜsᴀʙʟᴇ ᴄᴘᴜ(s) :</i></b> {cpu_use}
   </blockquote> """
    REPO_STATS = """<b><i>⌬ ʀᴇᴘᴏ sᴛᴀᴛɪsᴛɪᴄs :</i></b>
┠ <b><i>ʙᴏᴛ ᴜᴘᴅᴀᴛᴇᴅ :</i></b> {last_commit}
┠ <b><i>ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ :</i></b> {bot_version}
┠ <b><i>ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ :</i></b> {lat_version}
┖ <b><i>ʟᴀsᴛ ᴄʜᴀɴɢᴇʟᴏɢ :</i></b> {commit_details}

<b><i>⌬ ʀᴇᴍᴀʀᴋs :</i></b> <code>{remarks}</code>
    """
    BOT_LIMITS = """<blockquote><b><i>⌬ ʙᴏᴛ ʟɪᴍɪᴛᴀᴛɪᴏɴs :</i></b>
┠ <b><i>ᴅɪʀᴇᴄᴛ ʟɪᴍɪᴛ :</i></b> {DL} GB
┠ <b><i>ᴛᴏʀʀᴇɴᴛ ʟɪᴍɪᴛ :</i></b> {TL} GB
┠ <b><i>ɢᴅʀɪᴠᴇ ʟɪᴍɪᴛ :</i></b> {GL} GB
┠ <b><i>ʏᴛ-ᴅʟᴘ ʟɪᴍɪᴛ :</i></b> {YL} GB
┠ <b><i>ᴘʟᴀʏʟɪsᴛ ʟɪᴍɪᴛ :</i></b> {PL}
┠ <b><i>ᴍᴇɢᴀ ʟɪᴍɪᴛ :</i></b> {ML} GB
┠ <b><i>ᴄʟᴏɴᴇ ʟɪᴍɪᴛ :</i></b> {CL} GB
┖ <b><i>ʟᴇᴇᴄʜ ʟɪᴍɪᴛ :</i></b> {LL} GB</blockquote>

<blockquote><b><i>┎ ᴛᴏᴋᴇɴ ᴠᴀʟɪᴅɪᴛʏ :</i></b> {TV}
┠ <b><i>ᴜsᴇʀ ᴛɪᴍᴇ ʟɪᴍɪᴛ :</i></b> {UTI} / task
┠ <b><i>ᴜsᴇʀ ᴘᴀʀᴀʟʟᴇʟ ᴛᴀsᴋs :</i></b> {UT}
┖ <b><i>ʙᴏᴛ ᴘᴀʀᴀʟʟᴇʟ ᴛᴀsᴋs :</i></b> {BT}
    <blockquote>"""
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = "<b><i>ʀᴇsᴛᴀʀᴛɪɴɢ...</i></b>"
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = """<blockquote><b><i>⌬ ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!</i></b>
┠ <b><i>ᴅᴀᴛᴇ:</i></b> {date}
┠ <b><i>ᴛɪᴍᴇ:</i></b> {time}
┠ <b><i>ᴛɪᴍᴇᴢᴏɴᴇ:</i></b> {timz}
┖ <b><i>ᴠᴇʀsɪᴏɴ:</i></b> {version}<blockquote>"""
    RESTARTED = """<b><i>⌬ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ!</i></b>"""
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = "<b><i>sᴛᴀʀᴛɪɴɢ ᴘɪɴɢ..</i></b>"
    PING_VALUE = "<b><i>ᴘᴏɴɢ</i></b>\n<code>{value} ms..</code>"
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ</i></b>
┠ <b><i>ᴍᴏᴅᴇ:</i></b> {Mode}
┖ <b><i>ʙʏ:</i></b> {Tag}\n\n"""
    LINKS_SOURCE = """<b><i>➲ sᴏᴜʀᴄᴇ:</i></b>
┖ <b><i>ᴀᴅᴅᴇᴅ ᴏɴ:</i></b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "<b><i>➲ ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ :</i></b>\n┃\n┖ <b><i>ʟɪɴᴋ:</i></b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START = "<b><i>➲ ʟᴇᴇᴄʜ sᴛᴀʀᴛᴇᴅ :</i></b>\n┃\n┠ <b><i>ᴜsᴇʀ :</i></b> {mention} ( #ID{uid} )\n┖ <b><i>sᴏᴜʀᴄᴇ :</i></b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME = "<b><i>{Name}</i></b>\n┃\n"
    SIZE = "<b><i>┠ sɪᴢᴇ: </i></b>{Size}\n"
    ELAPSE = "<b><i>┠ ᴇʟᴀᴘsᴇᴅ: </i></b>{Time}\n"
    MODE = "<b><i>┠ ᴍᴏᴅᴇ: </i></b>{Mode}\n"

    # ----- LEECH -------
    L_TOTAL_FILES = "<b><i>┠ ᴛᴏᴛᴀʟ ғɪʟᴇs: </i></b>{Files}\n"
    L_CORRUPTED_FILES = "<b><i>┠ ᴄᴏʀʀᴜᴘᴛᴇᴅ ғɪʟᴇs: </i></b>{Corrupt}\n"
    L_CC = "<b><i>┖ ʙʏ: </i></b>{Tag}\n\n"
    PM_BOT_MSG = "<b><i>➲ ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴀʙᴏᴠᴇ</i></b>"
    L_BOT_MSG = "<b><i>➲ ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</i></b>"
    L_LL_MSG = "<b><i>➲ ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇss ᴠɪᴀ ʟɪɴᴋs...</i></b>\n"

    # ----- MIRROR -------
    M_TYPE = "<b><i>┠ ᴛʏᴘᴇ: </i></b>{Mimetype}\n"
    M_SUBFOLD = "<b><i>┠ sᴜʙғᴏʟᴅᴇʀs: </i></b>{Folder}\n"
    TOTAL_FILES = "<b><i>┠ ғɪʟᴇs: </i></b>{Files}\n"
    RCPATH = "<b><i>┠ ᴘᴀᴛʜ: </i></b><code>{RCpath}</code>\n"
    M_CC = "<b><i>┖ ʙʏ: </i></b>{Tag}\n\n"
    M_BOT_MSG = "<b><i>➲ ʟɪɴᴋ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</i></b>"
    # ----- BUTTONS -------
    CLOUD_LINK = "☁️ ᴄʟᴏᴜᴅ ʟɪɴᴋ"
    SAVE_MSG = "📨 sᴀᴠᴇ ᴍᴇssᴀɢᴇ"
    RCLONE_LINK = "♻️ ʀᴄʟᴏɴᴇ ʟɪɴᴋ"
    DDL_LINK = "📎 {Serv} ʟɪɴᴋ"
    SOURCE_URL = "🔐 sᴏᴜʀᴄᴇ ʟɪɴᴋ"
    INDEX_LINK_F = "🗂 ɪɴᴅᴇx ʟɪɴᴋ"
    INDEX_LINK_D = "⚡ ɪɴᴅᴇx ʟɪɴᴋ"
    VIEW_LINK = "🌐 ᴠɪᴇᴡ ʟɪɴᴋ"
    CHECK_PM = "📥 ᴠɪᴇᴡ ɪɴ ʙᴏᴛ ᴘᴍ"
    CHECK_LL = "<🖇 ᴠɪᴇᴡ ɪɴ ʟɪɴᴋs ʟᴏɢ"
    MEDIAINFO_LINK = "📃 ᴍᴇᴅɪᴀɪɴғᴏ"
    SCREENSHOTS = "🖼 sᴄʀᴇᴇɴsʜᴏᴛs"
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME = "<b><i>{Name}</i></b>"

    #####---------PROGRESSIVE STATUS-------
    BAR = "\n┏━━❪ Animeworld 💜❫━━━✘\n┃ <blockquote>{Bar}</blockquote>"
    PROCESSED = "\n┠ <b><i>ᴘʀᴏᴄᴇssᴇᴅ:</i></b> {Processed}"
    STATUS = '\n┠ <b><i>sᴛᴀᴛᴜs:</i></b> <a href="{Url}">{Status}</a>'
    ETA = "| <b><i> ᴇᴛᴀ:</i></b> {Eta}"
    SPEED = "\n┠ <b><i>sᴘᴇᴇᴅ:</i></b> {Speed}"
    ELAPSED = " | <b><i>ᴇʟᴀᴘsᴇᴅ:</i></b> {Elapsed}"
    ENGINE = "\n┠ <b><i>ᴇɴɢɪɴᴇ:</i></b> {Engine}"
    STA_MODE = "\n┠ <b><i>ᴍᴏᴅᴇ:</i></b> {Mode}"
    SEEDERS = "\n┠ <b><i>sᴇᴇᴅᴇʀs:</i></b> {Seeders} | "
    LEECHERS = "<b><i>ʟᴇᴇᴄʜᴇʀs:</i></b> {Leechers}"

    ####--------SEEDING----------
    SEED_SIZE = "<b><i>\n┠ sɪᴢᴇ: </i></b>{Size}"
    SEED_SPEED = "<b><i>\n┠ sᴘᴇᴇᴅ: </i></b> {Speed} | "
    UPLOADED = "<b><i>ᴜᴘʟᴏᴀᴅᴇᴅ: </i></b> {Upload}"
    RATIO = "<b><i>ʀᴀᴛɪᴏ: </i></b> {Ratio} | "
    TIME = "<b><i>ᴛɪᴍᴇ: </i></b> {Time}"
    SEED_ENGINE = "<b><i>\n┠ ᴇɴɢɪɴᴇ:</i></b> {Engine}"

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE = "<b><i>\n┠ sɪᴢᴇ: </i></b>{Size}"
    NON_ENGINE = "<b><i>\n┠ ᴇɴɢɪɴᴇ:</i></b> {Engine}"

    ####--------OVERALL MSG FOOTER----------
    USER = "<b><i>\n┠ ᴜsᴇʀ:</i></b> <code>{User}</code> | "
    ID = "<b><i>ɪᴅ:</i></b> <code>{Id}</code>"
    BTSEL = "<b><i>\n┠ sᴇʟᴇᴄᴛ:</i></b> {Btsel}"
    CANCEL = "<b><i>\n┖ {Cancel}\n\n</i></b>"

    ####------FOOTER--------
    FOOTER = "╭───────✦✧✦──────✘\n ⌬ <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>"
    TASKS = "<b><i>┠ ᴛᴀsᴋs:</i></b> {Tasks}\n"
    BOT_TASKS = "<b><i>┠ ᴛᴀsᴋs:</i></b> {Tasks}/{Ttask} | <b><i>ᴀᴠʟ:</i></b> {Free}\n"
    Cpu = "<b><i>┠ ᴄᴘᴜ:</i></b> {cpu}% | "
    FREE = "<b><i>ғ:</i></b> {free} [{free_p}%]"
    Ram = "<b><i>\n┠ ʀᴀᴍ:</i></b> {ram}% | "
    uptime = "<b><i>ᴜᴘᴛɪᴍᴇ:</i></b> {uptime}"
    DL = "<b><i>\n┠ ᴅʟ:</i></b> {DL}/s | "
    UL = "<b><i>ᴜʟ:</i></b> {UL}/s\n╰───────✦✧✦──────✘"

    ###--------BUTTONS-------
    PREVIOUS = "⫷"
    REFRESH = "ᴘᴀɢᴇs\n{Page}"
    NEXT = "⫸"
    # ---------------------

    # STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = (
        "<b><i>ғɪʟᴇ/ғᴏʟᴅᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅʀɪᴠᴇ.</i></b>\n<b><i>ʜᴇʀᴇ ᴀʀᴇ {content} ʟɪsᴛ ʀᴇsᴜʟᴛs:</i></b>"
    )
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = "<b><i>ᴄᴏᴜɴᴛɪɴɢ:</i></b> <code>{LINK}</code>"
    COUNT_NAME = "<b><i>{COUNT_NAME}</i></b>\n┃\n"
    COUNT_SIZE = "<b><i>┠ sɪᴢᴇ: </i></b>{COUNT_SIZE}\n"
    COUNT_TYPE = "<b><i>┠ ᴛʏᴘᴇ: </i></b>{COUNT_TYPE}\n"
    COUNT_SUB = "<b><i>┠ sᴜʙғᴏʟᴅᴇʀs: </i></b>{COUNT_SUB}\n"
    COUNT_FILE = "<b><i>┠ ғɪʟᴇs: </i></b>{COUNT_FILE}\n"
    COUNT_CC = "<b><i>┖ ʙʏ: </i></b>{COUNT_CC}\n"
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = "<b><i>sᴇᴀʀᴄʜɪɴɢ ғᴏʀ {NAME}</i></b>"
    LIST_FOUND = "<b><i>ғᴏᴜɴᴅ {NO} ʀᴇsᴜʟᴛ ғᴏʀ {NAME}</i></b>"
    LIST_NOT_FOUND = "<b><i>ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ {NAME}</i></b>"
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = """<blockquote><b><i>ɴᴏ ᴀᴄᴛɪᴠᴇ ᴅᴏᴡɴʟᴏᴀᴅs!</i></b>
    
<b><i>⌬ ʙᴏᴛ sᴛᴀᴛs</i></b>
┠ <b><i>ᴄᴘᴜ:</i></b> {cpu}% | <b><i>ғ:</i></b> {free} [{free_p}%]
┖ <b><i>ʀᴀᴍ:</i></b> {ram} | <b><i>ᴜᴘᴛɪᴍᴇ:</i></b> {uptime}
    </blockquote>"""
    # ---------------------

    # USER Setting --> user_setting.py
    USER_SETTING = """╭───────✦✧✦───────✘ 
<blockquote><b><i>㊂ ᴜsᴇʀ sᴇᴛᴛɪɴɢs :</i></b>
        
┎ <b><i>ɴᴀᴍᴇ :</i></b> {NAME} ( <code>{ID}</code> )
┠ <b><i>ᴜsᴇʀɴᴀᴍᴇ :</i></b> {USERNAME}
┠ <b><i>ᴛᴇʟᴇɢʀᴀᴍ ᴅᴄ :</i></b> {DC}
┠ <b><i>ʟᴀɴɢᴜᴀɢᴇ :</i></b> {LANG}</blockquote>
╰───────✦✧✦───────✘

<b><i>➲ ᴀᴠᴀɪʟᴀʙʟᴇ ᴀʀɢs:</i></b>
• <b>-s</b> or <b>-set</b>: <b><i>sᴇᴛ ᴅɪʀᴇᴄᴛʟʏ ᴠɪᴀ ᴀʀɢ</i></b>"""


    UNIVERSAL = """╭───────✦✧✦──────✘ 
    <b><i>㊂ ᴜɴɪᴠᴇʀsᴀʟ sᴇᴛᴛɪɴɢs : {NAME}</i></b>

┎<b><i> ʏᴛ-ᴅʟᴘ ᴏᴘᴛɪᴏɴs :</i></b> <b><code>{YT}</code></b>
┠<b><i> ᴅᴀɪʟʏ ᴛᴀsᴋs :</i></b> <code>{DT}</code> per day
┠<b><i> ʟᴀsᴛ ʙᴏᴛ ᴜsᴇᴅ :</i></b> <code>{LAST_USED}</code>
┠<b><i> ᴜsᴇʀ sᴇssɪᴏɴ :</i></b> <code>{USESS}</code>
┠<b><i> ᴍᴇᴅɪᴀɪɴғᴏ ᴍᴏᴅᴇ :</i></b> <code>{MEDIAINFO}</code>
┠<b><i> sᴀᴠᴇ ᴍᴏᴅᴇ :</i></b> <code>{SAVE_MODE}</code>
┠<b><i> ᴜsᴇʀ ʙᴏᴛ ᴘᴍ :</i></b> <code>{BOT_PM}</code>
╰───────✦✧✦──────✘"""

    MIRROR = """╭───────✦✧✦──────✘ 
    <b><i>㊂ ᴍɪʀʀᴏʀ/ᴄʟᴏɴᴇ sᴇᴛᴛɪɴɢs : {NAME}</i></b>

┎<b><i> ʀᴄʟᴏɴᴇ ᴄᴏɴғɪɢ :</i></b> <i>{RCLONE}</i>
┠<b><i> ᴍɪʀʀᴏʀ ᴘʀᴇғɪx :</i></b> <code>{MPREFIX}</code>
┠<b><i> ᴍɪʀʀᴏʀ sᴜғғɪx :</i></b> <code>{MSUFFIX}</code>
┠<b><i> ᴍɪʀʀᴏʀ ʀᴇᴍɴᴀᴍᴇ :</i></b> <code>{MREMNAME}</code>
┠<b><i> ᴅᴅʟ sᴇʀᴠᴇʀ(s) :</i></b> <i>{DDL_SERVER}</i>
┠<b><i> ᴜsᴇʀ ᴛᴅ ᴍᴏᴅᴇ :</i></b> <i>{TMODE}</i>
┠<b><i> ᴛᴏᴛᴀʟ ᴜsᴇʀ ᴛᴅ(s) :</i></b> <i>{USERTD}</i>
┠<b><i> ᴅᴀɪʟʏ ᴍɪʀʀᴏʀ :</i></b> <code>{DM}</code> per day
╰───────✦✧✦──────✘"""

    LEECH = """╭───────✦✧✦──────✘
    <b><i>㊂ ʟᴇᴇᴄʜ sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</i></b>

┎<b><i> ᴅᴀɪʟʏ ʟᴇᴇᴄʜ : </i></b><code>{DL}</code> per day
┠<b><i> ʟᴇᴇᴄʜ ᴛʏᴘᴇ :</i></b> <i>{LTYPE}</i>
┠<b><i> ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ :</i></b> <i>{THUMB}</i>
┠<b><i> ʟᴇᴇᴄʜ sᴘʟɪᴛ sɪᴢᴇ :</i></b> <code>{SPLIT_SIZE}</code>
┠<b><i> ᴇQᴜᴀʟ sᴘʟɪᴛs :</i></b> <i>{EQUAL_SPLIT}</i>
┠<b><i> ᴍᴇᴅɪᴀ ɢʀᴏᴜᴘ :</i></b> <i>{MEDIA_GROUP}</i>
┠<b><i> ʟᴇᴇᴄʜ ᴄᴀᴘᴛɪᴏɴ :</i></b> <code>{LCAPTION}</code>
┠<b><i> ʟᴇᴇᴄʜ ᴘʀᴇғɪx :</i></b> <code>{LPREFIX}</code>
┠<b><i> ʟᴇᴇᴄʜ sᴜғғɪx :</i></b> <code>{LSUFFIX}</code>
┠<b><i> ʟᴇᴇᴄʜ ᴅᴜᴍᴘs :</i></b> <code>{LDUMP}</code>
┠<b><i> ʟᴇᴇᴄʜ ʀᴇᴍɴᴀᴍᴇ :</i></b> <code>{LREMNAME}</code>
┖<b><i> ʟᴇᴇᴄʜ ᴍᴇᴛᴀᴅᴀᴛᴀ :</i></b> <code>{LMETA}</code>
╰───────✦✧✦──────✘"""
