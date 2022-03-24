
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/Gallery/ui/image_widget.ui')
class ImageWidget(Gtk.Widget):
    __gtype_name__ = 'ImageWidget'

    image_object = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def set_pixel_size(self, size):
        print("set size:", size)
        self.image_object.set_pixel_size(size)

    def set_from_file(self, file):
        print("set image:", file)
        self.image_object.set_from_file(file)


