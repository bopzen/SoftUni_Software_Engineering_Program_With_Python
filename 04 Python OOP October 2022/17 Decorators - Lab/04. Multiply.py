def multiply(times):
    def decorator(function):
        def wrapper(number):
            result = function(number)
            return times * result
        return wrapper
    return decorator