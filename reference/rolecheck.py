import discord
from discord.ext import commands


one = "**1**: Custodians - 150 EXP"
two = "**2**: Record Keeper - 350 EXP"
three = "**3**: Book Keeper - 750 EXP"
four = "**4**: Librarian - 1500 EXP"
five = "**5**: Vizier - 2400 EXP"
six = "**6**: Grand Vizier - 4770 EXP"
rhd = "*(You already have that role)*"
ino = "*(You must buy roles in order)*"

base = f"{one} \n {two} \n {three} \n {four} \n {five} \n {six}"

none = f"{one} \n ~~{two}~~ {ino} \n ~~{three}~~ {ino} \n ~~{four}~~ {ino} \n ~~{five}~~ {ino} \n ~~{six}~~ {ino}"
c = f"~~{one}~~ {rhd} \n {two} \n ~~{three}~~ {ino} \n ~~{four}~~ {ino} \n ~~{five}~~ {ino} \n ~~{six}~~ {ino}"
rk = f"~~{one}~~ {rhd} \n ~~{two}~~ {rhd} \n {three} \n ~~{four}~~ {ino} \n ~~{five}~~ {ino} \n ~~{six}~~ {ino}"
bk = f"~~{one}~~ {rhd} \n ~~{two}~~ {rhd} \n ~~{three}~~ {rhd} \n {four} \n ~~{five}~~ {ino} \n ~~{six}~~ {ino}"
li = f"~~{one}~~ {rhd} \n ~~{two}~~ {rhd} \n ~~{three}~~ {rhd} \n ~~{four}~~ {rhd} \n {five} \n ~~{six}~~ {ino}"
v = f"~~{one}~~ {rhd} \n ~~{two}~~ {rhd} \n ~~{three}~~ {rhd} \n ~~{four}~~ {rhd} \n ~~{five}~~ {rhd} \n {six}"
gv = f"~~{one}~~ {rhd} \n ~~{two}~~ {rhd} \n ~~{three}~~ {rhd} \n ~~{four}~~ {rhd} \n ~~{five}~~ {rhd} \n ~~{six}~~ {rhd}"


