#encoding=utf-8

# check argument exists: ['token', 'uid' ...]
def check_arguments(need_arg_list):
    def _decr(func):
        def __decr(*args, **kw):
            request_handler = args[0]
            req_args = request_handler.request.arguments
            miss_arguments = []
            for arg in need_arg_list:
                if arg not in req_args:
                    miss_arguments.append(arg)
                elif len(request_handler.get_argument(arg)) == 0:
                    miss_arguments.append(arg)
            if len(miss_arguments) == 0:
                func(*args, **kw)
            else:
                request_handler.finish({'ret': -102, 'msg': 'missing arguments:' + ','.join(miss_arguments)})
        return __decr
    return _decr
