from django_unicorn.components import UnicornView


class TabsView(UnicornView):
    tab = None

    def set_tab(self, selected_tab: int):
        self.tab = selected_tab
