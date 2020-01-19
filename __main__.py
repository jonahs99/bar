from asyncio import run, create_task, Queue

from config import bar
from util import async_map, drain, concat

def echo(text):
    print(text, flush=True)

if __name__ == '__main__':
    run(drain(async_map(echo, concat(bar))))
