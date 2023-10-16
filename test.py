"""MDScrollView:
			            #pos_hint:{"center_x":.5,"top":.9}
			            MDBoxLayout:
			                adaptive_height:True
			                size_hint_y:None
			                orientation:"vertical"
			                spacing:dp(15)
			                Details:
			                    VideoPlayer:
			                        source:"baki.mkv"
		                        FloatLayout:
								    MDLabel:
								        text:"Fish NoIcE"
								        halign:"left"
								        font_size:"23sp"
								        pos_hint:{"center_x":.55, "center_y":.8}
								        height: self.texture_size[1]
                                        width: self.texture_size[1]
								    MDLabel:
								        text:"Fish NoIcE"
								        halign:"left"
								        font_size:"14sp"
								        pos_hint:{"center_x":.6, "center_y":.6}
								        height: self.texture_size[1]
                                        width: self.texture_size[1]
					        Details:
					            AsyncImage:
							        source:"https://www.essence.com/wp-content/uploads/2023/08/LH_1-Cropped-scaled.jpg?width=1280"
							        pos_hint:{"center_x":.5, "center_y":.8}
							        #size:dp(300), dp(300)
							        size_hint:2, 2

							    FloatLayout:
								    MDLabel:
								        text:"Fish NoIcE"
								        halign:"left"
								        font_size:"23sp"
								        pos_hint:{"center_x":.55, "center_y":.8}
								    MDLabel:
								        text:"Fish NoIcE"
								        halign:"left"
								        font_size:"14sp"
								        pos_hint:{"center_x":.6, "center_y":.6}
								        """
