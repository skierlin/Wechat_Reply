# 获取鼠标位置
import time

import pyautogui as pg

# 截图的时候一定要用程序里的pg.screenshot截图 第三方截图软件和电脑自带截图没用的，因为会自动调整图片尺寸，导致pyautogui识别不了
# 截图时 把下面的注释拿开 一个一个来  然后把主程序注释掉  等截图完了后 再取消注释 然后截图的方法重新注释上
# 截取并保存局域内图片  截取桌面微信图标用
# pg.screenshot(r'/Users/bilbilDemos/PycharmProjects/inter000/venv/Resources/777.png',region=(786*2,838*2,40*2,40*2))
# 截取并保存局域内图片  截取对象聊天消息框用    ！！！重要  每一次微信窗口的位置如果发生移动 就要手动重新截取
# pg.screenshot(r'./888.png',region=(1040*2,160*2,370*2,410*2))
# 截取并保存局域内图片  截取文字输入窗口用
# pg.screenshot(r'/Users/bilbilDemos/PycharmProjects/inter000/venv/Resources/999.png',region=(1020*2,600*2,100*2,100*2))
# 方法2：截取微信聊天窗口上的笑脸 每次窗口移动后可以自动定位 用笑脸(x,y)值加减a,b到对象聊天消息框用位置(x+a,y+b)
# pg.screenshot(r'/Users/bilbilDemos/PycharmProjects/inter000/venv/Resources/666.png',region=(30*2,755*2,30*2,30*2))

# pg.screenshot(r'./message.png', region=(1063, 775, 600, 163))

def clickbutton():
    try:
        while True:
            # huifu_img = r'./huifu.png'
            huifu_img = r'./yinyong.png'
            pos_huifu = pg.locateOnScreen(huifu_img, grayscale=True, confidence=0.9)
            print(pos_huifu)
            if pos_huifu != None:
                center_huifu = pg.center(pos_huifu)
                print(center_huifu)
                if len(center_huifu) == 2:
                    pg.doubleClick(center_huifu.x, center_huifu.y, duration=0.5)  # 双击（ox,oy）位置
                    time.sleep(0.5)
                    pg.typewrite('1')
                    pg.press('enter')
    except KeyboardInterrupt:
        print("\n")



def FetchCenter():
    message_img = r'./message.png'
    huifu_img = r'./huifu.png'
    pos = pg.locateOnScreen(message_img, grayscale=True, confidence=0.9)
    center = pg.center(pos)
    print(pos)
    print(center)
    if len(center) == 2:
        pg.doubleClick(center.x, center.y, duration=0.5)  # 双击（ox,oy）位置
        time.sleep(0.3)
        pos_huifu = pg.locateOnScreen(huifu_img, grayscale=True, confidence=0.9)
        center_huifu = pg.center(pos_huifu)
        print(pos_huifu)
        print(center_huifu)

        if (len(center_huifu) == 2):
            pg.click(center_huifu.x, center_huifu.y)  # 双击（ox,oy）位置
            pg.typewrite('1')
            pg.press('enter')



def TestFunc():
    try:
        while True:
            x, y = pg.position()
            print(str(x) + " " + str(y))  # 输出鼠标位置

            if 1746 < x < 1800 and 2 < y < 33:
                pg.click()  # 左键单击
            if 1200 < x < 1270 and 600 < y < 620:
                pg.click(button='left')  # 右键单击
            if 1646 < x < 1700 and 2 < y < 33:
                pg.doubleClick()  # 左键双击

    except KeyboardInterrupt:
        print("\n")


if __name__ == '__main__':
    # TestFunc()
    # pg.screenshot(r'./yinyong.png', region=(1320, 874, 82, 20))
    # FetchCenter()
    clickbutton()
