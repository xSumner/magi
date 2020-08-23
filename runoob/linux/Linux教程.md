# Linux 教程

------

![linux](img/linux.jpg)

Linux 英文解释为 Linux is not Unix。

本教程，我们将为大家介绍如何使用Linux。

Linux其实很容易学，相信你们能很快学会。

[现在开始学习 Linux ！](https://www.runoob.com/linux/Linux-intro.html)

------

## 谁适合阅读？

本教程针对的是Linux服务器方面的知识，适合从事运维或后端开发的人员阅读。

------

## 需要具备的知识？

如果你熟悉操作系统方面的知识，相信你会很快学会 Linux。

本教程将于 Linux 的发行版本 Centos 为例来为大家介绍 Linux 系统的应用。

# Linux 简介

------

Linux 内核最初只是由芬兰人林纳斯·托瓦兹（Linus Torvalds）在赫尔辛基大学上学时出于个人爱好而编写的。

Linux 是一套免费使用和自由传播的类 Unix 操作系统，是一个基于 POSIX 和 UNIX 的多用户、多任务、支持多线程和多 CPU 的操作系统。

Linux 能运行主要的 UNIX 工具软件、应用程序和网络协议。它支持 32 位和 64 位硬件。Linux 继承了 Unix 以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。

------

## Linux 的发行版

Linux 的发行版说简单点就是将 Linux 内核与应用软件做一个打包。

![img](img/1511849829609658.jpg)

目前市面上较知名的发行版有：Ubuntu、RedHat、CentOS、Debian、Fedora、SuSE、OpenSUSE、Arch Linux、SolusOS 等。

![img](img/wKioL1bvVPWAu7hqAAEyirVUn3c446.jpg-wh_651x-s_3197843091.jpg)

------

## Linux 应用领域

今天各种场合都有使用各种 Linux 发行版，从嵌入式设备到超级计算机，并且在服务器领域确定了地位，通常服务器使用 LAMP（Linux + Apache + MySQL + PHP）或 LNMP（Linux + Nginx+ MySQL + PHP）组合。

目前 Linux 不仅在家庭与企业中使用，并且在政府中也很受欢迎。

- 巴西联邦政府由于支持 Linux 而世界闻名。
- 有新闻报道俄罗斯军队自己制造的 Linux 发布版的，做为 G.H.ost 项目已经取得成果。
- 印度的 Kerala 联邦计划在向全联邦的高中推广使用 Linux。
- 中华人民共和国为取得技术独立，在龙芯处理器中排他性地使用 Linux。
- 在西班牙的一些地区开发了自己的 Linux 发布版，并且在政府与教育领域广泛使用，如 Extremadura 地区的 gnuLinEx 和 Andalusia 地区的 Guadalinex。
- 葡萄牙同样使用自己的 Linux 发布版 Caixa Mágica，用于 Magalh?es 笔记本电脑和 e-escola 政府软件。
- 法国和德国同样开始逐步采用 Linux。

------

## Linux vs Windows

目前国内 Linux 更多的是应用于服务器上，而桌面操作系统更多使用的是 Windows。主要区别如下

| 比较     | Windows                                                      | Linux                                                        |
| :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 界面     | 界面统一，外壳程序固定所有 Windows 程序菜单几乎一致，快捷键也几乎相同 | 图形界面风格依发布版不同而不同，可能互不兼容。GNU/Linux 的终端机是从 UNIX 传承下来，基本命令和操作方法也几乎一致。 |
| 驱动程序 | 驱动程序丰富，版本更新频繁。默认安装程序里面一般包含有该版本发布时流行的硬件驱动程序，之后所出的新硬件驱动依赖于硬件厂商提供。对于一些老硬件，如果没有了原配的驱动有时很难支持。另外，有时硬件厂商未提供所需版本的 Windows 下的驱动，也会比较头痛。 | 由志愿者开发，由 Linux 核心开发小组发布，很多硬件厂商基于版权考虑并未提供驱动程序，尽管多数无需手动安装，但是涉及安装则相对复杂，使得新用户面对驱动程序问题（是否存在和安装方法）会一筹莫展。但是在开源开发模式下，许多老硬件尽管在Windows下很难支持的也容易找到驱动。HP、Intel、AMD 等硬件厂商逐步不同程度支持开源驱动，问题正在得到缓解。 |
| 使用     | 使用比较简单，容易入门。图形化界面对没有计算机背景知识的用户使用十分有利。 | 图形界面使用简单，容易入门。文字界面，需要学习才能掌握。     |
| 学习     | 系统构造复杂、变化频繁，且知识、技能淘汰快，深入学习困难。   | 系统构造简单、稳定，且知识、技能传承性好，深入学习相对容易。 |
| 软件     | 每一种特定功能可能都需要商业软件的支持，需要购买相应的授权。 | 大部分软件都可以自由获取，同样功能的软件选择较少。           |

# Linux 安装

本章节我们将为大家介绍 Linux 的安装，安装步骤比较繁琐，现在其实云服务器挺普遍的，价格也便宜，如果直接不想搭建，也可以直接买一台学习用用，参考[各大云服务器比较](https://www.runoob.com/linux/linux-cloud-server.html)。

本章节以 centos6.4 为例。

centos 下载地址：

可以去官网下载最新版本：https://www.centos.org/download/

![img](img/1497342019-2668-2a90-3944-9027-0352de39b1fe.jpg)

以下针对各个版本的ISO镜像文件，进行一一说明：

- **CentOS-7.0-x86_64-DVD-1503-01.iso** : 标准安装版，一般下载这个就可以了（推荐）
- **CentOS-7.0-x86_64-NetInstall-1503-01.iso** : 网络安装镜像（从网络安装或者救援系统）
- **CentOS-7.0-x86_64-Everything-1503-01.iso**: 对完整版安装盘的软件进行补充，集成所有软件。（包含centos7的一套完整的软件包，可以用来安装系统或者填充本地镜像）
- **CentOS-7.0-x86_64-GnomeLive-1503-01.iso**: GNOME桌面版
- **CentOS-7.0-x86_64-KdeLive-1503-01.iso**: KDE桌面版
- **CentOS-7.0-x86_64-livecd-1503-01.iso** : 光盘上运行的系统，类拟于winpe
- **CentOS-7.0-x86_64-minimal-1503-01.iso** : 精简版，自带的软件最少

> **注：**建议安装64位Linux系统。
>
> 旧版本下载地址：https://wiki.centos.org/Download

接下来你需要将下载的Linux系统刻录成光盘或U盘。

**注：**你也可以在Window上安装VMware虚拟机来安装Linux系统。

------

## Linux 安装步骤

1、首先，使用光驱或U盘或你下载的Linux ISO文件进行安装。

界面说明：

![image001](img/image001.png)

- Install or upgrade an existing system 安装或升级现有的系统

- Install system with basic video driver 安装过程中采用基本的显卡驱动

- Rescue installed system 进入系统修复模式

- Boot from local drive  退出安装从硬盘启动

- Memory test 内存检测


注：用联想E49安装时选择第一项安装时会出现屏幕显示异常的问题，后改用第二项安装时就没有出现问题

2、这时直接"skip"就可以了

![image002](img/image002.png)

3、出现引导界面，点击"next"

![image003](img/image003.png)

4、选中"English（English）"否则会有部分乱码问题

![image004](img/image004.png)

5、键盘布局选择"U.S.English"

![image005](img/image005.png)

6、选择"Basic Storage Devices"点击"Next"

![image006](img/image006.png)

7、询问是否忽略所有数据，新电脑安装系统选择"Yes,discard any data"

![image007](img/image007.png)

8、Hostname填写格式"英文名.姓"

![image008](img/image008.png)

9、网络设置安装图示顺序点击就可以了

![image009](img/image009.png)

10、时区可以在地图上点击，选择"shanghai"并取消System clock uses UTC前面的对勾

![image010](img/image010.png)

11、设置root的密码

![image011](img/image011.png)

12、硬盘分区，一定要按照图示点选

![image012](img/image012.png)

13、调整分区，必须要有/home这个分区，如果没有这个分区，安装部分软件会出现不能安装的问题

![image013](img/image013.png)

14、询问是否格式化分区

![image014](img/image014.png)

15、将更改写入到硬盘

![image015](img/image015.png)

16、引导程序安装位置

![image016](img/image016.png)

17、最重要的一步，也是本教程最关键的一步，也是其他教程没有提及的一步，按图示顺序点击

![image017](img/image017.png)

18、取消以下内容的所有选项

- **Applications**
- **Base System**

- **Servers**

并对Desktops进行如下设置

即取消如下选项：

- **Desktop Debugging and Performance Tools**
- **Desktop Platform**

- **Remote Desktop Clients**
- **Input Methods** **中仅保留ibus-pinyin-1.3.8-1.el6.x86_64,其他的全部取消**

![image018](img/image018.png)

![image019](img/image019.png)

19、选中Languages，并选中右侧的Chinese Support然后点击红色区域

![image020](img/image020.png)

20、调整完成后如下图所示

![image021](img/image021.png)

21、至此，一个最精简的桌面环境就设置完成了，

![image022](img/image022.png)

22、安装完成，重启

![image023](img/image023.png)

23、重启之后，的License Information

![image024](img/image024.png)

24、Create User

Username：填写您的英文名（不带.姓）

Full Name：填写您的英文名.姓（首字母大写）

![image025](img/image025.png)

25、"Date and Time" 选中 "Synchronize data and time over the network"

Finsh之后系统将重启

![image026](img/image026.png)

26、第一次登录，登录前不要做任何更改，这个很重要！！！登录之后紧接着退出

第二次登录，选择语言，在红色区域选择下拉小三角，选other，选中"汉语（中国）"

![image027](img/image027.png)

![image028](img/image028.png)

27、登录之后，请一定按照如下顺序点击！

至此，CentOS安装完成，如有其他问题，请随时与我联系！！

![image029](img/image029.png)

> 如果你使用的是 VMware，可以参考：[VMware 安装 Centos7](https://www.runoob.com/w3cnote/vmware-install-centos7.html)



# Linux 云服务器

自己安装服务器还是麻烦了些，现在一般都推荐大家使用云服务器，比较方便，价格也不贵。

目前市场上的云服务器很多，这边比较下[腾讯云](https://www.runoob.com/linux/linux-cloud-server.html#tx)跟[阿里云](https://www.runoob.com/linux/linux-cloud-server.html#ali)的服务器优惠活动，现在看来腾讯云性价比会高一些。

------

## 腾讯云

年末腾讯云活动已开始，以下几款性价比非常高，有几款是需要抢购的，大家看好时间基本能拿到。

- **1核2G** 95/年，可以用来学习，Linux 知识对技术人员的成才非常重要。
- **1核2G** 3 年 288。
- 另外还有香港的服务器，如果做网站不想去备案，可以考虑，香港速度还是很快的。

每个时间点都有不同的配置跟价格，具体信息，可以点击下面的图片：

[![img](img/7BE961C6-B837-41A7-984A-18E8DCB62C80.jpg)](https://url.cn/MGw7Pvh5)

另外企业用户还有更高配置的，价格也很实惠：

[![img](img/51A673D6-2411-40B2-A48D-0E93DA587E75.jpg)](https://url.cn/MGw7Pvh5)

------

## 阿里云

阿里也有一些活动，**不分新老用户，可以领红包参与满减活动，续费也有专门的优惠券**，有需求的也可以关注下。

具体信息，可以点击下面的图片。

**618 活动**

点击下列图片，查看详情：

[![img](img/C08B6F9E-4E29-4D07-A0E3-A3B2AD3E7A7F.jpg)](https://www.aliyun.com/activity/618/index?userCode=i5mn5r7m)

**注意**：阿里云**突发性能型的服务器**真的只能自己学习用，如果要用对外提供服务要慎重选择，因为它性能瓶颈限制很大，不过价格便宜就是了。

新用户专场，价格还是很实惠的(**2核4G5M-3年 ￥935.55**)：

[![img](img/FB5A4326-4BF8-4A62-95C6-786FB655BF6B.jpg)](https://www.aliyun.com/sale-season/2020/procurement-new-members?userCode=i5mn5r7m)

老户专场，价格也还行：

[![img](img/B015E281-5E86-406B-A7C8-7BA6E904B6F4.jpg)](https://www.aliyun.com/minisite/goods?userCode=i5mn5r7m&share_source=copy_link)

5 折活动页：

[![img](img/FD5CE717-3B48-4433-8ADD-20A3D21BC0BC.jpg)](https://www.aliyun.com/minisite/goods?userCode=i5mn5r7m&share_source=copy_link)

------

## 腾讯云服务器使用

本章节以腾讯云服务器为例。

**1、首先点击下图购买（更多服务器的配置信息见下文）：**

[![img](img/AE3CD782-2C0D-4EB1-9170-437A2B83709F.jpg)](https://url.cn/MGw7Pvh5)

**2、登陆腾讯云控制台，查看已购买的服务器：**

![img](img/812CFA9E-41F6-4EA2-8044-9FBCAB9C0AAE.jpg)

**3、在使用腾讯云服务器前，我们需要先创建一个 SSH 密钥，点击左侧的 \**SSH 密钥\** （使用密钥登录比密码更安全）：**

![img](img/018E95B9-756E-4B6C-A0A2-CED21B42F25A.jpg)

输入密钥名称，然后点击确定，就会自动生成一个密钥，密钥会自动下载到本地，请保存好下载的密钥，密钥文件名就是你输入的密钥名称。

**4、接着我们勾选已经创建的密钥，点击 `绑定/解绑实例` 按钮，弹窗中会出现我们的 ECS 服务器，将其绑定到这个密钥即可：**

![img](img/963AF776-FE8C-4340-A426-870D962BDC93.jpg)

**5、返回实例列表，点击实例右侧的 `登录` 按钮，弹窗中点击立即登录，这是会弹出一个新的浏览器窗口，我们选择密钥登录，密钥文件就是在第三个步骤创建的：**

![img](img/A23D733A-DA1B-42C9-91E8-12FB84A68400.jpg)

![img](img/7603BDAC-3103-4379-B0BE-8E669E069AF4.jpg)

![img](img/D1D8FA9C-4ECD-42A4-B24B-70520F854858.jpg)

当然你可以选择第三方客户端登录（如：SecureCRT），用户名为 ubuntu，其他系统估计略有不同，然后导入对应的 key 即可。



# Linux 系统启动过程

linux启动时我们会看到许多启动信息。

Linux系统的启动过程并不是大家想象中的那么复杂，其过程可以分为5个阶段：

- 内核的引导。
- 运行 init。
- 系统初始化。
- 建立终端 。
- 用户登录系统。

> init程序的类型：
>
> - **SysV:** init, CentOS 5之前, 配置文件： /etc/inittab。
> - **Upstart:** init,CentOS 6, 配置文件： /etc/inittab, /etc/init/*.conf。
> - **Systemd：** systemd, CentOS 7,配置文件： /usr/lib/systemd/system、 /etc/systemd/system。

------

## 内核引导

当计算机打开电源后，首先是BIOS开机自检，按照BIOS中设置的启动设备（通常是硬盘）来启动。

操作系统接管硬件以后，首先读入 /boot 目录下的内核文件。

![img](img/bg2013081702.png)

------

## 运行init

init 进程是系统所有进程的起点，你可以把它比拟成系统所有进程的老祖宗，没有这个进程，系统中任何进程都不会启动。

init 程序首先是需要读取配置文件 /etc/inittab。

![img](img/bg2013081703.png)



### 运行级别

许多程序需要开机启动。它们在Windows叫做"服务"（service），在Linux就叫做"守护进程"（daemon）。

init进程的一大任务，就是去运行这些开机启动的程序。

但是，不同的场合需要启动不同的程序，比如用作服务器时，需要启动Apache，用作桌面就不需要。

Linux允许为不同的场合，分配不同的开机启动程序，这就叫做"运行级别"（runlevel）。也就是说，启动时根据"运行级别"，确定要运行哪些程序。

![img](img/bg2013081704.png)

Linux系统有7个运行级别(runlevel)：

- 运行级别0：系统停机状态，系统默认运行级别不能设为0，否则不能正常启动
- 运行级别1：单用户工作状态，root权限，用于系统维护，禁止远程登陆
- 运行级别2：多用户状态(没有NFS)
- 运行级别3：完全的多用户状态(有NFS)，登陆后进入控制台命令行模式
- 运行级别4：系统未使用，保留
- 运行级别5：X11控制台，登陆后进入图形GUI模式
- 运行级别6：系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动

------

## 系统初始化

在init的配置文件中有这么一行： `si::sysinit:/etc/rc.d/rc.sysinit`　它调用执行了`/etc/rc.d/rc.sysinit`，而`rc.sysinit`是一个bash shell的脚本，它主要是完成一些系统初始化的工作，`rc.sysinit`是每一个运行级别都要首先运行的重要脚本。

它主要完成的工作有：激活交换分区，检查磁盘，加载硬件模块以及其它一些需要优先执行任务。

```bash
l5:5:wait:/etc/rc.d/rc 5
```

这一行表示以5为参数运行`/etc/rc.d/rc`，`/etc/rc.d/rc`是一个Shell脚本，它接受5作为参数，去执行`/etc/rc.d/rc5.d/`目录下的所有的rc启动脚本，`/etc/rc.d/rc5.d/`目录中的这些启动脚本实际上都是一些连接文件，而不是真正的rc启动脚本，真正的rc启动脚本实际上都是放在`/etc/rc.d/init.d/`目录下。

而这些rc启动脚本有着类似的用法，它们一般能接受start、stop、restart、status等参数。

`/etc/rc.d/rc5.d/`中的rc启动脚本通常是K或S开头的连接文件，对于以 S 开头的启动脚本，将以start参数来运行。

而如果发现存在相应的脚本也存在K打头的连接，而且已经处于运行态了(以`/var/lock/subsys/`下的文件作为标志)，则将首先以stop为参数停止这些已经启动了的守护进程，然后再重新运行。

这样做是为了保证是当init改变运行级别时，所有相关的守护进程都将重启。

至于在每个运行级中将运行哪些守护进程，用户可以通过chkconfig或setup中的"System Services"来自行设定。

![img](img/bg2013081705.png)

------

## 建立终端

rc执行完毕后，返回init。这时基本系统环境已经设置好了，各种守护进程也已经启动了。

init接下来会打开6个终端，以便用户登录系统。在inittab中的以下6行就是定义了6个终端：

```
1:2345:respawn:/sbin/mingetty tty1
2:2345:respawn:/sbin/mingetty tty2
3:2345:respawn:/sbin/mingetty tty3
4:2345:respawn:/sbin/mingetty tty4
5:2345:respawn:/sbin/mingetty tty5
6:2345:respawn:/sbin/mingetty tty6
```

从上面可以看出在2、3、4、5的运行级别中都将以respawn方式运行mingetty程序，mingetty程序能打开终端、设置模式。

同时它会显示一个文本登录界面，这个界面就是我们经常看到的登录界面，在这个登录界面中会提示用户输入用户名，而用户输入的用户将作为参数传给login程序来验证用户的身份。

------

## 用户登录系统

一般来说，用户的登录方式有三种：

- （1）命令行登录
- （2）ssh登录
- （3）图形界面登录

![img](img/bg2013081706.png)

对于运行级别为5的图形方式用户来说，他们的登录是通过一个图形化的登录界面。登录成功后可以直接进入 KDE、Gnome 等窗口管理器。

而本文主要讲的还是文本方式登录的情况：当我们看到mingetty的登录界面时，我们就可以输入用户名和密码来登录系统了。

Linux 的账号验证程序是 login，login 会接收 mingetty 传来的用户名作为用户名参数。

然后 login 会对用户名进行分析：如果用户名不是 root，且存在 `/etc/nologin` 文件，login 将输出 nologin 文件的内容，然后退出。

这通常用来系统维护时防止非root用户登录。只有`/etc/securetty`中登记了的终端才允许 root 用户登录，如果不存在这个文件，则 root 用户可以在任何终端上登录。

`/etc/usertty`文件用于对用户作出附加访问限制，如果不存在这个文件，则没有其他限制。

------

## 图形模式与文字模式的切换方式

Linux预设提供了六个命令窗口终端机让我们来登录。

默认我们登录的就是第一个窗口，也就是tty1，这个六个窗口分别为tty1,tty2 … tty6，你可以按下<kbd>Ctrl + Alt + F1 ~ F6</kbd> 来切换它们。

如果你安装了图形界面，默认情况下是进入图形界面的，此时你就可以按<kbd>Ctrl + Alt + F1 ~ F6</kbd>来进入其中一个命令窗口界面。

当你进入命令窗口界面后再返回图形界面只要按下<kbd>Ctrl + Alt + F7 </kbd>就回来了。

如果你用的vmware 虚拟机，命令窗口切换的快捷键为 <kbd>Alt + Space + F1~F6</kbd>. 如果你在图形界面下请按<kbd>Alt + Shift + Ctrl + F1~F6</kbd> 切换至命令窗口。

![img](img/bg2013081707.png)

------

## Linux 关机

在linux领域内大多用在服务器上，很少遇到关机的操作。毕竟服务器上跑一个服务是永无止境的，除非特殊情况下，不得已才会关机。

正确的关机流程为：sync > shutdown > reboot > halt

关机指令为：shutdown ，你可以man shutdown 来看一下帮助文档。

例如你可以运行如下命令关机：

```
sync 将数据由内存同步到硬盘中。

shutdown 关机指令，你可以man shutdown 来看一下帮助文档。例如你可以运行如下命令关机：

shutdown –h 10 ‘This server will shutdown after 10 mins’ 这个命令告诉大家，计算机将在10分钟后关机，并且会显示在登陆用户的当前屏幕中。

shutdown –h now 立马关机

shutdown –h 20:25 系统会在今天20:25关机

shutdown –h +10 十分钟后关机

shutdown –r now 系统立马重启

shutdown –r +10 系统十分钟后重启

reboot 就是重启，等同于 shutdown –r now

halt 关闭系统，等同于shutdown –h now 和 poweroff
```

最后总结一下，不管是重启系统还是关闭系统，首先要运行 **sync** 命令，把内存中的数据写到磁盘中。

关机的命令有 **shutdown –h now halt poweroff** 和 **init 0** , 重启系统的命令有 **shutdown –r now reboot init 6**。

------

参考文章：http://www.ruanyifeng.com/blog/2013/08/linux_boot_process.html

---

shutdown 会给系统计划一个时间关机。它可以被用于停止、关机、重启机器。shutdown 会给系统计划一个时间关机。它可以被用于停止、关机、重启机器。

```shell
# shutdown -p now  ### 关闭机器
# shutdown -H now  ### 停止机器      
# shutdown -r 09:35 ### 在 09:35am 重启机器
```

要取消即将进行的关机，只要输入下面的命令：

```shell
# shutdown -c
```

halt 命令通知硬件来停止所有的 CPU 功能，但是仍然保持通电。你可以用它使系统处于低层维护状态。注意在有些情况会它会完全关闭系统。

```shell
# halt             ### 停止机器
# halt -p          ### 关闭机器、关闭电源
# halt --reboot    ### 重启机器
```

poweroff 会发送一个 ACPI 信号来通知系统关机。

```shell
# poweroff           ### 关闭机器、关闭电源
# poweroff --halt    ### 停止机器
# poweroff --reboot  ### 重启机器
```

reboot 命令 reboot 通知系统重启。

```shell
# reboot           ### 重启机器
# reboot --halt    ### 停止机器
# reboot -p        ### 关闭机器
```

补充几个有时候很有用的快捷键；

- **[Tab] 有『命令补全』与『文件补齐』的功能**

```shell
[Tab]      ## 接在一串指令的第一个字的后面，则为『命令补全』
[Tab]      ## 接在一串指令的第二个字以后时，则为『文件补齐』
```

若安装 bash-completion 软件，则在某些指令后面使用 [tab] 按键时，可以进行『选项/参数的补齐』功能！

- **[Ctrl]+ C 如果在Linux 底下输入了错误的指令或参数，想让当前的程序『停掉』的话，可以输入：**

```shell
[Ctrl] + c 
```

- **[Ctrl]-d 『键盘输入结束(End Of File, EOF 或 End Of Input)』的意思**

另外，他也可以用来取代 exit 的输入。

例如你想要直接离开文字接口，可以直接按下：

```shell
[Ctrl] + d   ## 相当于输入 exit
```

- **[shift]+{[PageUP]|[Page Down]}**

```shell
[Shift]+[Page Up]    ## 往前翻页 

[Shift]+[Page Down] ## 往后翻页
```



# Linux 系统目录结构

登录系统后，在当前命令窗口下输入命令：

```shell
 ls / 
```

你会看到如下图所示:

![img](img/4_20.png)

树状目录结构：

![img](img/003vPl7Rty6E8kZRlAEdc690.jpg)

以下是对这些目录的解释：

- **/bin**：
  bin是Binary的缩写, 这个目录存放着最经常使用的命令。

- **/boot：**
  这里存放的是启动Linux时使用的一些核心文件，包括一些连接文件以及镜像文件。

- **/dev ：**
  dev是Device(设备)的缩写, 该目录下存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。

- **/etc：**
  这个目录用来存放所有的系统管理所需要的配置文件和子目录。

- **/home**：
  用户的主目录，在Linux中，每个用户都有一个自己的目录，一般该目录名是以用户的账号命名的。

- **/lib**：
  这个目录里存放着系统最基本的动态连接共享库，其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。

- **/lost+found**：
  这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。

- **/media**：
  linux 系统会自动识别一些设备，例如U盘、光驱等等，当识别后，linux会把识别的设备挂载到这个目录下。

- **/mnt**：
  系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。

- **/opt**：
   这是给主机额外安装软件所摆放的目录。比如你安装一个ORACLE数据库则就可以放到这个目录下。默认是空的。

- **/proc**：
  这个目录是一个虚拟的目录，它是系统内存的映射，我们可以通过直接访问这个目录来获取系统信息。
  这个目录的内容不在硬盘上而是在内存里，我们也可以直接修改里面的某些文件，比如可以通过下面的命令来屏蔽主机的ping命令，使别人无法ping你的机器：

  ```shell
  echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
  ```

- **/root**：
  该目录为系统管理员，也称作超级权限者的用户主目录。

- **/sbin**：
  s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。

- **/selinux**：
   这个目录是Redhat/CentOS所特有的目录，Selinux是一个安全机制，类似于windows的防火墙，但是这套机制比较复杂，这个目录就是存放selinux相关的文件的。

- **/srv**：
   该目录存放一些服务启动之后需要提取的数据。

- **/sys**：

   这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。

  sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。

  该文件系统是内核设备树的一个直观反映。

  当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中被创建。

- **/tmp**：
  这个目录是用来存放一些临时文件的。

- **/usr**：
   这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。

- **/usr/bin：**
  系统用户使用的应用程序。

- **/usr/sbin：**
  超级用户使用的比较高级的管理程序和系统守护程序。

- **/usr/src：**
  内核源代码默认的放置目录。

- **/var**：
  这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。

- **/run**：
  是一个临时文件系统，存储系统启动以来的信息。当系统重启时，这个目录下的文件应该被删掉或清除。如果你的系统上有 /var/run 目录，应该让它指向 run。

<font color=red>在 Linux 系统中，有几个目录是比较重要的，平时需要注意不要误删除或者随意更改内部文件。</font>

- **/etc**： 上边也提到了，这个是系统中的配置文件，如果你更改了该目录下的某个文件可能会导致系统不能启动。
- **/bin, /sbin, /usr/bin, /usr/sbin**: 这是系统预设的执行文件的放置目录，比如 ls 就是在/bin/ls 目录下的。

- 值得提出的是，/bin, /usr/bin 是给系统用户使用的指令（除root外的通用户），而/sbin, /usr/sbin 则是给root使用的指令。

- **/var**： 这是一个非常重要的目录，系统上跑了很多程序，那么每个程序都会有相应的日志产生，而这些日志就被记录到这个目录下，具体在/var/log 目录下，另外mail的预设放置也是在这里。

---

在 Linux 或 Unix 操作系统中，所有的文件和目录都被组织成以一个根节点开始的倒置的树状结构。

文件系统的最顶层是由根目录开始的，系统使用 **/** 来表示根目录。在根目录之下的既可以是目录，也可以是文件，而每一个目录中又可以包含子目录文件。如此反复就可以构成一个庞大的文件系统。

在Linux文件系统中有两个特殊的目录，一个用户所在的工作目录，也叫当前目录，可以使用一个点 **.** 来表示；另一个是当前目录的上一级目录，也叫父目录，可以使用两个点 **..** 来表示。

-  . ：代表当前的目录，也可以使用 ./ 来表示；
-  .. ：代表上一层目录，也可以 ../ 来代表。

如果一个目录或文件名以一个点 . 开始，表示这个目录或文件是一个隐藏目录或文件(如：.bashrc)。即以默认方式查找时，不显示该目录或文件。

**系统启动必须：**

- **/boot：**存放的启动Linux 时使用的内核文件，包括连接文件以及镜像文件。

- **/etc：**存放**所有**的系统需要的**配置文件**和**子目录列表，**更改目录下的文件可能会导致系统不能启动。

- **/lib**：存放基本代码库（比如c++库），其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。

- **/sys**： 这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。该文件系统是内核设备树的一个直观反映。当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中

**指令集合：**

- **/bin：**存放着最常用的程序和指令

- **/sbin：**只有系统管理员能使用的程序和指令。

**外部文件管理：**

- **/dev ：**Device(设备)的缩写, 存放的是Linux的外部设备。**注意：**在Linux中访问设备和访问文件的方式是相同的。

- **/media**：类windows的**其他设备，**例如U盘、光驱等等，识别后linux会把设备放到这个目录下。

- **/mnt**：临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。

**临时文件：**

- **/run**：是一个临时文件系统，存储系统启动以来的信息。当系统重启时，这个目录下的文件应该被删掉或清除。如果你的系统上有 /var/run 目录，应该让它指向 run。

- **/lost+found**：一般情况下为空的，系统非法关机后，这里就存放一些文件。

- **/tmp**：这个目录是用来存放一些临时文件的。

**账户：**

- **/root**：系统管理员的用户主目录。

- **/home**：用户的主目录，以用户的账号命名的。

- **/usr**：用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。

- **/usr/bin：**系统用户使用的应用程序与指令。

- **/usr/sbin：**超级用户使用的比较高级的管理程序和系统守护程序。

- **/usr/src：**内核源代码默认的放置目录。

**运行过程中要用：**

- **/var**：存放经常修改的数据，比如程序运行的日志文件（/var/log 目录下）。

- **/proc**：管理**内存空间！**虚拟的目录，是系统内存的映射，我们可以直接访问这个目录来，获取系统信息。这个目录的内容不在硬盘上而是在内存里，我们也可以直接修改里面的某些文件来做修改。

**扩展用的：**

- **/opt**：默认是空的，我们安装额外软件可以放在这个里面。

- **/srv**：存放服务启动后需要提取的数据**（不用服务器就是空）**

# Linux 忘记密码解决方法

很多朋友经常会忘记Linux系统的root密码，linux系统忘记root密码的情况该怎么办呢？重新安装系统吗？当然不用！进入单用户模式更改一下root密码即可。

步骤如下：

### 重启linux系统

![4_21](img/4_21.png)

3 秒之内要按一下回车，出现如下界面

![4_22](img/4_22.png)

然后输入e

![4_23](img/4_23.png)

在 第二行最后边输入 single，有一个空格。具体方法为按向下尖头移动到第二行，按"e"进入编辑模式

![4_24](img/4_24.png)在后边加上single 回车

![4_25](img/4_25.png)

最后按"b"启动，启动后就进入了单用户模式了

![4_26](img/4_26.png)

此时已经进入到单用户模式了，你可以更改root密码了。更密码的命令为 passwd

![4_27](img/4_27.png)



【**使用系统安装光盘的救援模式**】

救援模式即rescue ，这个模式主要是应用于，系统无法进入的情况。如，grub损坏或者某一个配置文件修改出错。如何使用rescue模式呢？

光盘启动，按F5 进入rescue模式

![4_28](img/4_28.png)

输入linux rescue 回车

![4_29](img/4_29.png)

选择语言，笔者建议你选择英语

![4_30](img/4_30.png)

选择us 键盘

![4_31](img/4_31.png)

![4_32](img/4_32.png)

这里问你是否启动网络，有时候可能会联网调试。我们选no

![4_33](img/4_33.png)

这里告诉我们，接下来会把系统挂载在/mnt/sysimage 中。

其中有三个选项:

- Continue 就是挂载后继续下一步。 
- Read-Only 挂载成只读，这样更安全，有时文件系统损坏时，只读模式会防止文件系统近一步损坏。
- Skip就是不挂载，进入一个命令窗口模式。 

这里我们选择Continue。

![4_34](img/4_34.png)

至此，系统已经挂载到了/mnt/sysimage中。接下来回车，输入chroot /mnt/sysimage 进入管理员环境。

![4_35](img/4_35.png)

**提示：** 其实也可以到rescue模式下更改root的密码的。这个rescue模式和windows PE系统很相近。

当运行了chroot /mnt/sysimage/ 后，再ls 看到目录结构和原来系统中的目录结构是一样的。

没错！现在的环境和原来系统的环境是一模一样的。你可以输入exit 或者按Ctrl + D退出这个环境。然后你再ls 看一下

![4_36](img/4_36.png)

这个目录其实就是rescue模式下的目录结构，而我们的系统文件全部在 /mnt/sysimage目录下。

# Linux 远程登录

Linux 一般作为服务器使用，而服务器一般放在机房，你不可能在机房操作你的 Linux 服务器。

这时我们就需要远程登录到Linux服务器来管理维护系统。

Linux 系统中是通过 ssh 服务实现的远程登录功能，默认 ssh 服务端口号为 22。

Window 系统上 Linux 远程登录客户端有 SecureCRT, Putty, SSH Secure Shell 等，本文以 Putty 为例来登录远程服务器。

Putty 下载地址：https://www.putty.org/

如果你下载了 Putty，请双击 putty.exe 然后弹出如下的窗口。

![img](img/5_1.png)

在Host Name( or IP address) 下面的框中输入你要登录的远程服务器IP(可以通过ifconfig命令查看服务器ip)，然后回车。

![img](img/5_12.png)

此时，提示我们输入要登录的用户名。

![img](img/5_13.png)

输入root 然后回车，再输入密码，就能登录到远程的linux系统了。

![img](img/5_14.png)

------

## 使用密钥认证机制远程登录linux

SSH 为 Secure Shell 的缩写，由 IETF 的网络工作小组（Network Working Group）所制定。

SSH 为建立在应用层和传输层基础上的安全协议。

首先使用工具 PUTTYGEN.EXE 生成密钥对。打开工具 PUTTYGEN.EXE 后如下图所示：

![img](img/5_15.png)

该工具可以生成三种格式的key ：SSH-1(RSA) SSH-2(RSA) SSH-2(DSA) ，我们采用默认的格式即 SSH-2(RSA)。Number of bits in a generated key 这个是指生成的key的大小，这个数值越大，生成的key就越复杂，安全性就越高。这里我们写 2048。

![img](img/5_16.png)

然后单击Generate 开始生成密钥对：

![img](img/5_17.png)

注意的是，在这个过程中鼠标要来回的动，否则这个进度条是不会动的。

![img](img/5_18.png)

到这里，密钥对已经生成了。你可以给你的密钥输入一个密码，（在Key Passphrase那里）也可以留空。然后点 Save public key 保存公钥，点 Save private Key 保存私钥。笔者建议你放到一个比较安全的地方，一来防止别人偷窥，二来防止误删除。接下来就该到远程 linux 主机上设置了。

1）创建目录 `/root/.ssh` 并设置权限

`[root@localhost ~]# mkdir /root/.ssh mkdir` 命令用来创建目录，以后会详细介绍，暂时只了解即可。

`[root@localhost ~]# chmod 700 /root/.ssh chmod` 命令是用来修改文件属性权限的，以后会详细介绍。

2）创建文件 `/ root/.ssh/authorized_keys`

`[root@localhost ~]# vim /root/.ssh/authorized_keys` vim 命令是编辑一个文本文件的命令，同样在后续章节详细介绍。

3）打开刚才生成的public key 文件，建议使用写字板打开，这样看着舒服一些，复制从AAAA开头至 "---- END SSH2 PUBLIC KEY ----" 该行上的所有内容，粘贴到`/root/.ssh/authorized_keys` 文件中，要保证所有字符在一行。（可以先把复制的内容拷贝至记事本，然后编辑成一行载粘贴到该文件中）。

在这里要简单介绍一下，如何粘贴，用vim打开那个文件后，该文件不存在，所以vim会自动创建。按一下字母"i"然后同时按shift + Insert 进行粘贴（或者单击鼠标右键即可），前提是已经复制到剪切板中了。粘贴好后，然后把光标移动到该行最前面输入 **ssh-rsa** ，然后按空格。再按ESC，然后输入冒号wq 即 :wq 就保存了。格式如下图：

![img](img/5_19.png)

4）再设置putty选项，点窗口左侧的SSh –> Auth ，单击窗口右侧的Browse… 选择刚刚生成的私钥， 再点Open ，此时输入root，就不用输入密码就能登录了。

![img](img/5_20.png)

如果在前面你设置了Key Passphrase ，那么此时就会提示你输入密码的。为了更加安全建议大家要设置一个Key Passphrase。

---

**终端利用ssh登录远程服务器**

安装ssh：

```shell
yum install ssh
```

启动ssh：

```shell
service sshd start
```

登录远程服务器：

```shell
ssh -p 50022 my@127.0.0.1
输入密码：
my@127.0.0.1:
```

- **-p** 后面是端口
- **my** 是服务器用户名

- **127.0.0.1** 是服务器 ip

回车输入密码即可登录

# Linux 文件基本属性

Linux系统是一种典型的多用户系统，不同的用户处于不同的地位，拥有不同的权限。为了保护系统的安全性，Linux系统对不同的用户访问同一文件（包括目录文件）的权限做了不同的规定。

在Linux中我们可以使用ll或者ls –l命令来显示一个文件的属性以及文件所属的用户和组，如：

```shell
[root@www /]# ls -l
total 64
dr-xr-xr-x   2 root root 4096 Dec 14  2012 bin
dr-xr-xr-x   4 root root 4096 Apr 19  2012 boot
……
```

实例中，bin文件的第一个属性用"d"表示。"d"在Linux中代表该文件是一个目录文件。

在Linux中第一个字符代表这个文件是目录、文件或链接文件等等。

- 当为[ **d** ]则是目录
- 当为[ **-** ]则是文件；
- 若是[ **l** ]则表示为链接文档(link file)；
- 若是[ **b** ]则表示为装置文件里面的可供储存的接口设备(可随机存取装置)；
- 若是[ **c** ]则表示为装置文件里面的串行端口设备，例如键盘、鼠标(一次性读取装置)。

接下来的字符中，以三个为一组，且均为『rwx』 的三个参数的组合。其中，[ r ]代表可读(read)、[ w ]代表可写(write)、[ x ]代表可执行(execute)。 要注意的是，这三个权限的位置不会改变，如果没有权限，就会出现减号[ - ]而已。

每个文件的属性由左边第一部分的10个字符来确定（如下图）。

![363003_1227493859FdXT](img/363003_1227493859FdXT.png)

从左至右用0-9这些数字来表示。

第0位确定文件类型，第1-3位确定属主（该文件的所有者）拥有该文件的权限。

第4-6位确定属组（所有者的同组用户）拥有该文件的权限，第7-9位确定其他用户拥有该文件的权限。

其中，第1、4、7位表示读权限，如果用"r"字符表示，则有读权限，如果用"-"字符表示，则没有读权限；

第2、5、8位表示写权限，如果用"w"字符表示，则有写权限，如果用"-"字符表示没有写权限；第3、6、9位表示可执行权限，如果用"x"字符表示，则有执行权限，如果用"-"字符表示，则没有执行权限。

------

## Linux文件属主和属组

```
[root@www /]# ls -l
total 64
drwxr-xr-x 2 root  root  4096 Feb 15 14:46 cron
drwxr-xr-x 3 mysql mysql 4096 Apr 21  2014 mysql
……
```

对于文件来说，它都有一个特定的所有者，也就是对该文件具有所有权的用户。

同时，在Linux系统中，用户是按组分类的，一个用户属于一个或多个组。

文件所有者以外的用户又可以分为文件所有者的同组用户和其他用户。

因此，Linux系统按文件所有者、文件所有者同组用户和其他用户来规定了不同的文件访问权限。

在以上实例中，mysql 文件是一个目录文件，属主和属组都为 mysql，属主有可读、可写、可执行的权限；与属主同组的其他用户有可读和可执行的权限；其他用户也有可读和可执行的权限。

对于 root 用户来说，一般情况下，文件的权限对其不起作用。

### 更改文件属性

**1、chgrp：更改文件属组**

语法：

```shell
chgrp [-R] 属组名 文件名
```

参数选项

- -R：递归更改文件属组，就是在更改某个目录文件的属组时，如果加上-R的参数，那么该目录下的所有文件的属组都会更改。

**2、chown：更改文件属主，也可以同时更改文件属组**

语法：

```
chown [–R] 属主名 文件名
chown [-R] 属主名：属组名 文件名
```

进入 /root 目录（~）将`install.log`的拥有者改为bin这个账号：

```
[root@www ~] cd ~
[root@www ~]# chown bin install.log
[root@www ~]# ls -l
-rw-r--r--  1 bin  users 68495 Jun 25 08:53 install.log
```

将install.log的拥有者与群组改回为root：

```
[root@www ~]# chown root:root install.log
[root@www ~]# ls -l
-rw-r--r--  1 root root 68495 Jun 25 08:53 install.log
```

**3、chmod：更改文件9个属性**

Linux文件属性有两种设置方法，一种是数字，一种是符号。

Linux文件的基本权限就有九个，分别是owner/group/others三种身份各有自己的read/write/execute权限。

先复习一下刚刚上面提到的数据：文件的权限字符为：『-rwxrwxrwx』， 这九个权限是三个三个一组的！其中，我们可以使用数字来代表各个权限，各权限的分数对照表如下：

- r:4
- w:2
- x:1

每种身份(owner/group/others)各自的三个权限(r/w/x)分数是需要累加的，例如当权限为： [-rwxrwx---] 分数则是：

- owner = rwx = 4+2+1 = 7
- group = rwx = 4+2+1 = 7
- others= --- = 0+0+0 = 0

所以等一下我们设定权限的变更时，该文件的权限数字就是770啦！变更权限的指令chmod的语法是这样的：

```
 chmod [-R] xyz 文件或目录
```

选项与参数：

- xyz : 就是刚刚提到的数字类型的权限属性，为 rwx 属性数值的相加。
- -R : 进行递归(recursive)的持续变更，亦即连同次目录下的所有文件都会变更

举例来说，如果要将.bashrc这个文件所有的权限都设定启用，那么命令如下：

```
[root@www ~]# ls -al .bashrc
-rw-r--r--  1 root root 395 Jul  4 11:45 .bashrc
[root@www ~]# chmod 777 .bashrc
[root@www ~]# ls -al .bashrc
-rwxrwxrwx  1 root root 395 Jul  4 11:45 .bashrc
```

那如果要将权限变成 *-rwxr-xr--* 呢？那么权限的分数就成为 [4+2+1][4+0+1][4+0+0]=754。

#### 符号类型改变文件权限

还有一个改变权限的方法，从之前的介绍中我们可以发现，基本上就九个权限分别是：

- (1)user
- (2)group
- (3)others

那么我们就可以使用 **u, g, o** 来代表三种身份的权限！

此外， **a** 则代表 **all**，即全部的身份。读写的权限可以写成 **r, w, x**，也就是可以使用下表的方式来看：



| chmod | u g o a | +(加入) -(除去) =(设定) | r w x | 文件或目录 |
| ----- | ------- | ----------------------- | ----- | ---------- |
|       |         |                         |       |            |

如果我们需要将文件权限设置为 **-rwxr-xr--** ，可以使用 **chmod u=rwx,g=rx,o=r 文件名** 来设定:

```
#  touch test1    // 创建 test1 文件
# ls -al test1    // 查看 test1 默认权限
-rw-r--r-- 1 root root 0 Nov 15 10:32 test1
# chmod u=rwx,g=rx,o=r  test1    // 修改 test1 权限
# ls -al test1
-rwxr-xr-- 1 root root 0 Nov 15 10:32 test1
```

而如果是要将权限去掉而不改变其他已存在的权限呢？例如要拿掉全部人的可执行权限，则：

```
#  chmod  a-x test1
# ls -al test1
-rw-r--r-- 1 root root 0 Nov 15 10:32 test1
```



# Linux 文件与目录管理

我们知道Linux的目录结构为树状结构，最顶级的目录为根目录 /。

其他目录通过挂载可以将它们添加到树中，通过解除挂载可以移除它们。

在开始本教程前我们需要先知道什么是绝对路径与相对路径。

- **绝对路径：**
  路径的写法，由根目录 / 写起，例如： /usr/share/doc 这个目录。
- **相对路径：**
  路径的写法，不是由 / 写起，例如由 /usr/share/doc 要到 /usr/share/man 底下时，可以写成： cd ../man 这就是相对路径的写法啦！

------

## 处理目录的常用命令

接下来我们就来看几个常见的处理目录的命令吧：

- ls: 列出目录及文件名
- cd：切换目录
- pwd：显示目前的目录
- mkdir：创建一个新的目录
- rmdir：删除一个空的目录
- cp: 复制文件或目录
- rm: 移除文件或目录
- mv: 移动文件与目录，或修改文件与目录的名称

你可以使用 *man [命令]* 来查看各个命令的使用文档，如 ：man cp。

### ls (列出目录)

在Linux系统当中， ls 命令可能是最常被运行的。

语法：

```
[root@www ~]# ls [-aAdfFhilnrRSt] 目录名称
[root@www ~]# ls [--color={never,auto,always}] 目录名称
[root@www ~]# ls [--full-time] 目录名称
```

选项与参数：

- -a ：全部的文件，连同隐藏文件( 开头为 . 的文件) 一起列出来(常用)
- -d ：仅列出目录本身，而不是列出目录内的文件数据(常用)
- -l ：长数据串列出，包含文件的属性与权限等等数据；(常用)

将家目录下的所有文件列出来(含属性与隐藏档)

```
[root@www ~]# ls -al ~
```

### cd (切换目录)

cd是Change Directory的缩写，这是用来变换工作目录的命令。

语法：

```
 cd [相对路径或绝对路径]
#使用 mkdir 命令创建 runoob 目录
[root@www ~]# mkdir runoob

#使用绝对路径切换到 runoob 目录
[root@www ~]# cd /root/runoob/

#使用相对路径切换到 runoob 目录
[root@www ~]# cd ./runoob/

# 表示回到自己的家目录，亦即是 /root 这个目录
[root@www runoob]# cd ~

# 表示去到目前的上一级目录，亦即是 /root 的上一级目录的意思；
[root@www ~]# cd ..
```

接下来大家多操作几次应该就可以很好的理解 cd 命令的。

### pwd (显示目前所在的目录)

pwd 是 **Print Working Directory** 的缩写，也就是显示目前所在目录的命令。

```
[root@www ~]# pwd [-P]
```

选项与参数：

- **-P** ：显示出确实的路径，而非使用连结 (link) 路径。

实例：单纯显示出目前的工作目录：

```
[root@www ~]# pwd
/root   <== 显示出目录啦～
```

实例显示出实际的工作目录，而非连结档本身的目录名而已。

```
[root@www ~]# cd /var/mail   <==注意，/var/mail是一个连结档
[root@www mail]# pwd
/var/mail         <==列出目前的工作目录
[root@www mail]# pwd -P
/var/spool/mail   <==怎么回事？有没有加 -P 差很多～
[root@www mail]# ls -ld /var/mail
lrwxrwxrwx 1 root root 10 Sep  4 17:54 /var/mail -> spool/mail
# 看到这里应该知道为啥了吧？因为 /var/mail 是连结档，连结到 /var/spool/mail 
# 所以，加上 pwd -P 的选项后，会不以连结档的数据显示，而是显示正确的完整路径啊！
```

### mkdir (创建新目录)

如果想要创建新的目录的话，那么就使用mkdir (make directory)吧。

语法：

```
mkdir [-mp] 目录名称
```

选项与参数：

- -m ：配置文件的权限喔！直接配置，不需要看默认权限 (umask) 的脸色～
- -p ：帮助你直接将所需要的目录(包含上一级目录)递归创建起来！

实例：请到/tmp底下尝试创建数个新目录看看：

```
[root@www ~]# cd /tmp
[root@www tmp]# mkdir test    <==创建一名为 test 的新目录
[root@www tmp]# mkdir test1/test2/test3/test4
mkdir: cannot create directory `test1/test2/test3/test4': 
No such file or directory       <== 没办法直接创建此目录啊！
[root@www tmp]# mkdir -p test1/test2/test3/test4
```

加了这个 -p 的选项，可以自行帮你创建多层目录！

实例：创建权限为 **rwx--x--x** 的目录。

```
[root@www tmp]# mkdir -m 711 test2
[root@www tmp]# ls -l
drwxr-xr-x  3 root  root 4096 Jul 18 12:50 test
drwxr-xr-x  3 root  root 4096 Jul 18 12:53 test1
drwx--x--x  2 root  root 4096 Jul 18 12:54 test2
```

上面的权限部分，如果没有加上 -m 来强制配置属性，系统会使用默认属性。

如果我们使用 -m ，如上例我们给予 -m 711 来给予新的目录 drwx--x--x 的权限。

### rmdir (删除空的目录)

语法：

```
 rmdir [-p] 目录名称
```

选项与参数：

- **-p ：**连同上一级『空的』目录也一起删除

删除 runoob 目录

```
[root@www tmp]# rmdir runoob/
```

将 mkdir 实例中创建的目录(/tmp 底下)删除掉！

```
[root@www tmp]# ls -l   <==看看有多少目录存在？
drwxr-xr-x  3 root  root 4096 Jul 18 12:50 test
drwxr-xr-x  3 root  root 4096 Jul 18 12:53 test1
drwx--x--x  2 root  root 4096 Jul 18 12:54 test2
[root@www tmp]# rmdir test   <==可直接删除掉，没问题
[root@www tmp]# rmdir test1  <==因为尚有内容，所以无法删除！
rmdir: `test1': Directory not empty
[root@www tmp]# rmdir -p test1/test2/test3/test4
[root@www tmp]# ls -l        <==您看看，底下的输出中test与test1不见了！
drwx--x--x  2 root  root 4096 Jul 18 12:54 test2
```

利用 -p 这个选项，立刻就可以将 test1/test2/test3/test4 一次删除。

不过要注意的是，这个 rmdir 仅能删除空的目录，你可以使用 rm 命令来删除非空目录。

### cp (复制文件或目录)

cp 即拷贝文件和目录。

语法:

```
[root@www ~]# cp [-adfilprsu] 来源档(source) 目标档(destination)
[root@www ~]# cp [options] source1 source2 source3 .... directory
```

选项与参数：

- **-a：**相当於 -pdr 的意思，至於 pdr 请参考下列说明；(常用)
- **-d：**若来源档为连结档的属性(link file)，则复制连结档属性而非文件本身；
- **-f：**为强制(force)的意思，若目标文件已经存在且无法开启，则移除后再尝试一次；
- **-i：**若目标档(destination)已经存在时，在覆盖时会先询问动作的进行(常用)
- **-l：**进行硬式连结(hard link)的连结档创建，而非复制文件本身；
- **-p：**连同文件的属性一起复制过去，而非使用默认属性(备份常用)；
- **-r：**递归持续复制，用於目录的复制行为；(常用)
- **-s：**复制成为符号连结档 (symbolic link)，亦即『捷径』文件；
- **-u：**若 destination 比 source 旧才升级 destination ！

用 root 身份，将 root 目录下的 .bashrc 复制到 /tmp 下，并命名为 bashrc

```
[root@www ~]# cp ~/.bashrc /tmp/bashrc
[root@www ~]# cp -i ~/.bashrc /tmp/bashrc
cp: overwrite `/tmp/bashrc'? n  <==n不覆盖，y为覆盖
```

### rm (移除文件或目录)

语法：

```
 rm [-fir] 文件或目录
```

选项与参数：

- -f ：就是 force 的意思，忽略不存在的文件，不会出现警告信息；
- -i ：互动模式，在删除前会询问使用者是否动作
- -r ：递归删除啊！最常用在目录的删除了！这是非常危险的选项！！！
- 

将刚刚在 cp 的实例中创建的 bashrc 删除掉！

```
[root@www tmp]# rm -i bashrc
rm: remove regular file `bashrc'? y
```

如果加上 -i 的选项就会主动询问喔，避免你删除到错误的档名！

### mv (移动文件与目录，或修改名称)

语法：

```
[root@www ~]# mv [-fiu] source destination
[root@www ~]# mv [options] source1 source2 source3 .... directory
```

选项与参数：

- -f ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；
- -i ：若目标文件 (destination) 已经存在时，就会询问是否覆盖！
- -u ：若目标文件已经存在，且 source 比较新，才会升级 (update)

复制一文件，创建一目录，将文件移动到目录中

```
[root@www ~]# cd /tmp
[root@www tmp]# cp ~/.bashrc bashrc
[root@www tmp]# mkdir mvtest
[root@www tmp]# mv bashrc mvtest
```

将某个文件移动到某个目录去，就是这样做！

将刚刚的目录名称更名为 mvtest2

```
[root@www tmp]# mv mvtest mvtest2
```

------

## Linux 文件内容查看

Linux系统中使用以下命令来查看文件的内容：

- cat 由第一行开始显示文件内容
- tac 从最后一行开始显示，可以看出 tac 是 cat 的倒着写！
- nl  显示的时候，顺道输出行号！
- more 一页一页的显示文件内容
- less 与 more 类似，但是比 more 更好的是，他可以往前翻页！
- head 只看头几行
- tail 只看尾巴几行

你可以使用 *man [命令]*来查看各个命令的使用文档，如 ：man cp。

### cat

由第一行开始显示文件内容

语法：

```
cat [-AbEnTv]
```

选项与参数：

- -A ：相当於 -vET 的整合选项，可列出一些特殊字符而不是空白而已；
- -b ：列出行号，仅针对非空白行做行号显示，空白行不标行号！
- -E ：将结尾的断行字节 $ 显示出来；
- -n ：列印出行号，连同空白行也会有行号，与 -b 的选项不同；
- -T ：将 [tab] 按键以 ^I 显示出来；
- -v ：列出一些看不出来的特殊字符

检看 /etc/issue 这个文件的内容：

```
[root@www ~]# cat /etc/issue
CentOS release 6.4 (Final)
Kernel \r on an \m
```

### tac

tac与cat命令刚好相反，文件内容从最后一行开始显示，可以看出 tac 是 cat 的倒着写！如：

```
[root@www ~]# tac /etc/issue

Kernel \r on an \m
CentOS release 6.4 (Final)
```

### nl

显示行号

语法：

```
nl [-bnw] 文件
```

选项与参数：

- -b ：指定行号指定的方式，主要有两种：
  -b a ：表示不论是否为空行，也同样列出行号(类似 cat -n)；
  -b t ：如果有空行，空的那一行不要列出行号(默认值)；
- -n ：列出行号表示的方法，主要有三种：
  -n ln ：行号在荧幕的最左方显示；
  -n rn ：行号在自己栏位的最右方显示，且不加 0 ；
  -n rz ：行号在自己栏位的最右方显示，且加 0 ；
- -w ：行号栏位的占用的位数。

实例一：用 nl 列出 /etc/issue 的内容

```
[root@www ~]# nl /etc/issue
     1  CentOS release 6.4 (Final)
     2  Kernel \r on an \m
```

### more

一页一页翻动

```
[root@www ~]# more /etc/man_db.config 
#
# Generated automatically from man.conf.in by the
# configure script.
#
# man.conf from man-1.6d
....(中间省略)....
--More--(28%)  <== 重点在这一行喔！你的光标也会在这里等待你的命令
```

在 more 这个程序的运行过程中，你有几个按键可以按的：

- 空白键 (space)：代表向下翻一页；
- Enter     ：代表向下翻『一行』；
- /字串     ：代表在这个显示的内容当中，向下搜寻『字串』这个关键字；
- :f      ：立刻显示出档名以及目前显示的行数；
- q       ：代表立刻离开 more ，不再显示该文件内容。
- b 或 [ctrl]-b ：代表往回翻页，不过这动作只对文件有用，对管线无用。

### less

一页一页翻动，以下实例输出/etc/man.config文件的内容：

```
[root@www ~]# less /etc/man.config
#
# Generated automatically from man.conf.in by the
# configure script.
#
# man.conf from man-1.6d
....(中间省略)....
:   <== 这里可以等待你输入命令！
```

less运行时可以输入的命令有：

- 空白键  ：向下翻动一页；
- [pagedown]：向下翻动一页；
- [pageup] ：向上翻动一页；
- /字串   ：向下搜寻『字串』的功能；
- ?字串   ：向上搜寻『字串』的功能；
- n     ：重复前一个搜寻 (与 / 或 ? 有关！)
- N     ：反向的重复前一个搜寻 (与 / 或 ? 有关！)
- q     ：离开 less 这个程序；

### head

取出文件前面几行

语法：

```
head [-n number] 文件 
```

选项与参数：

- -n ：后面接数字，代表显示几行的意思

```
[root@www ~]# head /etc/man.config
```

默认的情况中，显示前面 10 行！若要显示前 20 行，就得要这样：

```
[root@www ~]# head -n 20 /etc/man.config
```

### tail

取出文件后面几行

语法：

```
tail [-n number] 文件 
```

选项与参数：

- -n ：后面接数字，代表显示几行的意思
- -f ：表示持续侦测后面所接的档名，要等到按下[ctrl]-c才会结束tail的侦测

```
[root@www ~]# tail /etc/man.config
# 默认的情况中，显示最后的十行！若要显示最后的 20 行，就得要这样：
[root@www ~]# tail -n 20 /etc/man.config
```



### 1.Linux 链接概念

Linux 链接分两种，一种被称为硬链接（Hard Link），另一种被称为符号链接（Symbolic Link）。默认情况下，**ln** 命令产生硬链接。

**硬连接**

硬连接指通过索引节点来进行连接。在 Linux 的文件系统中，保存在磁盘分区中的文件不管是什么类型都给它分配一个编号，称为索引节点号(Inode Index)。在 Linux 中，多个文件名指向同一索引节点是存在的。比如：A 是 B 的硬链接（A 和 B 都是文件名），则 A 的目录项中的 inode 节点号与 B 的目录项中的 inode 节点号相同，即一个 inode 节点对应两个不同的文件名，两个文件名指向同一个文件，A 和 B 对文件系统来说是完全平等的。删除其中任何一个都不会影响另外一个的访问。

硬连接的作用是允许一个文件拥有多个有效路径名，这样用户就可以建立硬连接到重要文件，以防止“误删”的功能。其原因如上所述，因为对应该目录的索引节点有一个以上的连接。只删除一个连接并不影响索引节点本身和其它的连接，只有当最后一个连接被删除后，文件的数据块及目录的连接才会被释放。也就是说，文件真正删除的条件是与之相关的所有硬连接文件均被删除。

**软连接**

另外一种连接称之为符号连接（Symbolic Link），也叫软连接。软链接文件有类似于 Windows 的快捷方式。它实际上是一个特殊的文件。在符号连接中，文件实际上是一个文本文件，其中包含的有另一文件的位置信息。比如：A 是 B 的软链接（A 和 B 都是文件名），A 的目录项中的 inode 节点号与 B 的目录项中的 inode 节点号不相同，A 和 B 指向的是两个不同的 inode，继而指向两块不同的数据块。但是 A 的数据块中存放的只是 B 的路径名（可以根据这个找到 B 的目录项）。A 和 B 之间是“主从”关系，如果 B 被删除了，A 仍然存在（因为两个是不同的文件），但指向的是一个无效的链接。

### 2.通过实验加深理解

```
[oracle@Linux]$ touch f1          #创建一个测试文件f1
[oracle@Linux]$ ln f1 f2          #创建f1的一个硬连接文件f2
[oracle@Linux]$ ln -s f1 f3       #创建f1的一个符号连接文件f3
[oracle@Linux]$ ls -li            # -i参数显示文件的inode节点信息
total 0
9797648 -rw-r--r--  2 oracle oinstall 0 Apr 21 08:11 f1
9797648 -rw-r--r--  2 oracle oinstall 0 Apr 21 08:11 f2
9797649 lrwxrwxrwx  1 oracle oinstall 2 Apr 21 08:11 f3 -> f1
```

从上面的结果中可以看出，硬连接文件 f2 与原文件 f1 的 inode 节点相同，均为 9797648，然而符号连接文件的 inode 节点不同。

```
[oracle@Linux]$ echo "I am f1 file" >>f1
[oracle@Linux]$ cat f1
I am f1 file
[oracle@Linux]$ cat f2
I am f1 file
[oracle@Linux]$ cat f3
I am f1 file
[oracle@Linux]$ rm -f f1
[oracle@Linux]$ cat f2
I am f1 file
[oracle@Linux]$ cat f3
cat: f3: No such file or directory
```

通过上面的测试可以看出：当删除原始文件 f1 后，硬连接 f2 不受影响，但是符号连接 f1 文件无效

### 3.总结

依此您可以做一些相关的测试，可以得到以下全部结论：

-  1).删除符号连接f3,对f1,f2无影响；
-  2).删除硬连接f2，对f1,f3也无影响；
-  3).删除原文件f1，对硬连接f2没有影响，导致符号连接f3失效；
-  4).同时删除原文件f1,硬连接f2，整个文件会真正的被删除。

# Linux 用户和用户组管理

Linux系统是一个多用户多任务的分时操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。

用户的账号一方面可以帮助系统管理员对使用系统的用户进行跟踪，并控制他们对系统资源的访问；另一方面也可以帮助用户组织文件，并为用户提供安全性保护。

每个用户账号都拥有一个唯一的用户名和各自的口令。

用户在登录时键入正确的用户名和口令后，就能够进入系统和自己的主目录。

实现用户账号的管理，要完成的工作主要有如下几个方面：

- 用户账号的添加、删除与修改。
- 用户口令的管理。
- 用户组的管理。

------

## 一、Linux系统用户账号的管理

用户账号的管理工作主要涉及到用户账号的添加、修改和删除。

添加用户账号就是在系统中创建一个新账号，然后为新账号分配用户号、用户组、主目录和登录Shell等资源。刚添加的账号是被锁定的，无法使用。

### 1、添加新的用户账号使用useradd命令，其语法如下：

```
useradd 选项 用户名
```

参数说明：

- 选项:

  - -c comment 指定一段注释性描述。
  - -d 目录 指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。
  - -g 用户组 指定用户所属的用户组。
  - -G 用户组，用户组 指定用户所属的附加组。
  - -s Shell文件 指定用户的登录Shell。
  - -u 用户号 指定用户的用户号，如果同时有-o选项，则可以重复使用其他用户的标识号。

- 用户名:

  指定新账号的登录名。

#### 实例1

```
# useradd –d  /home/sam -m sam
```

此命令创建了一个用户sam，其中-d和-m选项用来为登录名sam产生一个主目录 /home/sam（/home为默认的用户主目录所在的父目录）。

#### 实例2

```
# useradd -s /bin/sh -g group –G adm,root gem
```

此命令新建了一个用户gem，该用户的登录Shell是 `/bin/sh`，它属于group用户组，同时又属于adm和root用户组，其中group用户组是其主组。

这里可能新建组：`#groupadd group及groupadd adm`

增加用户账号就是在/etc/passwd文件中为新用户增加一条记录，同时更新其他系统文件如/etc/shadow, /etc/group等。

Linux提供了集成的系统管理工具userconf，它可以用来对用户账号进行统一管理。

### 2、删除帐号

如果一个用户的账号不再使用，可以从系统中删除。删除用户账号就是要将/etc/passwd等系统文件中的该用户记录删除，必要时还删除用户的主目录。

删除一个已有的用户账号使用`userdel`命令，其格式如下：

```
userdel 选项 用户名
```

常用的选项是 **-r**，它的作用是把用户的主目录一起删除。

例如：

```
# userdel -r sam
```

此命令删除用户sam在系统文件中（主要是/etc/passwd, /etc/shadow, /etc/group等）的记录，同时删除用户的主目录。

### 3、修改帐号

修改用户账号就是根据实际情况更改用户的有关属性，如用户号、主目录、用户组、登录Shell等。

修改已有用户的信息使用`usermod`命令，其格式如下：

```
usermod 选项 用户名
```

常用的选项包括`-c, -d, -m, -g, -G, -s, -u以及-o等`，这些选项的意义与`useradd`命令中的选项一样，可以为用户指定新的资源值。

另外，有些系统可以使用选项：-l 新用户名

这个选项指定一个新的账号，即将原来的用户名改为新的用户名。

例如：

```
# usermod -s /bin/ksh -d /home/z –g developer sam
```

此命令将用户sam的登录Shell修改为ksh，主目录改为/home/z，用户组改为developer。

### 4、用户口令的管理

用户管理的一项重要内容是用户口令的管理。用户账号刚创建时没有口令，但是被系统锁定，无法使用，必须为其指定口令后才可以使用，即使是指定空口令。

指定和修改用户口令的Shell命令是`passwd`。超级用户可以为自己和其他用户指定口令，普通用户只能用它修改自己的口令。命令的格式为：

```
passwd 选项 用户名
```

可使用的选项：

- -l 锁定口令，即禁用账号。
- -u 口令解锁。
- -d 使账号无口令。
- -f 强迫用户下次登录时修改口令。

如果默认用户名，则修改当前用户的口令。

例如，假设当前用户是sam，则下面的命令修改该用户自己的口令：

```
$ passwd 
Old password:****** 
New password:******* 
Re-enter new password:*******
```

如果是超级用户，可以用下列形式指定任何用户的口令：

```
# passwd sam 
New password:******* 
Re-enter new password:*******
```

普通用户修改自己的口令时，passwd命令会先询问原口令，验证后再要求用户输入两遍新口令，如果两次输入的口令一致，则将这个口令指定给用户；而超级用户为用户指定口令时，就不需要知道原口令。

为了系统安全起见，用户应该选择比较复杂的口令，例如最好使用8位长的口令，口令中包含有大写、小写字母和数字，并且应该与姓名、生日等不相同。

为用户指定空口令时，执行下列形式的命令：

```
# passwd -d sam
```

此命令将用户 sam 的口令删除，这样用户 sam 下一次登录时，系统就不再允许该用户登录了。

passwd 命令还可以用 -l(lock) 选项锁定某一用户，使其不能登录，例如：

```
# passwd -l sam
```

------

## 二、Linux系统用户组的管理

每个用户都有一个用户组，系统可以对一个用户组中的所有用户进行集中管理。不同Linux 系统对用户组的规定有所不同，如Linux下的用户属于与它同名的用户组，这个用户组在创建用户时同时创建。

用户组的管理涉及用户组的添加、删除和修改。组的增加、删除和修改实际上就是对/etc/group文件的更新。

### 1、增加一个新的用户组使用groupadd命令。其格式如下：

```
groupadd 选项 用户组
```

可以使用的选项有：

- -g GID 指定新用户组的组标识号（GID）。
- -o 一般与-g选项同时使用，表示新用户组的GID可以与系统已有用户组的GID相同。

#### 实例1：

```
# groupadd group1
```

此命令向系统中增加了一个新组group1，新组的组标识号是在当前已有的最大组标识号的基础上加1。

#### 实例2：

```
# groupadd -g 101 group2
```

此命令向系统中增加了一个新组group2，同时指定新组的组标识号是101。

### 2、如果要删除一个已有的用户组，使用groupdel命令，其格式如下：

```
groupdel 用户组
```

#### 例如：

```
# groupdel group1
```

此命令从系统中删除组group1。

### 3、修改用户组的属性使用groupmod命令。其语法如下：

```
groupmod 选项 用户组
```

常用的选项有：

- -g GID 为用户组指定新的组标识号。
- -o 与-g选项同时使用，用户组的新GID可以与系统已有用户组的GID相同。
- -n新用户组 将用户组的名字改为新名字

#### 实例1：

```
# groupmod -g 102 group2
```

此命令将组group2的组标识号修改为102。

#### 实例2：

```
# groupmod –g 10000 -n group3 group2
```

此命令将组group2的标识号改为10000，组名修改为group3。

### 4、如果一个用户同时属于多个用户组，那么用户可以在用户组之间切换，以便具有其他用户组的权限。

用户可以在登录后，使用命令newgrp切换到其他用户组，这个命令的参数就是目的用户组。例如：

```
$ newgrp root
```

这条命令将当前用户切换到root用户组，前提条件是root用户组确实是该用户的主组或附加组。类似于用户账号的管理，用户组的管理也可以通过集成的系统管理工具来完成。

------

## 三、与用户账号有关的系统文件

完成用户管理的工作有许多种方法，但是每一种方法实际上都是对有关的系统文件进行修改。

与用户和用户组相关的信息都存放在一些系统文件中，这些文件包括/etc/passwd, /etc/shadow, /etc/group等。

下面分别介绍这些文件的内容。

### 1、/etc/passwd文件是用户管理工作涉及的最重要的一个文件。

Linux系统中的每个用户都在/etc/passwd文件中有一个对应的记录行，它记录了这个用户的一些基本属性。

这个文件对所有用户都是可读的。它的内容类似下面的例子：

```
＃ cat /etc/passwd

root:x:0:0:Superuser:/:
daemon:x:1:1:System daemons:/etc:
bin:x:2:2:Owner of system commands:/bin:
sys:x:3:3:Owner of system files:/usr/sys:
adm:x:4:4:System accounting:/usr/adm:
uucp:x:5:5:UUCP administrator:/usr/lib/uucp:
auth:x:7:21:Authentication administrator:/tcb/files/auth:
cron:x:9:16:Cron daemon:/usr/spool/cron:
listen:x:37:4:Network daemon:/usr/net/nls:
lp:x:71:18:Printer administrator:/usr/spool/lp:
sam:x:200:50:Sam san:/home/sam:/bin/sh
```

从上面的例子我们可以看到，/etc/passwd中一行记录对应着一个用户，每行记录又被冒号(:)分隔为7个字段，其格式和具体含义如下：

```
用户名:口令:用户标识号:组标识号:注释性描述:主目录:登录Shell
```

### 1）"用户名"是代表用户账号的字符串。

通常长度不超过8个字符，并且由大小写字母和/或数字组成。登录名中不能有冒号(:)，因为冒号在这里是分隔符。

为了兼容起见，登录名中最好不要包含点字符(.)，并且不使用连字符(-)和加号(+)打头。

### 2）“口令”一些系统中，存放着加密后的用户口令字。

虽然这个字段存放的只是用户口令的加密串，不是明文，但是由于/etc/passwd文件对所有用户都可读，所以这仍是一个安全隐患。因此，现在许多Linux 系统（如SVR4）都使用了shadow技术，把真正的加密后的用户口令字存放到/etc/shadow文件中，而在/etc/passwd文件的口令字段中只存放一个特殊的字符，例如“x”或者“*”。

### 3）“用户标识号”是一个整数，系统内部用它来标识用户。

一般情况下它与用户名是一一对应的。如果几个用户名对应的用户标识号是一样的，系统内部将把它们视为同一个用户，但是它们可以有不同的口令、不同的主目录以及不同的登录Shell等。

通常用户标识号的取值范围是0～65 535。0是超级用户root的标识号，1～99由系统保留，作为管理账号，普通用户的标识号从100开始。在Linux系统中，这个界限是500。

### 4）“组标识号”字段记录的是用户所属的用户组。

它对应着/etc/group文件中的一条记录。

### 5)“注释性描述”字段记录着用户的一些个人情况。

例如用户的真实姓名、电话、地址等，这个字段并没有什么实际的用途。在不同的Linux 系统中，这个字段的格式并没有统一。在许多Linux系统中，这个字段存放的是一段任意的注释性描述文字，用做finger命令的输出。

### 6)“主目录”，也就是用户的起始工作目录。

它是用户在登录到系统之后所处的目录。在大多数系统中，各用户的主目录都被组织在同一个特定的目录下，而用户主目录的名称就是该用户的登录名。各用户对自己的主目录有读、写、执行（搜索）权限，其他用户对此目录的访问权限则根据具体情况设置。

### 7)用户登录后，要启动一个进程，负责将用户的操作传给内核，这个进程是用户登录到系统后运行的命令解释器或某个特定的程序，即Shell。

Shell是用户与Linux系统之间的接口。Linux的Shell有许多种，每种都有不同的特点。常用的有sh(Bourne Shell), csh(C Shell), ksh(Korn Shell), tcsh(TENEX/TOPS-20 type C Shell), bash(Bourne Again Shell)等。

系统管理员可以根据系统情况和用户习惯为用户指定某个Shell。如果不指定Shell，那么系统使用sh为默认的登录Shell，即这个字段的值为/bin/sh。

用户的登录Shell也可以指定为某个特定的程序（此程序不是一个命令解释器）。

利用这一特点，我们可以限制用户只能运行指定的应用程序，在该应用程序运行结束后，用户就自动退出了系统。有些Linux 系统要求只有那些在系统中登记了的程序才能出现在这个字段中。

### 8)系统中有一类用户称为伪用户（pseudo users）。

这些用户在/etc/passwd文件中也占有一条记录，但是不能登录，因为它们的登录Shell为空。它们的存在主要是方便系统管理，满足相应的系统进程对文件属主的要求。

常见的伪用户如下所示：

```
伪 用 户 含 义 
bin 拥有可执行的用户命令文件 
sys 拥有系统文件 
adm 拥有帐户文件 
uucp UUCP使用 
lp lp或lpd子系统使用 
nobody NFS使用
```

------

## 拥有帐户文件

**1、除了上面列出的伪用户外，还有许多标准的伪用户，例如：audit, cron, mail, usenet等，它们也都各自为相关的进程和文件所需要。**

由于/etc/passwd文件是所有用户都可读的，如果用户的密码太简单或规律比较明显的话，一台普通的计算机就能够很容易地将它破解，因此对安全性要求较高的Linux系统都把加密后的口令字分离出来，单独存放在一个文件中，这个文件是/etc/shadow文件。 有超级用户才拥有该文件读权限，这就保证了用户密码的安全性。

**2、/etc/shadow中的记录行与/etc/passwd中的一一对应，它由pwconv命令根据/etc/passwd中的数据自动产生**

它的文件格式与/etc/passwd类似，由若干个字段组成，字段之间用":"隔开。这些字段是：

```
登录名:加密口令:最后一次修改时间:最小时间间隔:最大时间间隔:警告时间:不活动时间:失效时间:标志
```

1. "登录名"是与/etc/passwd文件中的登录名相一致的用户账号
2. "口令"字段存放的是加密后的用户口令字，长度为13个字符。如果为空，则对应用户没有口令，登录时不需要口令；如果含有不属于集合 { ./0-9A-Za-z }中的字符，则对应的用户不能登录。
3. "最后一次修改时间"表示的是从某个时刻起，到用户最后一次修改口令时的天数。时间起点对不同的系统可能不一样。例如在SCO Linux 中，这个时间起点是1970年1月1日。
4. "最小时间间隔"指的是两次修改口令之间所需的最小天数。
5. "最大时间间隔"指的是口令保持有效的最大天数。
6. "警告时间"字段表示的是从系统开始警告用户到用户密码正式失效之间的天数。
7. "不活动时间"表示的是用户没有登录活动但账号仍能保持有效的最大天数。
8. "失效时间"字段给出的是一个绝对的天数，如果使用了这个字段，那么就给出相应账号的生存期。期满后，该账号就不再是一个合法的账号，也就不能再用来登录了。

下面是/etc/shadow的一个例子：

```
＃ cat /etc/shadow

root:Dnakfw28zf38w:8764:0:168:7:::
daemon:*::0:0::::
bin:*::0:0::::
sys:*::0:0::::
adm:*::0:0::::
uucp:*::0:0::::
nuucp:*::0:0::::
auth:*::0:0::::
cron:*::0:0::::
listen:*::0:0::::
lp:*::0:0::::
sam:EkdiSECLWPdSa:9740:0:0::::
```

### 3、用户组的所有信息都存放在/etc/group文件中。

将用户分组是Linux 系统中对用户进行管理及控制访问权限的一种手段。

每个用户都属于某个用户组；一个组中可以有多个用户，一个用户也可以属于不同的组。

当一个用户同时是多个组中的成员时，在/etc/passwd文件中记录的是用户所属的主组，也就是登录时所属的默认组，而其他组称为附加组。

用户要访问属于附加组的文件时，必须首先使用newgrp命令使自己成为所要访问的组中的成员。

用户组的所有信息都存放在/etc/group文件中。此文件的格式也类似于/etc/passwd文件，由冒号(:)隔开若干个字段，这些字段有：

```
组名:口令:组标识号:组内用户列表
```

1. "组名"是用户组的名称，由字母或数字构成。与/etc/passwd中的登录名一样，组名不应重复。
2. "口令"字段存放的是用户组加密后的口令字。一般Linux 系统的用户组都没有口令，即这个字段一般为空，或者是*。
3. "组标识号"与用户标识号类似，也是一个整数，被系统内部用来标识组。
4. "组内用户列表"是属于这个组的所有用户的列表/b]，不同用户之间用逗号(,)分隔。这个用户组可能是用户的主组，也可能是附加组。

/etc/group文件的一个例子如下：

```
root::0:root
bin::2:root,bin
sys::3:root,uucp
adm::4:root,adm
daemon::5:root,daemon
lp::7:root,lp
users::20:root,sam
```

### 四、添加批量用户

添加和删除用户对每位Linux系统管理员都是轻而易举的事，比较棘手的是如果要添加几十个、上百个甚至上千个用户时，我们不太可能还使用useradd一个一个地添加，必然要找一种简便的创建大量用户的方法。Linux系统提供了创建大量用户的工具，可以让您立即创建大量用户，方法如下：

### （1）先编辑一个文本用户文件。

每一列按照`/etc/passwd`密码文件的格式书写，要注意每个用户的用户名、UID、宿主目录都不可以相同，其中密码栏可以留做空白或输入x号。一个范例文件user.txt内容如下：

```
user001::600:100:user:/home/user001:/bin/bash
user002::601:100:user:/home/user002:/bin/bash
user003::602:100:user:/home/user003:/bin/bash
user004::603:100:user:/home/user004:/bin/bash
user005::604:100:user:/home/user005:/bin/bash
user006::605:100:user:/home/user006:/bin/bash
```

### （2）以root身份执行命令 `/usr/sbin/newusers`，从刚创建的用户文件`user.txt`中导入数据，创建用户：

```
# newusers < user.txt
```

然后可以执行命令 `vipw` 或 `vi /etc/passwd` 检查 `/etc/passwd` 文件是否已经出现这些用户的数据，并且用户的宿主目录是否已经创建。

### （3）执行命令/usr/sbin/pwunconv。

将 `/etc/shadow` 产生的 `shadow` 密码解码，然后回写到 `/etc/passwd` 中，并将`/etc/shadow`的`shadow`密码栏删掉。这是为了方便下一步的密码转换工作，即先取消 `shadow password` 功能。

```
# pwunconv
```

### （4）编辑每个用户的密码对照文件。

格式为：

```
用户名:密码
```

实例文件 `passwd.txt` 内容如下：

```
user001:123456
user002:123456
user003:123456
user004:123456
user005:123456
user006:123456
```

### （5）以 root 身份执行命令 `/usr/sbin/chpasswd`。

创建用户密码，`chpasswd` 会将经过 `/usr/bin/passwd` 命令编码过的密码写入 `/etc/passwd` 的密码栏。

```
# chpasswd < passwd.txt
```

### （6）确定密码经编码写入/etc/passwd的密码栏后。

执行命令 `/usr/sbin/pwconv` 将密码编码为 `shadow password`，并将结果写入 `/etc/shadow`。

```
# pwconv
```

这样就完成了大量用户的创建了，之后您可以到/home下检查这些用户宿主目录的权限设置是否都正确，并登录验证用户密码是否正确。

**提示**：Linux 用户登陆输入密码时，字符是不显示的，这样可以防止别人看见你密码的位数，安全性稍高，若输入错误，可以按Backspace 重新输入。



批量添加用户，采用文中的方式没有成功，不知道是不是我理解不对，在其他地方找到另一种方式，执行成功了。

1、创建一个文件，内容格式和 **/etc/passwd** 一样，如 test.txt 内容如下：

```
us001:X:1000:1000::/home/us001:sbin/bash
us002:X:1001:1001::/home/us002:sbin/bash
```

2、在 tty 输入：

```
[root@localhost~]# newusers test.txt
```

3、创建一个口令文件，内容格式 **用户名:口令**，如 pass.txt 内容如下：

```
us001:123456
us002:123456
```

4、在 tty 输入：

```
[root@localhost~]#  chpasswd <pass.txt
```

使用**[幸福不朽](https://www.runoob.com/linux/linux-user-manage.html#comment-39265)**的方法添加成功了，但是可能登陆然后报错，说明sbin/bash找不到路径

我使用文章中的新增的时候，一直报错，删除/bin/bash前面的斜杠就好了，但是登陆也报错

然后手动将passwd里边的加上斜杠，就行了

# Linux 磁盘管理

Linux磁盘管理好坏直接关系到整个系统的性能问题。

Linux磁盘管理常用三个命令为df、du和fdisk。

- df：列出文件系统的整体磁盘使用量
- du：检查磁盘空间使用量
- fdisk：用于磁盘分区

------

## df

df命令参数功能：检查文件系统的磁盘空间占用情况。可以利用该命令来获取硬盘被占用了多少空间，目前还剩下多少空间等信息。

语法：

```
df [-ahikHTm] [目录或文件名]
```

选项与参数：

- -a ：列出所有的文件系统，包括系统特有的 /proc 等文件系统；
- -k ：以 KBytes 的容量显示各文件系统；
- -m ：以 MBytes 的容量显示各文件系统；
- -h ：以人们较易阅读的 GBytes, MBytes, KBytes 等格式自行显示；
- -H ：以 M=1000K 取代 M=1024K 的进位方式；
- -T ：显示文件系统类型, 连同该 partition 的 filesystem 名称 (例如 ext3) 也列出；
- -i ：不用硬盘容量，而以 inode 的数量来显示

### 实例 1

将系统内所有的文件系统列出来！

```
[root@www ~]# df
Filesystem      1K-blocks      Used Available Use% Mounted on
/dev/hdc2         9920624   3823112   5585444  41% /
/dev/hdc3         4956316    141376   4559108   4% /home
/dev/hdc1          101086     11126     84741  12% /boot
tmpfs              371332         0    371332   0% /dev/shm
```

在 Linux 底下如果 df 没有加任何选项，那么默认会将系统内所有的 (不含特殊内存内的文件系统与 swap) 都以 1 Kbytes 的容量来列出来！

### 实例 2

将容量结果以易读的容量格式显示出来

```
[root@www ~]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/hdc2             9.5G  3.7G  5.4G  41% /
/dev/hdc3             4.8G  139M  4.4G   4% /home
/dev/hdc1              99M   11M   83M  12% /boot
tmpfs                 363M     0  363M   0% /dev/shm
```

### 实例 3

将系统内的所有特殊文件格式及名称都列出来

```
[root@www ~]# df -aT
Filesystem    Type 1K-blocks    Used Available Use% Mounted on
/dev/hdc2     ext3   9920624 3823112   5585444  41% /
proc          proc         0       0         0   -  /proc
sysfs        sysfs         0       0         0   -  /sys
devpts      devpts         0       0         0   -  /dev/pts
/dev/hdc3     ext3   4956316  141376   4559108   4% /home
/dev/hdc1     ext3    101086   11126     84741  12% /boot
tmpfs        tmpfs    371332       0    371332   0% /dev/shm
none   binfmt_misc         0       0         0   -  /proc/sys/fs/binfmt_misc
sunrpc  rpc_pipefs         0       0         0   -  /var/lib/nfs/rpc_pipefs
```

### 实例 4

将 /etc 底下的可用的磁盘容量以易读的容量格式显示

```
[root@www ~]# df -h /etc
Filesystem            Size  Used Avail Use% Mounted on
/dev/hdc2             9.5G  3.7G  5.4G  41% /
```

------

## du

Linux du命令也是查看使用空间的，但是与df命令不同的是Linux du命令是对文件和目录磁盘使用的空间的查看，还是和df命令有一些区别的，这里介绍Linux du命令。

语法：

```
du [-ahskm] 文件或目录名称
```

选项与参数：

- -a ：列出所有的文件与目录容量，因为默认仅统计目录底下的文件量而已。
- -h ：以人们较易读的容量格式 (G/M) 显示；
- -s ：列出总量而已，而不列出每个各别的目录占用容量；
- -S ：不包括子目录下的总计，与 -s 有点差别。
- -k ：以 KBytes 列出容量显示；
- -m ：以 MBytes 列出容量显示；

### 实例 1

只列出当前目录下的所有文件夹容量（包括隐藏文件夹）:

```
[root@www ~]# du
8       ./test4     <==每个目录都会列出来
8       ./test2
....中间省略....
12      ./.gconfd   <==包括隐藏文件的目录
220     .           <==这个目录(.)所占用的总量
```

直接输入 du 没有加任何选项时，则 du 会分析当前所在目录的文件与目录所占用的硬盘空间。

### 实例 2

将文件的容量也列出来

```
[root@www ~]# du -a
12      ./install.log.syslog   <==有文件的列表了
8       ./.bash_logout
8       ./test4
8       ./test2
....中间省略....
12      ./.gconfd
220     .
```

### 实例 3

检查根目录底下每个目录所占用的容量

```
[root@www ~]# du -sm /*
7       /bin
6       /boot
.....中间省略....
0       /proc
.....中间省略....
1       /tmp
3859    /usr     <==系统初期最大就是他了啦！
77      /var
```

通配符 * 来代表每个目录。

与 df 不一样的是，du 这个命令其实会直接到文件系统内去搜寻所有的文件数据。

------

## fdisk

fdisk 是 Linux 的磁盘分区表操作工具。

语法：

```
fdisk [-l] 装置名称
```

选项与参数：

- -l ：输出后面接的装置所有的分区内容。若仅有 fdisk -l 时， 则系统将会把整个系统内能够搜寻到的装置的分区均列出来。

### 实例 1

列出所有分区信息

```
[root@AY120919111755c246621 tmp]# fdisk -l

Disk /dev/xvda: 21.5 GB, 21474836480 bytes
255 heads, 63 sectors/track, 2610 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

    Device Boot      Start         End      Blocks   Id  System
/dev/xvda1   *           1        2550    20480000   83  Linux
/dev/xvda2            2550        2611      490496   82  Linux swap / Solaris

Disk /dev/xvdb: 21.5 GB, 21474836480 bytes
255 heads, 63 sectors/track, 2610 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x56f40944

    Device Boot      Start         End      Blocks   Id  System
/dev/xvdb2               1        2610    20964793+  83  Linux
```

### 实例 2

找出你系统中的根目录所在磁盘，并查阅该硬盘内的相关信息

```
[root@www ~]# df /            <==注意：重点在找出磁盘文件名而已
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/hdc2              9920624   3823168   5585388  41% /

[root@www ~]# fdisk /dev/hdc  <==仔细看，不要加上数字喔！
The number of cylinders for this disk is set to 5005.
There is nothing wrong with that, but this is larger than 1024,
and could in certain setups cause problems with:
1) software that runs at boot time (e.g., old versions of LILO)
2) booting and partitioning software from other OSs
   (e.g., DOS FDISK, OS/2 FDISK)

Command (m for help):     <==等待你的输入！
```

输入 m 后，就会看到底下这些命令介绍

```
Command (m for help): m   <== 输入 m 后，就会看到底下这些命令介绍
Command action
   a   toggle a bootable flag
   b   edit bsd disklabel
   c   toggle the dos compatibility flag
   d   delete a partition            <==删除一个partition
   l   list known partition types
   m   print this menu
   n   add a new partition           <==新增一个partition
   o   create a new empty DOS partition table
   p   print the partition table     <==在屏幕上显示分割表
   q   quit without saving changes   <==不储存离开fdisk程序
   s   create a new empty Sun disklabel
   t   change a partition's system id
   u   change display/entry units
   v   verify the partition table
   w   write table to disk and exit  <==将刚刚的动作写入分割表
   x   extra functionality (experts only)
```

离开 fdisk 时按下 `q`，那么所有的动作都不会生效！相反的， 按下`w`就是动作生效的意思。

```
Command (m for help): p  <== 这里可以输出目前磁盘的状态

Disk /dev/hdc: 41.1 GB, 41174138880 bytes        <==这个磁盘的文件名与容量
255 heads, 63 sectors/track, 5005 cylinders      <==磁头、扇区与磁柱大小
Units = cylinders of 16065 * 512 = 8225280 bytes <==每个磁柱的大小

   Device Boot      Start         End      Blocks   Id  System
/dev/hdc1   *           1          13      104391   83  Linux
/dev/hdc2              14        1288    10241437+  83  Linux
/dev/hdc3            1289        1925     5116702+  83  Linux
/dev/hdc4            1926        5005    24740100    5  Extended
/dev/hdc5            1926        2052     1020096   82  Linux swap / Solaris
# 装置文件名 启动区否 开始磁柱    结束磁柱  1K大小容量 磁盘分区槽内的系统

Command (m for help): q
```

想要不储存离开吗？按下 q 就对了！不要随便按 w 啊！

使用 `p` 可以列出目前这颗磁盘的分割表信息，这个信息的上半部在显示整体磁盘的状态。

------

### 磁盘格式化

磁盘分割完毕后自然就是要进行文件系统的格式化，格式化的命令非常的简单，使用 `mkfs`（make filesystem） 命令。

语法：

```
mkfs [-t 文件系统格式] 装置文件名
```

选项与参数：

- -t ：可以接文件系统格式，例如 ext3, ext2, vfat 等(系统有支持才会生效)

### 实例 1

查看 mkfs 支持的文件格式

```
[root@www ~]# mkfs[tab][tab]
mkfs         mkfs.cramfs  mkfs.ext2    mkfs.ext3    mkfs.msdos   mkfs.vfat
```

按下两个[tab]，会发现 mkfs 支持的文件格式如上所示。

### 实例 2

将分区 /dev/hdc6（可指定你自己的分区） 格式化为 ext3 文件系统：

```
[root@www ~]# mkfs -t ext3 /dev/hdc6
mke2fs 1.39 (29-May-2006)
Filesystem label=                <==这里指的是分割槽的名称(label)
OS type: Linux
Block size=4096 (log=2)          <==block 的大小配置为 4K 
Fragment size=4096 (log=2)
251392 inodes, 502023 blocks     <==由此配置决定的inode/block数量
25101 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=515899392
16 block groups
32768 blocks per group, 32768 fragments per group
15712 inodes per group
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912

Writing inode tables: done
Creating journal (8192 blocks): done <==有日志记录
Writing superblocks and filesystem accounting information: done

This filesystem will be automatically checked every 34 mounts or
180 days, whichever comes first.  Use tune2fs -c or -i to override.
# 这样就创建起来我们所需要的 Ext3 文件系统了！简单明了！
```

------

## 磁盘检验

fsck（file system check）用来检查和维护不一致的文件系统。

若系统掉电或磁盘发生问题，可利用fsck命令对文件系统进行检查。

语法：

```
fsck [-t 文件系统] [-ACay] 装置名称
```

选项与参数：

- -t : 给定档案系统的型式，若在 /etc/fstab 中已有定义或 kernel 本身已支援的则不需加上此参数
- -s : 依序一个一个地执行 fsck 的指令来检查
- -A : 对/etc/fstab 中所有列出来的 分区（partition）做检查
- -C : 显示完整的检查进度
- -d : 打印出 e2fsck 的 debug 结果
- -p : 同时有 -A 条件时，同时有多个 fsck 的检查一起执行
- -R : 同时有 -A 条件时，省略 / 不检查
- -V : 详细显示模式
- -a : 如果检查有错则自动修复
- -r : 如果检查有错则由使用者回答是否修复
- -y : 选项指定检测每个文件是自动输入yes，在不确定那些是不正常的时候，可以执行 # fsck -y 全部检查修复。

### 实例 1

查看系统有多少文件系统支持的 fsck 命令：

```
[root@www ~]# fsck[tab][tab]
fsck         fsck.cramfs  fsck.ext2    fsck.ext3    fsck.msdos   fsck.vfat
```

### 实例 2

强制检测 /dev/hdc6 分区:

```
[root@www ~]# fsck -C -f -t ext3 /dev/hdc6 
fsck 1.39 (29-May-2006)
e2fsck 1.39 (29-May-2006)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
vbird_logical: 11/251968 files (9.1% non-contiguous), 36926/1004046 blocks
```

如果没有加上 -f 的选项，则由于这个文件系统不曾出现问题，检查的经过非常快速！若加上 -f 强制检查，才会一项一项的显示过程。

------

## 磁盘挂载与卸除

Linux 的磁盘挂载使用 `mount` 命令，卸载使用 `umount` 命令。

磁盘挂载语法：

```
mount [-t 文件系统] [-L Label名] [-o 额外选项] [-n]  装置文件名  挂载点
```

### 实例 1

用默认的方式，将刚刚创建的 /dev/hdc6 挂载到 /mnt/hdc6 上面！

```
[root@www ~]# mkdir /mnt/hdc6
[root@www ~]# mount /dev/hdc6 /mnt/hdc6
[root@www ~]# df
Filesystem           1K-blocks      Used Available Use% Mounted on
.....中间省略.....
/dev/hdc6              1976312     42072   1833836   3% /mnt/hdc6
```

磁盘卸载命令 `umount` 语法：

```
umount [-fn] 装置文件名或挂载点
```

选项与参数：

- -f ：强制卸除！可用在类似网络文件系统 (NFS) 无法读取到的情况下；
- -n ：不升级 /etc/mtab 情况下卸除。

卸载/dev/hdc6

```
[root@www ~]# umount /dev/hdc6     
```

Linux 操作系统的文件数据除了文件实际内容外，通常含有非常多的属性，例如 Linux 操作系统的文件权限（rwx）与文件属性（拥有者、群组、时间参数等）。文件系统通常会将这两部分的数据分别存放在不同的区块，权限与属性存放在 inode 中，至于实际数据则放置到 data block 区块中。另外，还有一个超级区块（superblock）会记录整个文件系统的整体信息，包括 inode 与 block 的总量、使用量、剩余量等。

inode：记录文件的属性，一个文件占用一个 inode，同时记录此文件的数据所在的 block。

在 Linux 中，可以使用 stat 命令查看某个文件的 inode 信息：

```
stat /etc/passwd
linux-peanut:~/Desktop # stat /etc/passwd
  File: `/etc/passwd'
  Size: 2269          Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d    Inode: 1149740     Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2018-04-09 17:16:42.000000000 +0800
Modify: 2018-04-09 17:16:36.000000000 +0800
Change: 2018-04-09 17:16:36.000000000 +0800
 Birth: -
```

可见，文件的绝大部分信息都存储在 inode 中。

```
Units = cylinders of 16065 * 512 = 8225280 bytes <==每个磁柱的大小
```

根据数学关系，Units = 扇区数 * 磁头数 * 每个扇区的容量。

磁盘顺序读取时是从一个磁头换到另一个磁头（磁头不用移动位置），而不是由一个磁柱换到另一个磁柱。

作者讲得很好，可惜具体操作方面有点问题（不具体）以及没有解释好挂载，在搭建在虚拟机上的linux挂载时，首先要增加硬盘，然后格式化硬盘，在硬盘上创建分区，创建目录，然后才是挂载。

看到一篇还不错的解释挂载的文章:

关于挂载的作用一直不是很清楚，今天在阅读教材时看见了 mount 这个命令，发现它的用处很隐晦但非常强大。奈何教材说的不明朗，因此在网上整合了一些优秀的解释，看完之后豁然开朗。

-  1.提一句Windows下，mount挂载，就是给磁盘分区提供一个盘符（C,D,E,...）。比如插入U盘后系统自动分配给了它I:盘符其实就是挂载，退优盘的时候进行安全弹出，其实就是卸载unmount。
-  2.Linux下，不像Windows可以有C,D,E,多个目录，Linux只有一个根目录/。在装系统时，我们分配给linux的所有区都在/下的某个位置，比如/home等等。
-  3.提问者插入了新硬盘，分了新磁盘区sdb1。它现在还不属于/。
-  4.我们虽然可以在一些图形桌面系统里找到他的位置，浏览管理里面的文件，但在命令行却不知怎么访问它的目录，比如无法使用cd或者ls。也无法在编程时指定一个目录对它操作。
-  5.这时提问者使用了 mount /dev/sdb1 ~/Share/ ，把新硬盘的区sdb1挂载到工作目录的~/Share/文件夹下，之后访问这个~/Share/文件夹就相当于访问这个硬盘2的sdb1分区了。对/Share/的任何操作，都相当于对sdb1里文件的操作。
-  6.所以Linux下，mount挂载的作用，就是将一个设备（通常是存储设备）挂接到一个已存在的目录上。访问这个目录就是访问该存储设备。
-  7.linux操作系统将所有的设备都看作文件，它将整个计算机的资源都整合成一个大的文件目录。我们要访问存储设备中的文件，必须将文件所在的分区挂载到一个已存在的目录上，然后通过访问这个目录来访问存储设备。挂载就是把设备放在一个目录下，让系统知道怎么管理这个设备里的文件，了解这个存储设备的可读写特性之类的过程。
-  8.我们不是有/dev/sdb1 吗，直接对它操作不就行了？这不是它的目录吗？
-  9.这不是它的目录。虽然/dev是个目录，但/dev/sdb1不是目录。可以发现ls/dev/sdb1无法执行。/dev/sdb1，是一个类似指针的东西，指向这个分区的原始数据块。mount前，系统并不知道这个数据块哪部分数据代表文件，如何对它们操作。
-  10.插入CD，系统其实自动执行了 mount /dev/cdrom /media/cdrom。所以可以直接在/media/cdrom中对CD中的内容进行管理。

# Linux vi/vim

所有的 Unix Like 系统都会内建 vi 文书编辑器，其他的文书编辑器则不一定会存在。

但是目前我们使用比较多的是 vim 编辑器。

vim 具有程序编辑的能力，可以主动的以字体颜色辨别语法的正确性，方便程序设计。

相关文章：[史上最全Vim快捷键键位图 — 入门到进阶](https://www.runoob.com/w3cnote/all-vim-cheatsheat.html)

------

## 什么是 vim？

Vim是从 vi 发展出来的一个文本编辑器。代码补完、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。

简单的来说， vi 是老式的字处理器，不过功能已经很齐全了，但是还是有可以进步的地方。 vim 则可以说是程序开发者的一项很好用的工具。

连 vim 的官方网站 ([http://www.vim.org](http://www.vim.org/)) 自己也说 vim 是一个程序开发工具而不是文字处理软件。

vim 键盘图：

![img](img/vi-vim-cheat-sheet-sch.gif)

------

## vi/vim 的使用

基本上 vi/vim 共分为三种模式，分别是**命令模式（Command mode）**，**输入模式（Insert mode）**和**底线命令模式（Last line mode）**。 这三种模式的作用分别是：

### 命令模式：

用户刚刚启动 vi/vim，便进入了命令模式。

此状态下敲击键盘动作会被Vim识别为命令，而非输入字符。比如我们此时按下i，并不会输入一个字符，i被当作了一个命令。

以下是常用的几个命令：

- **i** 切换到输入模式，以输入字符。
- **x** 删除当前光标所在处的字符。
- **:** 切换到底线命令模式，以在最底一行输入命令。

若想要编辑文本：启动Vim，进入了命令模式，按下i，切换到输入模式。

命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令。

### 输入模式

在命令模式下按下i就进入了输入模式。

在输入模式中，可以使用以下按键：

- **字符按键以及Shift组合**，输入字符
- **ENTER**，回车键，换行
- **BACK SPACE**，退格键，删除光标前一个字符
- **DEL**，删除键，删除光标后一个字符
- **方向键**，在文本中移动光标
- **HOME**/**END**，移动光标到行首/行尾
- **Page Up**/**Page Down**，上/下翻页
- **Insert**，切换光标为输入/替换模式，光标将变成竖线/下划线
- **ESC**，退出输入模式，切换到命令模式

### 底线命令模式

在命令模式下按下:（英文冒号）就进入了底线命令模式。

底线命令模式可以输入单个或多个字符的命令，可用的命令非常多。

在底线命令模式中，基本的命令有（已经省略了冒号）：

- q 退出程序
- w 保存文件

按ESC键可随时退出底线命令模式。

简单的说，我们可以将这三个模式想成底下的图标来表示：

![img](img/vim-vi-workmodel.png)

------

## vi/vim 使用实例

### 使用 vi/vim 进入一般模式

如果你想要使用 vi 来建立一个名为 runoob.txt 的文件时，你可以这样做：

```
$ vim runoob.txt
```

直接输入 **vi 文件名** 就能够进入 vi 的一般模式了。请注意，记得 vi 后面一定要加文件名，不管该文件存在与否！

![img](img/078207F0-B204-4464-AAEF-982F45EDDAE9.jpg)

### 按下 i 进入输入模式(也称为编辑模式)，开始编辑文字

在一般模式之中，只要按下 i, o, a 等字符就可以进入输入模式了！

在编辑模式当中，你可以发现在左下角状态栏中会出现 –INSERT- 的字样，那就是可以输入任意字符的提示。

这个时候，键盘上除了 **Esc** 这个按键之外，其他的按键都可以视作为一般的输入按钮了，所以你可以进行任何的编辑。

![img](img/1C928383-471E-4AF1-A61E-9E2CCBD5A913.jpg)

### 按下 ESC 按钮回到一般模式

好了，假设我已经按照上面的样式给他编辑完毕了，那么应该要如何退出呢？是的！没错！就是给他按下 **Esc** 这个按钮即可！马上你就会发现画面左下角的 – INSERT – 不见了！

### 在一般模式中按下 **:wq** 储存后离开 vi

OK，我们要存档了，存盘并离开的指令很简单，输入 **:wq** 即可保存离开！

![img](img/B2FB5146-327C-4019-AC96-DD7A8EE7460C.jpg)

OK! 这样我们就成功创建了一个 runoob.txt 的文件。

------

## vi/vim 按键说明

除了上面简易范例的 i, Esc, :wq 之外，其实 vim 还有非常多的按键可以使用。

### 第一部分：一般模式可用的光标移动、复制粘贴、搜索替换等

| 移动光标的方法                                               |                                                              |
| :----------------------------------------------------------- | ------------------------------------------------------------ |
| h 或 向左箭头键(←)                                           | 光标向左移动一个字符                                         |
| j 或 向下箭头键(↓)                                           | 光标向下移动一个字符                                         |
| k 或 向上箭头键(↑)                                           | 光标向上移动一个字符                                         |
| l 或 向右箭头键(→)                                           | 光标向右移动一个字符                                         |
| 如果你将右手放在键盘上的话，你会发现 hjkl 是排列在一起的，因此可以使用这四个按钮来移动光标。 如果想要进行多次移动的话，例如向下移动 30 行，可以使用 "30j" 或 "30↓" 的组合按键， 亦即加上想要进行的次数(数字)后，按下动作即可！ |                                                              |
| [Ctrl] + [f]                                                 | 屏幕『向下』移动一页，相当于 [Page Down]按键 (常用)          |
| [Ctrl] + [b]                                                 | 屏幕『向上』移动一页，相当于 [Page Up] 按键 (常用)           |
| [Ctrl] + [d]                                                 | 屏幕『向下』移动半页                                         |
| [Ctrl] + [u]                                                 | 屏幕『向上』移动半页                                         |
| +                                                            | 光标移动到非空格符的下一行                                   |
| -                                                            | 光标移动到非空格符的上一行                                   |
| n<space>                                                     | 那个 n 表示『数字』，例如 20 。按下数字后再按空格键，光标会向右移动这一行的 n 个字符。例如 20<space> 则光标会向后面移动 20 个字符距离。 |
| 0 或功能键[Home]                                             | 这是数字『 0 』：移动到这一行的最前面字符处 (常用)           |
| $ 或功能键[End]                                              | 移动到这一行的最后面字符处(常用)                             |
| H                                                            | 光标移动到这个屏幕的最上方那一行的第一个字符                 |
| M                                                            | 光标移动到这个屏幕的中央那一行的第一个字符                   |
| L                                                            | 光标移动到这个屏幕的最下方那一行的第一个字符                 |
| G                                                            | 移动到这个档案的最后一行(常用)                               |
| nG                                                           | n 为数字。移动到这个档案的第 n 行。例如 20G 则会移动到这个档案的第 20 行(可配合 :set nu) |
| gg                                                           | 移动到这个档案的第一行，相当于 1G 啊！ (常用)                |
| n<Enter>                                                     | n 为数字。光标向下移动 n 行(常用)                            |
| 搜索替换                                                     |                                                              |
| /word                                                        | 向光标之下寻找一个名称为 word 的字符串。例如要在档案内搜寻 vbird 这个字符串，就输入 /vbird 即可！ (常用) |
| ?word                                                        | 向光标之上寻找一个字符串名称为 word 的字符串。               |
| n                                                            | 这个 n 是英文按键。代表重复前一个搜寻的动作。举例来说， 如果刚刚我们执行 /vbird 去向下搜寻 vbird 这个字符串，则按下 n 后，会向下继续搜寻下一个名称为 vbird 的字符串。如果是执行 ?vbird 的话，那么按下 n 则会向上继续搜寻名称为 vbird 的字符串！ |
| N                                                            | 这个 N 是英文按键。与 n 刚好相反，为『反向』进行前一个搜寻动作。 例如 /vbird 后，按下 N 则表示『向上』搜寻 vbird 。 |
| 使用 /word 配合 n 及 N 是非常有帮助的！可以让你重复的找到一些你搜寻的关键词！ |                                                              |
| :n1,n2s/word1/word2/g                                        | n1 与 n2 为数字。在第 n1 与 n2 行之间寻找 word1 这个字符串，并将该字符串取代为 word2 ！举例来说，在 100 到 200 行之间搜寻 vbird 并取代为 VBIRD 则： 『:100,200s/vbird/VBIRD/g』。(常用) |
| **:1,$s/word1/word2/g** 或 **:%s/word1/word2/g**             | 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！(常用) |
| **:1,$s/word1/word2/gc** 或 **:%s/word1/word2/gc**           | 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！且在取代前显示提示字符给用户确认 (confirm) 是否需要取代！(常用) |
| 删除、复制与贴上                                             |                                                              |
| x, X                                                         | 在一行字当中，x 为向后删除一个字符 (相当于 [del] 按键)， X 为向前删除一个字符(相当于 [backspace] 亦即是退格键) (常用) |
| nx                                                           | n 为数字，连续向后删除 n 个字符。举例来说，我要连续删除 10 个字符， 『10x』。 |
| dd                                                           | 删除游标所在的那一整行(常用)                                 |
| ndd                                                          | n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行 (常用) |
| d1G                                                          | 删除光标所在到第一行的所有数据                               |
| dG                                                           | 删除光标所在到最后一行的所有数据                             |
| d$                                                           | 删除游标所在处，到该行的最后一个字符                         |
| d0                                                           | 那个是数字的 0 ，删除游标所在处，到该行的最前面一个字符      |
| yy                                                           | 复制游标所在的那一行(常用)                                   |
| nyy                                                          | n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行(常用) |
| y1G                                                          | 复制游标所在行到第一行的所有数据                             |
| yG                                                           | 复制游标所在行到最后一行的所有数据                           |
| y0                                                           | 复制光标所在的那个字符到该行行首的所有数据                   |
| y$                                                           | 复制光标所在的那个字符到该行行尾的所有数据                   |
| p, P                                                         | p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行！ 举例来说，我目前光标在第 20 行，且已经复制了 10 行数据。则按下 p 后， 那 10 行数据会贴在原本的 20 行之后，亦即由 21 行开始贴。但如果是按下 P 呢？ 那么原本的第 20 行会被推到变成 30 行。 (常用) |
| J                                                            | 将光标所在行与下一行的数据结合成同一行                       |
| c                                                            | 重复删除多个数据，例如向下删除 10 行，[ 10cj ]               |
| u                                                            | 复原前一个动作。(常用)                                       |
| [Ctrl]+r                                                     | 重做上一个动作。(常用)                                       |
| 这个 u 与 [Ctrl]+r 是很常用的指令！一个是复原，另一个则是重做一次～ 利用这两个功能按键，你的编辑，嘿嘿！很快乐的啦！ |                                                              |
| .                                                            | 不要怀疑！这就是小数点！意思是重复前一个动作的意思。 如果你想要重复删除、重复贴上等等动作，按下小数点『.』就好了！ (常用) |

### 第二部分：一般模式切换到编辑模式的可用的按钮说明

| 进入输入或取代的编辑模式                                     |                                                              |
| :----------------------------------------------------------- | ------------------------------------------------------------ |
| i, I                                                         | 进入输入模式(Insert mode)： i 为『从目前光标所在处输入』， I 为『在目前所在行的第一个非空格符处开始输入』。 (常用) |
| a, A                                                         | 进入输入模式(Insert mode)： a 为『从目前光标所在的下一个字符处开始输入』， A 为『从光标所在行的最后一个字符处开始输入』。(常用) |
| o, O                                                         | 进入输入模式(Insert mode)： 这是英文字母 o 的大小写。o 为『在目前光标所在的下一行处输入新的一行』； O 为在目前光标所在处的上一行输入新的一行！(常用) |
| r, R                                                         | 进入取代模式(Replace mode)： r 只会取代光标所在的那一个字符一次；R会一直取代光标所在的文字，直到按下 ESC 为止；(常用) |
| 上面这些按键中，在 vi 画面的左下角处会出现『--INSERT--』或『--REPLACE--』的字样。 由名称就知道该动作了吧！！特别注意的是，我们上面也提过了，你想要在档案里面输入字符时， 一定要在左下角处看到 INSERT 或 REPLACE 才能输入喔！ |                                                              |
| [Esc]                                                        | 退出编辑模式，回到一般模式中(常用)                           |

### 第三部分：一般模式切换到指令行模式的可用的按钮说明

| 指令行的储存、离开等指令                                     |                                                              |
| :----------------------------------------------------------- | ------------------------------------------------------------ |
| :w                                                           | 将编辑的数据写入硬盘档案中(常用)                             |
| :w!                                                          | 若文件属性为『只读』时，强制写入该档案。不过，到底能不能写入， 还是跟你对该档案的档案权限有关啊！ |
| :q                                                           | 离开 vi (常用)                                               |
| :q!                                                          | 若曾修改过档案，又不想储存，使用 ! 为强制离开不储存档案。    |
| 注意一下啊，那个惊叹号 (!) 在 vi 当中，常常具有『强制』的意思～ |                                                              |
| :wq                                                          | 储存后离开，若为 :wq! 则为强制储存后离开 (常用)              |
| ZZ                                                           | 这是大写的 Z 喔！如果修改过，保存当前文件，然后退出！效果等同于(保存并退出) |
| ZQ                                                           | 不保存，强制退出。效果等同于 **:q!**。                       |
| :w [filename]                                                | 将编辑的数据储存成另一个档案（类似另存新档）                 |
| :r [filename]                                                | 在编辑的数据中，读入另一个档案的数据。亦即将 『filename』 这个档案内容加到游标所在行后面 |
| :n1,n2 w [filename]                                          | 将 n1 到 n2 的内容储存成 filename 这个档案。                 |
| :! command                                                   | 暂时离开 vi 到指令行模式下执行 command 的显示结果！例如 『:! ls /home』即可在 vi 当中察看 /home 底下以 ls 输出的档案信息！ |
| vim 环境的变更                                               |                                                              |
| :set nu                                                      | 显示行号，设定之后，会在每一行的前缀显示该行的行号           |
| :set nonu                                                    | 与 set nu 相反，为取消行号！                                 |

特别注意，在 vi/vim 中，数字是很有意义的！数字通常代表重复做几次的意思！ 也有可能是代表去到第几个什么什么的意思。

举例来说，要删除 50 行，则是用 『50dd』 对吧！ 数字加在动作之前，如我要向下移动 20 行呢？那就是『20j』或者是『20↓』即可。

**vim 中批量添加注释**

方法一 ：块选择模式

批量注释：

**Ctrl + v** 进入块选择模式，然后移动光标选中你要注释的行，再按大写的 **I** 进入行首插入模式输入注释符号如 **//** 或 **#**，输入完毕之后，按两下 **ESC**，**Vim** 会自动将你选中的所有行首都加上注释，保存退出完成注释。

取消注释：

**Ctrl + v** 进入块选择模式，选中你要删除的行首的注释符号，注意 **//** 要选中两个，选好之后按 **d** 即可删除注释，**ESC** 保存退出。

方法二: 替换命令

批量注释。

使用下面命令在指定的行首添加注释。

使用名命令格式： **:起始行号,结束行号s/^/注释符/g**（注意冒号）。

取消注释：

使用名命令格式： **:起始行号,结束行号s/^注释符//g**（注意冒号）。

例子：

1、在 10 - 20 行添加 **//** 注释

```
:10,20s#^#//#g
```

2、在 10 - 20 行删除 **//** 注释

```
:10,20s#^//##g
```

3、在 10 - 20 行添加 **#** 注释

```
:10,20s/^/#/g
```

4、在 **10 - 20** 行删除 # 注释

```
:10,20s/#//g
```



# linux yum 命令

yum（ Yellow dog Updater, Modified）是一个在Fedora和RedHat以及SUSE中的Shell前端软件包管理器。

基於RPM包管理，能够从指定的服务器自动下载RPM包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软体包，无须繁琐地一次次下载、安装。

yum提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。

### yum 语法

```
yum [options] [command] [package ...]
```

- **options：**可选，选项包括-h（帮助），-y（当安装过程提示选择全部为"yes"），-q（不显示安装的过程）等等。
- **command：**要进行的操作。
- **package**操作的对象。

------

## yum常用命令

- 1.列出所有可更新的软件清单命令：yum check-update
- 2.更新所有软件命令：yum update
- 3.仅安装指定的软件命令：yum install <package_name>
- 4.仅更新指定的软件命令：yum update <package_name>
- 5.列出所有可安裝的软件清单命令：yum list
- 6.删除软件包命令：yum remove <package_name>
- 7.查找软件包 命令：yum search <keyword>
- 8.清除缓存命令:
  - yum clean packages: 清除缓存目录下的软件包
  - yum clean headers: 清除缓存目录下的 headers
  - yum clean oldheaders: 清除缓存目录下旧的 headers
  - yum clean, yum clean all (= yum clean packages; yum clean oldheaders) :清除缓存目录下的软件包及旧的headers

### 实例 1

安装 pam-devel

```
[root@www ~]# yum install pam-devel
Setting up Install Process
Parsing package install arguments
Resolving Dependencies  <==先检查软件的属性相依问题
--> Running transaction check
---> Package pam-devel.i386 0:0.99.6.2-4.el5 set to be updated
--> Processing Dependency: pam = 0.99.6.2-4.el5 for package: pam-devel
--> Running transaction check
---> Package pam.i386 0:0.99.6.2-4.el5 set to be updated
filelists.xml.gz          100% |=========================| 1.6 MB    00:05
filelists.xml.gz          100% |=========================| 138 kB    00:00
-> Finished Dependency Resolution
……(省略)
```

### 实例 2

移除 pam-devel

```
[root@www ~]# yum remove pam-devel
Setting up Remove Process
Resolving Dependencies  <==同样的，先解决属性相依的问题
--> Running transaction check
---> Package pam-devel.i386 0:0.99.6.2-4.el5 set to be erased
--> Finished Dependency Resolution

Dependencies Resolved

=============================================================================
 Package                 Arch       Version          Repository        Size
=============================================================================
Removing:
 pam-devel               i386       0.99.6.2-4.el5   installed         495 k

Transaction Summary
=============================================================================
Install      0 Package(s)
Update       0 Package(s)
Remove       1 Package(s)  <==还好，并没有属性相依的问题，单纯移除一个软件

Is this ok [y/N]: y
Downloading Packages:
Running rpm_check_debug
Running Transaction Test
Finished Transaction Test
Transaction Test Succeeded
Running Transaction
  Erasing   : pam-devel                    ######################### [1/1]

Removed: pam-devel.i386 0:0.99.6.2-4.el5
Complete!
```

### 实例 3

利用 yum 的功能，找出以 pam 为开头的软件名称有哪些？

```
[root@www ~]# yum list pam*
Installed Packages
pam.i386                  0.99.6.2-3.27.el5      installed
pam_ccreds.i386           3-5                    installed
pam_krb5.i386             2.2.14-1               installed
pam_passwdqc.i386         1.0.2-1.2.2            installed
pam_pkcs11.i386           0.5.3-23               installed
pam_smb.i386              1.1.7-7.2.1            installed
Available Packages <==底下则是『可升级』的或『未安装』的
pam.i386                  0.99.6.2-4.el5         base
pam-devel.i386            0.99.6.2-4.el5         base
pam_krb5.i386             2.2.14-10              base
```

------

## 国内 yum 源

网易（163）yum源是国内最好的yum源之一 ，无论是速度还是软件版本，都非常的不错。

将yum源设置为163 yum，可以提升软件包安装和更新的速度，同时避免一些常见软件版本无法找到。

### 安装步骤

首先备份/etc/yum.repos.d/CentOS-Base.repo

```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

下载对应版本 repo 文件, 放入 /etc/yum.repos.d/ (操作前请做好相应备份)

- [CentOS5](http://mirrors.163.com/.help/CentOS5-Base-163.repo) ：http://mirrors.163.com/.help/CentOS5-Base-163.repo
- [CentOS6](http://mirrors.163.com/.help/CentOS6-Base-163.repo) ：http://mirrors.163.com/.help/CentOS6-Base-163.repo
- [CentOS7](http://mirrors.163.com/.help/CentOS7-Base-163.repo) ：http://mirrors.163.com/.help/CentOS7-Base-163.repo

```
wget http://mirrors.163.com/.help/CentOS6-Base-163.repo
mv CentOS6-Base-163.repo CentOS-Base.repo
```

运行以下命令生成缓存

```
yum clean all
yum makecache
```

除了网易之外，国内还有其他不错的 yum 源，比如中科大和搜狐。

中科大的 yum 源，安装方法查看：https://lug.ustc.edu.cn/wiki/mirrors/help/centos

sohu 的 yum 源安装方法查看: http://mirrors.sohu.com/help/centos.html

**配置本地Yum仓库**

实现此案例需要按照如下步骤进行。

步骤一：搭建一个本地Yum，将RHEL6光盘手动挂载到/media

命令操作如下所示：

```
[root@localhost ~]# mount /dev/cdrom /media/
mount: block device /dev/sr0 is write-protected, mounting read-only
[root@localhost ~]# mount | tail -1
/dev/sr0 on /media type iso9660 (ro)
```

步骤二：将本地设置为客户端，进行Yum验证

Yum客户端需编辑配置文件，命令操作如下所示：

```
[root@localhost ~]# cd /etc/yum.repos.d/         //必须在这个路径下
[root@localhost yum.repos.d]# ls                  //此路径下事先有配置文件的模板
rhel-source.repo

[root@localhost yum.repos.d]# cp rhel-source.repo rhel6.repo //配置文件必须以.repo结尾
[root@localhost yum.repos.d]# vim rhel6.repo
[rhel-6]                                     //中括号里内容要求唯一，但不要出现特殊字符
name=Red Hat Enterprise Linux 6           //此为描述信息，可以看情况填写
baseurl=file:///media/                     //此项为yum软件仓库位置，指向光盘挂载点
enabled=1                                   //此项为是否开启，1为开启, 0为不开启
gpgcheck=1                                  //此项为是否检查签名，1为检测, 0为不检测
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release  //签名认证信息的路径

[root@localhost /]# yum repolist
Loaded plugins: product-id, refresh-packagekit, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
rhel-6                                            | 3.9 kB     00:00 ... 
rhel-6/primary_db                                  | 3.1 MB     00:00 ... 
repo id             repo name                                     status
rhel-6              Red Hat Enterprise Linux 6                    3,690
repolist: 3,690
```

对于 Linux 软件安装时提示缺失库的，可以使用 yum 的 provides 参数查看 libstdc++.so.6 的库文件包含在那个安装包中只需要执行：

```
yum provides libstdc++.so.6
```

然后按查询到安装包包名，使用 **yum install** 安装即可。





# Shell 教程

Shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。Shell 既是一种命令语言，又是一种程序设计语言。

Shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。

Ken Thompson 的 sh 是第一种 Unix Shell，Windows Explorer 是一个典型的图形界面 Shell。

[**Shell 在线工具**](https://www.runoob.com/try/showbash.php?filename=helloworld)

------

## Shell 脚本

Shell 脚本（shell script），是一种为 shell 编写的脚本程序。

业界所说的 shell 通常都是指 shell 脚本，但读者朋友要知道，shell 和 shell script 是两个不同的概念。

由于习惯的原因，简洁起见，本文出现的 "shell编程" 都是指 shell 脚本编程，不是指开发 shell 自身。

------

## Shell 环境

Shell 编程跟 JavaScript、php 编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux 的 Shell 种类众多，常见的有：

- Bourne Shell（/usr/bin/sh或/bin/sh）
- Bourne Again Shell（/bin/bash）
- C Shell（/usr/bin/csh）
- K Shell（/usr/bin/ksh）
- Shell for Root（/sbin/sh）
- ……

本教程关注的是 Bash，也就是 Bourne Again Shell，由于易用和免费，Bash 在日常工作中被广泛使用。同时，Bash 也是大多数Linux 系统默认的 Shell。

在一般情况下，人们并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 **#!/bin/sh**，它同样也可以改为 **#!/bin/bash**。

**#!** 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序。

------

## 第一个shell脚本

打开文本编辑器(可以使用 vi/vim 命令来创建文件)，新建一个文件 test.sh，扩展名为 sh（sh代表shell），扩展名并不影响脚本执行，见名知意就好，如果你用 php 写 shell 脚本，扩展名就用 php 好了。

输入一些代码，第一行一般是这样：

## 实例

*#!/bin/bash*
**echo** "Hello World !"


[运行实例 »](https://www.runoob.com/try/runcode.php?filename=helloworld&type=bash)

**#!** 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。

echo 命令用于向窗口输出文本。

### 运行 Shell 脚本有两种方法：

**1、作为可执行程序**

将上面的代码保存为 test.sh，并 cd 到相应目录：

```
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本
```

注意，一定要写成 **./test.sh**，而不是 **test.sh**，运行其它二进制的程序也一样，直接写 test.sh，linux 系统会去 PATH 里寻找有没有叫 test.sh 的，而只有 /bin, /sbin, /usr/bin，/usr/sbin 等在 PATH 里，你的当前目录通常不在 PATH 里，所以写成 test.sh 是会找不到命令的，要用 ./test.sh 告诉系统说，就在当前目录找。

**2、作为解释器参数**

这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：

```
/bin/sh test.sh
/bin/php test.php
```

这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。

## sh/bash/csh/Tcsh/ksh/pdksh等shell的区别

- 

  sh(全称 Bourne Shell)

  : 是UNIX最初使用的 shell，而且在每种 UNIX 上都可以使用。

  Bourne Shell 在 shell 编程方面相当优秀，但在处理与用户的交互方面做得不如其他几种 shell。

  

- **bash（全称 Bourne Again Shell）**: LinuxOS 默认的，它是 Bourne Shell 的扩展。 与 Bourne Shell 完全兼容，并且在 Bourne Shell 的基础上增加了很多特性。可以提供命令补全，命令编辑和命令历史等功能。它还包含了很多 C Shell 和 Korn Shell 中的优点，有灵活和强大的编辑接口，同时又很友好的用户界面。

- **csh(全称 C Shell)**: 是一种比 Bourne Shell更适合的变种 Shell，它的语法与 C 语言很相似。

- **Tcsh**: 是 Linux 提供的 C Shell 的一个扩展版本。
  Tcsh 包括命令行编辑，可编程单词补全，拼写校正，历史命令替换，作业控制和类似 C 语言的语法，他不仅和 Bash Shell 提示符兼容，而且还提供比 Bash Shell 更多的提示符参数。

- **ksh (全称 Korn Shell)**: 集合了 C Shell 和 Bourne Shell 的优点并且和 Bourne Shell 完全兼容。

-  **pdksh**: 是 Linux 系统提供的 ksh 的扩展。
  pdksh 支持人物控制，可以在命令行上挂起，后台执行，唤醒或终止程序。

如果不好理解的话，Shell 个人感觉可以对应成 win 中的 bat，通过代码来实现一些自动定时任务，自动备份或者执行的任务。

1、**chmod +x file** 加上执行权限，否则会提示无执行权限。

2、注意执行脚本时候或者全目录，或者 **./file.sh** ，如果不加的话，linux 默认会从PATH 里去找该 file.sh。

3、看了这篇教程，发现脚本后缀名可以任意修改，仍然可以正常运行。

4、语法类PHP，方便学习。

**首先，什么是脚本语言？**

脚本语言是像剧本一样教计算机办某个事情的语言。

比如你想让计算机执行复制某个文件的操作，如：**cp ~/Desktop/\*.txt ~/text**

你可以在文本编辑器写入上边的代码并且保存此文件，然后你通过执行这个文本文件来执行上面的代码，并不需要重复手动输入上边的代码。

下面这句话是我在网上看到的：

> 所以脚本其实就是短小的、用来让计算机自动化完成一系列工作的程序，这类程序可以用文本编辑器修改，不需要编译，通常是解释运行的。

## ubuntu（linux）下 source、sh、bash、./ 执行脚本的区别是什么？

**1. source命令用法：**

```
source FileName
```

作用:在当前 bash 环境下读取并执行 FileName 中的命令。该 filename 文件可以无 "执行权限"。

注：该命令通常用命令 **.** 来替代。

**2. sh、bash的命令用法：**

```
sh FileName
或
bash FileName
```

作用:打开一个子 shell 来读取并执行 FileName 中命令。该 filename 文件可以无 "执行权限"。

注：运行一个shell脚本时会启动另一个命令解释器。

**3、./的命令用法：**

```
./FileName
```

作用: 打开一个子 shell 来读取并执行 FileName 中命令，该 filename 文件需要 "执行权限"。

注：运行一个 shell 脚本时会启动另一个命令解释器。

## shell 和 shell 脚本的概念

shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。Ken Thompson 的 sh 是第一种 Unix Shell，Windows Explorer 是一个典型的图形界面 Shell。

shell 脚本（shell script），是一种为 shell 编写的脚本程序。业界所说的 shell 通常都是指 shell 脚本，但读者朋友要知道，shell 和 shell script 是两个不同的概念。由于习惯的原因，简洁起见，本文出现的 "shell编程" 都是指 shell 脚本编程，不是指开发 shell 自身（如Windows Explorer扩展开发）。

# Shell 变量

定义变量时，变量名不加美元符号（$，PHP语言中变量需要），如：

```
your_name="runoob.com"
```

注意，变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样。同时，变量名的命名须遵循如下规则：

- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）。

有效的 Shell 变量名示例如下：

```
RUNOOB
LD_LIBRARY_PATH
_var
var2
```

无效的变量命名：

```
?var=123
user*name=runoob
```

除了显式地直接赋值，还可以用语句给变量赋值，如：

```
for file in `ls /etc`
或
for file in $(ls /etc)
```

以上语句将 /etc 下目录的文件名循环出来。

------

### 使用变量

使用一个定义过的变量，只要在变量名前面加美元符号即可，如：

```
your_name="qinjx"
echo $your_name
echo ${your_name}
```

变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界，比如下面这种情况：

```
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```

如果不给skill变量加花括号，写成echo "I am good at $skillScript"，解释器就会把$skillScript当成一个变量（其值为空），代码执行结果就不是我们期望的样子了。

推荐给所有变量加上花括号，这是个好的编程习惯。

已定义的变量，可以被重新定义，如：

```
your_name="tom"
echo $your_name
your_name="alibaba"
echo $your_name
```

这样写是合法的，但注意，第二次赋值的时候不能写$your_name="alibaba"，使用变量的时候才加美元符（$）。

### 只读变量

使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。

下面的例子尝试更改只读变量，结果报错：

```
#!/bin/bash
myUrl="https://www.google.com"
readonly myUrl
myUrl="https://www.runoob.com"
```

运行脚本，结果如下：

```
/bin/sh: NAME: This variable is read only.
```

### 删除变量

使用 unset 命令可以删除变量。语法：

```
unset variable_name
```

变量被删除后不能再次使用。unset 命令不能删除只读变量。

**实例**

```
#!/bin/sh
myUrl="https://www.runoob.com"
unset myUrl
echo $myUrl
```

以上实例执行将没有任何输出。

### 变量类型

运行shell时，会同时存在三种变量：

- **1) 局部变量** 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
- **2) 环境变量** 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
- **3) shell变量** shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行

------

## Shell 字符串

字符串是shell编程中最常用最有用的数据类型（除了数字和字符串，也没啥其它类型好用了），字符串可以用单引号，也可以用双引号，也可以不用引号。单双引号的区别跟PHP类似。

### 单引号

```
str='this is a string'
```

单引号字符串的限制：

- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
- 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

### 双引号

```
your_name='runoob'
str="Hello, I know you are \"$your_name\"! \n"
echo -e $str
```

输出结果为：

```
Hello, I know you are "runoob"! 
```

双引号的优点：

- 双引号里可以有变量
- 双引号里可以出现转义字符

### 拼接字符串

```
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3
```

输出结果为：

```
hello, runoob ! hello, runoob !
hello, runoob ! hello, ${your_name} !
```

### 获取字符串长度

```
string="abcd"
echo ${#string} #输出 4
```

### 提取子字符串

以下实例从字符串第 **2** 个字符开始截取 **4** 个字符：

```
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo
```

**注意**：第一个字符的索引值为 **0**。

### 查找子字符串

查找字符 **i** 或 **o** 的位置(哪个字母先出现就计算哪个)：

```
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4
```

**注意：** 以上脚本中 **`** 是反引号，而不是单引号 **'**，不要看错了哦。

------

## Shell 数组

bash支持一维数组（不支持多维数组），并且没有限定数组的大小。

类似于 C 语言，数组元素的下标由 0 开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，其值应大于或等于 0。

### 定义数组

在 Shell 中，用括号来表示数组，数组元素用"空格"符号分割开。定义数组的一般形式为：

```
数组名=(值1 值2 ... 值n)
```

例如：

```
array_name=(value0 value1 value2 value3)
```

或者

```
array_name=(
value0
value1
value2
value3
)
```

还可以单独定义数组的各个分量：

```
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen
```

可以不使用连续的下标，而且下标的范围没有限制。

### 读取数组

读取数组元素值的一般格式是：

```
${数组名[下标]}
```

例如：

```
valuen=${array_name[n]}
```

使用 **@** 符号可以获取数组中的所有元素，例如：

```
echo ${array_name[@]}
```

### 获取数组的长度

获取数组长度的方法与获取字符串长度的方法相同，例如：

```
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```

------

## Shell 注释

以 **#** 开头的行就是注释，会被解释器忽略。

通过每一行加一个 **#** 号设置多行注释，像这样：

```
#--------------------------------------------
# 这是一个注释
# author：菜鸟教程
# site：www.runoob.com
# slogan：学的不仅是技术，更是梦想！
#--------------------------------------------
##### 用户配置区 开始 #####
#
#
# 这里可以添加脚本描述信息
# 
#
##### 用户配置区 结束  #####
```

如果在开发过程中，遇到大段的代码需要临时注释起来，过一会儿又取消注释，怎么办呢？

每一行加个#符号太费力了，可以把这一段要注释的代码用一对花括号括起来，定义成一个函数，没有地方调用这个函数，这块代码就不会执行，达到了和注释一样的效果。

### 多行注释

多行注释还可以使用以下格式：

```
:<<EOF
注释内容...
注释内容...
注释内容...
EOF
```

EOF 也可以使用其他符号:

```
:<<'
注释内容...
注释内容...
注释内容...
'

:<<!
注释内容...
注释内容...
注释内容...
!
```

Linux 的字符串截取很有用。有八种方法。

假设有变量 var=http://www.aaa.com/123.htm

**1. # 号截取，删除左边字符，保留右边字符。**

```
echo ${var#*//}
```

其中 var 是变量名，# 号是运算符，*// 表示从左边开始删除第一个 // 号及左边的所有字符

即删除 http://

结果是 ：www.aaa.com/123.htm

**2. ## 号截取，删除左边字符，保留右边字符。**

```
echo ${var##*/}
```

\##*/ 表示从左边开始删除最后（最右边）一个 / 号及左边的所有字符

即删除 http://www.aaa.com/

结果是 123.htm

**3. %号截取，删除右边字符，保留左边字符**

```
echo ${var%/*}
```

%/* 表示从右边开始，删除第一个 / 号及右边的字符

结果是：http://www.aaa.com

**4. %% 号截取，删除右边字符，保留左边字符**

```
echo ${var%%/*}
```

%%/* 表示从右边开始，删除最后（最左边）一个 / 号及右边的字符

结果是：http:

**5. 从左边第几个字符开始，及字符的个数**

```
echo ${var:0:5}
```

其中的 0 表示左边第一个字符开始，5 表示字符的总个数。

结果是：http:

**6. 从左边第几个字符开始，一直到结束。**

```
echo ${var:7}
```

其中的 7 表示左边第8个字符开始，一直到结束。

结果是 ：www.aaa.com/123.htm

**7. 从右边第几个字符开始，及字符的个数**

```
echo ${var:0-7:3}
```

其中的 0-7 表示右边算起第七个字符开始，3 表示字符的个数。

结果是：123

**8. 从右边第几个字符开始，一直到结束。**

```
echo ${var:0-7}
```

表示从右边第七个字符开始，一直到结束。

结果是：123.htm

**注：**（左边的第一个字符是用 0 表示，右边的第一个字符用 0-1 表示）

描述的有点儿不容易懂，看了好久才勉强明白 **#** **##** **%** **%%**。

**#**、**##** 表示从左边开始删除。一个 **#** 表示从左边删除到第一个指定的字符；两个 **#** 表示从左边删除到最后一个指定的字符。

**%**、**%%** 表示从右边开始删除。一个 **%** 表示从右边删除到第一个指定的字符；两个 **%** 表示从左边删除到最后一个指定的字符。

删除包括了指定的字符本身。

```
#!bin/bash
#author:amau

var="http://www.runoob.com/linux/linux-shell-variable.html"

s1=${var%%t*}
s2=${var%t*}
s3=${var%%.*}
s4=${var#*/}
s5=${var##*/}
```

echo "关于字符串的截取%，#的使用方法" echo "原字符串为："${var} echo "%%t*的效果："${s1} echo "%t*的效果："${s2} echo "%%.*的效果："${s3} echo "#*/的效果："${s4} echo "##*/的效果："${s5}

运行结果：

```
关于字符串的截取%，#的使用方法
原字符串为：http://www.runoob.com/linux/linux-shell-variable.html
%%t*的效果：h
%t*的效果：http://www.runoob.com/linux/linux-shell-variable.h
%%.*的效果：http://www
#*/的效果：/www.runoob.com/linux/linux-shell-variable.html
##*/的效果：linux-shell-variable.html
```

计算字符长度也可是使用 **length**:

```
string="hello,everyone my name is xiaoming"
expr length "$string"
```

输出:34

**注意**：string字符串里边有空格,所以需要添加双引号

使用 **expr** 命令时，表达式中的运算符左右必须包含空格，如果不包含空格，将会输出表达式本身:

```
expr 5+6    // 直接输出 5+6
expr 5 + 6       // 输出 11
```

对于某些运算符，还需要我们使用符号"\"进行转义，否则就会提示语法错误。

```
expr 5 * 6       // 输出错误
expr 5 \* 6      // 输出30
```

**[read](https://www.runoob.com/linux/linux-comm-read.html) 命令用于获取键盘输入信息**

它的语法形式一般是：

```
read [-options] [variable...]
```

以下实例读取键盘输入的内容并将其赋值给shell变量，为：-p 参数由于设置提示信息：

```
read -p "input a val:" a    #获取键盘输入的 a 变量数字
read -p "input b val:" b    #获取键盘输入的 b 变量数字
r=$[a+b]                    #计算a+b的结果 赋值给r  不能有空格
echo "result = ${r}"        #输出显示结果 r
```

测试结果：

```
input a val:1
input b val:2
result = 3
```

看了上面各位的描述，自己来测试下 **###%%%\*** 的用法：

```
#!/bin/bash
# 字符串截取（界定字符本身也会被删除）
str="www.runoob.com/linux/linux-shell-variable.html"
echo "str    : ${str}"
echo "str#*/    : ${str#*/}"   # 从 字符串开头 删除到 左数第一个'/'
echo "str##*/    : ${str##*/}"  # 从 字符串开头 删除到 左数最后一个'/'
echo "str%/*    : ${str%/*}"   # 从 字符串末尾 删除到 右数第一个'/'
echo "str%%/*    : ${str%%/*}"  # 从 字符串末尾 删除到 右数最后一个'/'
echo
echo "str#/*    : ${str#/*}"   # 无效果
echo "str##/*    : ${str##/*}"  # 无效果
echo "str%*/    : ${str%*/}"   # 无效果
echo "str%%*/    : ${str%%*/}"  # 无效果
```

输出结果：

```
str     : www.runoob.com/linux/linux-shell-variable.html
str#*/  : linux/linux-shell-variable.html
str##*/ : linux-shell-variable.html
str%/*  : www.runoob.com/linux
str%%/* : www.runoob.com

str#/*  : www.runoob.com/linux/linux-shell-variable.html
str##/* : www.runoob.com/linux/linux-shell-variable.html
str%*/  : www.runoob.com/linux/linux-shell-variable.html
str%%*/ : www.runoob.com/linux/linux-shell-variable.html
```

# Shell 传递参数

我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：**$n**。**n** 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……

### 实例

以下实例我们向脚本传递三个参数，并分别输出，其中 **$0** 为执行的文件名（包含文件路径）：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
```

为脚本设置可执行权限，并执行脚本，输出结果如下所示：

```
$ chmod +x test.sh 
$ ./test.sh 1 2 3
Shell 传递参数实例！
执行的文件名：./test.sh
第一个参数为：1
第二个参数为：2
第三个参数为：3
```

另外，还有几个特殊字符用来处理参数：

| 参数处理 | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| $#       | 传递到脚本的参数个数                                         |
| $*       | 以一个单字符串显示所有向脚本传递的参数。 如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 |
| $$       | 脚本运行的当前进程ID号                                       |
| $!       | 后台运行的最后一个进程的ID号                                 |
| $@       | 与$*相同，但是使用时加引号，并在引号中返回每个参数。 如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 |
| $-       | 显示Shell使用的当前选项，与[set命令](https://www.runoob.com/linux/linux-comm-set.html)功能相同。 |
| $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

echo "Shell 传递参数实例！";
echo "第一个参数为：$1";

echo "参数个数为：$#";
echo "传递的参数作为一个字符串显示：$*";
```

执行脚本，输出结果如下所示：

```
$ chmod +x test.sh 
$ ./test.sh 1 2 3
Shell 传递参数实例！
第一个参数为：1
参数个数为：3
传递的参数作为一个字符串显示：1 2 3
```

$* 与 $@ 区别：

- 相同点：都是引用所有参数。
- 不同点：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，，则 " * " 等价于 "1 2 3"（传递了一个参数），而 "@" 等价于 "1" "2" "3"（传递了三个参数）。

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```

执行脚本，输出结果如下所示：

```
$ chmod +x test.sh 
$ ./test.sh 1 2 3
-- $* 演示 ---
1 2 3
-- $@ 演示 ---
1
2
3
```

在为shell脚本传递的参数中**如果包含空格，应该使用单引号或者双引号将该参数括起来，以便于脚本将这个参数作为整体来接收**。

在有参数时，可以使用对参数进行校验的方式处理以减少错误发生：

```
if [ -n "$1" ]; then
    echo "包含第一个参数"
else
    echo "没有包含第一参数"
fi
```

**注意**：中括号 **[]** 与其中间的代码应该有空格隔开

Shell 里面的中括号（包括单中括号与双中括号）可用于一些条件的测试：

- 算术比较, 比如一个变量是否为0, `[ $var -eq 0 ]`。
- 文件属性测试，比如一个文件是否存在，`[ -e $var ]`, 是否是目录，`[ -d $var ]`。
- 字符串比较, 比如两个字符串是否相同， `[[ $var1 = $var2 ]]`。

> [] 常常可以使用 test 命令来代替，具体可参看：[Shell 中的中括号用法总结](https://www.runoob.com/w3cnote/shell-summary-brackets.html)。

# Shell 数组

数组中可以存放多个值。Bash Shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小（与 PHP 类似）。

与大部分编程语言类似，数组元素的下标由0开始。

Shell 数组用括号来表示，元素用"空格"符号分割开，语法格式如下：

```
array_name=(value1 value2 ... valuen)
```

### 实例

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

my_array=(A B "C" D)
```

我们也可以使用下标来定义数组:

```
array_name[0]=value0
array_name[1]=value1
array_name[2]=value2
```

### 读取数组

读取数组元素值的一般格式是：

```
${array_name[index]}
```

### 实例

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

my_array=(A B "C" D)

echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]}"
echo "第三个元素为: ${my_array[2]}"
echo "第四个元素为: ${my_array[3]}"
```

执行脚本，输出结果如下所示：

```
$ chmod +x test.sh 
$ ./test.sh
第一个元素为: A
第二个元素为: B
第三个元素为: C
第四个元素为: D
```

### 获取数组中的所有元素

使用@ 或 * 可以获取数组中的所有元素，例如：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组的元素为: ${my_array[*]}"
echo "数组的元素为: ${my_array[@]}"
```

执行脚本，输出结果如下所示：

```
$ chmod +x test.sh 
$ ./test.sh
数组的元素为: A B C D
数组的元素为: A B C D
```

### 获取数组的长度

获取数组长度的方法与获取字符串长度的方法相同，例如：



```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组元素个数为: ${#my_array[*]}"
echo "数组元素个数为: ${#my_array[@]}"
```

执行脚本，输出结果如下所示：

```
$ chmod +x test.sh 
$ ./test.sh
数组元素个数为: 4
数组元素个数为: 4
```

数组的值也可以写入变量。

例如：

```
A=1
my_array=($A B C D)
echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]}"
echo "第三个元素为: ${my_array[2]}"
echo "第四个元素为: ${my_array[3]}"
```

输出为：

```
第一个元素为: 1第二个元素为: B第三个元素为: c第四个元素为: D
```

根据数组元素索引获取该数组元素值时，数组下标可为变量。

例如：

```
arr=(a b c d)
i=2
echo ${arr[i]}
```

输出为：

c

看数组的时候，觉得遍历数组用的比较多，所以自己试着写了写遍历，同时试了一下在SHELL脚本中的变量自增几个写法，在就新手学习的时候注意一下 [ 和 $ 之间要有空格，没有空格运行会报错，新手可能不太注意这一点，我开始就没注意到～～～～

示例如下：

```
#!/bin/bash

my_arry=(a b "c","d" abc)
echo "-------FOR循环遍历输出数组--------"
for i in ${my_arry[@]};
do
  echo $i
done

echo "-------::::WHILE循环输出 使用 let i++ 自增:::::---------"
j=0
while [ $j -lt ${#my_arry[@]} ]
do
  echo ${my_arry[$j]}
  let j++
done

echo "--------:::WHILE循环输出 使用 let  "n++ "自增: 多了双引号，其实不用也可以:::---------"
n=0
while [ $n -lt ${#my_arry[@]} ]
do
  echo ${my_arry[$n]}
  let "n++"
done

echo "---------::::WHILE循环输出 使用 let m+=1 自增,这种写法其他编程中也常用::::----------"
m=0
while [ $m -lt ${#my_arry[@]} ]
do
  echo ${my_arry[$m]}
  let m+=1
done

echo "-------::WHILE循环输出 使用 a=$[$a+1] 自增,个人觉得这种写法比较麻烦::::----------"
a=0
while [ $a -lt ${#my_arry[@]} ]
do
 echo ${my_arry[$a]}
 a=$[$a+1]
done
```

Bourne shell（原生kernel下）下不支持数组，只能通过模拟来实现类似数组功能。

实例 1

```
#!/bin/sh
#注意不是/bin/bash
echo "##############使用eval函数###############"
echo "使用参考:"
echo "http://www.runoob.com/linux/linux-comm-eval.html"
eval a1=bili
eval a2=nico
eval a3=yama

for i in 1 2 3 ; do
  eval echo "\$a$i"
done
```

输出结果：

```
##############使用eval函数###############
使用参考:
http://www.runoob.com/linux/linux-comm-eval.html
bili
nico
yama
```

实例 2

```
#!/bin/sh
#注意不是/bin/bash
echo "##########################################"
echo "指令参考:"
echo "http://www.runoob.com/linux/linux-comm-expr.html"
:<<!
根据用户输入的一句话来定义数组
并遍历数组元素
!
echo "输入字符串（以空格分开）:"
read str
i=0
for word in $str; do
    i=`expr $i + 1`
    eval a$i="$word"
    eval echo "数组的第 $i 个元素为: \$a$i"
done
```

输出结果：

```
##########################################
指令参考:
http://www.runoob.com/linux/linux-comm-expr.html
输入字符串（以空格分开）:
runoob google taobao
数组的第 1 个元素为: runoob
数组的第 2 个元素为: google
数组的第 3 个元素为: taobao
```

用 for 循环遍历数组：

```
#!/bin/bash
  arr=(1 2 3 4 5 6 7 8 9 10)
  for a in ${arr[*]}
  do
    echo $a
  done
```

# Shell 基本运算符

Shell 和其他编程语言一样，支持多种运算符，包括：

- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符

原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。

expr 是一款表达式计算工具，使用它能完成表达式的求值操作。

例如，两个数相加(**注意使用的是反引号 ` 而不是单引号 '**)：

## 实例

*#!/bin/bash*

val=**`****expr** 2 + 2**`**
**echo** "两数之和为 : $val"


[运行实例 »](https://www.runoob.com/try/runcode.php?filename=add2data&type=bash)

执行脚本，输出结果如下所示：

```
两数之和为 : 4
```

两点注意：

- 表达式和运算符之间要有空格，例如 2+2 是不对的，必须写成 2 + 2，这与我们熟悉的大多数编程语言不一样。
- 完整的表达式要被 **` `** 包含，注意这个字符不是常用的单引号，在 Esc 键下边。

------

## 算术运算符

下表列出了常用的算术运算符，假定变量 a 为 10，变量 b 为 20：

| 运算符 | 说明                                          | 举例                          |
| :----- | :-------------------------------------------- | :---------------------------- |
| +      | 加法                                          | `expr $a + $b` 结果为 30。    |
| -      | 减法                                          | `expr $a - $b` 结果为 -10。   |
| *      | 乘法                                          | `expr $a \* $b` 结果为  200。 |
| /      | 除法                                          | `expr $b / $a` 结果为 2。     |
| %      | 取余                                          | `expr $b % $a` 结果为 0。     |
| =      | 赋值                                          | a=$b 将把变量 b 的值赋给 a。  |
| ==     | 相等。用于比较两个数字，相同则返回 true。     | [ $a == $b ] 返回 false。     |
| !=     | 不相等。用于比较两个数字，不相同则返回 true。 | [ $a != $b ] 返回 true。      |

**注意：**条件表达式要放在方括号之间，并且要有空格，例如: **[$a==$b]** 是错误的，必须写成 **[ $a == $b ]**。

### 实例

算术运算符实例如下：

## 实例

*#!/bin/bash*
*# author:菜鸟教程*
*# url:www.runoob.com*

a=10
b=20

val=**`****expr** $a + $b**`**
**echo** "a + b : $val"

val=**`****expr** $a - $b**`**
**echo** "a - b : $val"

val=**`****expr** $a \***** $b**`**
**echo** "a * b : $val"

val=**`****expr** $b **/** $a**`**
**echo** "b / a : $val"

val=**`****expr** $b **%** $a**`**
**echo** "b % a : $val"

**if** **[** $a == $b **]**
**then**
  **echo** "a 等于 b"
**fi**
**if** **[** $a **!**= $b **]**
**then**
  **echo** "a 不等于 b"
**fi**

执行脚本，输出结果如下所示：

```
a + b : 30
a - b : -10
a * b : 200
b / a : 2
b % a : 0
a 不等于 b
```

> **注意：**
>
> - 乘号(*)前边必须加反斜杠(\)才能实现乘法运算；
> - if...then...fi 是条件语句，后续将会讲解。
> - 在 MAC 中 shell 的 expr 语法是：**$((表达式))**，此处表达式中的 "*" 不需要转义符号 "\" 。

------

## 关系运算符

关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

下表列出了常用的关系运算符，假定变量 a 为 10，变量 b 为 20：

| 运算符 | 说明                                                  | 举例                       |
| :----- | :---------------------------------------------------- | :------------------------- |
| -eq    | 检测两个数是否相等，相等返回 true。                   | [ $a -eq $b ] 返回 false。 |
| -ne    | 检测两个数是否不相等，不相等返回 true。               | [ $a -ne $b ] 返回 true。  |
| -gt    | 检测左边的数是否大于右边的，如果是，则返回 true。     | [ $a -gt $b ] 返回 false。 |
| -lt    | 检测左边的数是否小于右边的，如果是，则返回 true。     | [ $a -lt $b ] 返回 true。  |
| -ge    | 检测左边的数是否大于等于右边的，如果是，则返回 true。 | [ $a -ge $b ] 返回 false。 |
| -le    | 检测左边的数是否小于等于右边的，如果是，则返回 true。 | [ $a -le $b ] 返回 true。  |

### 实例

关系运算符实例如下：

## 实例


*#!/bin/bash*
*# author:菜鸟教程*
*# url:www.runoob.com*

a=10
b=20

**if** **[** $a -eq $b **]**
**then**
  **echo** "$a -eq $b : a 等于 b"
**else**
  **echo** "$a -eq $b: a 不等于 b"
**fi**
**if** **[** $a -ne $b **]**
**then**
  **echo** "$a -ne $b: a 不等于 b"
**else**
  **echo** "$a -ne $b : a 等于 b"
**fi**
**if** **[** $a -gt $b **]**
**then**
  **echo** "$a -gt $b: a 大于 b"
**else**
  **echo** "$a -gt $b: a 不大于 b"
**fi**
**if** **[** $a -lt $b **]**
**then**
  **echo** "$a -lt $b: a 小于 b"
**else**
  **echo** "$a -lt $b: a 不小于 b"
**fi**
**if** **[** $a -ge $b **]**
**then**
  **echo** "$a -ge $b: a 大于或等于 b"
**else**
  **echo** "$a -ge $b: a 小于 b"
**fi**
**if** **[** $a -le $b **]**
**then**
  **echo** "$a -le $b: a 小于或等于 b"
**else**
  **echo** "$a -le $b: a 大于 b"
**fi**

执行脚本，输出结果如下所示：

```
10 -eq 20: a 不等于 b
10 -ne 20: a 不等于 b
10 -gt 20: a 不大于 b
10 -lt 20: a 小于 b
10 -ge 20: a 小于 b
10 -le 20: a 小于或等于 b
```

------

## 布尔运算符

下表列出了常用的布尔运算符，假定变量 a 为 10，变量 b 为 20：

| 运算符 | 说明                                                | 举例                                     |
| :----- | :-------------------------------------------------- | :--------------------------------------- |
| !      | 非运算，表达式为 true 则返回 false，否则返回 true。 | [ ! false ] 返回 true。                  |
| -o     | 或运算，有一个表达式为 true 则返回 true。           | [ $a -lt 20 -o $b -gt 100 ] 返回 true。  |
| -a     | 与运算，两个表达式都为 true 才返回 true。           | [ $a -lt 20 -a $b -gt 100 ] 返回 false。 |

### 实例

布尔运算符实例如下：

## 实例

*#!/bin/bash*
*# author:菜鸟教程*
*# url:www.runoob.com*

a=10
b=20

**if** **[** $a **!**= $b **]**
**then**
  **echo** "$a != $b : a 不等于 b"
**else**
  **echo** "$a == $b: a 等于 b"
**fi**
**if** **[** $a -lt 100 -a $b -gt 15 **]**
**then**
  **echo** "$a 小于 100 且 $b 大于 15 : 返回 true"
**else**
  **echo** "$a 小于 100 且 $b 大于 15 : 返回 false"
**fi**
**if** **[** $a -lt 100 -o $b -gt 100 **]**
**then**
  **echo** "$a 小于 100 或 $b 大于 100 : 返回 true"
**else**
  **echo** "$a 小于 100 或 $b 大于 100 : 返回 false"
**fi**
**if** **[** $a -lt 5 -o $b -gt 100 **]**
**then**
  **echo** "$a 小于 5 或 $b 大于 100 : 返回 true"
**else**
  **echo** "$a 小于 5 或 $b 大于 100 : 返回 false"
**fi**

执行脚本，输出结果如下所示：

```
10 != 20 : a 不等于 b
10 小于 100 且 20 大于 15 : 返回 true
10 小于 100 或 20 大于 100 : 返回 true
10 小于 5 或 20 大于 100 : 返回 false
```

------

## 逻辑运算符

以下介绍 Shell 的逻辑运算符，假定变量 a 为 10，变量 b 为 20:

| 运算符 | 说明       | 举例                                      |
| :----- | :--------- | :---------------------------------------- |
| &&     | 逻辑的 AND | [[ $a -lt 100 && $b -gt 100 ]] 返回 false |
| \|\|   | 逻辑的 OR  | [[ $a -lt 100 || $b -gt 100 ]] 返回 true  |

### 实例

逻辑运算符实例如下：

## 实例


*#!/bin/bash*
*# author:菜鸟教程*
*# url:www.runoob.com*

a=10
b=20

**if** **[****[** $a -lt 100 **&&** $b -gt 100 **]****]**
**then**
  **echo** "返回 true"
**else**
  **echo** "返回 false"
**fi**

**if** **[****[** $a -lt 100 **||** $b -gt 100 **]****]**
**then**
  **echo** "返回 true"
**else**
  **echo** "返回 false"
**fi**

执行脚本，输出结果如下所示：

```
返回 false
返回 true
```

------

## 字符串运算符

下表列出了常用的字符串运算符，假定变量 a 为 "abc"，变量 b 为 "efg"：

| 运算符 | 说明                                         | 举例                     |
| :----- | :------------------------------------------- | :----------------------- |
| =      | 检测两个字符串是否相等，相等返回 true。      | [ $a = $b ] 返回 false。 |
| !=     | 检测两个字符串是否相等，不相等返回 true。    | [ $a != $b ] 返回 true。 |
| -z     | 检测字符串长度是否为0，为0返回 true。        | [ -z $a ] 返回 false。   |
| -n     | 检测字符串长度是否不为 0，不为 0 返回 true。 | [ -n "$a" ] 返回 true。  |
| $      | 检测字符串是否为空，不为空返回 true。        | [ $a ] 返回 true。       |

### 实例

字符串运算符实例如下：

## 实例


*#!/bin/bash*
*# author:菜鸟教程*
*# url:www.runoob.com*

a="abc"
b="efg"

**if** **[** $a = $b **]**
**then**
  **echo** "$a = $b : a 等于 b"
**else**
  **echo** "$a = $b: a 不等于 b"
**fi**
**if** **[** $a **!**= $b **]**
**then**
  **echo** "$a != $b : a 不等于 b"
**else**
  **echo** "$a != $b: a 等于 b"
**fi**
**if** **[** -z $a **]**
**then**
  **echo** "-z $a : 字符串长度为 0"
**else**
  **echo** "-z $a : 字符串长度不为 0"
**fi**
**if** **[** -n "$a" **]**
**then**
  **echo** "-n $a : 字符串长度不为 0"
**else**
  **echo** "-n $a : 字符串长度为 0"
**fi**
**if** **[** $a **]**
**then**
  **echo** "$a : 字符串不为空"
**else**
  **echo** "$a : 字符串为空"
**fi**

执行脚本，输出结果如下所示：

```
abc = efg: a 不等于 b
abc != efg : a 不等于 b
-z abc : 字符串长度不为 0
-n abc : 字符串长度不为 0
abc : 字符串不为空
```

------

## 文件测试运算符

文件测试运算符用于检测 Unix 文件的各种属性。

属性检测描述如下：

| 操作符  | 说明                                                         | 举例                      |
| :------ | :----------------------------------------------------------- | :------------------------ |
| -b file | 检测文件是否是块设备文件，如果是，则返回 true。              | [ -b $file ] 返回 false。 |
| -c file | 检测文件是否是字符设备文件，如果是，则返回 true。            | [ -c $file ] 返回 false。 |
| -d file | 检测文件是否是目录，如果是，则返回 true。                    | [ -d $file ] 返回 false。 |
| -f file | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。  |
| -g file | 检测文件是否设置了 SGID 位，如果是，则返回 true。            | [ -g $file ] 返回 false。 |
| -k file | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。  | [ -k $file ] 返回 false。 |
| -p file | 检测文件是否是有名管道，如果是，则返回 true。                | [ -p $file ] 返回 false。 |
| -u file | 检测文件是否设置了 SUID 位，如果是，则返回 true。            | [ -u $file ] 返回 false。 |
| -r file | 检测文件是否可读，如果是，则返回 true。                      | [ -r $file ] 返回 true。  |
| -w file | 检测文件是否可写，如果是，则返回 true。                      | [ -w $file ] 返回 true。  |
| -x file | 检测文件是否可执行，如果是，则返回 true。                    | [ -x $file ] 返回 true。  |
| -s file | 检测文件是否为空（文件大小是否大于0），不为空返回 true。     | [ -s $file ] 返回 true。  |
| -e file | 检测文件（包括目录）是否存在，如果是，则返回 true。          | [ -e $file ] 返回 true。  |

其他检查符：

- **-S**: 判断某文件是否 socket。
- **-L**: 检测文件是否存在并且是一个符号链接。



### 实例

变量 file 表示文件 **/var/www/runoob/test.sh**，它的大小为 100 字节，具有 **rwx** 权限。下面的代码，将检测该文件的各种属性：



## 实例

*#!/bin/bash*
*# author:菜鸟教程*
*# url:www.runoob.com*

file="/var/www/runoob/test.sh"
**if** **[** -r $file **]**
**then**
  **echo** "文件可读"
**else**
  **echo** "文件不可读"
**fi**
**if** **[** -w $file **]**
**then**
  **echo** "文件可写"
**else**
  **echo** "文件不可写"
**fi**
**if** **[** -x $file **]**
**then**
  **echo** "文件可执行"
**else**
  **echo** "文件不可执行"
**fi**
**if** **[** -f $file **]**
**then**
  **echo** "文件为普通文件"
**else**
  **echo** "文件为特殊文件"
**fi**
**if** **[** -d $file **]**
**then**
  **echo** "文件是个目录"
**else**
  **echo** "文件不是个目录"
**fi**
**if** **[** -s $file **]**
**then**
  **echo** "文件不为空"
**else**
  **echo** "文件为空"
**fi**
**if** **[** -e $file **]**
**then**
  **echo** "文件存在"
**else**
  **echo** "文件不存在"
**fi**

执行脚本，输出结果如下所示：

```
文件可读
文件可写
文件可执行
文件为普通文件
文件不是个目录
文件不为空
文件存在
```

EQ 就是 EQUAL等于

NE 就是 NOT EQUAL不等于 

GT 就是 GREATER THAN大于　 

LT 就是 LESS THAN小于 

GE 就是 GREATER THAN OR EQUAL 大于等于 

LE 就是 LESS THAN OR EQUAL 小于等于

使用 **[[ ... ]]** 条件判断结构，而不是 **[ ... ]**，能够防止脚本中的许多逻辑错误。比如，**&&**、**||**、**<** 和 **>** 操作符能够正常存在于 **[[ ]]** 条件判断结构中，但是如果出现在 **[ ]** 结构中的话，会报错。

1、进行数值比较时，可以使用 **[ expression1 OPexpression2 ]**，**OP** 可以为 **-gt、-lt、-ge、-le、-eq、-ne** 也可以使用 **((expression1 OP expression2))**，**OP** 可以为 **>、<、>=、<=、==、!=**。这几个关系运算符都是测试整数表达式 expression1 和 expression2 之间的大小关系。

2、 **>、<、==、!=** 也可以进行字符串比较。

3、进行字符串比较时，== 可以使用 = 替代。

4、 == 和 !=进行字符串比较时，可以使用 [ string1 OP string2 ] 或者 [[ string1 OP string2 ]] 的形式。

5、 > 和 < 进行字符串比较时，需要使用[[ string1 OP string2 ]] 或者 [ string1 \OP string2 ]。也就是使用 [] 时，> 和 < 需要使用反斜线转义。

字符串比较是否为 **null** 这里:

```
#!/bin/bash

a=""
if [ -n $a ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
```

输出结果为：

```
-n  : 字符串长度不为 0
```

从结果上看 **-n $a** 返回 true，这并正确，正确的做法是 **$a** 这里应该加上双引号，否则 **-n $a** 的结果永远是 true：

```
#!/bin/bash

a=""
if [ -n "$a" ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
```

输出结果为：

```
-n  : 字符串长度为 0
```

Shell 相加目前发现有 3 种写法：

**1.**

```
a=10
b=20
c=`expr ${a} + ${b}`
echo "$c"
```

**2.**

```
c=$[ `expr 10 + 20` ]
echo "$c"
```

**3.**

```
c=$[ 10 + 20 ]
echo "$c"
```

初学者推荐第一种写法，虽然看着复杂，但逻辑清晰，不易混淆。

推荐用 **$()** 代替 **``**:

```
val=`expr 10 + 20`

val=$(expr 10 + 20)
```

相加补充一种方式：

```
a=10
b=20
c=$(($a+$b))
```

**[] 表达式**

**注意**：在 [] 表达式中，常见的 >, < 需要加转义字符，表示字符串大小比较，以 acill 码位置作为比较。不直接支持 >, < 运算符，还有逻辑运算符 || 、&& ，它需要用 -a[and] –o[or] 表示。

**[[ ]] 表达式**

**注意**：[[]] 运算符只是 [] 运算符的扩充。能够支持 >, < 符号运算不需要转义符，它还是以字符串比较大小。里面支持逻辑运算符：**|| &&** ，不再使用 **-a -o**。

## Shell echo命令

Shell 的 echo 指令与 PHP 的 echo 指令类似，都是用于字符串的输出。命令格式：

```
echo string
```

您可以使用echo实现更复杂的输出格式控制。

### 1.显示普通字符串:

```
echo "It is a test"
```

这里的双引号完全可以省略，以下命令与上面实例效果一致：

```
echo It is a test
```

### 2.显示转义字符

```
echo "\"It is a test\""
```

结果将是:

```
"It is a test"
```

同样，双引号也可以省略

### 3.显示变量

read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量

```
#!/bin/sh
read name 
echo "$name It is a test"
```

以上代码保存为 test.sh，name 接收标准输入的变量，结果将是:

```
[root@www ~]# sh test.sh
OK                     #标准输入
OK It is a test        #输出
```

### 4.显示换行

```
echo -e "OK! \n" # -e 开启转义
echo "It is a test"
```

输出结果：

```
OK!

It is a test
```

### 5.显示不换行

```
#!/bin/sh
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"
```

输出结果：

```
OK! It is a test
```

### 6.显示结果定向至文件

```
echo "It is a test" > myfile
```

### 7.原样输出字符串，不进行转义或取变量(用单引号)

```
echo '$name\"'
```

输出结果：

```
$name\"
```

### 8.显示命令执行结果

```
echo `date`
```

**注意：** 这里使用的是反引号 **`**, 而不是单引号 **'**。

结果将显示当前日期

```
Thu Jul 24 10:08:46 CST 2014
```

echo输出的字符串总结

===================================================================

​    能否引用变量  |  能否引用转移符  |  能否引用文本格式符(如：换行符、制表符)

单引号  |      否      |       否       |               否

双引号  |      能      |       能       |               能

无引号  |      能      |       能       |               否              

===================================================================

read 命令一个一个词组地接收输入的参数，每个词组需要使用空格进行分隔；如果输入的词组个数大于需要的参数个数，则多出的词组将被作为整体为最后一个参数接收。

测试文件 test.sh 代码如下：

```
read firstStr secondStr
echo "第一个参数:$firstStr; 第二个参数:$secondStr"
```

执行测试：

```
$ sh test.sh 
一 二 三 四
第一个参数:一; 第二个参数:二 三 四
```

实例, 文件 test.sh:

```
read -p "请输入一段文字:" -n 6 -t 5 -s password
echo -e "\npassword is $password"
```

参数说明：

-  **-p** 输入提示文字
-  **-n** 输入字符长度限制(达到6位，自动结束)
-  **-t** 输入限时
-  **-s** 隐藏输入内容

```
$ sh test.sh 
请输入一段文字:
password is asdfgh
```

**>** 重定向输出到某个位置，替换原有文件的所有内容。

**>>** 重定向追加到某个位置，在原有文件的末尾添加内容。

**<** 重定向输入某个位置文件。

**2>** 重定向错误输出。

**2>>** 重定向错误追加输出到文件末尾。

**&>** 混合输出错误的和正确的都输出。

# Shell printf 命令

上一章节我们学习了 Shell 的 echo 命令，本章节我们来学习 Shell 的另一个输出命令 printf。

printf 命令模仿 C 程序库（library）里的 printf() 程序。

printf 由 POSIX 标准所定义，因此使用 printf 的脚本比使用 echo 移植性好。

printf 使用引用文本或空格分隔的参数，外面可以在 printf 中使用格式化字符串，还可以制定字符串的宽度、左右对齐方式等。默认 printf 不会像 echo 自动添加换行符，我们可以手动添加 \n。

printf 命令的语法：

```
printf  format-string  [arguments...]
```

**参数说明：**

- **format-string:** 为格式控制字符串
- **arguments:** 为参数列表。

实例如下：

```
$ echo "Hello, Shell"
Hello, Shell
$ printf "Hello, Shell\n"
Hello, Shell
$
```

接下来,我来用一个脚本来体现printf的强大功能：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com
 
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876 
```

执行脚本，输出结果如下所示：

```
姓名     性别   体重kg
郭靖     男      66.12
杨过     男      48.65
郭芙     女      47.99
```

%s %c %d %f都是格式替代符

%-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。

%-4.2f 指格式化为小数，其中.2指保留2位小数。



更多实例：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com
 
# format-string为双引号
printf "%d %s\n" 1 "abc"

# 单引号与双引号效果一样 
printf '%d %s\n' 1 "abc" 

# 没有引号也可以输出
printf %s abcdef

# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def

printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j

# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
printf "%s and %d \n" 
```

执行脚本，输出结果如下所示：

```
1 abc
1 abc
abcdefabcdefabc
def
a b c
d e f
g h i
j  
 and 0
```

------

## printf的转义序列

| 序列  | 说明                                                         |
| :---- | :----------------------------------------------------------- |
| \a    | 警告字符，通常为ASCII的BEL字符                               |
| \b    | 后退                                                         |
| \c    | 抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略 |
| \f    | 换页（formfeed）                                             |
| \n    | 换行                                                         |
| \r    | 回车（Carriage return）                                      |
| \t    | 水平制表符                                                   |
| \v    | 垂直制表符                                                   |
| \\    | 一个字面上的反斜杠字符                                       |
| \ddd  | 表示1到3位数八进制值的字符。仅在格式字符串中有效             |
| \0ddd | 表示1到3位的八进制值字符                                     |

### 实例

```
$ printf "a string, no processing:<%s>\n" "A\nB"
a string, no processing:<A\nB>

$ printf "a string, no processing:<%b>\n" "A\nB"
a string, no processing:<A
B>

$ printf "www.runoob.com \a"
www.runoob.com $                  #不换行
```

**%d %s %c %f** 格式替代符详解:

**d: Decimal 十进制整数** -- 对应位置参数必须是十进制整数，否则报错！

**s: String 字符串** -- 对应位置参数必须是字符串或者字符型，否则报错！

**c: Char 字符** -- 对应位置参数必须是字符串或者字符型，否则报错！

**f: Float 浮点** -- 对应位置参数必须是数字型，否则报错！

如：其中最后一个参数是 "def"，%c 自动截取字符串的第一个字符作为结果输出。

```
$  printf "%d %s %c\n" 1 "abc" "def"
1 abc d
```

补充格式符 %b:

**%b: 字符串--**相对应的参数被视为含有要被处理的转义序列之字符串

```
$ printf "a string, no processing:<%b>\n" "A\nB"
a string, no processing:<A
B>
```

无论时在格式字符串内还是在使用 %b 所打印的参数字符串里，大部分的转义序列都是被相同对待。

无论如何，\c 与 \0ddd 只有搭配 %b 使用才有效，而 \ddd 只有在格式字符串里才会被解释。

**%f** 格式化浮点数默认支持 6 位小数:

```
$ printf "%d %s %c %f\n" 10 "abc" "def" "3.1415926"
10 abc d 3.141593          # 格式化浮点数默认支持小数点后六位，后面多出的四舍五入
```

# Shell test 命令

Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

------

## 数值测试

| 参数 | 说明           |
| :--- | :------------- |
| -eq  | 等于则为真     |
| -ne  | 不等于则为真   |
| -gt  | 大于则为真     |
| -ge  | 大于等于则为真 |
| -lt  | 小于则为真     |
| -le  | 小于等于则为真 |

## 实例

num1=100
num2=100
**if** **test** $**[**num1**]** -eq $**[**num2**]**
**then**
  **echo** '两个数相等！'
**else**
  **echo** '两个数不相等！'
**fi**

输出结果：

```
两个数相等！
```

代码中的 **[]** 执行基本的算数运算，如：

## 实例

*#!/bin/bash*

a=5
b=6

result=$**[**a+b**]** *# 注意等号两边不能有空格*
**echo** "result 为： $result"

结果为:

```
result 为： 11
```

------

## 字符串测试

| 参数      | 说明                     |
| :-------- | :----------------------- |
| =         | 等于则为真               |
| !=        | 不相等则为真             |
| -z 字符串 | 字符串的长度为零则为真   |
| -n 字符串 | 字符串的长度不为零则为真 |

## 实例

num1="ru1noob"
num2="runoob"
**if** **test** $num1 = $num2
**then**
  **echo** '两个字符串相等!'
**else**
  **echo** '两个字符串不相等!'
**fi**

输出结果：

```
两个字符串不相等!
```

------

## 文件测试

| 参数      | 说明                                 |
| :-------- | :----------------------------------- |
| -e 文件名 | 如果文件存在则为真                   |
| -r 文件名 | 如果文件存在且可读则为真             |
| -w 文件名 | 如果文件存在且可写则为真             |
| -x 文件名 | 如果文件存在且可执行则为真           |
| -s 文件名 | 如果文件存在且至少有一个字符则为真   |
| -d 文件名 | 如果文件存在且为目录则为真           |
| -f 文件名 | 如果文件存在且为普通文件则为真       |
| -c 文件名 | 如果文件存在且为字符型特殊文件则为真 |
| -b 文件名 | 如果文件存在且为块特殊文件则为真     |

## 实例

**cd** **/**bin
**if** **test** -e .**/****bash**
**then**
  **echo** '文件已存在!'
**else**
  **echo** '文件不存在!'
**fi**

输出结果：

```
文件已存在!
```

另外，Shell 还提供了与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为： **!** 最高， **-a** 次之， **-o** 最低。例如：

## 实例

**cd** **/**bin
**if** **test** -e .**/**notFile -o -e .**/****bash**
**then**
  **echo** '至少有一个文件存在!'
**else**
  **echo** '两个文件都不存在'
**fi**

输出结果：

```
至少有一个文件存在!
```

**符号含义：**

\1. eq （equal的缩写），表示等于为真

\2. ne  (not equal的缩写），表示不等于为真

\3. gt   (greater than的缩写），表示大于为真

\4. ge （greater&equal的缩写），表示大于等于为真

\5. lt  （lower than的缩写），表示小于为真

\6. le  （lower&equal的缩写），表示小于等于为真

```
result=$[a + b]
```

等同于：

```
result=`expr $a + $b `
```

**shell 判断文件夹或文件是否存在**

文件夹不存在则创建

```
if [ ! -d "/data/" ];then
  mkdir /data
  else
  echo "文件夹已经存在"
fi
```

文件存在则删除

```
if [ ! -f "/data/filename" ];then
  echo "文件不存在"
  else
  rm -f /data/filename
fi
```

判断文件夹是否存在

```
if [ -d "/data/" ];then
  echo "文件夹存在"
  else
  echo "文件夹不存在"
fi
```

判断文件是否存在

```
if [ -f "/data/filename" ];then
  echo "文件存在"
  else
  echo "文件不存在"
fi
```

文件比较符

```
-e 判断对象是否存在
-d 判断对象是否存在，并且为目录
-f 判断对象是否存在，并且为常规文件
-L 判断对象是否存在，并且为符号链接
-h 判断对象是否存在，并且为软链接
-s 判断对象是否存在，并且长度不为0
-r 判断对象是否存在，并且可读
-w 判断对象是否存在，并且可写
-x 判断对象是否存在，并且可执行
-O 判断对象是否存在，并且属于当前用户
-G 判断对象是否存在，并且属于当前用户组
-nt 判断file1是否比file2新  [ "/data/file1" -nt "/data/file2" ]
-ot 判断file1是否比file2旧  [ "/data/file1" -ot "/data/file2" ]
```

除非你清楚自己在干什么，**否则请避免在”Shell test命令“中使用单引号**——使用它可能会导致难以察觉的错误，尤其是对于Shell初学者。



让我用下列实例更进一步地解释为什么：



```
#! /bin/bash
# 模拟终端某一指令输出为空时用 test -z 配合单引号进行判断的效果 
wrong=``
#注意：反引号内没有任何字符
echo $wrong
if test -z '$wrong'; then
   echo "The result is empty."
else
   echo "The result is not empty."
fi
```

执行一下：

```
$ ./script-name.sh
The result is not empty.
```

执行后的结果与我们所期望的正好**相反**。这是**因为单引号会将其内部的内容原样输出。**

**此时不论**命令的输出**是否****非空，最终都会**被判为**非空。**

而如果你此时没有察觉到错误的根源是单引号，相信我：你会想方设法去掉脚本输出的空格——而空格根本既无法消除又没有实际作用。

```
if [ -d "/data/" ];then
  echo "文件夹存在"
  else
  echo "文件夹不存在"
fi
```

**"/data/"** 双引号可以去掉。

**[]** 内部两端要有空格、**-d** 参数和其他内容之间要有空格， 如果 then 另起一行的话 then 前不需要加 **;** 否则需要在 then 前加 **;**。

```
if test -d /data/
then
    echo '文件夹存在!'
else
    echo '文件夹不存在!'
fi
```

**-d** 参数和其他内容之间要有空格。

then 要另起一行。

# Shell 流程控制

和Java、PHP等语言不一样，sh的流程控制不可为空，如(以下为PHP流程控制写法)：

```
<?php
if (isset($_GET["q"])) {
    search(q);
}
else {
    // 不做任何事情
}
```

在sh/bash里可不能这么写，如果else分支没有语句执行，就不要写这个else。

------

## if else

### if

if 语句语法格式：

```
if condition
then
    command1 
    command2
    ...
    commandN 
fi
```

写成一行（适用于终端命令提示符）：

```
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```

末尾的fi就是if倒过来拼写，后面还会遇到类似的。

### if else

if else 语法格式：

```
if condition
then
    command1 
    command2
    ...
    commandN
else
    command
fi
```

### if else-if else

if else-if else 语法格式：

```
if condition1
then
    command1
elif condition2 
then 
    command2
else
    commandN
fi
```

以下实例判断两个变量是否相等：

```
a=10
b=20
if [ $a == $b ]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi
```

输出结果：

```
a 小于 b
```

if else语句经常与test命令结合使用，如下所示：

```
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi
```

输出结果：

```
两个数字相等!
```

------

## for 循环

与其他编程语言类似，Shell支持for循环。

for循环一般格式为：

```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```

写成一行：

```
for var in item1 item2 ... itemN; do command1; command2… done;
```

当变量值在列表里，for循环即执行一次所有命令，使用变量名获取列表中的当前取值。命令可为任何有效的shell命令和语句。in列表可以包含替换、字符串和文件名。

in列表是可选的，如果不用它，for循环使用命令行的位置参数。

例如，顺序输出当前列表中的数字：

```
for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done
```

输出结果：

```
The value is: 1
The value is: 2
The value is: 3
The value is: 4
The value is: 5
```

顺序输出字符串中的字符：

```
for str in 'This is a string'
do
    echo $str
done
```

输出结果：

```
This is a string
```

------

## while 语句

while循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。其格式为：

```
while condition
do
    command
done
```

以下是一个基本的while循环，测试条件是：如果int小于等于5，那么条件返回真。int从0开始，每次循环处理时，int加1。运行上述脚本，返回数字1到5，然后终止。

```
#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
```

运行脚本，输出：

```
1
2
3
4
5
```

以上实例使用了 Bash let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量，具体可查阅：[Bash let 命令](https://www.runoob.com/linux/linux-comm-let.html)

。

while循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量FILM，按<Ctrl-D>结束循环。

```
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done
```

运行脚本，输出类似下面：

```
按下 <CTRL-D> 退出
输入你最喜欢的网站名:菜鸟教程
是的！菜鸟教程 是一个好网站
```

### 无限循环

无限循环语法格式：

```
while :
do
    command
done
```

或者

```
while true
do
    command
done
```

或者

```
for (( ; ; ))
```



------

## until 循环

until 循环执行一系列命令直至条件为 true 时停止。

until 循环与 while 循环在处理方式上刚好相反。

一般 while 循环优于 until 循环，但在某些时候—也只是极少数情况下，until 循环更加有用。

until 语法格式:

```
until condition
do
    command
done
```

condition 一般为条件表达式，如果返回值为 false，则继续执行循环体内的语句，否则跳出循环。

以下实例我们使用 until 命令来输出 0 ~ 9 的数字：

```
#!/bin/bash

a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```

运行结果：

输出结果为：

```
0
1
2
3
4
5
6
7
8
9
```

------

## case

Shell case语句为多选择语句。可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。case语句格式如下：

```
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

case工作方式如上所示。取值后面必须为单词in，每一模式必须以右括号结束。取值可以为变量或常数。匹配发现取值符合某一模式后，其间所有命令开始执行直至 ;;。

取值将检测匹配的每一个模式。一旦模式匹配，则执行完匹配模式相应命令后不再继续其他模式。如果无一匹配模式，使用星号 * 捕获该值，再执行后面的命令。

下面的脚本提示输入1到4，与每一种模式进行匹配：

```
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

输入不同的内容，会有不同的结果，例如：

```
输入 1 到 4 之间的数字:
你输入的数字为:
3
你选择了 3
```

------

## 跳出循环

在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell使用两个命令来实现该功能：break和continue。

### break命令

break命令允许跳出所有循环（终止执行后面的所有循环）。

下面的例子中，脚本进入死循环直至用户输入数字大于5。要跳出这个循环，返回到shell提示符下，需要使用break命令。

```
#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
            break
        ;;
    esac
done
```

执行以上代码，输出结果为：

```
输入 1 到 5 之间的数字:3
你输入的数字为 3!
输入 1 到 5 之间的数字:7
你输入的数字不是 1 到 5 之间的! 游戏结束
```

### continue

continue命令与break命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

对上面的例子进行修改：

```
#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done
```

运行代码发现，当输入大于5的数字时，该例中的循环不会结束，语句 **echo "游戏结束"** 永远不会被执行。

------

## case ... esac



**case ... esac** 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构，每个 case 分支用右圆括号开始，用两个分号 **;;** 表示 break，即执行结束，跳出整个 case ... esac 语句，esac（就是 case 反过来）作为结束标记。

case ... esac 语法格式如下：

```
case 值 in
模式1)
    command1
    command2
    command3
    ;;
模式2）
    command1
    command2
    command3
    ;;
*)
    command1
    command2
    command3
    ;;
esac
```

case 后为取值，值可以为变量或常数。

值后为关键字 in，接下来是匹配的各种模式，每一模式最后必须以右括号结束，模式支持正则表达式。

## 实例

*#!/bin/sh*

site="runoob"

**case** "$site" **in**
  "runoob"**)** **echo** "菜鸟教程"
  **;;**
  "google"**)** **echo** "Google 搜索"
  **;;**
  "taobao"**)** **echo** "淘宝网"
  **;;**
**esac**

输出结果为：

```
菜鸟教程
```

shell 中的 for 循环不仅可以用文章所述的方法。

对于习惯其他语言 for 循环的朋友来说可能有点别扭。

```
for((assignment;condition:next));do
    command_1;
    command_2;
    commond_..;
done;
```

如上所示，这里的 for 循环与 C 中的相似，但并不完全相同。

通常情况下 shell 变量调用需要加 $,但是 for 的 (()) 中不需要,下面来看一个例子：

```
#!/bin/bash
for((i=1;i<=5;i++));do
    echo "这是第 $i 次调用";
done;
```

执行结果：

```
这是第1次调用
这是第2次调用
这是第3次调用
这是第4次调用
这是第5次调用
```

与 C 中相似，赋值和下一步执行可以放到代码之前循环语句之中执行，这里要注意一点：如果要在循环体中进行 for 中的 next 操作，记得变量要加 $，不然程序会变成死循环。

# Shell 函数

linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。

shell中函数的定义格式如下：

```
[ function ] funname [()]

{

    action;

    [return int;]

}
```

说明：

- 1、可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
- 2、参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255

下面的例子定义了一个函数并进行调用：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

demoFun(){
    echo "这是我的第一个 shell 函数!"
}
echo "-----函数开始执行-----"
demoFun
echo "-----函数执行完毕-----"
```

输出结果：

```
-----函数开始执行-----
这是我的第一个 shell 函数!
-----函数执行完毕-----
```

下面定义一个带有return语句的函数：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
```

输出类似下面：

```
这个函数会对输入的两个数字进行相加运算...
输入第一个数字: 
1
输入第二个数字: 
2
两个数字分别为 1 和 2 !
输入的两个数字之和为 3 !
```

函数返回值在调用该函数后通过 $? 来获得。

注意：所有函数在使用前必须定义。这意味着必须将函数放在脚本开始部分，直至shell解释器首次发现它时，才可以使用。调用函数仅使用其函数名即可。

------

## 函数参数

在Shell中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...

带参数的函数示例：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

输出结果：

```
第一个参数为 1 !
第二个参数为 2 !
第十个参数为 10 !
第十个参数为 34 !
第十一个参数为 73 !
参数总数有 11 个!
作为一个字符串输出所有参数 1 2 3 4 5 6 7 8 9 34 73 !
```

注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。

另外，还有几个特殊字符用来处理参数：

| 参数处理 | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| $#       | 传递到脚本或函数的参数个数                                   |
| $*       | 以一个单字符串显示所有向脚本传递的参数                       |
| $$       | 脚本运行的当前进程ID号                                       |
| $!       | 后台运行的最后一个进程的ID号                                 |
| $@       | 与$*相同，但是使用时加引号，并在引号中返回每个参数。         |
| $-       | 显示Shell使用的当前选项，与set命令功能相同。                 |
| $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |

**$?** 仅对其上一条指令负责，一旦函数返回后其返回值没有立即保存入参数，那么其返回值将不再能通过 **$?** 获得。

测试代码：

```
#!/bin/bash
function demoFun1(){
    echo "这是我的第一个 shell 函数!"
    return `expr 1 + 1`
}

demoFun1
echo $?

function demoFun2(){
 echo "这是我的第二个 shell 函数!"
 expr 1 + 1
}

demoFun2
echo $?
demoFun1
echo 在这里插入命令！
echo $?
```

输出结果：

```
这是我的第一个 shell 函数!
2
这是我的第二个 shell 函数!
2
0
这是我的第一个 shell 函数!
在这里插入命令！
0
```

调用 demoFun2 后，函数最后一条命令 expr 1 + 1 得到的返回值（$?值）为 0，意思是这个命令没有出错。所有的命令的返回值仅表示其是否出错，而不会有其他有含义的结果。

第二次调用 demoFun1 后，没有立即查看 $? 的值，而是先插入了一条别的 echo 命令，最后再查看 $? 的值得到的是 0，也就是上一条 echo 命令的结果，而 demoFun1 的返回值被覆盖了。

下面这个测试，连续使用两次 **echo $?**，得到的结果不同，更为直观：

```
#!/bin/bash

function demoFun1(){
    echo "这是我的第一个 shell 函数!"
    return `expr 1 + 1`
}

demoFun1
echo $?
echo $?
```

输出结果：

```
这是我的第一个 shell 函数!
2
0
```

函数与命令的执行结果可以作为条件语句使用。要注意的是，和 C 语言不同，shell 语言中 0 代表 true，0 以外的值代表 false。

请参见下例：

```
#!/bin/bash

echo "Hello World !" | grep -e Hello
echo $?
echo "Hello World !" | grep -e Bye
echo $?
if echo "Hello World !" | grep -e Hello
then
    echo true
else
    echo false
fi

if echo "Hello World !" | grep -e Bye
then
    echo true
else
    echo false
fi

function demoFun1(){
    return 0
}

function demoFun2(){
    return 12
}

if demoFun1
then
    echo true
else
    echo false
fi

if demoFun2
then
    echo ture
else
    echo false
fi
```

其执行结果如下：

```
Hello World !
0
1
Hello World !
true
false
true
false
```

grep 是从给定字符串中寻找匹配内容的命令。首先看出如果找到了匹配的内容，会打印匹配部分且得到的返回值 $? 为 0，如果找不到，则返回值 $? 为 1。

接下来分别将这两次执行的 grep 命令当作条件语句交给 if 判断，得出返回值 $? 为 0，即执行成功时，条件语句为 true，当返回值 $? 为 1，即执行失败时，条件语句为 false。

之后再用函数的 return 值作为测试，其中 demoFun1 返回值为 0，demoFun2 返回值选择了任意一个和 0 不同的整数，这里为 12。

将函数作为条件语句交给 if 判断，得出返回值为 0 时，依然为 true，而返回值只要不是 0，条件语句都判断为 false。

# Shell 输入/输出重定向

大多数 UNIX 系统命令从你的终端接受输入并将所产生的输出发送回到您的终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。

重定向命令列表如下：

| 命令            | 说明                                               |
| :-------------- | :------------------------------------------------- |
| command > file  | 将输出重定向到 file。                              |
| command < file  | 将输入重定向到 file。                              |
| command >> file | 将输出以追加的方式重定向到 file。                  |
| n > file        | 将文件描述符为 n 的文件重定向到 file。             |
| n >> file       | 将文件描述符为 n 的文件以追加的方式重定向到 file。 |
| n >& m          | 将输出文件 m 和 n 合并。                           |
| n <& m          | 将输入文件 m 和 n 合并。                           |
| << tag          | 将开始标记 tag 和结束标记 tag 之间的内容作为输入。 |

> 需要注意的是文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。

------

## 输出重定向

重定向一般通过在命令间插入特定的符号来实现。特别的，这些符号的语法如下所示:

```
command1 > file1
```

上面这个命令执行command1然后将输出的内容存入file1。

注意任何file1内的已经存在的内容将被新内容替代。如果要将新内容添加在文件末尾，请使用>>操作符。

### 实例

执行下面的 who 命令，它将命令的完整的输出重定向在用户文件中(users):

```
$ who > users
```

执行后，并没有在终端输出信息，这是因为输出已被从默认的标准输出设备（终端）重定向到指定的文件。

你可以使用 cat 命令查看文件内容：

```
$ cat users
_mbsetupuser console  Oct 31 17:35 
tianqixin    console  Oct 31 17:35 
tianqixin    ttys000  Dec  1 11:33 
```

输出重定向会覆盖文件内容，请看下面的例子：

```
$ echo "菜鸟教程：www.runoob.com" > users
$ cat users
菜鸟教程：www.runoob.com
$
```

如果不希望文件内容被覆盖，可以使用 >> 追加到文件末尾，例如：

```
$ echo "菜鸟教程：www.runoob.com" >> users
$ cat users
菜鸟教程：www.runoob.com
菜鸟教程：www.runoob.com
$
```

------

## 输入重定向

和输出重定向一样，Unix 命令也可以从文件获取输入，语法为：

```
command1 < file1
```

这样，本来需要从键盘获取输入的命令会转移到文件读取内容。

注意：输出重定向是大于号(>)，输入重定向是小于号(<)。

### 实例

接着以上实例，我们需要统计 users 文件的行数,执行以下命令：

```
$ wc -l users
       2 users
```

也可以将输入重定向到 users 文件：

```
$  wc -l < users
       2 
```

注意：上面两个例子的结果不同：第一个例子，会输出文件名；第二个不会，因为它仅仅知道从标准输入读取内容。

```
command1 < infile > outfile
```

同时替换输入和输出，执行command1，从文件infile读取内容，然后将输出写入到outfile中。

### 重定向深入讲解

一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：

- 标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据。
- 标准输出文件(stdout)：stdout 的文件描述符为1，Unix程序默认向stdout输出数据。
- 标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。

默认情况下，command > file 将 stdout 重定向到 file，command < file 将stdin 重定向到 file。

如果希望 stderr 重定向到 file，可以这样写：

```
$ command 2 > file
```

如果希望 stderr 追加到 file 文件末尾，可以这样写：

```
$ command 2 >> file
```

**2** 表示标准错误文件(stderr)。

如果希望将 stdout 和 stderr 合并后重定向到 file，可以这样写：

```
$ command > file 2>&1

或者

$ command >> file 2>&1
```

如果希望对 stdin 和 stdout 都重定向，可以这样写：

```
$ command < file1 >file2
```

command 命令将 stdin 重定向到 file1，将 stdout 重定向到 file2。

------

## Here Document

Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序。

它的基本的形式如下：

```
command << delimiter
    document
delimiter
```

它的作用是将两个 delimiter 之间的内容(document) 作为输入传递给 command。

> 注意：
>
> - 结尾的delimiter 一定要顶格写，前面不能有任何字符，后面也不能有任何字符，包括空格和 tab 缩进。
> - 开始的delimiter前后的空格会被忽略掉。

### 实例

在命令行中通过 wc -l 命令计算 Here Document 的行数：

```
$ wc -l << EOF
    欢迎来到
    菜鸟教程
    www.runoob.com
EOF
3          # 输出结果为 3 行
$
```

我们也可以将 Here Document 用在脚本中，例如：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

cat << EOF
欢迎来到
菜鸟教程
www.runoob.com
EOF
```

执行以上脚本，输出结果：

```
欢迎来到
菜鸟教程
www.runoob.com
```

------

## /dev/null 文件

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null：

```
$ command > /dev/null
```

/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：

```
$ command > /dev/null 2>&1
```

> **注意：**0 是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。
>
> 这里的 **2** 和 **>** 之间不可以有空格，**2>** 是一体的时候才表示错误输出。

```
$ command > file 2>&1
$ command >> file 2>&1
```

这里的**&**没有固定的意思

放在**>**后面的**&**，表示重定向的目标不是一个**文件**，而是一个**文件描述符**，内置的文件描述符如下

```
1 => stdout
2 => stderr
0 => stdin
```

换言之 **2>1** 代表将**stderr**重定向到当前路径下文件名为**1**的**regular file**中，而**2>&1**代表将**stderr**重定向到**文件描述符**为**1**的文件(即**/dev/stdout**)中，这个文件就是**stdout**在**file system**中的映射

而**&>file**是一种特殊的用法，也可以写成**>&file**，二者的意思完全相同，都等价于

```
>file 2>&1
```

此处**&>**或者**>&**视作整体，分开没有单独的含义

------

**顺序问题：**

```
find /etc -name .bashrc > list 2>&1
# 我想问为什么不能调下顺序,比如这样
find /etc -name .bashrc 2>&1 > list
```

这个是从左到右有顺序的

第一种

```
xxx > list 2>&1
```

先将要输出到**stdout**的内容重定向到文件，此时文件**list**就是这个程序的**stdout**，再将**stderr**重定向到**stdout**，也就是文件**list**

第二种

```
xxx 2>&1 > list
```

先将要输出到**stderr**的内容重定向到**stdout**，此时会产生一个**stdout的拷贝**，作为程序的**stderr**，而程序原本要输出到**stdout**的内容，依然是对接在**stdout原身**上的，因此第二步重定向**stdout**，对**stdout的拷贝**不产生任何影响

对于上面 '2>&1'，举个例子，比如说:

```
$ find /etc -names "*.txt"  >list 2>&1
```

从左往右执行，执行到 >list，此时的 stdout 为 list；而执行到 2>&1，表示 stderr 重定向到 stdout，这里也就是 list 文件。

因为 **[ find /etc -names "\*.txt" ]** 这条命令是错误的( -names 应该是 -name)。

本来要输出到终端屏幕的错误信息:

```
find: unknown predicate `-names`
```

被重定向到了 stdout 也就是 list 文件中，所以屏幕不会出现错误信息，而是打印到了 list 文件中。

**cat list** 可以查看到 find: unknown predicate `-names' 就在里面。

直接在 FreeBSD 或者 csh 中使用 **command > file 2>&1** 时候会得到这个错误：**Ambiguous output redirect**。

出错的原因在于 FreeBSD 默认使用 csh，在 csh 中如果想把标准输出和错误输出同时重定向到一个文件，需要用下面命令 **command >& file**。

# Shell 文件包含

和其他语言一样，Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。

Shell 文件包含的语法格式如下：

```
. filename   # 注意点号(.)和文件名中间有一空格

或

source filename
```

### 实例

创建两个 shell 脚本文件。

test1.sh 代码如下：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

url="http://www.runoob.com"
```

test2.sh 代码如下：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

#使用 . 号来引用test1.sh 文件
. ./test1.sh

# 或者使用以下包含文件代码
# source ./test1.sh

echo "菜鸟教程官网地址：$url"
```

接下来，我们为 test2.sh 添加可执行权限并执行：

```
$ chmod +x test2.sh 
$ ./test2.sh 
菜鸟教程官网地址：http://www.runoob.com
```

> **注：**被包含的文件 test1.sh 不需要可执行权限。

# Linux 命令大全

| Linux 命令大全                                               |                                                              |                                                              |                                                              |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1、文件管理**                                              |                                                              |                                                              |                                                              |
| [cat](https://www.runoob.com/linux/linux-comm-cat.html)      | [chattr](https://www.runoob.com/linux/linux-comm-chattr.html) | [chgrp](https://www.runoob.com/linux/linux-comm-chgrp.html)  | [chmod](https://www.runoob.com/linux/linux-comm-chmod.html)  |
| [chown](https://www.runoob.com/linux/linux-comm-chown.html)  | [cksum](https://www.runoob.com/linux/linux-comm-cksum.html)  | [cmp](https://www.runoob.com/linux/linux-comm-cmp.html)      | [diff](https://www.runoob.com/linux/linux-comm-diff.html)    |
| [diffstat](https://www.runoob.com/linux/linux-comm-diffstat.html) | [file](https://www.runoob.com/linux/linux-comm-file.html)    | [find](https://www.runoob.com/linux/linux-comm-find.html)    | [git](https://www.runoob.com/linux/linux-comm-git.html)      |
| [gitview](https://www.runoob.com/linux/linux-comm-gitview.html) | [indent](https://www.runoob.com/linux/linux-comm-indent.html) | [cut](https://www.runoob.com/linux/linux-comm-cut.html)      | [ln](https://www.runoob.com/linux/linux-comm-ln.html)        |
| [less](https://www.runoob.com/linux/linux-comm-less.html)    | [locate](https://www.runoob.com/linux/linux-comm-locate.html) | [lsattr](https://www.runoob.com/linux/linux-comm-lsattr.html) | [mattrib](https://www.runoob.com/linux/linux-comm-mattrib.html) |
| [mc](https://www.runoob.com/linux/linux-comm-mc.html)        | [mdel](https://www.runoob.com/linux/linux-comm-mdel.html)    | [mdir](https://www.runoob.com/linux/linux-comm-mdir.html)    | [mktemp](https://www.runoob.com/linux/linux-comm-mktemp.html) |
| [more](https://www.runoob.com/linux/linux-comm-more.html)    | [mmove](https://www.runoob.com/linux/linux-comm-mmove.html)  | [mread](https://www.runoob.com/linux/linux-comm-mread.html)  | [mren](https://www.runoob.com/linux/linux-comm-mren.html)    |
| [mtools](https://www.runoob.com/linux/linux-comm-mtools.html) | [mtoolstest](https://www.runoob.com/linux/linux-comm-mtoolstest.html) | [mv](https://www.runoob.com/linux/linux-comm-mv.html)        | [od](https://www.runoob.com/linux/linux-comm-od.html)        |
| [paste](https://www.runoob.com/linux/linux-comm-paste.html)  | [patch](https://www.runoob.com/linux/linux-comm-patch.html)  | [rcp](https://www.runoob.com/linux/linux-comm-rcp.html)      | [rm](https://www.runoob.com/linux/linux-comm-rm.html)        |
| [slocate](https://www.runoob.com/linux/linux-comm-slocate.html) | [split](https://www.runoob.com/linux/linux-comm-split.html)  | [tee](https://www.runoob.com/linux/linux-comm-tee.html)      | [tmpwatch](https://www.runoob.com/linux/linux-comm-tmpwatch.html) |
| [touch](https://www.runoob.com/linux/linux-comm-touch.html)  | [umask](https://www.runoob.com/linux/linux-comm-umask.html)  | [which](https://www.runoob.com/linux/linux-comm-which.html)  | [cp](https://www.runoob.com/linux/linux-comm-cp.html)        |
| [whereis](https://www.runoob.com/linux/linux-comm-whereis.html) | [mcopy](https://www.runoob.com/linux/linux-comm-mcopy.html)  | [mshowfat](https://www.runoob.com/linux/linux-comm-mshowfat.html) | [rhmask](https://www.runoob.com/linux/linux-comm-rhmask.html) |
| [scp](https://www.runoob.com/linux/linux-comm-scp.html)      | [awk](https://www.runoob.com/linux/linux-comm-awk.html)      | [read](https://www.runoob.com/linux/linux-comm-read.html)    | [updatedb](https://www.runoob.com/linux/linux-comm-updatedb.html) |
| **2、文档编辑**                                              |                                                              |                                                              |                                                              |
| [col](https://www.runoob.com/linux/linux-comm-col.html)      | [colrm](https://www.runoob.com/linux/linux-comm-colrm.html)  | [comm](https://www.runoob.com/linux/linux-comm-comm.html)    | [csplit](https://www.runoob.com/linux/linux-comm-csplit.html) |
| [ed](https://www.runoob.com/linux/linux-comm-ed.html)        | [egrep](https://www.runoob.com/linux/linux-comm-egrep.html)  | [ex](https://www.runoob.com/linux/linux-comm-ex.html)        | [fgrep](https://www.runoob.com/linux/linux-comm-fgrep.html)  |
| [fmt](https://www.runoob.com/linux/linux-comm-fmt.html)      | [fold](https://www.runoob.com/linux/linux-comm-fold.html)    | [grep](https://www.runoob.com/linux/linux-comm-grep.html)    | [ispell](https://www.runoob.com/linux/linux-comm-ispell.html) |
| [jed](https://www.runoob.com/linux/linux-comm-jed.html)      | [joe](https://www.runoob.com/linux/linux-comm-joe.html)      | [join](https://www.runoob.com/linux/linux-comm-join.html)    | [look](https://www.runoob.com/linux/linux-comm-look.html)    |
| [mtype](https://www.runoob.com/linux/linux-comm-mtype.html)  | [pico](https://www.runoob.com/linux/linux-comm-pico.html)    | [rgrep](https://www.runoob.com/linux/linux-comm-rgrep.html)  | [sed](https://www.runoob.com/linux/linux-comm-sed.html)      |
| [sort](https://www.runoob.com/linux/linux-comm-sort.html)    | [spell](https://www.runoob.com/linux/linux-comm-spell.html)  | [tr](https://www.runoob.com/linux/linux-comm-tr.html)        | [expr](https://www.runoob.com/linux/linux-comm-expr.html)    |
| [uniq](https://www.runoob.com/linux/linux-comm-uniq.html)    | [wc](https://www.runoob.com/linux/linux-comm-wc.html)        | [let](https://www.runoob.com/linux/linux-comm-let.html)      |                                                              |
| **3、文件传输**                                              |                                                              |                                                              |                                                              |
| [lprm](https://www.runoob.com/linux/linux-comm-lprm.html)    | [lpr](https://www.runoob.com/linux/linux-comm-lpr.html)      | [lpq](https://www.runoob.com/linux/linux-comm-lpq.html)      | [lpd](https://www.runoob.com/linux/linux-comm-lpd.html)      |
| [bye](https://www.runoob.com/linux/linux-comm-bye.html)      | [ftp](https://www.runoob.com/linux/linux-comm-ftp.html)      | [uuto](https://www.runoob.com/linux/linux-comm-uuto.html)    | [uupick](https://www.runoob.com/linux/linux-comm-uupick.html) |
| [uucp](https://www.runoob.com/linux/linux-comm-uucp.html)    | [uucico](https://www.runoob.com/linux/linux-comm-uucico.html) | [tftp](https://www.runoob.com/linux/linux-comm-tftp.html)    | [ncftp](https://www.runoob.com/linux/linux-comm-ncftp.html)  |
| [ftpshut](https://www.runoob.com/linux/linux-comm-ftpshut.html) | [ftpwho](https://www.runoob.com/linux/linux-comm-ftpwho.html) | [ftpcount](https://www.runoob.com/linux/linux-comm-ftpcount.html) |                                                              |
| **4、磁盘管理**                                              |                                                              |                                                              |                                                              |
| [cd](https://www.runoob.com/linux/linux-comm-cd.html)        | [df](https://www.runoob.com/linux/linux-comm-df.html)        | [dirs](https://www.runoob.com/linux/linux-comm-dirs.html)    | [du](https://www.runoob.com/linux/linux-comm-du.html)        |
| [edquota](https://www.runoob.com/linux/linux-comm-edquota.html) | [eject](https://www.runoob.com/linux/linux-comm-eject.html)  | [mcd](https://www.runoob.com/linux/linux-comm-mcd.html)      | [mdeltree](https://www.runoob.com/linux/linux-comm-mdeltree.html) |
| [mdu](https://www.runoob.com/linux/linux-comm-mdu.html)      | [mkdir](https://www.runoob.com/linux/linux-comm-mkdir.html)  | [mlabel](https://www.runoob.com/linux/linux-comm-mlabel.html) | [mmd](https://www.runoob.com/linux/linux-comm-mmd.html)      |
| [mrd](https://www.runoob.com/linux/linux-comm-mrd.html)      | [mzip](https://www.runoob.com/linux/linux-comm-mzip.html)    | [pwd](https://www.runoob.com/linux/linux-comm-pwd.html)      | [quota](https://www.runoob.com/linux/linux-comm-quota.html)  |
| [mount](https://www.runoob.com/linux/linux-comm-mount.html)  | [mmount](https://www.runoob.com/linux/linux-comm-mmount.html) | [rmdir](https://www.runoob.com/linux/linux-comm-rmdir.html)  | [rmt](https://www.runoob.com/linux/linux-comm-rmt.html)      |
| [stat](https://www.runoob.com/linux/linux-comm-stat.html)    | [tree](https://www.runoob.com/linux/linux-comm-tree.html)    | [umount](https://www.runoob.com/linux/linux-comm-umount.html) | [ls](https://www.runoob.com/linux/linux-comm-ls.html)        |
| [quotacheck](https://www.runoob.com/linux/linux-comm-quotacheck.html) | [quotaoff](https://www.runoob.com/linux/linux-comm-quotaoff.html) | [lndir](https://www.runoob.com/linux/linux-comm-lndir.html)  | [repquota](https://www.runoob.com/linux/linux-comm-repquota.html) |
| [quotaon](https://www.runoob.com/linux/linux-comm-quotaon.html) |                                                              |                                                              |                                                              |
| **5、磁盘维护**                                              |                                                              |                                                              |                                                              |
| [badblocks](https://www.runoob.com/linux/linux-comm-badblocks.html) | [cfdisk](https://www.runoob.com/linux/linux-comm-cfdisk.html) | [dd](https://www.runoob.com/linux/linux-comm-dd.html)        | [e2fsck](https://www.runoob.com/linux/linux-comm-e2fsck.html) |
| [ext2ed](https://www.runoob.com/linux/linux-comm-ext2ed.html) | [fsck](https://www.runoob.com/linux/linux-comm-fsck.html)    | [fsck.minix](https://www.runoob.com/linux/linux-comm-fsck-minix.html) | [fsconf](https://www.runoob.com/linux/linux-comm-fsconf.html) |
| [fdformat](https://www.runoob.com/linux/linux-comm-fdformat.html) | [hdparm](https://www.runoob.com/linux/linux-comm-hdparm.html) | [mformat](https://www.runoob.com/linux/linux-comm-mformat.html) | [mkbootdisk](https://www.runoob.com/linux/linux-comm-mkbootdisk.html) |
| [mkdosfs](https://www.runoob.com/linux/linux-comm-mkdosfs.html) | [mke2fs](https://www.runoob.com/linux/linux-comm-mke2fs.html) | [mkfs.ext2](https://www.runoob.com/linux/linux-comm-mkfs-ext2.html) | [mkfs.msdos](https://www.runoob.com/linux/linux-comm-mkfs-msdos.html) |
| [mkinitrd](https://www.runoob.com/linux/linux-comm-mkinitrd.html) | [mkisofs](https://www.runoob.com/linux/linux-comm-mkisofs.html) | [mkswap](https://www.runoob.com/linux/linux-comm-mkswap.html) | [mpartition](https://www.runoob.com/linux/linux-comm-mpartition.html) |
| [swapon](https://www.runoob.com/linux/linux-comm-swapon.html) | [symlinks](https://www.runoob.com/linux/linux-comm-symlinks.html) | [sync](https://www.runoob.com/linux/linux-comm-sync.html)    | [mbadblocks](https://www.runoob.com/linux/linux-comm-mbadblocks.html) |
| [mkfs.minix](https://www.runoob.com/linux/linux-comm-mkfs-minix.html) | [fsck.ext2](https://www.runoob.com/linux/linux-comm-fsck-ext2.html) | [fdisk](https://www.runoob.com/linux/linux-comm-fdisk.html)  | [losetup](https://www.runoob.com/linux/linux-comm-losetup.html) |
| [mkfs](https://www.runoob.com/linux/linux-comm-mkfs.html)    | [sfdisk](https://www.runoob.com/linux/linux-comm-sfdisk.html) | [swapoff](https://www.runoob.com/linux/linux-comm-swapoff.html) |                                                              |
| **6、网络通讯**                                              |                                                              |                                                              |                                                              |
| [apachectl](https://www.runoob.com/linux/linux-comm-apachectl.html) | [arpwatch](https://www.runoob.com/linux/linux-comm-arpwatch.html) | [dip](https://www.runoob.com/linux/linux-comm-dip.html)      | [getty](https://www.runoob.com/linux/linux-comm-getty.html)  |
| [mingetty](https://www.runoob.com/linux/linux-comm-mingetty.html) | [uux](https://www.runoob.com/linux/linux-comm-uux.html)      | [telnet](https://www.runoob.com/linux/linux-comm-telnet.html) | [uulog](https://www.runoob.com/linux/linux-comm-uulog.html)  |
| [uustat](https://www.runoob.com/linux/linux-comm-uustat.html) | [ppp-off](https://www.runoob.com/linux/linux-comm-ppp-off.html) | [netconfig](https://www.runoob.com/linux/linux-comm-netconfig.html) | [nc](https://www.runoob.com/linux/linux-comm-nc.html)        |
| [httpd](https://www.runoob.com/linux/linux-comm-httpd.html)  | [ifconfig](https://www.runoob.com/linux/linux-comm-ifconfig.html) | [minicom](https://www.runoob.com/linux/linux-comm-minicom.html) | [mesg](https://www.runoob.com/linux/linux-comm-mesg.html)    |
| [dnsconf](https://www.runoob.com/linux/linux-comm-dnsconf.html) | [wall](https://www.runoob.com/linux/linux-comm-wall.html)    | [netstat](https://www.runoob.com/linux/linux-comm-netstat.html) | [ping](https://www.runoob.com/linux/linux-comm-ping.html)    |
| [pppstats](https://www.runoob.com/linux/linux-comm-pppstats.html) | [samba](https://www.runoob.com/linux/linux-comm-samba.html)  | [setserial](https://www.runoob.com/linux/linux-comm-setserial.html) | [talk](https://www.runoob.com/linux/linux-comm-talk.html)    |
| [traceroute](https://www.runoob.com/linux/linux-comm-traceroute.html) | [tty](https://www.runoob.com/linux/linux-comm-tty.html)      | [newaliases](https://www.runoob.com/linux/linux-comm-newaliases.html) | [uuname](https://www.runoob.com/linux/linux-comm-uuname.html) |
| [netconf](https://www.runoob.com/linux/linux-comm-netconf.html) | [write](https://www.runoob.com/linux/linux-comm-write.html)  | [statserial](https://www.runoob.com/linux/linux-comm-statserial.html) | [efax](https://www.runoob.com/linux/linux-comm-efax.html)    |
| [pppsetup](https://www.runoob.com/linux/linux-comm-pppsetup.html) | [tcpdump](https://www.runoob.com/linux/linux-comm-tcpdump.html) | [ytalk](https://www.runoob.com/linux/linux-comm-ytalk.html)  | [cu](https://www.runoob.com/linux/linux-comm-cu.html)        |
| [smbd](https://www.runoob.com/linux/linux-comm-smbd.html)    | [testparm](https://www.runoob.com/linux/linux-comm-testparm.html) | [smbclient](https://www.runoob.com/linux/linux-comm-smbclient.html) | [shapecfg](https://www.runoob.com/linux/linux-comm-shapecfg.html) |
| **7、系统管理**                                              |                                                              |                                                              |                                                              |
| [adduser](https://www.runoob.com/linux/linux-comm-adduser.html) | [chfn](https://www.runoob.com/linux/linux-comm-chfn.html)    | [useradd](https://www.runoob.com/linux/linux-comm-useradd.html) | [date](https://www.runoob.com/linux/linux-comm-date.html)    |
| [exit](https://www.runoob.com/linux/linux-comm-exit.html)    | [finger](https://www.runoob.com/linux/linux-comm-finger.html) | [fwhios](https://www.runoob.com/linux/linux-comm-fwhios.html) | [sleep](https://www.runoob.com/linux/linux-comm-sleep.html)  |
| [suspend](https://www.runoob.com/linux/linux-comm-suspend.html) | [groupdel](https://www.runoob.com/linux/linux-comm-groupdel.html) | [groupmod](https://www.runoob.com/linux/linux-comm-groupmod.html) | [halt](https://www.runoob.com/linux/linux-comm-halt.html)    |
| [kill](https://www.runoob.com/linux/linux-comm-kill.html)    | [last](https://www.runoob.com/linux/linux-comm-last.html)    | [lastb](https://www.runoob.com/linux/linux-comm-lastb.html)  | [login](https://www.runoob.com/linux/linux-comm-login.html)  |
| [logname](https://www.runoob.com/linux/linux-comm-logname.html) | [logout](https://www.runoob.com/linux/linux-comm-logout.html) | [ps](https://www.runoob.com/linux/linux-comm-ps.html)        | [nice](https://www.runoob.com/linux/linux-comm-nice.html)    |
| [procinfo](https://www.runoob.com/linux/linux-comm-procinfo.html) | [top](https://www.runoob.com/linux/linux-comm-top.html)      | [pstree](https://www.runoob.com/linux/linux-comm-pstree.html) | [reboot](https://www.runoob.com/linux/linux-comm-reboot.html) |
| [rlogin](https://www.runoob.com/linux/linux-comm-rlogin.html) | [rsh](https://www.runoob.com/linux/linux-comm-rsh.html)      | [sliplogin](https://www.runoob.com/linux/linux-comm-sliplogin.html) | [screen](https://www.runoob.com/linux/linux-comm-screen.html) |
| [shutdown](https://www.runoob.com/linux/linux-comm-shutdown.html) | [rwho](https://www.runoob.com/linux/linux-comm-rwho.html)    | [sudo](https://www.runoob.com/linux/linux-comm-sudo.html)    | [gitps](https://www.runoob.com/linux/linux-comm-gitps.html)  |
| [swatch](https://www.runoob.com/linux/linux-comm-swatch.html) | [tload](https://www.runoob.com/linux/linux-comm-tload.html)  | [logrotate](https://www.runoob.com/linux/linux-comm-logrotate.html) | [uname](https://www.runoob.com/linux/linux-comm-uname.html)  |
| [chsh](https://www.runoob.com/linux/linux-comm-chsh.html)    | [userconf](https://www.runoob.com/linux/linux-comm-userconf.html) | [userdel](https://www.runoob.com/linux/linux-comm-userdel.html) | [usermod](https://www.runoob.com/linux/linux-comm-usermod.html) |
| [vlock](https://www.runoob.com/linux/linux-comm-vlock.html)  | [who](https://www.runoob.com/linux/linux-comm-who.html)      | [whoami](https://www.runoob.com/linux/linux-comm-whoami.html) | [whois](https://www.runoob.com/linux/linux-comm-whois.html)  |
| [newgrp](https://www.runoob.com/linux/linux-comm-newgrp.html) | [renice](https://www.runoob.com/linux/linux-comm-renice.html) | [su](https://www.runoob.com/linux/linux-comm-su.html)        | [skill](https://www.runoob.com/linux/linux-comm-skill.html)  |
| [w](https://www.runoob.com/linux/linux-comm-w.html)          | [id](https://www.runoob.com/linux/linux-comm-id.html)        | [groupadd](https://www.runoob.com/linux/linux-comm-groupadd.html) | [free](https://www.runoob.com/linux/linux-comm-free.html)    |
| **8、系统设置**                                              |                                                              |                                                              |                                                              |
| [reset](https://www.runoob.com/linux/linux-comm-reset.html)  | [clear](https://www.runoob.com/linux/linux-comm-clear.html)  | [alias](https://www.runoob.com/linux/linux-comm-alias.html)  | [dircolors](https://www.runoob.com/linux/linux-comm-dircolors.html) |
| [aumix](https://www.runoob.com/linux/linux-comm-aumix.html)  | [bind](https://www.runoob.com/linux/linux-comm-bind.html)    | [chroot](https://www.runoob.com/linux/linux-comm-chroot.html) | [clock](https://www.runoob.com/linux/linux-comm-clock.html)  |
| [crontab](https://www.runoob.com/linux/linux-comm-crontab.html) | [declare](https://www.runoob.com/linux/linux-comm-declare.html) | [depmod](https://www.runoob.com/linux/linux-comm-depmod.html) | [dmesg](https://www.runoob.com/linux/linux-comm-dmesg.html)  |
| [enable](https://www.runoob.com/linux/linux-comm-enable.html) | [eval](https://www.runoob.com/linux/linux-comm-eval.html)    | [export](https://www.runoob.com/linux/linux-comm-export.html) | [pwunconv](https://www.runoob.com/linux/linux-comm-pwunconv.html) |
| [grpconv](https://www.runoob.com/linux/linux-comm-grpconv.html) | [rpm](https://www.runoob.com/linux/linux-comm-rpm.html)      | [insmod](https://www.runoob.com/linux/linux-comm-insmod.html) | [kbdconfig](https://www.runoob.com/linux/linux-comm-kbdconfig.html) |
| [lilo](https://www.runoob.com/linux/linux-comm-lilo.html)    | [liloconfig](https://www.runoob.com/linux/linux-comm-liloconfig.html) | [lsmod](https://www.runoob.com/linux/linux-comm-lsmod.html)  | [minfo](https://www.runoob.com/linux/linux-comm-minfo.html)  |
| [set](https://www.runoob.com/linux/linux-comm-set.html)      | [modprobe](https://www.runoob.com/linux/linux-comm-modprobe.html) | [ntsysv](https://www.runoob.com/linux/linux-comm-ntsysv.html) | [mouseconfig](https://www.runoob.com/linux/linux-comm-mouseconfig.html) |
| [passwd](https://www.runoob.com/linux/linux-comm-passwd.html) | [pwconv](https://www.runoob.com/linux/linux-comm-pwconv.html) | [rdate](https://www.runoob.com/linux/linux-comm-rdate.html)  | [resize](https://www.runoob.com/linux/linux-comm-resize.html) |
| [rmmod](https://www.runoob.com/linux/linux-comm-rmmod.html)  | [grpunconv](https://www.runoob.com/linux/linux-comm-grpunconv.html) | [modinfo](https://www.runoob.com/linux/linux-comm-modinfo.html) | [time](https://www.runoob.com/linux/linux-comm-time.html)    |
| [setup](https://www.runoob.com/linux/linux-comm-setup.html)  | [sndconfig](https://www.runoob.com/linux/linux-comm-sndconfig.html) | [setenv](https://www.runoob.com/linux/linux-comm-setenv.html) | [setconsole](https://www.runoob.com/linux/linux-comm-setconsole.html) |
| [timeconfig](https://www.runoob.com/linux/linux-comm-timeconfig.html) | [ulimit](https://www.runoob.com/linux/linux-comm-ulimit.html) | [unset](https://www.runoob.com/linux/linux-comm-unset.html)  | [chkconfig](https://www.runoob.com/linux/linux-comm-chkconfig.html) |
| [apmd](https://www.runoob.com/linux/linux-comm-apmd.html)    | [hwclock](https://www.runoob.com/linux/linux-comm-hwclock.html) | [mkkickstart](https://www.runoob.com/linux/linux-comm-mkkickstart.html) | [fbset](https://www.runoob.com/linux/linux-comm-fbset.html)  |
| [unalias](https://www.runoob.com/linux/linux-comm-unalias.html) | [SVGATextMode](https://www.runoob.com/linux/linux-comm-svgatextmode.html) | [gpasswd](https://www.runoob.com/linux/linux-comm-gpasswd.html) |                                                              |
| **9、备份压缩**                                              |                                                              |                                                              |                                                              |
| [ar](https://www.runoob.com/linux/linux-comm-ar.html)        | [bunzip2](https://www.runoob.com/linux/linux-comm-bunzip2.html) | [bzip2](https://www.runoob.com/linux/linux-comm-bzip2.html)  | [bzip2recover](https://www.runoob.com/linux/linux-comm-bzip2recover.html) |
| [gunzip](https://www.runoob.com/linux/linux-comm-gunzip.html) | [unarj](https://www.runoob.com/linux/linux-comm-unarj.html)  | [compress](https://www.runoob.com/linux/linux-comm-compress.html) | [cpio](https://www.runoob.com/linux/linux-comm-cpio.html)    |
| [dump](https://www.runoob.com/linux/linux-comm-dump.html)    | [uuencode](https://www.runoob.com/linux/linux-comm-uuencode.html) | [gzexe](https://www.runoob.com/linux/linux-comm-gzexe.html)  | [gzip](https://www.runoob.com/linux/linux-comm-gzip.html)    |
| [lha](https://www.runoob.com/linux/linux-comm-lha.html)      | [restore](https://www.runoob.com/linux/linux-comm-restore.html) | [tar](https://www.runoob.com/linux/linux-comm-tar.html)      | [uudecode](https://www.runoob.com/linux/linux-comm-uudecode.html) |
| [unzip](https://www.runoob.com/linux/linux-comm-unzip.html)  | [zip](https://www.runoob.com/linux/linux-comm-zip.html)      | [zipinfo](https://www.runoob.com/linux/linux-comm-zipinfo.html) |                                                              |
| **10、设备管理**                                             |                                                              |                                                              |                                                              |
| [setleds](https://www.runoob.com/linux/linux-comm-setleds.html) | [loadkeys](https://www.runoob.com/linux/linux-comm-loadkeys.html) | [rdev](https://www.runoob.com/linux/linux-comm-rdev.html)    | [dumpkeys](https://www.runoob.com/linux/linux-comm-dumpkeys.html) |
| [MAKEDEV](https://www.runoob.com/linux/linux-comm-makedev.html) | [poweroff](https://www.runoob.com/linux/linux-comm-poweroff.html) |                                                              |                                                              |

------

## 其他命令

- [Linux bc 命令](https://www.runoob.com/linux/linux-comm-bc.html)
- [Linux tail 命令](https://www.runoob.com/linux/linux-comm-tail.html)
- [Linux head 命令](https://www.runoob.com/linux/linux-comm-head.html)
- [Linux xargs 命令](https://www.runoob.com/linux/linux-comm-xargs.html)
- [Linux ip 命令](https://www.runoob.com/linux/linux-comm-ip.html)
- [Linux nohup 命令](https://www.runoob.com/linux/linux-comm-nohup.html)
- [Linux killall 命令](https://www.runoob.com/linux/linux-comm-killall.html)
- [Linux pkill 命令](https://www.runoob.com/linux/linux-comm-pkill.html)

### 扩展文章

- [Linux 常用命令全拼](https://www.runoob.com/w3cnote/linux-command-full-fight.html)

# Nginx 安装配置

![img](img/nginx.jpg)

Nginx("engine x")是一款是由俄罗斯的程序设计师Igor Sysoev所开发高性能的 Web和 反向代理 服务器，也是一个 IMAP/POP3/SMTP 代理服务器。

在高连接并发的情况下，Nginx是Apache服务器不错的替代品。

------

## Nginx 安装

系统平台：CentOS release 6.6 (Final) 64位。

### 一、安装编译工具及库文件

```
yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
```

### 二、首先要安装 PCRE

PCRE 作用是让 Nginx 支持 Rewrite 功能。

1、下载 PCRE 安装包，下载地址： http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz

```
[root@bogon src]# cd /usr/local/src/
[root@bogon src]# wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
```

![img](img/nginx1.png)

2、解压安装包:

```
[root@bogon src]# tar zxvf pcre-8.35.tar.gz
```

3、进入安装包目录

```
[root@bogon src]# cd pcre-8.35
```

4、编译安装 

```
[root@bogon pcre-8.35]# ./configure
[root@bogon pcre-8.35]# make && make install
```

5、查看pcre版本

```
[root@bogon pcre-8.35]# pcre-config --version
```

![img](img/nginx2.png)

### 安装 Nginx

1、下载 Nginx，下载地址：http://nginx.org/download/nginx-1.6.2.tar.gz

```
[root@bogon src]# cd /usr/local/src/
[root@bogon src]# wget http://nginx.org/download/nginx-1.6.2.tar.gz
```

![img](img/nginx3.png) 2、解压安装包

```
[root@bogon src]# tar zxvf nginx-1.6.2.tar.gz
```

3、进入安装包目录

```
[root@bogon src]# cd nginx-1.6.2
```

4、编译安装

```
[root@bogon nginx-1.6.2]# ./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35
[root@bogon nginx-1.6.2]# make
[root@bogon nginx-1.6.2]# make install
```

5、查看nginx版本

```
[root@bogon nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -v
```

![img](img/nginx4.png)

到此，nginx安装完成。

------

## Nginx 配置

创建 Nginx 运行使用的用户 www：

```
[root@bogon conf]# /usr/sbin/groupadd www 
[root@bogon conf]# /usr/sbin/useradd -g www www
```

配置nginx.conf ，将/usr/local/webserver/nginx/conf/nginx.conf替换为以下内容



```
[root@bogon conf]#  cat /usr/local/webserver/nginx/conf/nginx.conf

user www www;
worker_processes 2; #设置值和CPU核心数一致
error_log /usr/local/webserver/nginx/logs/nginx_error.log crit; #日志位置和日志级别
pid /usr/local/webserver/nginx/nginx.pid;
#Specifies the value for maximum file descriptors that can be opened by this process.
worker_rlimit_nofile 65535;
events
{
  use epoll;
  worker_connections 65535;
}
http
{
  include mime.types;
  default_type application/octet-stream;
  log_format main  '$remote_addr - $remote_user [$time_local] "$request" '
               '$status $body_bytes_sent "$http_referer" '
               '"$http_user_agent" $http_x_forwarded_for';
  
#charset gb2312;
     
  server_names_hash_bucket_size 128;
  client_header_buffer_size 32k;
  large_client_header_buffers 4 32k;
  client_max_body_size 8m;
     
  sendfile on;
  tcp_nopush on;
  keepalive_timeout 60;
  tcp_nodelay on;
  fastcgi_connect_timeout 300;
  fastcgi_send_timeout 300;
  fastcgi_read_timeout 300;
  fastcgi_buffer_size 64k;
  fastcgi_buffers 4 64k;
  fastcgi_busy_buffers_size 128k;
  fastcgi_temp_file_write_size 128k;
  gzip on; 
  gzip_min_length 1k;
  gzip_buffers 4 16k;
  gzip_http_version 1.0;
  gzip_comp_level 2;
  gzip_types text/plain application/x-javascript text/css application/xml;
  gzip_vary on;
 
  #limit_zone crawler $binary_remote_addr 10m;
 #下面是server虚拟主机的配置
 server
  {
    listen 80;#监听端口
    server_name localhost;#域名
    index index.html index.htm index.php;
    root /usr/local/webserver/nginx/html;#站点目录
      location ~ .*\.(php|php5)?$
    {
      #fastcgi_pass unix:/tmp/php-cgi.sock;
      fastcgi_pass 127.0.0.1:9000;
      fastcgi_index index.php;
      include fastcgi.conf;
    }
    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf|ico)$
    {
      expires 30d;
  # access_log off;
    }
    location ~ .*\.(js|css)?$
    {
      expires 15d;
   # access_log off;
    }
    access_log off;
  }

}
```

检查配置文件nginx.conf的正确性命令：

```
[root@bogon conf]# /usr/local/webserver/nginx/sbin/nginx -t
```

![img](img/nginx5.png)

------

## 启动 Nginx

Nginx 启动命令如下：

```
[root@bogon conf]# /usr/local/webserver/nginx/sbin/nginx
```

![img](img/nginx6.png)

------

## 访问站点

从浏览器访问我们配置的站点ip：

![img](img/nginx7.png)

------

## Nginx 其他命令

以下包含了 Nginx 常用的几个命令：

```
/usr/local/webserver/nginx/sbin/nginx -s reload            # 重新载入配置文件
/usr/local/webserver/nginx/sbin/nginx -s reopen            # 重启 Nginx
/usr/local/webserver/nginx/sbin/nginx -s stop              # 停止 Nginx
```

**worker_processes** 这个参数最好是设置成 **auto** 自动匹配进程数。

语法:

```
worker_processes number | auto;
```

auto 在 nginx 1.3.8 和 1.2.5 之后的版本开始支持。

默认:

```
worker_processes 1;
```

**proxy_next_upstream** 这个参数默认的是超时跟错误都会重发，对于一些请求时间过长的连接，最好只设置成错误重发，不然的话会造成二重数据。

nginx 启动时提示错误：

```
# /usr/local/nginx/sbin/nginx -t
/usr/local/nginx/sbin/nginx: error while loading shared libraries: libpcre.so.1: cannot open shared object file: No such file or directory
```

解决方法：

64 位系统：

```
ln -s /usr/local/lib/libpcre.so.1 /lib64
```

32 位系统:

```
ln -s /usr/local/lib/libpcre.so.1 /lib
```

/usr/local/lib/libpcre.so.1 为 prce 安装后的文件地址。

低版本 prce 对应的 libpcre.so.1 为 libpcre.so.0。

## 关于 uri 的截取

**location 中的 root 和 alias**

-  root 指令只是将搜索的根设置为 root 设定的目录，即不会截断 uri，而是使用原始 uri 跳转该目录下查找文件
-  aias 指令则会截断匹配的 uri，然后使用 alias 设定的路径加上剩余的 uri 作为子路径进行查找

示例 1：root

```
#------------目录结构----------
/www/x1/index.html
/www/x2/index.html

#--------配置-----------------------
index index.html index.php;
location /x/ {
    root "/www/";
}

#-------访问--------------
curl http://localhost/x1/index.html
curl http://localhost/x2/index.html
```

示例 2：alias

```
#----------配置-----------------
location /y/z/ {
    alias /www/x1/;
}

#---------访问--------------
curl http://localhost/y/z/index.html
```

**location 中的 proxy_pass 的 uri**

如果 proxy_pass 的 url 不带 uri

如果尾部是"/"，则会截断匹配的uri

如果尾部不是"/"，则不会截断匹配的uri

如果proxy_pass的url带uri，则会截断匹配的uri

示例：

```
#-------servers配置--------------------
location / {
    echo $uri    #回显请求的uri
}

#--------proxy_pass配置---------------------
location /t1/ { proxy_pass http://servers; }    #正常，不截断
location /t2/ { proxy_pass http://servers/; }    #正常，截断
location /t3  { proxy_pass http://servers; }    #正常，不截断
location /t4  { proxy_pass http://servers/; }    #正常，截断
location /t5/ { proxy_pass http://servers/test/; }    #正常，截断
location /t6/ { proxy_pass http://servers/test; }    #缺"/"，截断
location /t7  { proxy_pass http://servers/test/; }    #含"//"，截断
location /t8  { proxy_pass http://servers/test; }    #正常，截断
#---------访问----------------------
for i in $(seq 6)
do
    url=http://localhost/t$i/doc/index.html
    echo "-----------$url-----------"
    curl url
done

#--------结果---------------------------
----------http://localhost:8080/t1/doc/index.html------------
/t1/doc/index.html

----------http://localhost:8080/t2/doc/index.html------------
/doc/index.html

----------http://localhost:8080/t3/doc/index.html------------
/t3/doc/index.html

----------http://localhost:8080/t4/doc/index.html------------
/doc/index.html

----------http://localhost:8080/t5/doc/index.html------------
/test/doc/index.html

----------http://localhost:8080/t6/doc/index.html------------
/testdoc/index.html

----------http://localhost:8080/t7/doc/index.html------------
/test//doc/index.html

----------http://localhost:8080/t8/doc/index.html------------
/test/doc/index.html
```

**Nginx 配置文件结构**

默认的 nginx 配置文件 nginx.conf 内容如下：

```
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
```

**nginx 文件结构**

```
...              #全局块

events {         #events块
   ...
}

http      #http块
{
    ...   #http全局块
    server        #server块
    { 
        ...       #server全局块
        location [PATTERN]   #location块
        {
            ...
        }
        location [PATTERN] 
        {
            ...
        }
    }
    server
    {
      ...
    }
    ...     #http全局块
}
```

-  1、**全局块**：配置影响nginx全局的指令。一般有运行nginx服务器的用户组，nginx进程pid存放路径，日志存放路径，配置文件引入，允许生成worker process数等。
-  2、**events块**：配置影响nginx服务器或与用户的网络连接。有每个进程的最大连接数，选取哪种事件驱动模型处理连接请求，是否允许同时接受多个网路连接，开启多个网络连接序列化等。
-  3、**http块**：可以嵌套多个server，配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置。如文件引入，mime-type定义，日志自定义，是否使用sendfile传输文件，连接超时时间，单连接请求数等。
-  4、**server块**：配置虚拟主机的相关参数，一个http中可以有多个server。
-  5、**location块**：配置请求的路由，以及各种页面的处理情况。

下面给大家上一个配置文件，作为理解。

```
########### 每个指令必须有分号结束。#################
#user administrator administrators;  #配置用户或者组，默认为nobody nobody。
#worker_processes 2;  #允许生成的进程数，默认为1
#pid /nginx/pid/nginx.pid;   #指定nginx进程运行文件存放地址
error_log log/error.log debug;  #制定日志路径，级别。这个设置可以放入全局块，http块，server块，级别以此为：debug|info|notice|warn|error|crit|alert|emerg
events {
    accept_mutex on;   #设置网路连接序列化，防止惊群现象发生，默认为on
    multi_accept on;  #设置一个进程是否同时接受多个网络连接，默认为off
    #use epoll;      #事件驱动模型，select|poll|kqueue|epoll|resig|/dev/poll|eventport
    worker_connections  1024;    #最大连接数，默认为512
}
http {
    include       mime.types;   #文件扩展名与文件类型映射表
    default_type  application/octet-stream; #默认文件类型，默认为text/plain
    #access_log off; #取消服务日志    
    log_format myFormat '$remote_addr–$remote_user [$time_local] $request $status $body_bytes_sent $http_referer $http_user_agent $http_x_forwarded_for'; #自定义格式
    access_log log/access.log myFormat;  #combined为日志格式的默认值
    sendfile on;   #允许sendfile方式传输文件，默认为off，可以在http块，server块，location块。
    sendfile_max_chunk 100k;  #每个进程每次调用传输数量不能大于设定的值，默认为0，即不设上限。
    keepalive_timeout 65;  #连接超时时间，默认为75s，可以在http，server，location块。

    upstream mysvr {   
      server 127.0.0.1:7878;
      server 192.168.10.121:3333 backup;  #热备
    }
    error_page 404 https://www.baidu.com; #错误页
    server {
        keepalive_requests 120; #单连接请求上限次数。
        listen       4545;   #监听端口
        server_name  127.0.0.1;   #监听地址       
        location  ~*^.+$ {       #请求的url过滤，正则匹配，~为区分大小写，~*为不区分大小写。
           #root path;  #根目录
           #index vv.txt;  #设置默认页
           proxy_pass  http://mysvr;  #请求转向mysvr 定义的服务器列表
           deny 127.0.0.1;  #拒绝的ip
           allow 172.18.5.54; #允许的ip           
        } 
    }
}
```

上面是nginx的基本配置，需要注意的有以下几点：

1、几个常见配置项：

-  1.$remote_addr 与 $http_x_forwarded_for 用以记录客户端的ip地址；
-  2.$remote_user ：用来记录客户端用户名称；
-  3.$time_local ： 用来记录访问时间与时区；
-  4.$request ： 用来记录请求的url与http协议；
-  5.$status ： 用来记录请求状态；成功是200；
-  6.$body_bytes_s ent ：记录发送给客户端文件主体内容大小；
-  7.$http_referer ：用来记录从那个页面链接访问过来的；
-  8.$http_user_agent ：记录客户端浏览器的相关信息；

2、惊群现象：一个网路连接到来，多个睡眠的进程被同事叫醒，但只有一个进程能获得链接，这样会影响系统性能。

3、每个指令必须有分号结束。

# MySQL 安装配置

MySQL 是最流行的关系型数据库管理系统，由瑞典MySQL AB公司开发，目前属于Oracle公司。

MySQL所使用的SQL语言是用于访问数据库的最常用标准化语言。

MySQL由于其体积小、速度快、总体拥有成本低，尤其是开放源码这一特点，一般中小型网站的开发都选择MySQL作为网站数据库。

------

## MySQL 安装

本教程的系统平台：CentOS release 6.6 (Final) 64位。

### 一、安装编译工具及库文件

```
yum -y install gcc gcc-c++ make autoconf libtool-ltdl-devel gd-devel freetype-devel libxml2-devel libjpeg-devel libpng-devel openssl-devel curl-devel bison patch unzip libmcrypt-devel libmhash-devel ncurses-devel sudo bzip2 flex libaio-devel
```

### 二、 安装cmake 编译器

cmake 版本：cmake-3.1.1。

1、下载地址：http://www.cmake.org/files/v3.1/cmake-3.1.1.tar.gz

```
$ wget http://www.cmake.org/files/v3.1/cmake-3.1.1.tar.gz
```

![mysql1](img/mysql1.png)

2、解压安装包

```
$ tar zxvf cmake-3.1.1.tar.gz
```

3、进入安装包目录

```
$ cd cmake-3.1.1
```

4、编译安装 

```
$ ./bootstrap
$ make && make install
```

------

### 三、安装 MySQL

MySQL版本：mysql-5.6.15。

1、下载地址： http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.15.tar.gz

```
$ wget http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.15.tar.gz
```

![mysql2](img/mysql2.png)

2、解压安装包

```
$ tar zxvf mysql-5.6.15.tar.gz
```

3、进入安装包目录

```
$ cd mysql-5.6.15
```

4、编译安装 

```
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/local/webserver/mysql/ -DMYSQL_UNIX_ADDR=/tmp/mysql.sock -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_EXTRA_CHARSETS=all -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DWITH_INNODB_MEMCACHED=1 -DWITH_DEBUG=OFF -DWITH_ZLIB=bundled -DENABLED_LOCAL_INFILE=1 -DENABLED_PROFILING=ON -DMYSQL_MAINTAINER_MODE=OFF -DMYSQL_DATADIR=/usr/local/webserver/mysql/data -DMYSQL_TCP_PORT=3306
$ make && make install
```

5、查看mysql版本:

```
$ /usr/local/webserver/mysql/bin/mysql --version
```

![mysql3](img/mysql3.png)

到此，mysql安装完成。

------

## MySQL 配置

1、创建mysql运行使用的用户mysql：

```
$ /usr/sbin/groupadd mysql
$ /usr/sbin/useradd -g mysql mysql
```

2、创建binlog和库的存储路径并赋予mysql用户权限

```
$ mkdir -p /usr/local/webserver/mysql/binlog /www/data_mysql
$ chown mysql.mysql /usr/local/webserver/mysql/binlog/ /www/data_mysql/
```

3、创建my.cnf配置文件

将/etc/my.cnf替换为下面内容

```
$ cat /etc/my.cnf

[client]
port = 3306
socket = /tmp/mysql.sock
[mysqld]
replicate-ignore-db = mysql
replicate-ignore-db = test
replicate-ignore-db = information_schema
user = mysql
port = 3306
socket = /tmp/mysql.sock
basedir = /usr/local/webserver/mysql
datadir = /www/data_mysql
log-error = /usr/local/webserver/mysql/mysql_error.log
pid-file = /usr/local/webserver/mysql/mysql.pid
open_files_limit = 65535
back_log = 600
max_connections = 5000
max_connect_errors = 1000
table_open_cache = 1024
external-locking = FALSE
max_allowed_packet = 32M
sort_buffer_size = 1M
join_buffer_size = 1M
thread_cache_size = 600
#thread_concurrency = 8
query_cache_size = 128M
query_cache_limit = 2M
query_cache_min_res_unit = 2k
default-storage-engine = MyISAM
default-tmp-storage-engine=MYISAM
thread_stack = 192K
transaction_isolation = READ-COMMITTED
tmp_table_size = 128M
max_heap_table_size = 128M
log-slave-updates
log-bin = /usr/local/webserver/mysql/binlog/binlog
binlog-do-db=oa_fb
binlog-ignore-db=mysql
binlog_cache_size = 4M
binlog_format = MIXED
max_binlog_cache_size = 8M
max_binlog_size = 1G
relay-log-index = /usr/local/webserver/mysql/relaylog/relaylog
relay-log-info-file = /usr/local/webserver/mysql/relaylog/relaylog
relay-log = /usr/local/webserver/mysql/relaylog/relaylog
expire_logs_days = 10
key_buffer_size = 256M
read_buffer_size = 1M
read_rnd_buffer_size = 16M
bulk_insert_buffer_size = 64M
myisam_sort_buffer_size = 128M
myisam_max_sort_file_size = 10G
myisam_repair_threads = 1
myisam_recover
interactive_timeout = 120
wait_timeout = 120
skip-name-resolve
#master-connect-retry = 10
slave-skip-errors = 1032,1062,126,1114,1146,1048,1396
#master-host = 192.168.1.2
#master-user = username
#master-password = password
#master-port = 3306
server-id = 1
loose-innodb-trx=0 
loose-innodb-locks=0 
loose-innodb-lock-waits=0 
loose-innodb-cmp=0 
loose-innodb-cmp-per-index=0
loose-innodb-cmp-per-index-reset=0
loose-innodb-cmp-reset=0 
loose-innodb-cmpmem=0 
loose-innodb-cmpmem-reset=0 
loose-innodb-buffer-page=0 
loose-innodb-buffer-page-lru=0 
loose-innodb-buffer-pool-stats=0 
loose-innodb-metrics=0 
loose-innodb-ft-default-stopword=0 
loose-innodb-ft-inserted=0 
loose-innodb-ft-deleted=0 
loose-innodb-ft-being-deleted=0 
loose-innodb-ft-config=0 
loose-innodb-ft-index-cache=0 
loose-innodb-ft-index-table=0 
loose-innodb-sys-tables=0 
loose-innodb-sys-tablestats=0 
loose-innodb-sys-indexes=0 
loose-innodb-sys-columns=0 
loose-innodb-sys-fields=0 
loose-innodb-sys-foreign=0 
loose-innodb-sys-foreign-cols=0

slow_query_log_file=/usr/local/webserver/mysql/mysql_slow.log
long_query_time = 1
[mysqldump]
quick
max_allowed_packet = 32M
```

4、初始化数据库

```
$/usr/local/webserver/mysql/scripts/mysql_install_db --defaults-file=/etc/my.cnf  --user=mysql
```

显示如下信息：

```
Installing MySQL system tables...2015-01-26 20:18:51 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
OK

Filling help tables...2015-01-26 20:18:57 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
OK
...
```

5、创建开机启动脚本

```
$ cd /usr/local/webserver/mysql/
$ cp support-files/mysql.server /etc/rc.d/init.d/mysqld 
$ chkconfig --add mysqld 
$ chkconfig --level 35 mysqld on
```

6、启动mysql服务器

```
$ service mysqld start
```

![mysql4](img/mysql4.png)

7、连接 MySQL

```
$ /usr/local/webserver/mysql/bin/mysql -u root -p
```

![mysql5](img/mysql5.png)

## 修改MySQL用户密码

```
mysqladmin -u用户名 -p旧密码 password 新密码
```

或进入mysql命令行

```
SET PASSWORD FOR '用户名'@'主机' = PASSWORD(‘密码');
```

创建新用户并授权:

```
grant all privileges on *.* to 用户名@'%' identified by '密码' with grant option;
```

### 其他命令

- 启动：service mysqld start
- 停止：service mysqld stop
- 重启：service mysqld restart
- 重载配置：service mysqld reload

启动MySQL服务器程序，确认状态

1）启动MySQL服务程序

启动服务并查看状态：

```
[root@dbsvr1 pub]# service mysql start
Starting MySQL...                                     [确定]
[root@dbsvr1 pub]# service mysql status
MySQL running (31724)                                 [确定]
```

服务器进程为mysqld，监听的默认端口为TCP 3306：

```
[root@dbsvr1 pub]# netstat -anpt | grep mysql
tcp        0      0 :::3306        :::*       LISTEN      31724/mysqld
```

2）查看MySQL服务器进程、运行用户

提供连接服务的进程为mysqld，由其父进程mysqld_safe启动。

```
[root@dbsvr1 pub]# ps -elf | grep mysqld

4 S root     31619     1  0  80   0 -  2834 wait   15:14 pts/0    00:00:00 /bin/sh /usr/bin/mysqld_safe --datadir=/var/lib/mysql --pid file=/var/lib/mysql/dbsvr1.tarena.com.pid

4 S mysql    31724 31619  0  80   0 - 252496 poll_s 15:14 pts/0   00:00:01 /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --user=mysql --log-error=/var/lib/mysql/dbsvr1.tarena.com.err --pid-file=/var/lib/mysql/dbsvr1.tarena.com.pid
```

数据库的默认存放位置为 /var/lib/mysql：

```
[root@dbsvr1 pub]# ls /var/lib/mysql/
auto.cnf               ibdata1      mysql               RPM_UPGRADE_HISTORY
dbsvr1.tarena.com.err  ib_logfile0  mysql.sock          RPM_UPGRADE_MARKER-LAST
dbsvr1.tarena.com.pid  ib_logfile1  performance_schema  test
```