def url_extract(s):
    if '$' in s:
        d=dict()
        a = s.split('$')
        b=a[1]
        a[1]=b[1:]
        d['text']=a[0]
        d['url']=a[1]
        return d
    else:
        c=dict()
        c['text']=s
        return c