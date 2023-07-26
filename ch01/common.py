import threading
import time
import argparse


def hello_from_thread() -> None:
    print(f'Hello from thread {threading.current_thread()}!')
    time.sleep(1)
    print(f"Second print statement from thread {threading.current_thread()}")


def parse_and_return_args():
    parser = argparse.ArgumentParser(description='Run threading example')
    parser.add_argument('num_iterations', default=2, type=int,
                        help='number of iterations to run')
    return parser.parse_args()
