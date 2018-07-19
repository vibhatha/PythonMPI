import threading
import time
import ThreadImpl

EXIT_FLAG = 0

class ThreadHandler(threading.Thread):

    def __init__(self, threadId, obj):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.obj = obj
        thread = threading.Thread(target=self.run, args=())

    def run(self):
        print(self.threadId, self.obj)
        #self.object.execute()


threadHandler = ThreadHandler("1", ThreadImpl)
