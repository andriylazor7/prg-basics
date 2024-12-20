class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0  # Initial volume level is 0
    
    def turn_on(self):
        self.is_on = True
        print("TV is turned on")
    
    def turn_off(self):
        self.is_on = False
        print("TV is turned off")
    
    def set_channel(self, new_channel_no):
        if 1 <= new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
        else:
            print("Invalid channel number")
    
    def set_channels(self, channels_list):
        self.channels = channels_list
    
    def show_channels(self):
        if not self.channels:
            print("No channels available. Please set the channel list.")
        else:
            print("Channel list:")
            for i, channel in enumerate(self.channels):
                print(f"{i+1}. {channel}")
    
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume is already at maximum level (10)")
    
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is already at minimum level (0)")
    
    def show_status(self):
        print(f"TV status: {'ON' if self.is_on else 'OFF'}")
        if self.is_on:
            if self.channels:
                print(f"Channel: {self.channel_no} ({self.channels[self.channel_no-1]})")
            else:
                print("No channels set.")
            print(f"Volume: {self.volume}")
        else:
            print("TV is OFF. No status to display.")