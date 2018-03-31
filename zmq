import zmq
import logging
import numpy
from numpy.lib.format import header_data_from_array_1_0
import six
if six.PY3:
  buffer_ = memoryview
else:
  buffer_ = buffer

logger = logging.getLogger(__name__)
def send_arrays(socket, arrays, stop=False):
  if arrays:
    arrays = [numpy.ascontiguousarray(array) for array in arrays]
  if stop:
    headers = {'stop': True}
    socker.send_json(headers)
  else:
    headers = [header_data_from_array_1_0(array) for array in arrays]
    socket.send_json(headers, zmq.SNDMORE)
    for array in arrays[:-1]:
      socket.send(array, zmq.SNDMORE)
    socket.send(arrays[-1])

def recv_arrays(socket):
  headers = socket.recv_json()
  if 'stop' in headers:
    raise StopIteration
  arrays = []
  for header in headers:
    data = socket.recv()
    buf = buffer_(data)
    array = numpy.frombuffer(buf, dtype=numpy.dtype(header['descr']))
    array.shape = header['shape']
    if header['fortran_order']:
      array.shape = header['shape'][::-1]
      array = array.transpose()
    arrays.append(array)
  return arrays  

def client_generator(port=5557,host="localhost",hwm=20):
  context = zmq.Context()
  socket = context.socket(zmq.PULL)
  socket.set_hwm(hwm)
  socket.connect("tcp://{}:{}".format(host, port))
  logger.info('client started')
  while True:
    data = recv_arrays(socket)
    yield tuple(data)

port = 5557
hwm = 20
context = zmq.Context()
socket = context.socker(zmq.PUSH)
socker.set_hwm(hwm)
socker.bind('tcp://*:{}'.format(port))

logging.basicConfig(level='INFO')

while True:
  try:
    data = "data"
    stop = False
    logger.debug("sending {} arrays".format(len(data)))
  except StopIteration:
    stop = True
    logger.debug("sending StopInteration")
  send_arrays(socker,data,stop=stop)
