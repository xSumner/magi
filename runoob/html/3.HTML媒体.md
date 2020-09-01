# HTML 多媒体

------

Web 上的多媒体指的是音效、音乐、视频和动画。

现代网络浏览器已支持很多多媒体格式。

------

## 什么是多媒体？

多媒体来自多种不同的格式。它可以是您听到或看到的任何内容，文字、图片、音乐、音效、录音、电影、动画等等。

在因特网上，您会经常发现嵌入网页中的多媒体元素，现代浏览器已支持多种多媒体格式。

在本教程中，您将了解到不同的多媒体格式，以及如何在您的网页中使用它们。

------

## 浏览器支持

第一款因特网浏览器只支持文本，而且即使是对文本的支持也仅限于单一字体和单一颜色。随后诞生了支持颜色、字体和文本样式的浏览器，图片支持也被加入。

不同的浏览器以不同的方式处理对音效、动画和视频的支持。某些元素能够以内联的方式处理，而某些则需要额外的插件。

您将在下面的章节学习更多有关插件的知识。

------

## 多媒体格式

格式 多媒体元素（比如视频和音频）存储于媒体文件中。

确定媒体类型的最常用的方法是查看文件扩展名。当浏览器得到文件扩展名 .htm 或 .html 时，它会假定该文件是 HTML 页面。.xml 扩展名指示 XML 文件，而 .css 扩展名指示样式表。图片格式则通过 .gif 或 .jpg 来识别。

多媒体元素元素也拥有带有不同扩展名的文件格式，比如 .swf、.wmv、.mp3 以及 .mp4。

------

## 视频格式

| ![pic_video](img/pic_video.jpg) | MP4是互联网推出新的视频格式。  YouTube 推荐使用 MP4 。  Flash Players 支持 MP4  HTML5 支持 MP4。 |
| ------------------------------- | ------------------------------------------------------------ |
|                                 |                                                              |

| 格式      | 文件      | 描述                                                         |
| :-------- | :-------- | :----------------------------------------------------------- |
| AVI       | .avi      | AVI (Audio Video Interleave) 格式是由微软开发的。所有运行 Windows 的计算机都支持 AVI 格式。它是因特网上很常见的格式，但非 Windows 计算机并不总是能够播放。 |
| WMV       | .wmv      | Windows Media 格式是由微软开发的。Windows Media 在因特网上很常见，但是如果未安装额外的（免费）组件，就无法播放 Windows Media 电影。一些后期的 Windows Media 电影在所有非 Windows 计算机上都无法播放，因为没有合适的播放器。 |
| MPEG      | .mpg.mpeg | MPEG (Moving Pictures Expert Group) 格式是因特网上最流行的格式。它是跨平台的，得到了所有最流行的浏览器的支持。 |
| QuickTime | .mov      | QuickTime 格式是由苹果公司开发的。QuickTime 是因特网上常见的格式，但是 QuickTime 电影不能在没有安装额外的（免费）组件的 Windows 计算机上播放。 |
| RealVideo | .rm.ram   | RealVideo 格式是由 Real Media 针对因特网开发的。该格式允许低带宽条件下（在线视频、网络电视）的视频流。由于是低带宽优先的，质量常会降低。 |
| Flash     | .swf.flv  | Flash (Shockwave) 格式是由 Macromedia 开发的。Shockwave 格式需要额外的组件来播放。但是该组件会预装到 Firefox 或 IE 之类的浏览器上。 |
| Mpeg-4    | .mp4      | Mpeg-4 (with H.264 video compression) 是一种针对因特网的新格式。事实上，YouTube 推荐使用 MP4。YouTube 接收多种格式，然后全部转换为 .flv 或 .mp4 以供分发。越来越多的视频发布者转到 MP4，将其作为 Flash 播放器和 HTML5 的因特网共享格式。 |



| ![Note](img/lamp.jpg) | 最新的 HTML5 标准只支持 MP4, WebM, 和 Ogg 视频格式。 |
| --------------------- | ---------------------------------------------------- |
|                       |                                                      |

## 声音格式

MP3是一种音频压缩技术，其全称是动态影像专家压缩标准音频层面3（Moving Picture Experts Group Audio Layer III），简称为MP3。它被设计用来大幅度地降低音频数据量。如果你的站点是音乐类型的，你可以选择mp3格式。

| 格式      | 文件      | 描述                                                         |
| :-------- | :-------- | :----------------------------------------------------------- |
| MIDI      | .mid.midi | MIDI (Musical Instrument Digital Interface) 是一种针对电子音乐设备（比如合成器和声卡）的格式。MIDI 文件不含有声音，但包含可被电子产品（比如声卡）播放的数字音乐指令。[点击这里播放 The Beatles](https://www.runoob.com/try/demo_source/beatles.mid)。因为 MIDI 格式仅包含指令，所以 MIDI 文件极其小巧。上面的例子只有 23k 的大小，但却能播放将近 5 分钟。MIDI 得到了广泛的平台上的大量软件的支持。大多数流行的网络浏览器都支持 MIDI。 |
| RealAudio | .rm.ram   | RealAudio 格式是由 Real Media 针对因特网开发的。该格式也支持视频。该格式允许低带宽条件下的音频流（在线音乐、网络音乐）。由于是低带宽优先的，质量常会降低。 |
| Wave      | .wav      | Wave (waveform) 格式是由 IBM 和微软开发的。所有运行 Windows 的计算机和所有网络浏览器（除了 Google Chrome）都支持它。 |
| WMA       | .wma      | WMA 格式 (Windows Media Audio)，质量优于 MP3，兼容大多数播放器，除了 iPod。WMA 文件可作为连续的数据流来传输，这使它对于网络电台或在线音乐很实用。 |
| MP3       | .mp3.mpga | MP3 文件实际上是 MPEG 文件的声音部分。MPEG 格式最初是由运动图像专家组开发的。MP3 是其中最受欢迎的针对音乐的声音格式。期待未来的软件系统都支持它。 |



| ![Note](img/lamp.jpg) | HTML5 的最新标准支持 MP3, WAV, 和 Ogg 音频格式。 |
| --------------------- | ------------------------------------------------ |
|                       |                                                  |



# HTML 插件

------

插件的功能是扩展 HTML 浏览器的功能。

------

## HTML 助手（插件）

辅助应用程序（helper application）是可由浏览器启动的程序。辅助应用程序也称为插件。

辅助程序可用于播放音频和视频（以及其他）。辅助程序是使用 <object> 标签来加载的。

使用辅助程序播放视频和音频的一个优势是，您能够允许用户来控制部分或全部播放设置。

插件可以通过 <object> 标签或者 <embed> 标签添加在页面中。 

大多数辅助应用程序允许对音量设置和播放功能（比如后退、暂停、停止和播放）的手工（或程序的）控制。

| ![Note](img/lamp.jpg) | 我们可以使用 <video> 和 <audio> 标签来显示视频和音频 |
| --------------------- | ---------------------------------------------------- |
|                       |                                                      |

------

## <object> 元素

所有主流浏览器都支持 <object> 标签。

<object> 元素定义了在 HTML 文档中嵌入的对象。



该标签用于插入对象 (例如在网页中嵌入 Java 小程序, PDF 阅读器, Flash 播放器) 。

## 实例

<object width="400" height="50" data="bookmark.swf"></object>


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_object_plugin)

<object> 元素同样可用于包含HTML文件：



## 实例

<object width="100%" height="500px" data="snippet.html"></object>


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_object_html)

或者插入一张图片:

## 实例

<object data="audi.jpeg"></object>


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_object_image)

------

## <embed> 元素

所有主流浏览器都支持 <embed> 元素。

<embed> 元素表示一个 HTML Embed 对象 。



<embed> 元素已经出现很长一段时间了，但是在 HTML5 前并未被详细说明，该元素在 HTML 5 页面上会被验证，在 HTML 4 上不会。



## 实例

<embed width="400" height="50" src="bookmark.swf">




[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_embed_plugin)



| ![Note](img/lamp.jpg) | 注意 <embed> 元素没有关闭标签。 不能使用替代文本。 |
| --------------------- | -------------------------------------------------- |
|                       |                                                    |

<embed> 元素同样可用于包含 HTML 文件：



## 实例

<embed width="100%" height="500px" src="snippet.html">




[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_embed_html)

或者插入一张图片:

## 实例

<embed src="audi.jpeg">




[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_embed_image)



# HTML 音频(Audio)

------

声音在HTML中可以以不同的方式播放.

------

## 问题以及解决方法

在 HTML 中播放音频并不容易！

您需要谙熟大量技巧，以确保您的音频文件在所有浏览器中（Internet Explorer, Chrome, Firefox, Safari, Opera）和所有硬件上（PC, Mac , iPad, iPhone）都能够播放。

在本章，菜鸟教程为您总结了问题和解决方法。

------

## 使用插件

浏览器插件是一种扩展浏览器标准功能的小型计算机程序。

插件可以使用 <object> 标签 或者 <embed> 标签添加在页面上. 

这些标签定义资源（通常非 HTML 资源）的容器，根据类型，它们即会由浏览器显示，也会由外部插件显示。

------

## 使用 <embed> 元素

<embed>标签定义外部（非 HTML）内容的容器。（这是一个 HTML5 标签，在 HTML4 中是非法的，但是所有浏览器中都有效）。



下面的代码片段能够显示嵌入网页中的 MP3 文件：

## 实例

<embed height="50" width="100" src="horse.mp3">




[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_soundmidiembed)

### **问题:**

- <embed> 标签在 HTML 4 中是无效的。页面无法通过 HTML 4 验证。

- 不同的浏览器对音频格式的支持也不同。

- 如果浏览器不支持该文件格式，没有插件的话就无法播放该音频。

- 如果用户的计算机未安装插件，无法播放音频。

- 如果把该文件转换为其他格式，仍然无法在所有浏览器中播放。

------

## 使用 <object> 元素

<object tag> 标签也可以定义外部（非 HTML）内容的容器。



下面的代码片段能够显示嵌入网页中的 MP3 文件：

## 实例

<object height="50" width="100" data="horse.mp3"></object>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_soundmidobject)

### **问题:**

- 不同的浏览器对音频格式的支持也不同。
- 如果浏览器不支持该文件格式，没有插件的话就无法播放该音频。
- 如果用户的计算机未安装插件，无法播放音频。
- 如果把该文件转换为其他格式，仍然无法在所有浏览器中播放。

------

## 使用 HTML5 <audio> 元素

HTML5 <audio> 元素是一个 HTML5 元素，在 HTML 4 中是非法的，但在所有浏览器中都有效。

The <audio> element works in all modern browsers.

### 流量器兼容

格中的数字表示支持该属性的第一个浏览器版本号。

| 元素    |      |      |      |      |      |
| :------ | ---- | ---- | ---- | ---- | ---- |
| <audio> | 4.0  | 9.0  | 3.5  | 4.0  | 10.5 |

以下我们将使用 <audio> 标签来描述 MP3 文件(Internet Explorer、Chrome 以及 Safari 中是有效的), 同样添加了一个 OGG 类型文件(Firefox 和 Opera浏览器中有效).如果失败，它会显示一个错误文本信息:

## 实例

<audio controls>  <source src="horse.mp3" type="audio/mpeg">  <source src="horse.ogg" type="audio/ogg">  Your browser does not support this audio format.</audio>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_audio_5)

### **问题:**

- <audio> 标签在 HTML 4 中是无效的。您的页面无法通过 HTML 4 验证。

- 您必须把音频文件转换为不同的格式。

- <audio> 元素在老式浏览器中不起作用。

------

## 最好的 HTML 解决方法

下面的例子使用了两个不同的音频格式。HTML5 <audio> 元素会尝试以 mp3 或 ogg 来播放音频。如果失败，代码将回退尝试 <embed> 元素。

## 实例

<audio controls height="100" width="100">  <source src="horse.mp3" type="audio/mpeg">  <source src="horse.ogg" type="audio/ogg">  <embed height="50" width="100" src="horse.mp3"></audio>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_audio_all)

### **问题:**

- 您必须把音频转换为不同的格式。

- <embed> 元素无法回退来显示错误消息。

------

## 使用超链接

如果网页包含指向媒体文件的超链接，大多数浏览器会使用"辅助应用程序"来播放文件。

以下代码片段显示指向 mp3 文件的链接。如果用户点击该链接，浏览器会启动"辅助应用程序"来播放该文件：

## 实例

<a href="horse.mp3">Play the sound</a>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_sound_mp3link)



------

## 内联的声音说明

当您在网页中包含声音，或者作为网页的组成部分时，它被称为内联声音。

如果您打算在 web 应用程序中使用内联声音，您需要意识到很多人都觉得内联声音令人恼火。同时请注意，用户可能已经关闭了浏览器中的内联声音选项。

我们最好的建议是只在用户希望听到内联声音的地方包含它们。一个正面的例子是，在用户需要听到录音并点击某个链接时，会打开页面然后播放录音。

------

## HTML 多媒体标签

**New** : HTML5 新标签

| 标签                                                   | 描述                                                         |
| :----------------------------------------------------- | :----------------------------------------------------------- |
| [](https://www.runoob.com/tags/tag-embed.html)         | 定义内嵌对象。HTML4 中不赞成，HTML5 中允许。                 |
| [](https://www.runoob.com/tags/tag-object.html)        | 定义内嵌对象。                                               |
| [](https://www.runoob.com/tags/tag-param.html)         | 定义对象的参数。                                             |
| [](https://www.runoob.com/tags/tag-audio.html)**New**  | 定义了声音内容                                               |
| [](https://www.runoob.com/tags/tag-video.html)**New**  | 定义一个视频或者影片                                         |
| [](https://www.runoob.com/tags/tag-source.html)**New** | 定义了media元素的多媒体资源(<video> 和 <audio>)              |
| [](https://www.runoob.com/tags/tag-track.html)**New**  | 规定media元素的字幕文件或其他包含文本的文件 (<video> 和<audio>) |

# HTML 视频（Video）

------

在 HTML 中播放视频的方法有很多种。

------

## HTML视频（Videos）播放

## 实例

<video width="320" height="240" controls>   <source src="movie.mp4" type="video/mp4">   <source src="movie.ogg" type="video/ogg">   <source src="movie.webm" type="video/webm">   <object data="movie.mp4" width="320" height="240">     <embed src="movie.swf" width="320" height="240">   </object>  </video>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_video_html5_4)



------

## 问题以及解决方法

在 HTML 中播放视频并不容易！

您需要谙熟大量技巧，以确保您的视频文件在所有浏览器中（Internet Explorer, Chrome, Firefox, Safari, Opera）和所有硬件上（PC, Mac , iPad, iPhone）都能够播放。

在本章，菜鸟教程为您总结了问题和解决方法。

------

## 使用 <embed> 标签

<embed> 标签的作用是在 HTML 页面中嵌入多媒体元素。



下面的 HTML 代码显示嵌入网页的 Flash 视频：

## 实例

<embed src="intro.swf" height="200" width="200">




[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videoembed)

**问题**

- HTML4 无法识别 <embed> 标签。您的页面无法通过验证。
- 如果浏览器不支持 Flash，那么视频将无法播放
- iPad 和 iPhone 不能显示 Flash 视频。
- 如果您将视频转换为其他格式，那么它仍然不能在所有浏览器中播放。

------

## 使用 <object> 标签

<object> 标签的作用是在 HTML 页面中嵌入多媒体元素。



下面的 HTML 片段显示嵌入网页的一段 Flash 视频：

## 实例

<object data="intro.swf" height="200" width="200"></object>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videoobject)

**问题:**

- 如果浏览器不支持 Flash，将无法播放视频。
- iPad 和 iPhone 不能显示 Flash 视频。
- 如果您将视频转换为其他格式，那么它仍然不能在所有浏览器中播放。

------

## 使用 HTML5 <video> 元素

HTML5 <video> 标签定义了一个视频或者影片.

<video> 元素在所有现代浏览器中都支持。



以下 HTML 片段会显示一段嵌入网页的 ogg、mp4 或 webm 格式的视频：

## 实例

<video width="320" height="240" controls>  <source src="movie.mp4" type="video/mp4">  <source src="movie.ogg" type="video/ogg">  <source src="movie.webm" type="video/webm">您的浏览器不支持 video 标签。</video>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_video_html5)

**问题:**

- 您必须把视频转换为很多不同的格式。

- <video> 元素在老式浏览器中无效。

------

## 最好的 HTML 解决方法

以下实例中使用了 4 种不同的视频格式。HTML 5 <video> 元素会尝试播放以 mp4、ogg 或 webm 格式中的一种来播放视频。如果均失败，则回退到 <embed> 元素。

## HTML 5 + <object> + <embed>

<video width="320" height="240" controls>  <source src="movie.mp4" type="video/mp4">  <source src="movie.ogg" type="video/ogg">  <source src="movie.webm" type="video/webm">  <object data="movie.mp4" width="320" height="240">    <embed src="movie.swf" width="320" height="240">  </object></video>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_video_html5_4)

**问题:**

- 您必须把视频转换为很多不同的格式

------

## 优酷解决方案

在 HTML 中显示视频的最简单的方法是使用优酷等视频网站。

如果您希望在网页中播放视频，那么您可以把视频上传到优酷等视频网站，然后在您的网页中插入 HTML 代码即可播放视频。

你可以在各大视频网站的分享入口，找到嵌入的 HTML 代码。

![img](img/36B8ED24-2F40-44EC-A751-2617F749447C.jpg)

## 实例

<embed src='https://player.youku.com/player.php/sid/XMTQ3MjM5Mjc0MA==/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videoyouku)

------

## 使用超链接

如果网页包含指向媒体文件的超链接，大多数浏览器会使用"辅助应用程序"来播放文件。

以下代码片段显示指向 AVI 文件的链接。如果用户点击该链接，浏览器会启动"辅助应用程序"，比如 Windows Media Player 来播放这个 AVI 文件：

## 实例

<a href="intro.swf">Play a video file</a>


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videolink)



------

## 关于内联视频的说明

当视频被包含在网页中时，它被称为内联视频。

如果您打算在 web 应用程序中使用内联视频，您需要意识到很多人都觉得内联视频令人恼火。

同时请注意，用户可能已经关闭了浏览器中的内联视频选项。

我们最好的建议是只在用户希望看到内联视频的地方包含它们。一个正面的例子是，在用户需要看到视频并点击某个链接时，会打开页面然后播放视频。

------

## HTML 多媒体标签

**New** : HTML5新标签.

| 标签                                                   | 描述                                                         |
| :----------------------------------------------------- | :----------------------------------------------------------- |
| [](https://www.runoob.com/tags/tag-embed.html)         | 定义内嵌对象。HTML4 中不赞成，HTML5 中允许。                 |
| [](https://www.runoob.com/tags/tag-object.html)        | 定义内嵌对象。                                               |
| [](https://www.runoob.com/tags/tag-param.html)         | 定义对象的参数。                                             |
| [](https://www.runoob.com/tags/tag-audio.html)**New**  | 定义了声音内容                                               |
| [](https://www.runoob.com/tags/tag-video.html)**New**  | 定义一个视频或者影片                                         |
| [](https://www.runoob.com/tags/tag-source.html)**New** | 定义了media元素的多媒体资源(<video> 和 <audio>)              |
| [](https://www.runoob.com/tags/tag-track.html)**New**  | 规定media元素的字幕文件或其他包含文本的文件 (<video> 和<audio>) |

# HTML 实例

------

**HTML 基础**

[非常简单的HTML文档](https://www.runoob.com/try/try.php?filename=tryhtml_intro)
[HTML 标题](https://www.runoob.com/try/try.php?filename=tryhtml_headers)
[HTML 段落](https://www.runoob.com/try/try.php?filename=tryhtml_paragraphs1)
[HTML 链接](https://www.runoob.com/try/try.php?filename=tryhtml_basic_link)
[HTML 图片](https://www.runoob.com/try/try.php?filename=tryhtml_basic_img)

[实例解析](https://www.runoob.com/html/html-basic.html)

------

**HTML 标题**

[HTML 标题](https://www.runoob.com/try/try.php?filename=tryhtml_headers)
[在html源码中插入注释](https://www.runoob.com/try/try.php?filename=tryhtml_comment)
[插入水平线](https://www.runoob.com/try/try.php?filename=tryhtml_hr)

[实例解析](https://www.runoob.com/html/html-headings.html)

------

**HTML 段落**

[HTML 段落](https://www.runoob.com/try/try.php?filename=tryhtml_paragraphs1)
[更多段落](https://www.runoob.com/try/try.php?filename=tryhtml_paragraphs2)
[本例演示在 HTML 文档中折行的使用。](https://www.runoob.com/try/try.php?filename=tryhtml_paragraphs)
[HTML 格式化的某些问题。](https://www.runoob.com/try/try.php?filename=tryhtml_poem)

[实例解析](https://www.runoob.com/html/html-paragraphs.html)

------

**HTML 文本格式化**

[文本格式化](https://www.runoob.com/try/try.php?filename=tryhtml_formattingch)
[此例演示如何使用 pre 标签对空行和空格进行控制。](https://www.runoob.com/try/try.php?filename=tryhtml_pre)
[此例演示不同的"计算机输出"标签的显示效果。](https://www.runoob.com/try/try.php?filename=tryhtml_computeroutput)
[此例演示如何在 HTML 文件中写地址。](https://www.runoob.com/try/try.php?filename=tryhtml_address)
[此例演示如何实现缩写或首字母缩写。](https://www.runoob.com/try/try.php?filename=tryhtml_abbr)
[此例演示如何改变文字的方向。](https://www.runoob.com/try/try.php?filename=tryhtml_bdo)
[此例演示如何实现长短不一的引用语。](https://www.runoob.com/try/try.php?filename=tryhtml_q)
[文本下划线与删除线](https://www.runoob.com/try/try.php?filename=tryhtml_del)

[实例解析](https://www.runoob.com/html/html-formatting.html)

------

**HTML 样式**

[HTML Style 元素](https://www.runoob.com/try/try.php?filename=tryhtml_styles)
[背景色样式](https://www.runoob.com/try/try.php?filename=tryhtml_bodybgstyle)
[字体样式，颜色，大小](https://www.runoob.com/try/try.php?filename=tryhtml_newfont)
[文本对齐样式](https://www.runoob.com/try/try.php?filename=tryhtml_headeralign)
[设置文本字体](https://www.runoob.com/try/try.php?filename=tryhtml_font-family)
[设置文本字体大小](https://www.runoob.com/try/try.php?filename=tryhtml_font-size)
[设置文本字体颜色](https://www.runoob.com/try/try.php?filename=tryhtml_color)
[设置文本字体，字体大小，字体颜色](https://www.runoob.com/try/try.php?filename=tryhtml_fontall)
[HTML使用不同样式](https://www.runoob.com/try/try.php?filename=tryhtml_style)
[没有下划线的链接](https://www.runoob.com/try/try.php?filename=tryhtml_linknoline)
[链接到一个外部样式表](https://www.runoob.com/try/try.php?filename=tryhtml_link)

[实例解析](https://www.runoob.com/html/html-css.html)

------

**HTML 链接**

[创建超级链接](https://www.runoob.com/try/try.php?filename=tryhtml_links)
[将图像作为链接](https://www.runoob.com/try/try.php?filename=tryhtml_imglink)
[在新的浏览器窗口打开链接](https://www.runoob.com/try/try.php?filename=tryhtml_link_target)
[链接到同一个页面的不同位置](https://www.runoob.com/try/try.php?filename=tryhtml_link_locations&basepath=0)
[跳出框架](https://www.runoob.com/try/try.php?filename=tryhtml_frame_getfree)
[创建电子邮件链接](https://www.runoob.com/try/try.php?filename=tryhtml_mailto)
[创建电子邮件链接 2](https://www.runoob.com/try/try.php?filename=tryhtml_mailto2)

[实例解析](https://www.runoob.com/html/html-links.html)

------

**HTML 图像**

[插入图像](https://www.runoob.com/try/try.php?filename=tryhtml_images)
[从不同的位置插入图片](https://www.runoob.com/try/try.php?filename=tryhtml_images2)
[排列图片](https://www.runoob.com/try/try.php?filename=tryhtml_image_align)
[本例演示如何使图片浮动至段落的左边或右边。](https://www.runoob.com/try/try.php?filename=tryhtml_image_float)
[制作图像链接](https://www.runoob.com/try/try.php?filename=tryhtml_imglink)
[创建图像映射](https://www.runoob.com/try/try.php?filename=tryhtml_areamap)

[实例解析](https://www.runoob.com/html/html-images.html)

------

**HTML 表格**

[简单的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables)
[没有边框的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables3)
[表格中的表头](https://www.runoob.com/try/try.php?filename=tryhtml_table_headers)
[带有标题的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables2)
[跨行或跨列的表格单元格](https://www.runoob.com/try/try.php?filename=tryhtml_table_span)
[表格内的标签](https://www.runoob.com/try/try.php?filename=tryhtml_table_elements)
[单元格边距(Cell padding)](https://www.runoob.com/try/try.php?filename=tryhtml_table_cellpadding)
[单元格间距(Cell spacing)](https://www.runoob.com/try/try.php?filename=tryhtml_table_cellspacing)

[实例解析](https://www.runoob.com/html/html-tables.html)

------

**HTML 列表**

[无序列表](https://www.runoob.com/try/try.php?filename=tryhtml_lists4)
[有序列表](https://www.runoob.com/try/try.php?filename=tryhtml_lists)
[不同类型的有序列表](https://www.runoob.com/try/try.php?filename=tryhtml_lists_ordered)
[不同类型的无序列表](https://www.runoob.com/try/try.php?filename=tryhtml_lists_unordered)
[嵌套列表](https://www.runoob.com/try/try.php?filename=tryhtml_lists2)
[嵌套列表 2](https://www.runoob.com/try/try.php?filename=tryhtml_nestedlists2)
[定义列表](https://www.runoob.com/try/try.php?filename=tryhtml_lists3)

[实例解析](https://www.runoob.com/html/html-lists.html)

------

**HTML Forms 和 Input**

[创建文本域(Text fields)](https://www.runoob.com/try/try.php?filename=tryhtml_input)
[创建密码域](https://www.runoob.com/try/try.php?filename=tryhtml_inputpassword)
[复选框](https://www.runoob.com/try/try.php?filename=tryhtml_checkbox)
[单选按钮](https://www.runoob.com/try/try.php?filename=tryhtml_radio)
[简单的下拉列表](https://www.runoob.com/try/try.php?filename=tryhtml_select2)
[预选下拉列表](https://www.runoob.com/try/try.php?filename=tryhtml_select3)
[本例演示如何创建一个文本域（多行文本输入控件）。](https://www.runoob.com/try/try.php?filename=tryhtml_textarea)
[创建一个按钮](https://www.runoob.com/try/try.php?filename=tryhtml_button)
[本例演示如何在数据周围绘制一个带标题的框。](https://www.runoob.com/try/try.php?filename=tryhtml_legend)
[带有文本域与输入域的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_submit)
[带有复选框与提交按钮的form表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_checkbox)
[带有单选框与提交按钮的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_radio)
[发送邮件表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_mail)

[实例解析](https://www.runoob.com/html/html-forms.html)

------

**HTML iframe**

[内联框架 (HTML页面中插入框架)](https://www.runoob.com/try/try.php?filename=tryhtml_iframe)

[实例解析](https://www.runoob.com/html/html-iframe.html)

------

**HTML 头部元素**

[描述了文档标题](https://www.runoob.com/try/try.php?filename=tryhtml_title)
[HTML页面中默认的URL链接](https://www.runoob.com/try/try.php?filename=tryhtml_base)
[提供文档元数据](https://www.runoob.com/try/try.php?filename=tryhtml_meta)

[实例解析](https://www.runoob.com/html/html-head.html)

------

**HTML 脚本**

[插入一个脚本](https://www.runoob.com/try/try.php?filename=tryhtml_script)
[使用  标签](https://www.runoob.com/try/try.php?filename=tryhtml_noscript)

[实例解析](https://www.runoob.com/html/html-scripts.html)







