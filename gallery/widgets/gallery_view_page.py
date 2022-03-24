
from gi.repository import Gtk, Gio, GObject

@Gtk.Template(resource_path='/org/gnome/Gallery/ui/gallery_view_page.ui')
class GalleryViewPage(Gtk.ScrolledWindow):

    __gtype_name__ = 'GalleryViewPage'

    __gsignals__ = {'image_selected' : (GObject.SIGNAL_RUN_LAST, GObject.TYPE_NONE, (GObject.TYPE_PYOBJECT, )) }

    grid_layout = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.model_items = Gtk.DirectoryList()
        self.model_items.set_file(Gio.File.new_for_path('/home/sandal/Pictures/'))


        self.list_model = Gtk.SingleSelection(model=self.model_items)
        self.list_model.connect('selection-changed', self.selection_changed)

        self.factory = Gtk.SignalListItemFactory()
        self.factory.connect('setup', self.on_factory_setup)
        self.factory.connect('bind', self.on_factory_bind)
        self.factory.connect('unbind', self.on_factory_unbind)
        self.factory.connect('teardown', self.on_factory_teardown)

        self.grid_layout.set_model(self.list_model)
        self.grid_layout.set_factory(self.factory)

    def on_factory_setup(self, widget, item: Gtk.ListItem):
        iw = Gtk.Image()
        #iw = image_widget.ImageWidget()
        iw.set_pixel_size(200)
        item.set_child(iw)

    def on_factory_bind(self, widget: Gtk.ListView, item: Gtk.ListItem):
        data = item.get_item()
        gfile = data.get_attribute_object("standard::file")
        image = item.get_child()
        # print("file path:", gfile.get_path(), image)
        image.set_from_file(gfile.get_path())

    def on_factory_unbind(self, widget, item: Gtk.ListItem):
        pass

    def on_factory_teardown(self, widget, item: Gtk.ListItem):
        pass

    def selection_changed(self, sel: Gtk.SingleSelection, pos, qty):
        selected = self.list_model.get_selected_item()
        gfile = selected.get_attribute_object("standard::file")
        print("image path:", gfile.get_path())
        self.emit("image_selected", gfile)



