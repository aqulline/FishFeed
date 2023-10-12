from kivy.base import EventLoop
from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import utils
from kivymd.toast import toast

from database import FireBase as FB

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
Clock.max_iteration = 250

if utils.platform != 'android':
    Window.size = (412, 732)


class MainApp(MDApp):
    # app
    size_x, size_y = Window.size

    # screen
    screens = ['home']
    screens_size = NumericProperty(len(screens) - 1)
    current = StringProperty(screens[len(screens) - 1])

    def on_start(self):
        #self.add_feeds()
        #self.add_sellers()

        self.keyboard_hooker()

    def keyboard_hooker(self, *args):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        print(self.screens_size)
        if key == 27 and self.screens_size > 0:
            print(f"your were in {self.current}")
            last_screens = self.current
            self.screens.remove(last_screens)
            print(self.screens)
            self.screens_size = len(self.screens) - 1
            self.current = self.screens[len(self.screens) - 1]
            self.screen_capture(self.current)
            return True
        elif key == 27 and self.screens_size == 0:
            toast('Press Home button!')
            return True



    """
    
            FEEDS FUNCTION
    
    """

    def add_feeds(self):
        data = FB.company_products(FB(), "0715700411")
        #self.root.ids.feeds.data= {}
        for x, y in data.items():
            self.root.ids.feeds.data.append(
                {
                    "viewclass": "Details",
                    "title": y["product_name"],
                    "image": y["image_url"],
                    "description": y["product_description"],
                    "id": x
                }
            )

    """
            END FEEDS FUNCTION
            
    """
    """

               SHOP FUNCTION

       """

    def add_sellers(self):
        data = FB.get_sellers(FB())

        for x, y in data.items():
            self.root.ids.sellers.data.append(
                {
                    "viewclass": "Shops",
                    "retailer_name": y["name"],
                    "retailer_image": f"https://storage.googleapis.com/farmzon-abdcb.appspot.com/Letters/{y['name'][0].capitalize()}",
                    "description":y["email"],
                    "phone": x,
                    "id": x
                }
            )

    """
            END SHOP FUNCTION

    """




















    def screen_capture(self, screen):
        sm = self.root
        sm.current = screen
        if screen in self.screens:
            pass
        else:
            self.screens.append(screen)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        print(f'size {self.screens_size}')
        print(f'current screen {screen}')

    def screen_leave(self):
        print(f"your were in {self.current}")
        last_screens = self.current
        self.screens.remove(last_screens)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        self.screen_capture(self.current)

    def build(self):
        self.theme_cls.material_style = "M3"


MainApp().run()
