from django import template

register = template.Library()

@register.filter(name='cut_custom')
def custom_built_cut_filter(value, arg):
    """
    This cuts out all values of 'arg' from the string
    """
    # ASSUMPTION: value is a string
    return value.replace(arg, '')

# # arg1: string used to call filter in the template tag
# # arg2: call the actual function
# register.filter('cut_custom', custom_built_cut_filter)
