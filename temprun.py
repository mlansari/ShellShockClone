print("Starting")
import ShellShockClone
print("Managed to import the ShellShockClone Module file")

# this is some ugly as hell bad form just catching at the top smh
try:
    ShellShockClone.game.run()
except e as Exception:
    print(e)
