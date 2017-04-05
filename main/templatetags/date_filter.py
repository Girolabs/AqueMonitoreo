from django import template

register = template.Library()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')



def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()



def anio(value): # Only one argument.
    """Converts a string into all lowercase"""
    
    if value is None:
    	return value.replace('2017',"hola")
    return value


register.filter('cut', cut)
register.filter('lower', lower)
register.filter('anio', anio)