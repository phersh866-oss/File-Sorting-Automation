# Let's Sort Your Messy Downloads Folder!

from pathlib import Path

# 📦 Global Variables
#---------------------------------------------------------------------------
PATH_DOWNLOADS = r'C:\Users\hpat2\Downloads'        # Dev/Local
PATH_DOWNLOADS = Path.home() / 'Downloads'          # Universal


#---------------------------------------------------------------------------
# Define Sorting Rules

# the keys are the folder names
# the values are the type of file extension

CATEGORIES = {
    '_Images'       : ['.jpg', '.jpeg', '.png'],
    '_GIF'          : ['.gif'],
    '_Videos'       : ['.mp4', '.mkv', '.avi', '.mov'],
    '_Docs'         : ['.pdf', '.docx', '.txt'],
    '_ZIPs'         : ['.zip', '.rar', '.7z'],
    '_Installers'   : ['.exe', '.msi'],
    '_Code'         : ['.py', '.js', '.html', '.css', '.md'],
    '_Data'         : ['.csv', '.xlsx']
}


# Read All Files

# Get File Category (based on rules)

# Create Sorting Folders

# Move Files

# Report Results

# Bonus: Create CMD-Command

