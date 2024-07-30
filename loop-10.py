from prefect import flow, task
import time

# Define the task that will be run by each node
@task
def sleep_task(i):
    time.sleep(1)
    print(f"Completed task {i}")

@flow(log_prints=True)
def benchmark_sequential_flow():
    # Create and run the tasks in a sequential manner
    for i in range(10):
        sleep_task(i)

if __name__ == "__main__":
    benchmark_sequential_flow.serve(name="benchmark-sequential-flow",
                                    tags=["benchmark"],
                                    interval=86400)  # Schedule to run every day (86400 seconds)


if __name__ == "__main__":
    benchmark_sequential_flow.from_source(
        source="https://github.com/hanzhang177/prefect-test",
        entrypoint="loop-10.py:benchmark_sequential_flow"
    ).deploy(
        name="benchmark-sequential-flow",
        work_pool_name="wp-1",
    )
    