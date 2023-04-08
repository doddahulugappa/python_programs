from multiprocessing import Process, Queue, Pipe
from mp2 import child_program

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child_program, args=(child_conn,))
    p.start()
    height = 0.1
    for i in range(1, 50):
        event = parent_conn.recv()
        if event:
            print("Received Event processing", event)

        else:
            height += 0.1
        print(i)
    print(height)