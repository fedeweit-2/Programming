# Implementation of the Queue presenter.
class QueuePresenter:

    @staticmethod
    def present(queue):
        unloaded = []

        length = len(queue)

        for _ in range(length):
            unloaded.append(queue.dequeue())

        print(f"<- {str(unloaded)} <-")

        for j in range(length):
            queue.enqueue(unloaded[j])
