import time

def evaluate(f, *args):
    t0 = time.time()
    result = f(*args)
    dt = time.time() - t0
    print("Result: ", result, "in", dt)
    return result