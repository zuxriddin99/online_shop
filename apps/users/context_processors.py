from apps.products.models import Category
from apps.users.cart import Cart


def fet_cart(request):
    cart = Cart(request)
    return {'cart': cart}


def footer_categories(request):
    return {'footer_cats': Category.objects.all()[:4]}


def wishlist(request):
    if not request.user.is_anonymous:
        return {'wish_list': request.user.favorites.all()}
    return {'wish_list': 0}
