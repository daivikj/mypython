def convert(str):
    lst = str.split(";")
    final = []
    t = ()
    for i in lst:
        t = tuple(filter(None,i.split("=")))
        final.append(t)
    print(final)

convert("a=b;c=d;e=f;g=h")
