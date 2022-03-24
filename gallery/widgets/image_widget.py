
from gi.repository import Gtk


@Gtk.Template(resource_path='/org/gnome/Gallery/ui/image-widget.ui')
class ImageWidget(Gtk.Image):
    __gtype_name__ = 'ImageWidget'

    image_object = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def set_image(self, path):
        self.image_object.set_from_file(path)


