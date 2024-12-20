import tv



def main():
  my_tv = tv.TV()
  my_tv.show_status()  # Should display the TV is OFF

  # Turn on the TV
  my_tv.turn_on()

  # Set some channels
  my_tv.set_channels(["BBC", "Discovery", "National Geographic", "CNN"])
  my_tv.show_channels()

  # Change the channel
  my_tv.set_channel(2)
  my_tv.show_status()

  # Adjust the volume
  my_tv.increase_volume()
  my_tv.increase_volume()
  my_tv.increase_volume()
  my_tv.show_status()  # Should show volume level 3

  # Decrease the volume
  my_tv.decrease_volume()
  my_tv.decrease_volume()
  my_tv.show_status()  # Should show volume level 1

  # Try to exceed the volume limits
  my_tv.decrease_volume()
  my_tv.decrease_volume()  # Minimum limit reached
  my_tv.increase_volume()
  for _ in range(12):  # Attempt to increase volume beyond max limit
      my_tv.increase_volume()
  my_tv.show_status()
  
  
if __name__ == "__main__":
  main()