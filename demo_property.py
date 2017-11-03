is_android = True


def android(**params):
    def deco(f):
        def wrap(*args, **kwargs):
            if is_android:
                return params
            return f()

        wrap.__decorated_by_mobile__ = True
        return wrap

    return deco


def ios(**params):
    def deco(f):
        f.wrapped = True

        def wrap(*args, **kwargs):
            if not is_android:
                return params
            return f()

        wrap.__decorated_by_mobile__ = True
        return wrap

    return deco


def class_deco(cls):
    for name, method in cls.__dict__.items():
        if hasattr(method, '__decorated_by_mobile__'):
            setattr(cls, name, method())
    return cls


@class_deco
class Foo:
    @android(a=1)
    @ios(a=2)
    def by_foo(self):
        pass

    def foo(self):
        print(1)
        return 1

@class_deco
class Bar(Foo):

    @android(b=2)
    def bar(self):
        pass


f = Foo()
print(f.by_foo)
print(f.foo)

b = Bar()
print(b.bar)