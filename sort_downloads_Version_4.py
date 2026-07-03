# Let's Sort Your Messy Downloads Folder!

# Imports
#---------------------------------------------------------------------------
import os
from pathlib import Path

# this library lets you move files
import shutil

# 📦 Global Variables
#---------------------------------------------------------------------------
# PATH_DOWNLOADS = r'C:\Users\hpat2\Downloads'        # Dev/Local
PATH_DOWNLOADS = Path.home() / 'Downloads'          # Universal


# Define Sorting Rules
#---------------------------------------------------------------------------


# the keys are the folder names  ---> cat
# the values are the type of file extension ---> list_keywords

CATEGORIES = {
    '_Invoices'              : ['invoice', 'receipt', 'rechnung'],
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

    """ Find Sorting Folder by name


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

    # the joins in this case with go into the folder path directly
    file_path = os.path.join(PATH_DOWNLOADS, filename)

    if os.path.isdir(file_path):

        # activate this print statement to help you for testing
        # print("It's a folder")

        return '_Folders'



    # File

    else:

        # activate this print statement to help you for testing
        # print("It's a file")



        # Option A - For File Extensions


        # # Looking for Category
        # # for a certain file we need to find the category
        # for cat, list_keywords in CATEGORIES.items():
        #
        #     if file_extension.lower() in list_keywords:
        #
        #         # you have to return it here because the file extension was found
        #         return cat

        file_extension = '.' + file.split('.')[-1]

        for cat, list_keywords in CATEGORIES.items():

            for keyword in list_keywords:

                if keyword.lower() in filename:

                    return cat


        print(f' {file_extension} - Not Supported. File: ({filename}) (Placed in _Others)')

        # place unknown file names in others
        return '_Others'





# Read All Files
for file in os.listdir(PATH_DOWNLOADS):

    # calling function and putting the return value into cat
    dir_name = get_file_cat(file)
    #print(dir_name,file)

    if (dir_name):

        # joing these paths
        dir_filepath = os.path.join(PATH_DOWNLOADS, dir_name)

        # Create Sorting Folders

        # do this is the file path does not exist
        if not os.path.exists(dir_filepath):

            os.makedirs(dir_filepath)




        # Define Old/New Paths
        old_path = PATH_DOWNLOADS / file
        new_path = os.path.join(PATH_DOWNLOADS, dir_name, file)

        # Move Files

        # this try except block help if you have an open file
        try:

            shutil.move(old_path, new_path)
            print(f' {dir_name} / {file}')

        except Exception as e:

            print(f' {dir_name} / {file} - {e}')



# Read All Files

def sort_downloads():

    all_files = os.listdir(PATH_DOWNLOADS)

    folder  =   [f for f in all_files]
    files   =   [f for f in all_files]


    for file in all_files:

        # calling function and putting the return value into cat
        dir_name = get_file_cat(file)
        #print(dir_name,file)

        if (dir_name):

            # joing these paths
            dir_filepath = os.path.join(PATH_DOWNLOADS, dir_name)

            # Create Sorting Folders

            # do this is the file path does not exist
            if not os.path.exists(dir_filepath):

                os.makedirs(dir_filepath)




            # Define Old/New Paths
            old_path = PATH_DOWNLOADS / file
            new_path = os.path.join(PATH_DOWNLOADS, dir_name, file)

            # Move Files

            # this try except block help if you have an open file
            try:

                shutil.move(old_path, new_path)
                print(f' {dir_name} / {file}')

            except Exception as e:

                print(f' {dir_name} / {file} - {e}')



if __name__ == '__main__':

    sort_downloads()
# Report Results




