import time

def print_progress(iteration, total, prefix='Progress:', suffix='Complete', decimals=1, length=50, fill='█', tick_mark='✓'):
    """
    Call in a loop to create terminal progress bar

    Args:
        iteration: Current iteration (Int)
        total: Total iterations (Int)
        prefix: Prefix string (Str)
        suffix: Suffix string (Str)
        decimals: Positive number of decimals in percent complete (Int)
        length: Character length of bar (Int)
        fill: Bar fill character (Str)
        tick_mark: Symbol to display after completion (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    # Print tick mark on Complete
    if iteration == total:
        print(f'{tick_mark} {suffix}')

