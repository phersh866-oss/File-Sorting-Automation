# Let's Sort Your Messy Downloads Folder!

# Imports
#---------------------------------------------------------------------------
import os
from pathlib import Path

# 📦 Global Variables
#---------------------------------------------------------------------------
PATH_DOWNLOADS = r'C:\Users\hpat2\Downloads'        # Dev/Local
PATH_DOWNLOADS = Path.home() / 'Downloads'          # Universal


# Define Sorting Rules
#---------------------------------------------------------------------------


# the keys are the folder names  ---> cat
# the values are the type of file extension ---> list_keywords

CATEGORIES = {
    '_Images'               : ['.jpg', '.jpeg', '.png'],
    '_GIF'                  : ['.gif'],
    '_Videos'               : ['.mp4', '.mkv', '.avi', '.mov'],
    '_Docs'                 : ['.pdf', '.docx', '.txt', '.json'],
    '_ZIPs'                 : ['.zip', '.rar', '.7z'],
    '_Installers'           : ['.exe', '.msi'],
    '_Code'                 : ['.py', '.js', '.html', '.css', '.md'],
    '_Data'                 : ['.csv', '.xlsx'],
    '_Design'               : ['.fig', '.psd', '.svg'],
    '_Subtitles'            : ['.vtt'],
    '_System_and_Setting'   : ['.ini']
}


# Functions
#---------------------------------------------------------------------------
def get_file_cat(filename):

    """ Find SOrting Folder by name


    :param filename: FIlename inside of Downloads Folder
    :return:         Name of Sorting Folder
    """


    '''
    # example of using file.split('.')[-1]
    file_extension = 'Hersh.Patel.mp4'

    ['Hersh', 'Patel', 'mp4']

    # when you take [-1] you get:

            mp4

    '''


    # Ignore Sorting Folders
    if filename.startswith('_'):

        return None

    # Folder

    # the joins in this case with go into the golder path directly
    file_path = os.path.join(PATH_DOWNLOADS, filename)

    if os.path.isdir(file_path):

        # activate this print statement to help you for testing
        # print("It's a folder")

        return '_Folder'



    # File

    else:

        # activate this print statement to help you for testing
        # print("It's a file")


        file_extension = '.' + file.split('.')[-1]

        # Looking for Category
        # for a certain file we need to find the category
        for cat, list_keywords in CATEGORIES.items():

            if file_extension.lower() in list_keywords:

                # you have to return it here because the file extension was found
                return cat



        # this prints if the extension was not found. An example is a folder name can print out
        print(f' {file_extension} - Not Supported. File: ({filename}) (Placed in _Others)')

        # place unknown file names in others
        return '_Others'





# Read All Files
for file in os.listdir(PATH_DOWNLOADS):

    # calling function and putting the return value into cat
    dir_name = get_file_cat(file)
    #print(dir_name,file)







# Get File Category (based on rules)

# Create Sorting Folders

# Move Files

# Report Results

# Bonus: Create CMD-Command

