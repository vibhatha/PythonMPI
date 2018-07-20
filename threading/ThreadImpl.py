import threading
import thread


class ThreadImpl:
    def __init__(self, threadId, taskName):
        self.threadId = threadId
        self.taskName = taskName


    def execute(self):
        print(self.threadId, self.taskName)


threadImpl = ThreadImpl("1", "Task 1")

#t = threading.Thread(target=threadImpl.execute)
#t.start()

