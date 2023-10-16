from kivy.base import EventLoop
from kivy.properties import NumericProperty, StringProperty, DictProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import utils
from kivymd.toast import toast
import ssl

from database import FireBase as FB

ssl._create_default_https_context = ssl._create_unverified_context

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
        # self.add_feeds()
        self.add_sellers()

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
        self.root.ids.feeds.data= {}
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

    seller_data = DictProperty({})
    company_name = StringProperty("")
    company_logo = StringProperty('')
    company_followers = StringProperty("")
    company_bio = StringProperty("")


    def add_sellers(self):
        self.seller_data = FB.get_sellers(FB())

        for x, y in self.seller_data.items():
            self.root.ids.sellers.data.append(
                {
                    "viewclass": "Shops",
                    "retailer_name": y["customer_name"],
                    "retailer_image": y["logo"],
                    "description": y["bio"],
                    "phone": x,
                    "id": x
                }
            )

    def get_specific(self, phone):
        print("get specific")
        self.company_name = self.seller_data[phone]["customer_name"]
        self.company_logo = self.seller_data[phone]["logo"]
        self.company_followers = self.seller_data[phone]["followers"]
        self.company_bio = self.seller_data[phone]["bio"]
        self.screen_capture("compan")

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
