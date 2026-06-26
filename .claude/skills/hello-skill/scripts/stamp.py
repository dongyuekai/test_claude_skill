#!/usr/bin/env python3
"""hello-skill 的演示脚本：返回一行带时间戳的盖章信息。

存在的意义：证明 skill 的“资源层”——脚本可以被模型直接执行拿到
确定性结果，而不必把脚本内容读进上下文。
"""
import sys
import hashlib
from datetime import datetime


def main():
    payload = sys.argv[1] if len(sys.argv) > 1 else "（无输入）"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 用一个短哈希当“盖章编号”，让每次输出都不一样，便于确认是真跑了
    stamp = hashlib.sha1(f"{payload}{now}".encode()).hexdigest()[:8]
    print(f"🟢 STAMP #{stamp} | {now} | 收到内容：{payload}")


if __name__ == "__main__":
    main()