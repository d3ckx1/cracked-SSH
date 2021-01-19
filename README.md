# cracked-SSH

介绍：用于批量对目标IP进行SSH爆破工作。

工具先探测IP端口开放情况（默认22端口）,后再根据开放的IP进行批量爆破工作，如果爆破成功保存为“ssh-pwn.txt”，并执行命令“hostname”（这个命令可以替换成你懂的命令...），直观的确认是否有爆破成功。

使用范围：渗透测试中、红队渗透中、内网渗透中，使用字典对IP资产进行SSH服务自动化爆破工作。

后期还会继续追加新功能！！！！

使用方法：python cracked_ssh.py -t ip.txt -u user.txt -p pass.txt

演示图：
![Image text](https://github.com/d3ckx1/cracked-SSH/blob/main/截屏2021-01-19%20下午2.15.20.png)
![Image text](https://github.com/d3ckx1/cracked-SSH/blob/main/WechatIMG4647.jpeg)
