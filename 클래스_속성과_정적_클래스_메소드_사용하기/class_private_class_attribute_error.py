class Knight:
    __item_limit = 10
    def print_limit_item(self):
        print(Knight.__item_limit)
x = Knight()
x.print_limit_item()
print(Knight.__item_limit)