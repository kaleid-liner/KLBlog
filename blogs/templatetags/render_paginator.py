from django.template import Library

register = Library()


@register.inclusion_tag('blogs/paginator.html', takes_context=True)
def render_paginator(context, adjacent_pages=3):
    start_page = context['page_obj'].number - adjacent_pages
    if start_page <= 3:
        start_page = 1
    end_page = context['page_obj'].number + adjacent_pages
    if end_page >= context['paginator'].num_pages - 2:
        end_page = context['paginator'].num_pages
    page_numbers = range(start_page, end_page + 1)
    return {
        'page_obj': context['page_obj'],
        'paginator': context['paginator'],
        'page_numbers': page_numbers,
    }



