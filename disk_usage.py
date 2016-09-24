import os


def disk_usage(path):
    """Returns the disk space used (in bytes) by the directory specified by path.
    This functionality mirrors the unix/linux du command.
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            total += disk_usage(child_path)

    print("{0:<7}".format(total), path)
    return total


if __name__ == '__main__':
    path = input("Enter directory path whose size you want to know:\n")
    print("{0} uses {1} bytes of storage".format(path, disk_usage(path)))