from django.conf import settings
from django.shortcuts import get_object_or_404
from programmes.models import Programme


def bag_contents(request):

    bag_items = []
    product_count = 0
    total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Programme, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id' : item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
    }

    return context
