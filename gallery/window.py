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
#from .library import *
from gallery.widgets import image_widget, image_view_page, gallery_view_page

@Gtk.Template(resource_path='/org/gnome/Gallery/ui/window.cmb.ui')
class GalleryWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'GalleryWindow'

    # label = Gtk.Template.Child()

    page_stack = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # define pages
        self.gallery_page = gallery_view_page.GalleryViewPage()
        self.image_page = image_view_page.ImageViewPage()

        self.image_page.set_image('/home/sandal/Pictures/toplevel.png')


        #self.page_stack.add_named(self.gallery_page, 'gallery_view_page')
        self.page_stack.add_child(self.image_page)
        #self.page_stack.add_named(self.image_page, 'image_view_page')
        #self.page_stack.set_visible_child_name('image_view_page')
        #self.page_stack.add_titled(self.gallery_page, 'gallery_view_page', 'Images')
        #self.page_stack.set_visible_child_name('gallery_view_page')
        print(self.page_stack.get_visible_child())



class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'gallery'
        self.props.version = "0.1.0"
        self.props.authors = ['Daniel Wood']
        self.props.copyright = '(C) 2021 Daniel Wood'
        self.props.logo_icon_name = 'org.gnome.Gallery'
        self.set_transient_for(parent)
