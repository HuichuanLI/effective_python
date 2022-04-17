# -*- coding:utf-8 -*-
# @Time : 2022/4/17 8:18 下午
# @Author : huichuan LI
# @File : subporcess.py
# @Software: PyCharm
import subprocess

# 子进程可以独立于父进程而运行，这里的父进程指 Python 解释器所在的那条进程。假如刚才那条子进程不是通过 run 函数启动，而是由 Popen 类启动的，那么我们就可以在它启动之后，
# 让 Python 程序去做别的任务，每做一段时间就来查询一次子进程的状态以决定要不要继续执行任务。


result = subprocess.run(
    ['echo', 'Hello from the child!'],
    capture_output=True,
    encoding='utf-8')

result.check_returncode()  # No exception means it exited cleanly
print(result.stdout)

# Python 里面有许多方式都可以运行子进程（例如 os.popen 函数以及 os.exec*系列的函数），
# 其中最好的办法是通过内置的 subprocess 模块来管理。用这个模块运行子进程是很简单的。
# 下面我们就通过 run 函数启动一条进程，然后确认该进程已经正常终止，最后打印它的输出值。


proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('Working...')
    # Some time-consuming work here
    import time

    time.sleep(0.3)

print('Exit status', proc.poll())

#
# 从统计结果可以看出，这 10 条子进程确实表现出了平行的效果。假如它们是按顺序执行的，那么程序耗费的总时长至少应该是 10 秒，而不是现在看到的 1 秒左右。
#
# 我们还可以在 Python 程序里面把数据通过管道发送给子进程所运行的外部命令，然后将那条命令的输出结果获取到 Python 程序之中。而且，在执行外部命令的这个环节中，可以平行地运行多条命令。例如，要用 oepnssl 这样的命令行工具来加密数据。首先以适当的命令行参数构建一批子进程，并配置好相应的 I/O 管道，这在 Python 里很容易就能做到。


import time

start = time.time()
sleep_procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_procs.append(proc)

for proc in sleep_procs:
    proc.communicate()

end = time.time()
delta = end - start
print(f'Finished in {delta:.3} seconds')

import os


def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure that the child gets input
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])

proc = subprocess.Popen(['sleep', '10'])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())
