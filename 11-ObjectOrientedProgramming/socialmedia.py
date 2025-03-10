class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
        
    def display_timeline(self):
        print('Username:', self.username)
        print('Posts\n')
        for i, post in enumerate(self.posts):
            print(f'{i+1}. {post}')
            
            
            
            
            
            
def main():
    profile1 = SocialMediaProfile('JohnDoe')
    
    profile1.add_post('Hello, world!')
    profile1.add_post('Had a great day at the park!')
    profile1.add_post('What`s up, Natalie? How are you?')
    
    profile1.display_timeline()
    
    
    

if __name__ == "__main__":
    main()
    
        
            
        

