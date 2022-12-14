# Quixl uses the GNU General Public License v3.0, also known as GNU GPLv3. Check '[Install Directory]/COPYING' for more information
import os, sys, time
print("This installer will do the following:")
print("Uninstall current versions of pygame/pillow (if installed)\nDownload and new versions of pygame/pillow.\nSelf-Destruct (The installer will delete itself when done.")
print("-----------\nIf you do not want this to happen, you have 5 seconds to cancel by stopping the python script...")
print("5..."); time.sleep(1)
print("4..."); time.sleep(1)
print("3..."); time.sleep(1)
print("2..."); time.sleep(1)
print("1..."); time.sleep(1)
print("0.")
print("----- Beginning quixl required package installation -----")
os.system("pip uninstall pygame -y")
os.system("pip uninstall pillow -y")
os.system("pip install pygame")
os.system("pip install pillow")
print("Install complete!")
os.remove(sys.argv[0])
print("Self-Destructed")
print("I hope you enjoy quixl!")