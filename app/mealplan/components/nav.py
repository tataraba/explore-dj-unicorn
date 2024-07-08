from django_unicorn.components import UnicornView


class NavView(UnicornView):
    
    selected_nav = "home"
    
    nav_items = [
        "home",
        "meal",
    ]
    
    class Meta:
        javascript_exclude = ("nav_items",)
