from Message.MessageReply import reply
class Process(object):
    """
    Message type:
    - @help
    - #search:{district}-{location} (-{number of camera})
    - #show:{district}-{location} (-{number of camera} ) 
    """
    @classmethod
    def distinguish(self, message):
        try: method, param = message.split(':')
        except: return Process.help()
        if method == '#search' : return Process.search(param)
        elif method == '#show' : return Process.show(param)
        else: return Process.nothis()
    
    @classmethod
    def help(self):
        return reply.help()
    
    @classmethod
    def search(self,param):
        try: 
            district, location, camera = param.split('-')
            return reply.search(district, location, camera)
        except:
            district, location = param.split('-')
            return reply.search(district, location)

    @classmethod
    def show(self,param):
        try: 
            district, location, camera = param.split('-')
            return reply.show(district, location, camera)
        except:
            district, location = param.split('-')
            return reply.show(district, location)
        
    @classmethod
    def nothis(self):
        return reply.nothis()

Process.distinguish('a')