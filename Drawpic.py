from Sheet import sheet
from Config import config
import datetime
import matplotlib.pyplot as plt
import pyimgur
DetectionSetting = config(section='Draw').data()

class drawpic:
    @classmethod
    def drax(self):
        nt = datetime.datetime.now()
        c = nt.hour*60 + nt.minute

        st = sheet()
        value = st.ws.get_all_values()
        for i in value:
            if i[0] == '':break
            else:print(i[0])

        print(c+420)
        obj = [eval(v[0].split('-')[1]) for v in value if ((v[0] != '') and (int(v[0].split('-')[0])> c+420))]
        print(obj)

        while(len(obj)<20):
            obj.insert(0,None)
        while(len(obj)>20):
            obj.pop(0)

        month = range(1,len(obj)+1)
        plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
        plt.plot(month,obj,'s-',color = 'r', label="Percentage of People")
        plt.title("Danger Warning", x=0.5, y=1.03)
        plt.xticks(range(1,21,1),range(60,0,-3))
        plt.yticks(range(0,101,10))
        plt.xlabel("How long from now", fontsize=30, labelpad = 15)
        plt.ylabel("Percentage of people wearing masks", fontsize=30, labelpad = 20)
        plt.legend(loc = "best", fontsize=20)
        plt.savefig('image.png')
    @classmethod
    def upload(self):
        CLIENT_ID = DetectionSetting['CLIENT_ID']
        PATH = "image.png"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
        return uploaded_image.link

