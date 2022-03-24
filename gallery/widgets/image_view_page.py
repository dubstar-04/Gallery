
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/Gallery/ui/image_view_page.ui')
class ImageViewPage(Gtk.Widget):

    __gtype_name__ = 'image_view_page'

    display_image = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def set_image(self, image_path):
        self.display_image.set_from_file(image)



