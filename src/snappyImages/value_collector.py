vc_values = ''

def value_collector_init():
    global vc_values
    vc_values = ''

vc_batch_size = 5
vc_value_size = 6

def value_collector_put_value(value):
    global vc_values
    if len(vc_values) == vc_batch_size*vc_value_size + vc_batch_size-1:
        vc_values = vc_values[vc_value_size + 1:]
    if vc_values == '':
        vc_values = value
    else:
        vc_values = vc_values + " " + value

def value_collector_get_batch():
    return '[' + vc_values + ']'
