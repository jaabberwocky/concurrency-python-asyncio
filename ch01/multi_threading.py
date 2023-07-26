import threading
from common import hello_from_thread, parse_and_return_args


if __name__ == '__main__':
    args = parse_and_return_args()
    print(f"Multi thread with {args.num_iterations} iterations")

    threads = []

    for i in range(args.num_iterations):
        hello_thread = threading.Thread(target=hello_from_thread)
        hello_thread.start()
        threads.append(hello_thread)

    total_threads = threading.active_count()
    thread_name = threading.current_thread().name

    print(f'Python is currently running {total_threads} thread(s)')
    print(f'The current thread is {thread_name}')

    for thread in threads:
        thread.join()

    print(f"Main thread {threading.current_thread()} exiting...")
