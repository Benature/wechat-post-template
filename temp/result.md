# Trick | MacBook 多显示器案例

Tags 🏷: 软件应用 APPs
Category: Tricks

*依赖（全部列出，但并非全部必选）*


- 硬件依赖
    - Display Link 拓展坞
- 软件依赖
    - DisplayLink Manager <sup>[1]</sup>
    - BetterDisplay <sup>[2]</sup>
    - Karabiner <sup>[3]</sup>
    - Scroll Reserver <sup>[4]</sup>
    - Logitech G Hub <sup>[5]</sup>


![Screenshot 2023-12-27 at 17.04.11.png](https://s2.loli.net/2023/12/29/Y3QvIxKNCH18AgE.png)

# 连接多显示器

## tset

MacBook 如果是 Intel 芯片可以连两个显示器，如果是 M 系芯片则只能连一个屏幕，连多个显示器也只会显示同一个屏幕的画面。为了使得我的 MacBook M2 可以连上多台拓展屏，需要额外的硬件加持——DisplayLink 拓展坞。

![DisplayLink 拓展坞](https://s2.loli.net/2023/12/29/N2RBtWglpmTnDeP.jpg)


（我买的拓展坞有三个输出口——两个 HDMI、一个 DP，因此如果缺少相应的数据线，可以在买拓展坞的时候记得一起把线买了）

直接使用 DisplayLink 拓展坞的话其实只会连接一个显示器，因为软件上还需要安装 DisplayLink Manager <sup>[1]</sup>（放心，软件是免费的了），启动后即可惊喜地发现三个显示器都亮屏了，而且不是镜像。

![Screenshot 2023-12-28 at 14.29.00.png](https://s2.loli.net/2023/12/29/TCsRo4SlegxhKcy.png)

多个显示器的设置在系统设置的 Displays，但更精细化的配置需要安装 https://github.com/waydabber/BetterDisplay。比如我目前三块显示器的分辨率并不一致，两块 1080 分辨率、一块 2K 画质。我把分辨率最好的屏幕放中间作为主屏，但鼠标穿越到其他屏幕的时候会有点“瞬移”（因为分辨率不同但实际大小一样）。为了避免这种割裂感，我只好”稍作让步“，在BetterDisplay中把主屏的分辨率也设置为 1080，如此一来三块屏幕终于“平起平坐”了。

![Screenshot 2023-12-27 at 17.04.11.png](https://s2.loli.net/2023/12/29/Y3QvIxKNCH18AgE.png)

# 键鼠配置

如果使用鼠标，会发现鼠标的滚轮移动方向和我们习惯的操作是反过来的。如果在系统设置中把滑动效果调转过来，又会影响到触摸板的控制。Scroll Reserver <sup>[4]</sup> 可以很好地解决这个问题，它只将鼠标滚轮调转回我们习惯的方向，不影响到触摸板原来的操作。

![Untitled](https://s2.loli.net/2023/12/29/RtY47TQ91HgNDaJ.png)

有时候为了省电、护眼（少一块屏幕辐射）、节省桌面空间之类，我会把 MacBook 屏幕合上。那么虚拟屏幕的切换就没那么顺手了，只能依赖快捷键 `ctrl+左`、`ctrl+右`。如果鼠标有多的功能键，可以把快捷键绑到鼠标功能键上，比如 KeyBoard Maestro <sup>[6]</sup>、Better Touch Tool <sup>[7]</sup>。因为我使用的是罗技的鼠标，直接安装官方的 Logitech G Hub <sup>[5]</sup> 来配置了。

![Screenshot 2023-12-28 at 11.58.19.png](https://s2.loli.net/2023/12/29/17i9nadz6FKteEj.png)

至于键盘，因为一般而言都是 Windows 的键盘布局，我为了用得更顺手，拿 Karabiner <sup>[3]</sup> 来修改了键映射，使得更接近于 MacBook 自身的键盘布局。

![Screenshot 2023-12-28 at 14.51.57.png](https://s2.loli.net/2023/12/29/m49uBOsxH7FKwlc.png)
<p></p>
---

\[1\]: https://www.synaptics.com/products/displaylink-graphics/downloads  
\[2\]: https://github.com/waydabber/BetterDisplay  
\[3\]: https://karabiner-elements.pqrs.org/  
\[4\]: https://pilotmoon.com/scrollreverser/  
\[5\]: https://www.logitechg.com/en-us/innovation/g-hub.html  
\[6\]: https://www.keyboardmaestro.com/main/  
\[7\]: https://folivora.ai/  