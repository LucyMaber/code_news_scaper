
import asyncio as aio
import random

@aio.coroutine
def async_eval(input_, sec):
  yield from aio.sleep(sec)
  print("")
  try:
    result = eval(input_)
  except Exception as e:
    print("< {!r} does not compute >".format(input_))
  else:  
    print("< {!r} = {} >".format(input_, result))

@aio.coroutine
def main(loop):
  while True:
    input_ = yield from loop.run_in_executor(None, input, "> ")

    if input_ == "quit":
      break
    elif input_ == "":
      continue
    else:
      sec = random.uniform(5, 10)
      print("< {!r} scheduled for execution in {:.02} sec>".format(input_, sec))
      aio.async(async_eval(input_, sec))

loop = aio.get_event_loop()

loop.run_until_complete(main(loop))
loop.close()