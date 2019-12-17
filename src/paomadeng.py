import os
import time


# 滚动展示社会主义核心价值观
def main():
    content = '富强 民主 文明 和谐 自由 平等 公正 法制 爱国 敬业 诚信 友善 '
    con = content[:10]
    while True:
        # 清理屏幕上的输出
        os.system('clear')
        print(con)
        # 休眠200毫秒
        time.sleep(0.3)
        content = content[1:] + content[0]
        con = content[:10]


if __name__ == '__main__':
    main()
