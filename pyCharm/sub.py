import subprocess
from time import sleep


def call_shell():
    ps = subprocess.Popen('cd /home/anisa/Documents/AnalyticsBot/sempre && ./run @mode=simple -Grammar.inPaths /home/anisa/Documents/AnalyticsBot/sempre/analyticsBot/interface.grammar',
                         shell=True, stdin=subprocess.PIPE, stdout=open("/tmp/output", 'w'), bufsize=10)

    sleep(1)
    ps.stdin.write("client x volume\n")
    sleep(2)
    with open("/tmp/output", "r") as f:
        print(f.read())


if __name__ == '__main__':
    call_shell()