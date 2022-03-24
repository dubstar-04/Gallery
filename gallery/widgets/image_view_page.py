
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/Gallery/ui/image_view_page.ui')
class ImageViewPage(Gtk.Box):

    __gtype_name__ = 'ImageViewPage'

    display_image = Gtk.Template.Child()
    #gesture_zoom = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        zoom_gesture = Gtk.GestureZoom.new()
        zoom_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        zoom_gesture.connect("scale-changed", self.zoomed, self.display_image)
        self.display_image.add_controller(zoom_gesture)

        press_gesture = Gtk.GestureLongPress.new()
        press_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        press_gesture.connect("pressed", self.pressed, self.display_image)
        self.display_image.add_controller(press_gesture)

        swipe_gesture = Gtk.GestureSwipe.new()
        swipe_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        swipe_gesture.connect("swipe", self.swiped, self.display_image)
        self.display_image.add_controller(swipe_gesture)

    def set_image(self, image_path):
        self.display_image.set_from_file(image_path)
        self.display_image.set_pixel_size(500)

    def zoomed(self, sender, three, four, five):
        print("scale changed")

    def swiped(self, sender, three, four, five):
        print("swiped")

    def pressed(self, sender, two, three, four):
        print("pressed")
        print(two, three, four)
