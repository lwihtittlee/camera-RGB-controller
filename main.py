from fuction2 import show_rgb

show_rgb = show_rgb(color=ord("r"))   /#输入“r,g,b” 输出原始图，单通道灰度图，单通道融合图
sess.run(show_rgb)