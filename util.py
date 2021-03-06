import sys
from subprocess import run, PIPE
import asyncio
from asyncio import create_subprocess_exec, create_task, sleep, subprocess, Queue
import aionotify

async def drain(gen):
    async for _ in gen: pass

async def async_map(fn, it, filter_none=True):
    async for item in it:
        mapped = fn(item)
        if not filter_none or mapped is not None:
            yield mapped

async def poll(fn, interval=1):
    while True:
        txt = fn()
        if txt:
            yield txt
        await sleep(interval)

async def listen(*cmd, immediate=None):
    if immediate:
        yield immediate
    proc = await create_subprocess_exec(
        *cmd,
        stdout=subprocess.PIPE,
        stderr=sys.stderr)
    while True:
        line = await proc.stdout.readline()
        yield line.decode().rstrip()

async def watch(path, immediate=True):
    if immediate:
        yield readline(path)
    watcher = aionotify.Watcher()
    watcher.watch(path=path, flags=aionotify.Flags.MODIFY)
    await watcher.setup(asyncio.get_event_loop())
    while True:
        await watcher.get_event()
        yield readline(path)
    watcher.close()

async def concat(gens):
    q = Queue()

    items = [ g if isinstance(g, str) else '' for g in gens ]
    
    async def run_on_queue(index, it):
        async for item in it:
            await q.put((index, item))

    for i, gen in enumerate(gens):
        if isinstance(gen, str):
            continue
        create_task(run_on_queue(i, gen)) 

    last_output = None
    while True:
        i, item = await q.get()
        items[i] = item
        output = ''.join(items)
        if output != last_output:
            last_output = output
            yield output

def readline(path, default=''):
    try:
        return open(path).readline().rstrip()
    except:
        return default

def execute(*cmd):
    result = run(cmd, stdout=PIPE)
    return result.stdout.decode().rstrip()

