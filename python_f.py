import tkinter as tk
import random
import threading
import time

def show_warn_tip():
    # 创建窗口
    window = tk.Tk()
    
    # 获取屏幕宽高
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 窗口尺寸扩大1.5倍
    window_width = 270  # 180 * 1.5 = 270
    window_height = 75  # 50 * 1.5 = 75
    x = random.randrange(0, screen_width - window_width)
    y = random.randrange(0, screen_height - window_height)
    
    # 设置窗口标题和位置
    window.title('关心')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # 关心生活健康的话语（30条）
    tips = [
        '好好吃饭', '好好休息', '早点休息', '天天开心',
        '记得喝水', '按时吃饭', '别熬夜了', '照顾好自己',
        '注意身体', '记得运动', '放松一下', '保持微笑',
        '劳逸结合', '别太劳累', '记得午休', '多吃水果',
        '出去走走', '呼吸新鲜空气', '保持好心情', '别久坐',
        '记得早餐', '保护眼睛', '注意保暖', '别着凉',
        '保持健康', '平安喜乐', '开心每一天', '一切顺利',
        '万事如意', '心想事成'
    ]
    
    tip = random.choice(tips)
    
    # 更多背景颜色选择
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
        'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew',
        'peachpuff', 'paleturquoise', 'lavenderblush', 'oldlace', 'lemonchiffon',
        'lightcyan', 'lightgray', 'lightpink', 'lightsalmon', 'lightseagreen',
        'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow'
    ]
    bg = random.choice(bg_colors)
    
    # 先创建并显示Label，再设置窗口属性
    label = tk.Label(
        window, 
        text=tip, 
        bg=bg, 
        font=('仿宋', 18),
        width=15,
        height=2
    )
    label.pack()
    
    # 立即更新窗口显示
    window.update()
    
    # 窗口置顶
    window.attributes('-topmost', True)
    
    # 3秒自动关闭（加快关闭速度，避免长期占用资源）
    window.after(10000, window.destroy)
    
    window.mainloop()

if __name__ == "__main__":
    # 根据屏幕大小计算所需窗口数量（确保铺满）
    window_count = 300  # 减少窗口数量，避免过于密集
    
    # 快速创建窗口（缩短间隔）
    for i in range(window_count):
        t = threading.Thread(target=show_warn_tip)
        t.daemon = True  # 守护线程，主程序退出时自动结束
        t.start()
        time.sleep(0.01)  # 极短间隔，快速创建

    # 保持主程序运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 按Ctrl+C退出
        pass