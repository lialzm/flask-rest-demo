# _*_coding:utf-8 _*_

import multiprocessing
import os
import sys

bind = "0.0.0.0:5000"
# 等待队列最大长度,超过这个长度的链接将被拒绝连接
backlog = 2048
#  进程数 = cup数量 * 2 + 1
workers = multiprocessing.cpu_count() * 2 + 1
threads=5
worker_connections = 1000
timeout = 900
keepalive = 2