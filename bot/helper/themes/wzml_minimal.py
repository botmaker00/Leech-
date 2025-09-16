#!/usr/bin/env python3

class WZMLStyle:
    """
    WZMLStyle class for defining styled messages and buttons for the WZML-X Mirror-Leech Bot.
    Emojis and formatting have been added for better readability and user engagement.
    """

    # === Bot Information ===
    ST_BN1_NAME = "Owner 👤"
    ST_BN1_URL = "https://t.me/V_Sbotmaker"
    ST_BN2_NAME = "Updates 📢"
    ST_BN2_URL = "https://t.me/Animeworld_zone"

    # === Start Messages ===
    ST_MSG = """
    <b><i>🚀 This bot can mirror all your links, files, and torrents to Google Drive, any Rclone cloud, Telegram, or DDL servers! 🌐</i></b>
    <b><i>📝 Type <code>{help_command}</code> to get a list of available commands.</i></b>
    """
    ST_BOTPM = """
    <b><i>📬 Now, this bot will send all your files and links here. Start using it! 🚀</i></b>
    """
    ST_UNAUTH = """
    <b><i>🚫 You are not an authorized user! Please deploy your own WZML-X Mirror-Leech Bot.</i></b>
    """

    # === Token Messages ===
    OWN_TOKEN_GENERATE = """
    <b><i>🔑 Temporary token is not yours!</i></b>
    <b><i>📌 Kindly generate your own.</i></b>
    """
    USED_TOKEN = """
    <b><i>🔑 Temporary token already used!</i></b>
    <b><i>📌 Kindly generate a new one.</i></b>
    """
    LOGGED_PASSWORD = """
    <b><i>🔒 Bot already logged in via password.</i></b>
    <b><i>📌 No need to accept temporary tokens.</i></b>
    """
    ACTIVATE_BUTTON = "<b><i>🔓 Activate Temporary Token</i></b>"
    TOKEN_MSG = """
    <b><i><u>🔑 Generated Temporary Login Token!</u></i></b>
    <b><i>🔐 Temp Token:</i></b> <code>{token}</code>
    <b><i>⏳ Validity:</i></b> {validity}
    """

    # === Token Callback ===
    ACTIVATED = "<b><i>✅ Activated Successfully!</i></b>"

    # === Login Messages ===
    LOGGED_IN = "<b><i>🔐 Already logged in!</i></b>"
    INVALID_PASS = """
    <b><i>❌ Invalid Password!</i></b>
    <b><i>📌 Kindly enter the correct password.</i></b>
    """
    PASS_LOGGED = "<b><i>🔓 Bot permanent login successful!</i></b>"
    LOGIN_USED = """
    <b><i>🔐 Bot Login Usage:</i></b>
    <code>/cmd [password]</code>
    """

    # === Log Display ===
    LOG_DISPLAY_BT = "<b><i>📑 Log Display</i></b>"
    WEB_PASTE_BT = "<b><i>📨 Web Paste (SB)</i></b>"

    # === Help Menu ===
    BASIC_BT = "<b><i>📚 Basic</i></b>"
    USER_BT = "<b><i>👥 Users</i></b>"
    MICS_BT = "<b><i>🛠 Mics</i></b>"
    O_S_BT = "<b><i>👑 Owner & Sudo</i></b>"
    CLOSE_BT = "<b><i>❌ Close</i></b>"
    HELP_HEADER = """
    <b><i>📖 Help Guide Menu!</i></b>
    <b><i>📝 Note: Click on any command to see more details.</i></b>
    """

    # === Bot Statistics ===
    BOT_STATS = """
    <b><i>📊 Bot Statistics:</i></b>
    ┖ <b><i>⏰ Bot Uptime:</i></b> {bot_uptime}

    <b><i>┎ 💾 RAM (Memory):</i></b>
    ┃ {ram_bar} {ram}%
    ┖ <b><i>📈 Used:</i></b> {ram_u} | <b><i>🆓 Free:</i></b> {ram_f} | <b><i>📊 Total:</i></b> {ram_t}

    <b><i>┎ 💿 Swap Memory:</i></b>
    ┃ {swap_bar} {swap}%
    ┖ <b><i>📈 Used:</i></b> {swap_u} | <b><i>🆓 Free:</i></b> {swap_f} | <b><i>📊 Total:</i></b> {swap_t}

    <b><i>┎ 🗄 Disk:</i></b>
    ┃ {disk_bar} {disk}%
    ┃ <b><i>📥 Total Disk Read:</i></b> {disk_read}
    ┃ <b><i>📤 Total Disk Write:</i></b> {disk_write}
    ┖ <b><i>📈 Used:</i></b> {disk_u} | <b><i>🆓 Free:</i></b> {disk_f} | <b><i>📊 Total:</i></b> {disk_t}
    """

    SYS_STATS = """
    <blockquote><b><i>🖥 OS System:</i></b>
    ┠ <b><i>⏰ OS Uptime:</i></b> {os_uptime}
    ┠ <b><i>📟 OS Version:</i></b> {os_version}
    ┖ <b><i>⚙️ OS Arch:</i></b> {os_arch}</blockquote>

    <blockquote><b><i>🌐 Network Stats:</i></b>
    ┠ <b><i>📤 Upload Data:</i></b> {up_data}
    ┠ <b><i>📥 Download Data:</i></b> {dl_data}
    ┠ <b><i>📤 Pkts Sent:</i></b> {pkt_sent}k
    ┠ <b><i>📥 Pkts Received:</i></b> {pkt_recv}k
    ┖ <b><i>📊 Total I/O Data:</i></b> {tl_data}</blockquote>

    <blockquote><b><i>┎ 🧠 CPU:</i></b>
    ┃ {cpu_bar} {cpu}%
    ┠ <b><i>⚡ CPU Frequency:</i></b> {cpu_freq}
    ┠ <b><i>📊 System Avg Load:</i></b> {sys_load}
    ┠ <b><i>🔢 P-Core(s):</i></b> {p_core} | <b><i>🔢 V-Core(s):</i></b> {v_core}
    ┠ <b><i>🔢 Total Core(s):</i></b> {total_core}
    ┖ <b><i>🔢 Usable CPU(s):</i></b> {cpu_use}</blockquote>
    """

    REPO_STATS = """
    <b><i>📦 Repo Statistics:</i></b>
    ┠ <b><i>⏰ Bot Updated:</i></b> {last_commit}
    ┠ <b><i>🔖 Current Version:</i></b> {bot_version}
    ┠ <b><i>🔖 Latest Version:</i></b> {lat_version}
    ┖ <b><i>📜 Last Changelog:</i></b> {commit_details}

    <b><i>📝 Remarks:</i></b> <code>{remarks}</code>
    """

    BOT_LIMITS = """
    <blockquote><b><i>⚠️ Bot Limitations:</i></b>
    ┠ <b><i>📥 Direct Limit:</i></b> {DL} GB
    ┠ <b><i>🌊 Torrent Limit:</i></b> {TL} GB
    ┠ <b><i>☁️ GDrive Limit:</i></b> {GL} GB
    ┠ <b><i>🎥 YT-DLP Limit:</i></b> {YL} GB
    ┠ <b><i>🎶 Playlist Limit:</i></b> {PL}
    ┠ <b><i>📦 Mega Limit:</i></b> {ML} GB
    ┠ <b><i>📋 Clone Limit:</i></b> {CL} GB
    ┖ <b><i>📤 Leech Limit:</i></b> {LL} GB</blockquote>

    <blockquote><b><i>┎ ⏳ Token Validity:</i></b> {TV}
    ┠ <b><i>⏱ User Time Limit:</i></b> {UTI} / task
    ┠ <b><i>🔄 User Parallel Tasks:</i></b> {UT}
    ┖ <b><i>🔄 Bot Parallel Tasks:</i></b> {BT}</blockquote>
    """

    # === Restart Messages ===
    RESTARTING = "<b><i>🔄 Restarting...</i></b>"
    RESTART_SUCCESS = """
    <blockquote><b><i>✅ Restarted Successfully!</i></b>
    ┠ <b><i>📅 Date:</i></b> {date}
    ┠ <b><i>⏰ Time:</i></b> {time}
    ┠ <b><i>🌍 Timezone:</i></b> {timz}
    ┖ <b><i>🔖 Version:</i></b> {version}</blockquote>
    """
    RESTARTED = "<b><i>🔄 Bot Restarted!</i></b>"

    # === Ping Messages ===
    PING = "<b><i>🏓 Starting Ping...</i></b>"
    PING_VALUE = "<b><i>🏓 Pong!</i></b>\n<code>{value} ms</code>"

    # === Download/Upload Messages ===
    LINKS_START = """
    <b><i>🚀 Task Started</i></b>
    ┠ <b><i>📋 Mode:</i></b> {Mode}
    ┖ <b><i>👤 By:</i></b> {Tag}\n
    """
    LINKS_SOURCE = """
    <b><i>🔗 Source:</i></b>
    ┖ <b><i>📅 Added On:</i></b> {On}
    ------------------------------------------\n
    {Source}\n
    ------------------------------------------\n
    """

    PM_START = """
    <b><i>🚀 Task Started:</i></b>
    ┖ <b><i>🔗 Link:</i></b> <a href='{msg_link}'>Click Here</a>
    """
    L_LOG_START = """
    <b><i>📤 Leech Started:</i></b>
    ┠ <b><i>👤 User:</i></b> {mention} ( #ID{uid} )
    ┖ <b><i>🔗 Source:</i></b> <a href='{msg_link}'>Click Here</a>
    """

    # === Upload Complete ===
    NAME = "<b><i>{Name}</i></b>\n┃\n"
    SIZE = "<b><i>┠ 📏 Size:</i></b> {Size}\n"
    ELAPSE = "<b><i>┠ ⏱ Elapsed:</i></b> {Time}\n"
    MODE = "<b><i>┠ 📋 Mode:</i></b> {Mode}\n"

    # === Leech Messages ===
    L_TOTAL_FILES = "<b><i>┠ 📂 Total Files:</i></b> {Files}\n"
    L_CORRUPTED_FILES = "<b><i>┠ ⚠️ Corrupted Files:</i></b> {Corrupt}\n"
    L_CC = "<b><i>┖ 👤 By:</i></b> {Tag}\n\n"
    PM_BOT_MSG = "<b><i>📬 File(s) sent above</i></b>"
    L_BOT_MSG = "<b><i>📬 File(s) sent to Bot PM (Private)</i></b>"
    L_LL_MSG = "<b><i>📬 File(s) sent. Access via links...</i></b>\n"

    # === Mirror Messages ===
    M_TYPE = "<b><i>┠ 📄 Type:</i></b> {Mimetype}\n"
    M_SUBFOLD = "<b><i>┠ 📁 Subfolders:</i></b> {Folder}\n"
    TOTAL_FILES = "<b><i>┠ 📂 Files:</i></b> {Files}\n"
    RCPATH = "<b><i>┠ 📍 Path:</i></b> <code>{RCpath}</code>\n"
    M_CC = "<b><i>┖ 👤 By:</i></b> {Tag}\n\n"
    M_BOT_MSG = "<b><i>📬 Link(s) sent to Bot PM (Private)</i></b>"

    # === Buttons ===
    CLOUD_LINK = "☁️ Cloud Link"
    SAVE_MSG = "📨 Save Message"
    RCLONE_LINK = "♻️ Rclone Link"
    DDL_LINK = "📎 {Serv} Link"
    SOURCE_URL = "🔐 Source Link"
    INDEX_LINK_F = "🗂 Index Link (File)"
    INDEX_LINK_D = "⚡ Index Link (Dir)"
    VIEW_LINK = "🌐 View Link"
    CHECK_PM = "📥 View in Bot PM"
    CHECK_LL = "🖇 View in Links Log"
    MEDIAINFO_LINK = "📃 MediaInfo"
    SCREENSHOTS = "🖼 Screenshots"

    # === Status Messages ===
    STATUS_NAME = "<b><i>{Name}</i></b>"
    BAR = "\n┏━━❪ Animeworld 💜 ❫━━━✘\n┃ <blockquote>{Bar}</blockquote>"
    PROCESSED = "\n┠ <b><i>📈 Processed:</i></b> {Processed}"
    STATUS = '\n┠ <b><i>📊 Status:</i></b> <a href="{Url}">{Status}</a>'
    ETA = "| <b><i> ⏳ ETA:</i></b> {Eta}"
    SPEED = "\n┠ <b><i>⚡ Speed:</i></b> {Speed}"
    ELAPSED = " | <b><i>⏱ Elapsed:</i></b> {Elapsed}"
    ENGINE = "\n┠ <b><i>🛠 Engine:</i></b> {Engine}"
    STA_MODE = "\n┠ <b><i>📋 Mode:</i></b> {Mode}"
    SEEDERS = "\n┠ <b><i>🌱 Seeders:</i></b> {Seeders} | "
    LEECHERS = "<b><i>📤 Leechers:</i></b> {Leechers}"

    # === Seeding ===
    SEED_SIZE = "<b><i>\n┠ 📏 Size:</i></b> {Size}"
    SEED_SPEED = "<b><i>\n┠ ⚡ Speed:</i></b> {Speed} | "
    UPLOADED = "<b><i>📤 Uploaded:</i></b> {Upload}"
    RATIO = "<b><i>📊 Ratio:</i></b> {Ratio} | "
    TIME = "<b><i>⏱ Time:</i></b> {Time}"
    SEED_ENGINE = "<b><i>\n┠ 🛠 Engine:</i></b> {Engine}"

    # === Non-Progressive Status ===
    STATUS_SIZE = "<b><i>\n┠ 📏 Size:</i></b> {Size}"
    NON_ENGINE = "<b><i>\n┠ 🛠 Engine:</i></b> {Engine}"

    # === Footer ===
    USER = "\n┠ <b><i>👤 User:</i></b> <code>{User}</code> | "
    ID = "<b><i>🆔 ID:</i></b> <code>{Id}</code>"
    BTSEL = "\n┠ <b><i>🔘 Select:</i></b> {Btsel}"
    CANCEL = "\n┖ <b><i>❌ {Cancel}\n\n</i></b>"
    FOOTER = "╭───────✦✧✦──────✘\n ⌬ <b><i>📊 Bot Stats</i></b>"
    TASKS = "<b><i>┠ 📋 Tasks:</i></b> {Tasks}\n"
    BOT_TASKS = "<b><i>┠ 📋 Tasks:</i></b> {Tasks}/{Ttask} | <b><i>🆓 Avl:</i></b> {Free}\n"
    Cpu = "<b><i>┠ 🧠 CPU:</i></b> {cpu}% | "
    FREE = "<b><i>🆓 Free:</i></b> {free} [{free_p}%]"
    Ram = "<b><i>\n┠ 💾 RAM:</i></b> {ram}% | "
    uptime = "<b><i>⏰ Uptime:</i></b> {uptime}"
    DL = "<b><i>\n┠ 📥 DL:</i></b> {DL}/s | "
    UL = "<b><i>📤 UL:</i></b> {UL}/s\n╰───────✦✧✦──────✘"

    # === Buttons ===
    PREVIOUS = "⫷ Previous"
    REFRESH = "🔄 Pages\n{Page}"
    NEXT = "⫸ Next"

    # === Duplicate Check ===
    STOP_DUPLICATE = """
    <b><i>⚠️ File/Folder already available in Drive.</i></b>
    <b><i>📜 Here are {content} list results:</i></b>
    """

    # === Count Node ===
    COUNT_MSG = "<b><i>🔍 Counting:</i></b> <code>{LINK}</code>"
    COUNT_NAME = "<b><i>{COUNT_NAME}</i></b>\n┃\n"
    COUNT_SIZE = "<b><i>┠ 📏 Size:</i></b> {COUNT_SIZE}\n"
    COUNT_TYPE = "<b><i>┠ 📄 Type:</i></b> {COUNT_TYPE}\n"
    COUNT_SUB = "<b><i>┠ 📁 Subfolders:</i></b> {COUNT_SUB}\n"
    COUNT_FILE = "<b><i>┠ 📂 Files:</i></b> {COUNT_FILE}\n"
    COUNT_CC = "<b><i>┖ 👤 By:</i></b> {COUNT_CC}\n"

    # === List Search ===
    LIST_SEARCHING = "<b><i>🔍 Searching for {NAME}</i></b>"
    LIST_FOUND = "<b><i>✅ Found {NO} result(s) for {NAME}</i></b>"
    LIST_NOT_FOUND = "<b><i>❌ No result found for {NAME}</i></b>"

    # === Mirror Status ===
    NO_ACTIVE_DL = """
    <blockquote><b><i>🚫 No Active Downloads!</i></b>
    
    <b><i>📊 Bot Stats</i></b>
    ┠ <b><i>🧠 CPU:</i></b> {cpu}% | <b><i>🆓 Free:</i></b> {free} [{free_p}%]
    ┖ <b><i>💾 RAM:</i></b> {ram} | <b><i>⏰ Uptime:</i></b> {uptime}
    </blockquote>
    """

    # === User Settings ===
    USER_SETTING = """
    ╭───────✦✧✦───────✘ 
    <blockquote><b><i>⚙️ User Settings:</i></b>
    
    ┎ <b><i>👤 Name:</i></b> {NAME} ( <code>{ID}</code> )
    ┠ <b><i>📛 Username:</i></b> {USERNAME}
    ┠ <b><i>🌐 Telegram DC:</i></b> {DC}
    ┠ <b><i>🗣 Language:</i></b> {LANG}</blockquote>
    ╰───────✦✧✦───────✘

    <b><i>➲ Available Args:</i></b>
    • <b>-s</b> or <b>-set</b>: <b><i>🔧 Set directly via arg</i></b>
    """

    UNIVERSAL = """
    ╭───────✦✧✦──────✘ 
    <b><i>🌐 Universal Settings: {NAME}</i></b>

    ┎ <b><i>🎥 YT-DLP Options:</i></b> <code>{YT}</code>
    ┠ <b><i>📅 Daily Tasks:</i></b> <code>{DT}</code> per day
    ┠ <b><i>🤖 Last Bot Used:</i></b> <code>{LAST_USED}</code>
    ┠ <b><i>🔐 User Session:</i></b> <code>{USESS}</code>
    ┠ <b><i>📃 MediaInfo Mode:</i></b> <code>{MEDIAINFO}</code>
    ┠ <b><i>💾 Save Mode:</i></b> <code>{SAVE_MODE}</code>
    ┠ <b><i>📬 User Bot PM:</i></b> <code>{BOT_PM}</code>
    ╰───────✦✧✦──────✘
    """

    MIRROR = """
    ╭───────✦✧✦──────✘ 
    <b><i>📤 Mirror/Clone Settings: {NAME}</i></b>

    ┎ <b><i>♻️ Rclone Config:</i></b> <i>{RCLONE}</i>
    ┠ <b><i>📝 Mirror Prefix:</i></b> <code>{MPREFIX}</code>
    ┠ <b><i>📝 Mirror Suffix:</i></b> <code>{MSUFFIX}</code>
    ┠ <b><i>📝 Mirror Rename:</i></b> <code>{MREMNAME}</code>
    ┠ <b><i>🌐 DDL Server(s):</i></b> <i>{DDL_SERVER}</i>
    ┠ <b><i>📂 User TD Mode:</i></b> <i>{TMODE}</i>
    ┠ <b><i>📂 Total User TD(s):</i></b> <i>{USERTD}</i>
    ┠ <b><i>📅 Daily Mirror:</i></b> <code>{DM}</code> per day
    ╰───────✦✧✦──────✘
    """

    LEECH = """
    ╭───────✦✧✦──────✘
    <b><i>📥 Leech Settings for {NAME}</i></b>

    ┎ <b><i>📅 Daily Leech:</i></b> <code>{DL}</code> per day
    ┠ <b><i>📄 Leech Type:</i></b> <i>{LTYPE}</i>
    ┠ <b><i>🖼 Custom Thumbnail:</i></b> <i>{THUMB}</i>
    ┠ <b><i>📏 Leech Split Size:</i></b> <code>{SPLIT_SIZE}</code>
    ┠ <b><i>📏 Equal Splits:</i></b> <i>{EQUAL_SPLIT}</i>
    ┠ <b><i>📂 Media Group:</i></b> <i>{MEDIA_GROUP}</i>
    ┠ <b><i>📝 Leech Caption:</i></b> <code>{LCAPTION}</code>
    ┠ <b><i>📝 Leech Prefix:</i></b> <code>{LPREFIX}</code>
    ┠ <b><i>📝 Leech Suffix:</i></b> <code>{LSUFFIX}</code>
    ┠ <b><i>📤 Leech Dumps:</i></b> <code>{LDUMP}</code>
    ┠ <b><i>📝 Leech Rename:</i></b> <code>{LREMNAME}</code>
    ┖ <b><i>📄 Leech Metadata:</i></b> <code>{LMETA}</code>
    ╰───────✦✧✦──────✘
    """
