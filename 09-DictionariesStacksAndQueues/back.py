import queue

# Create a visited_websites stack
visited_websites = queue.LifoQueue()

# Some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        if visited_websites.empty():
            print("No more websites to go back to.")
            break
        else:
            website = visited_websites.get()
            print('<-- Going back to a previously visited website')

    elif website != "":
        visited_websites.put(website)

    print('You are currently viewing:', website)
    print()
    
