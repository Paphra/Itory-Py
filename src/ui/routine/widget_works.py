
def enable(widgets):
    for widget in widgets:
        widget.configure(state='enabled')


def disable(widgets):
    for widget in widgets:
        widget.configure(state='disabled')


def clear(variables):
    for variable in variables:
        variable.set('')
