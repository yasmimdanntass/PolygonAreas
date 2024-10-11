
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        picture = ''
        for i in range(self.height):
            picture += self.width * '*' + '\n'
        return picture
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def get_amount_inside(self, argument):

        return self.get_area()//argument.get_area()

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        super().set_height(side)
        super().set_width(side)

    def __str__(self):
        return f'Square(side={self.width})'


