#!/usr/bin/env python3
import time
def main(func):
        def timer():
                start_time=time.time()
                for i in range(5):
                        func()
                end_time=time.time()
                print("the process speed: {}".format(end_time-start_time))
        return timer
@main
def io_task():
        time.sleep(1)
if __name__ == '__main__':
        io_task()
