from common import hello_from_thread, parse_and_return_args
import threading


if __name__ == '__main__':
    args = parse_and_return_args()
    print(f"Single thread with {args.num_iterations} iterations")

    for _ in range(args.num_iterations):
        hello_from_thread()

    print(f"Main thread {threading.current_thread()} exiting...")
