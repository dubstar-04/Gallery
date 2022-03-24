
from gi.repository import Gtk,  Gdk, GdkPixbuf
import cairo

@Gtk.Template(resource_path='/org/gnome/Gallery/ui/image_view_page.ui')
class ImageViewPage(Gtk.Box):

    __gtype_name__ = 'ImageViewPage'

    display_image = Gtk.Template.Child()
    drawing_area = Gtk.Template.Child()
    #gesture_zoom = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        # setup tranlation
        self.off_x = 0
        self.off_y = 0
        self.scale = 1

        # setup gestures
        zoom_gesture = Gtk.GestureZoom.new()
        zoom_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        zoom_gesture.connect("scale-changed", self.zoomed)
        self.drawing_area.add_controller(zoom_gesture)

        press_gesture = Gtk.GestureLongPress.new()
        press_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        press_gesture.connect("pressed", self.pressed)
        self.drawing_area.add_controller(press_gesture)

        swipe_gesture = Gtk.GestureSwipe.new()
        swipe_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        #swipe_gesture.connect("swipe", self.swiped)
        self.drawing_area.add_controller(swipe_gesture)

        drag_gesture = Gtk.GestureDrag.new()
        drag_gesture.set_propagation_phase(Gtk.PropagationPhase.BUBBLE)
        drag_gesture.connect("drag-update", self.drag)
        drag_gesture.connect("drag-end", self.drag_end)
        self.drawing_area.add_controller(drag_gesture)

        # setup mouse input handling
        click_gesture = Gtk.GestureClick.new()
        click_gesture.set_propagation_phase(Gtk.PropagationPhase.CAPTURE)
        click_gesture.connect("pressed", self.click)
        self.drawing_area.add_controller(click_gesture)

        scroll_event = Gtk.EventControllerScroll.new(Gtk.EventControllerScrollFlags.VERTICAL)
        #click_gesture.set_propagation_phase(Gtk.PropagationPhase.CAPTURE)
        scroll_event.connect("scroll", self.scroll)
        self.drawing_area.add_controller(scroll_event)

        self.drawing_area.set_draw_func(self.on_draw)

    def set_image(self, image_path):
        self.reset()
        self.image = GdkPixbuf.Pixbuf.new_from_file(image_path)

    def zoomed(self, sender, three, four):
        print("scale changed")

    def swiped(self, sender, three, four):
        print("swiped")

    def drag(self, sender, off_x, off_y):
        print("dragged")
        self.off_x = off_x
        self.off_y = off_y
        self.drawing_area.queue_draw()

    def drag_end(self, sender, off_x, off_y):
        print("drag_end")
        print("offset:", off_x, off_y)

    def pressed(self, sender, two, three):
        print("pressed")
        print(two, three)

    def click(self, sender, count, x, y):
        print("mouse clicked - count:", count)
        if count > 1:
            self.reset()

    def scroll(self, sender, horizonal, vertical):
        print("scroll:", horizonal, vertical)
        self.scale += vertical * 0.1
        print("scroll scale:", self.scale)
        self.drawing_area.queue_draw()

    def reset(self):
        print("reset")
        self.off_x = 0
        self.off_y = 0
        self.scale = 1
        self.drawing_area.queue_draw()

    def get_scale(self):

        area_rect = self.drawing_area.get_allocation()
        img_width = float(self.image.get_width())
        img_height = float(self.image.get_height())
        width_ratio = area_rect.width / img_width
        height_ratio = area_rect.height / img_height

        scale = min(width_ratio, height_ratio)

        off_x = (area_rect.width - round(img_width * scale)) * 0.5
        off_y = (area_rect.height - round(img_height * scale)) * 0.5

        return scale, off_x, off_y


    def on_draw(self, sender, context, four, five):
        print("ondraw")

        scale, off_x, off_y = self.get_scale()
        context.save()
        context.translate(self.off_x, self.off_y)

        if scale:
            context.translate(off_x, off_y)
            context.scale(scale, scale)

        if self.scale:
            context.scale(self.scale, self.scale)

        Gdk.cairo_set_source_pixbuf(context, self.image, 0, 0)

        context.paint()
        context.restore()
