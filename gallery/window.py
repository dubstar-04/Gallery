# window.py
#
# Copyright 2022 Daniel Wood
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Gio
from .library import *
from gallery.widgets import image_widget, image_view_page

#import os
#print('dirname:     ', os.path.abspath(__file__))

class factory(Gtk.ListItemFactory):

    def __init__(self):
        super().__init__()


@Gtk.Template(resource_path='/org/gnome/Gallery/ui/window.cmb.ui')
class GalleryWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'GalleryWindow'

    label = Gtk.Template.Child()
    grid_layout = Gtk.Template.Child()
    page_stack = Gtk.Template.Child()

    #test_image = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.model_items = Gtk.DirectoryList()
        self.model_items.set_file(Gio.File.new_for_path('/home/sandal/Pictures/'))
        self.list_model = Gtk.SingleSelection(model=self.model_items)
        self.grid_layout.set_model(self.list_model)

        self.factory = Gtk.SignalListItemFactory()
        self.factory.connect('setup', self.on_factory_setup)
        self.factory.connect('bind', self.on_factory_bind)
        self.factory.connect('unbind', self.on_factory_unbind)
        self.factory.connect('teardown', self.on_factory_teardown)

        self.grid_layout.set_factory(self.factory)

        self.image_page = image_view_page.ImageViewPage()
        #self.page_stack.add_child(self.image_page)

    def on_factory_setup(self, widget, item: Gtk.ListItem):
        iw = Gtk.Image()
        iw.set_pixel_size(200)
        item.set_child(iw)

    def on_factory_bind(self, widget: Gtk.ListView, item: Gtk.ListItem):
        data = item.get_item()
        gfile = data.get_attribute_object("standard::file")
        image = item.get_child()
        image.set_from_file(gfile.get_path())

    def on_factory_unbind(self, widget, item: Gtk.ListItem):
        pass

    def on_factory_teardown(self, widget, item: Gtk.ListItem):
        pass

class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'gallery'
        self.props.version = "0.1.0"
        self.props.authors = ['Daniel Wood']
        self.props.copyright = '(C) 2021 Daniel Wood'
        self.props.logo_icon_name = 'org.gnome.Gallery'
        self.set_transient_for(parent)
