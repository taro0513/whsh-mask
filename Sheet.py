import pygsheets
from Config import config
import datetime
conf = config(section='Sheet')
setting = conf.data()

class sheet():
    def __init__(self,
                 sheet_url= setting['sheet_url'],
                 worksheet_name= setting['worksheet_name'],
                 client_path= setting['client_path']):
        self.sheet_url = sheet_url
        self.worksheet_name = worksheet_name
        self.client_path = client_path
        self._sheet = pygsheets.authorize(service_file=self.client_path)
        self.sheet = self._sheet.open_by_url(self.sheet_url)
        self.ws = self.sheet.worksheet_by_title(self.worksheet_name)

    def read(self, coordinate):
        try: return self.ws.cell(coordinate).value
        except: return None

    def read_all(self, coordinate, direction='col') -> list:
        if direction == 'col':
            return self.ws.get_col(coordinate)
        else: return self.ws.get_row(coordinate)



    def edit(self, coordinate, value, worksheet_name= None):
        worksheet_name = self.worksheet_name if worksheet_name == None else worksheet_name
        if not(self.ws and worksheet_name):raise FileNotFoundError(self.worksheet_name)
        else:
            self.ws = self.sheet.worksheet_by_title(worksheet_name)
            try: self.ws.update_value(coordinate,value)
            except ValueError as e: print(e)

    def delete(self, coordinate, worksheet_name= None):
        worksheet_name = self.worksheet_name if worksheet_name == None else worksheet_name
        if not(self.ws and worksheet_name):raise FileNotFoundError(self.worksheet_name)
        else:
            self.ws = self.sheet.worksheet_by_title(worksheet_name)
            self.ws.update_value(coordinate, '')

    def add(self, value, coordinate_x=False, Plus=True, worksheetname= None):
        if coordinate_x :
            self.edit(self.last(),value)
            if Plus:self.add_last()
            else:pass
        else:
            if isinstance(value, list):
                for _value in value:
                    self.edit(self.now(),_value)
            else:
                self.edit(self.now(),value,worksheet_name)
    @classmethod
    def ssplit(self, value, plus=False):
        _l = 0
        for _v in value:
            if _v.isalpha(): _l += 1
            else: break
        if plus:return '%s%d'%(value[:_l],int(value[_l:])+1)
        else:return '%s%s'%(value[:_l],value[_l:])

    @classmethod
    def last(self, coordinate_x=None, worksheetname= None):
        if setting['last_coordinate'][0] != self.now()[0]:
            conf.edit('last_coordinate', '%s1'%self.now()[0])
            return '%s1'%self.now()[0]   
        else: 
            return self.ssplit(setting['last_coordinate'])

    
    @classmethod
    def add_last(self,plus=True):
        conf.edit(key='last_coordinate',value=self.ssplit(setting['last_coordinate'],plus=plus))

    def new(self, value=None, auto= None, worksheetname= None):
        ...
    
    @classmethod
    def now(self):
        dt = datetime.datetime.now()
        return '%s%d'%(chr(int(dt.day)+64),(int(dt.hour)*60+int(dt.minute)//3))

    
    def add2last(self,value):
        values = self.ws.get_all_values()
        k = [eval(v[0]) for v in values if ((v[0] != ''))]
        self.edit('A%i'%(len(k)+1),value)
