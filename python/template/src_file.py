if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def filename(num: int) -> int:
    pass
