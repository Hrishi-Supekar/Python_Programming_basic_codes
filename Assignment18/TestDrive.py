from threading import Thread
from time import sleep


class Medical(Thread):
    def run(self) -> None:
        print("Medical Test Started")
        sleep(2)
        print("Medical Test Completed")


class TestDrive(Thread):
    def run(self) -> None:
        print("TestDrive Started")
        sleep(2)
        print("TestDrive Completed")


class Officer(Thread):
    def run(self) -> None:
        print("Officer work in progress")
        sleep(2)
        print("Officer work Completed")


m = Medical()
m.start()
m.join()
t = TestDrive()
t.start()
t.join()
o = Officer()
o.start()
o.join()
print("You have received your licence")
