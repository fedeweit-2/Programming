from queue import *
from queue_presenter import *

if __name__ == '__main__':
    q = Queue()
    q.enqueue(9)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    QueuePresenter.present(q)