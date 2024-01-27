from .models import Category


def show_category(request):
    category = Category.objects.order_by('title').prefetch_related('products').prefetch_related('subs').select_related('parent')

    return { 'category': category}