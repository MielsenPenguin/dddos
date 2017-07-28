import os
import sys
import shutil
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
main = raw_input (''+T+'' + color.UNDERLINE + 'Chiar vrei să dezinstalezi Trity :( ?>' + color.END)
if main == "yes" or "y" or "Yes" or "Y":
    try:
        shutil.rmtree('/opt/trity')
        os.remove('/usr/bin/trity')
        print (''+G+'' + color.UNDERLINE + 'Trity a fost  eliminata cu succes din pacate :( !' + color.END)
    except:
        print (color.FAIL + 'Trinity este deja dezinstalata sau nu este incă instalata!' + color.END)
else:
    print (''+G+'' + color.UNDERLINE + 'Okay!' + color.END)
    sys.exit()