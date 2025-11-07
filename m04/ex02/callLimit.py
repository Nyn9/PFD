def callLimit(limit: int):
    """Limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Limits the number of times a function can be called."""
        def limit_function(*args: any, **kwds: any):
            """ Function wrapper to limit calls """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
            else:
                function(*args, **kwds)
                count += 1
        return limit_function
    return callLimiter
