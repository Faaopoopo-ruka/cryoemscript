#Author：Alex.Zhang
import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    # 假装等待I/O一段时间
    # yield from asyncio.sleep(3)
    yield from asyncio.sleep(3)  # 把控制权交给主循环，在休眠结束之后恢复这个协程
    return 5  # 协程中获取的值都是return 中的值


@asyncio.coroutine
def supervisor():
    # asyncio.async() 函数排定spin协程的运行时间， 使用一个task对象包装spin协程并立即返回
    spinner = asyncio.async(spin('thinking!'))
    print('spinner object:', spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
