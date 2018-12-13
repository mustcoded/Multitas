import threading
import os
import filecmp

class Remove(threading.Thread):

    def __init__(self, massage,  filename, fullfilename, directory_path, aLabel):

        threading.Thread.__init__(self)
        self.massage = massage
        self.filename, self.file_extension = os.path.splitext(filename)
        self.fullfilename = fullfilename
        self.directory_path = directory_path
        self.count = 0
        self.aLabel = aLabel

    def run(self):

        filepaths = os.listdir(self.massage)

        for filepath in list(filepaths):
            os.chdir(self.massage)
            if(os.getcwd() != self.directory_path): # make sure that we will not delete the same file in the selected file directory
                if(os.path.isfile(filepath)):
                    filename, file_extension = os.path.splitext(filepath)
                    self.remove_file(file_extension, filepath)
                else:
                    self.delete_duplicate(os.path.join(self.massage, filepath))
            else:
                continue

        if(self.count > 0):
            self.aLabel.message = 'Removed ' + str(self.count) + ' duplicate : ' + self.filename # show this message box each time a set of duplicate files have been removed
        else:
            self.aLabel.message = "No duplicate file found :  " + self.filename

    def delete_duplicate(self, folder): # sub method to pass folder to

        filepaths = os.listdir(folder)

        for filepath in list(filepaths):
            os.chdir(folder)
            if(os.getcwd() != self.directory_path):

                if(os.path.isfile(filepath)):
                    filename, file_extension = os.path.splitext(filepath)
                    self.remove_file(file_extension, filepath)
                else:
                    self.delete_duplicate(os.path.join(folder, filepath))

            else:
                continue

    def remove_file(self, file_extension, filepath):
        if (file_extension == self.file_extension):
            if filecmp.cmp(filepath, self.fullfilename, shallow=False):
                os.remove(filepath)
                self.count += 1




