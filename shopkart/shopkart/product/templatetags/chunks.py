from django import template #for products itrations

register = template.Library() #it is using for products disply 1 by i

@register.filter(name='chunks') #@register.filter() is a widget
def chunks(list_data,chunk_size):
    chunk=[]
    i=0
    for data in list_data:
        chunk.append(data)
        i = i + 1
        if i == chunk_size:
            yield chunk
            i = 0
            chunk=[]
    if chunk:
        yield chunk