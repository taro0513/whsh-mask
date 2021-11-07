from linebot.models import *
helpmsg = """[@help] 顯示此訊息!
[#search:{district}-{location}] 顯示最近地區的資料
[#show:{district}-{location}] 顯示地區的圖片
"""
class reply: 
    @classmethod
    def test(self,url):
        return ImageSendMessage(
        original_content_url= url,
        preview_image_url= url
    )

    @classmethod 
    def help(self):
        return TextSendMessage(text=helpmsg)
    @classmethod
    def nothis(self):
        # return TextSendMessage(text='https://www.youtube.com/watch?v=FWzlJNFM7_k')
        return TextSendMessage(text='No this command! (Enter: @help for help)')

    @classmethod
    def search(district, location, camera=None):
        if camera is None:
            ...

    @classmethod
    def searchT():
        ...

    @classmethod
    def GUI(self):
        return TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://blog.whsh.tc.edu.tw/wp-content/uploads/2020/08/2.jpg',
                        title='現場測試',
                        text='請從下選擇區域!', 
                        actions=[
                            MessageTemplateAction(label='筆電鏡頭',text='search:test'),
                            MessageTemplateAction(label='筆電鏡頭2',text='search:test2')]
                        ),
                    CarouselColumn(
                        thumbnail_image_url='https://blog.whsh.tc.edu.tw/wp-content/uploads/2020/08/2.jpg',
                        title='文華高中',
                        text='請從下選擇區域!', 
                        actions=[
                            MessageTemplateAction(label='福利社',text='search:whsh-stores'),
                            MessageTemplateAction(label='圖書館',text='search:whsh-library'),
                            MessageTemplateAction(label='電腦教室(三)',text='search:whsh-computer3')]
                        ),
                    CarouselColumn(
                        thumbnail_image_url='https://pic.pimg.tw/anrine910070/1584640894-623479486.jpg',
                        title='逢甲夜市',
                        text='尚未開放',
                        actions=[
                            MessageTemplateAction(label='文華路',text='None'),
                            MessageTemplateAction(label='福星路',text='None'),
                            MessageTemplateAction(label='逢甲路', text='None')]
                            )
                        ]
                    )
                )

    @classmethod
    def GUI2(self):
        return TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://blog.whsh.tc.edu.tw/wp-content/uploads/2020/08/2.jpg',
                        title='文華高中',
                        text='請從下選擇區域!', 
                        actions=[
                            MessageTemplateAction(label='筆電測試',text='search:test'),
                            MessageTemplateAction(label='圖書館',text='search:whsh-library'),
                            MessageTemplateAction(label='電腦教室(三)',text='search:whsh-computer3')]
                        )
                    ]
                )
            )
    
# print(reply.help())