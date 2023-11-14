from functools import wraps


class FuncDeco:
    """函数装饰器"""

    @classmethod
    def if_func_error(cls):

        def decorate(func):

            @wraps(func)
            def wrapper(*args, **kwargs):

                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception as e:

                    raise e

            return wrapper

        return decorate
