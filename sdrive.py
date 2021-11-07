from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class drive:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.CommandLineAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload(self, filename, parent_id=None):
        if parent_id:
            self.file = self.drive.CreateFile({'parents': [{'id': parent_id}]})  
        else:
            self.file = self.drive.CreateFile()
        self.file.SetContentFile(filename)
        try:self.file.Upload()
        except Exception as e:print('Unknown Error :%s'%e)
    
    def get_id(self,filename=None,folder_id='1n_3lkP5MqpyOGYhF_SwlSJtD6O0JmhVF'):
        hint = "\'" + folder_id + "\'" + " in parents and trashed=false"    
        file_list = self.drive.ListFile({'q': hint}).GetList()
        if filename:
            for file in file_list:
                if file['title'] == filename:return file['id']
            
        else:
            rt = []
            for file in file_list:
                rt.append([file['title'],file['id']])
            return rt

    def download(self, filename, new_Name=None,  file_id=None, folder_id='1n_3lkP5MqpyOGYhF_SwlSJtD6O0JmhVF'):
        if file_id: self.file = self.drive.CreateFile({'id': file_id})  
        else: self.file = self.drive.CreateFile({'id': self.get_id(filename,folder_id)})
        if new_Name: self.file.GetContentFile(new_Name)
        else: self.file.GetContentFile(filename)


up = drive()
# # up.upload('images.jpg','1n_3lkP5MqpyOGYhF_SwlSJtD6O0JmhVF')
up.download('images.jpg','aa.jpg')