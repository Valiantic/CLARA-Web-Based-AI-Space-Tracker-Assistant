
import random
from engine.command import speak 

# >> FOOD RECOMMENDATION <<
def Foodrecommendation(query):
    
    #Collection of food ideas 
    foodideas = ["I just got the best thing for you. since the weather is kinda hot these days. i would recommend" + 
                 " halo halo with it's various ingredients like sweetened beans, fruits, jellies, leche flan (custard)," +
                 "and evaporated milk. that will surely cool down your hot day.", 
                 
                 "How about trying biko?. with its sticky rice cake is made with glutinous rice, coconut milk, and brown sugar." + 
                 "It's a popular dessert with a chewy texture and sweet flavor.", 
                 
                 "Longanissa is a filipino sausage. typically made from pork and seasoned with garlic, pepper, and other spices." +
                 "It's often served for breakfast, fried and paired with eggs and rice.",
                 
                 "I would personally recommend my creator's favorite lunch food, Sisig. This sizzling dish is made from chopped" + 
                 "pork face and ears, seasoned with chilies, onions, and calamansi" +
                 "It's often served on a hot plate and eaten with rice or tortillas.",
                 
                 "Try pancit, filipinoes best noodle dish! pancit canton (made with egg noodles), and pancit palabok" +
                 "(made with rice noodles in a thick shrimp sauce). They're typically stir-fried with meat, seafood," +
                 "and vegetables."]

    # # Print the first element (foodideas)
    
    # # Shuffle the foodideas randomly
    random_foodideas = random.choice(foodideas)
    
     # # Print the first element (foodideas)
    print(random_foodideas)
    speak(random_foodideas)

# >> BOOK RECOMMENDATION <<
def Bookdrecommenadtion(query):
    
        #Collection of book ideas 
        bookideas = ["As a Artificial Intelligence made by a filipino. I would be proud to recommend Noli Me Tangere" + 
                     "(Touch me not) by Jose Rizal. This is a classic novel considered the national epic of the Philippines." + 
                     "It is a scathing social commentary on the Spanish colonial rule in the Philippines during the 19th century.",
                     
                     "The Woman Who Had Two Navels by Nick Joaquin: This novel is a historical fiction that explores the life of Gabriela Silang," +
                     "a Filipina revolutionary leader who fought against the Spanish colonial rule alongside her husband Diego Silang.",
                     
                     "Po-on by F. Sionil Jose: This novel is the first book in the Rosales saga, a five-novel series that chronicles the lives " + 
                     "of the Rosales family over several generations in the Philippines. ",
                     
                     "Smaller and Smaller Circles by F.H. Batacan: This is a crime novel set in contemporary Manila. It follows the story of two" + 
                     "detectives investigating the serial murders of children.",
                     
                     "Ilustrado by Miguel Syjuco: This historical novel tells the story of Crispin Salvador, a young Filipino man who travels" +
                     "to the United States in the early 20th century to pursue his education. He grapples with issues of identity, colonialism, "
                     "and the search for belonging."]
        
        random_bookideas = random.choice(bookideas)
            
        print(random_bookideas)
        speak(random_bookideas)
        
# >> APPRECIATION <<
def Appreciation(query):
    
        #Collection of appreciation words 
        appreciations = ["Thank you for having the courage to tell me. I appreciate it so much. Life could be pretty " +
                      "heavy if you carry it all at once. try to take a rest and release those things that brings burden to you.",
                      
                      "Your body is wise to tell you it needs a break. Listen to it and recharge, you'll be back at your best soon.",
                      
                      "Don't worry about slowing down today. Sometimes, even superheroes need to nap to save the world tomorrow.",
                      
                      "The world will still be here when you wake up feeling refreshed. Take care of yourself, and the rest can wait.",
                      
                      "You're not lazy for being tired, you're human. Listen to your body and prioritize rest, it's the most productive thing you can do right now."
                      ]
        
        random_appreciations = random.choice(appreciations)
            
        print(random_appreciations)
        speak(random_appreciations)
        
# >> Space trivia <<
def Spacetrivia(query):
    
        #Collection of appreciation words 
        aboutspace = ["Outer space is virtually silent because sound waves require a medium, like air or water, " + 
                      "to travel. The near-vacuum of space lacks the necessary density for sound to propagate.",
                      
                      "While the first human steps on the Moon were made in 1969, the lack of atmosphere and " +
                      "moisture means these footprints are expected to remain largely undisturbed for millions of " +
                      "years.",
                      
                      "Our Sun, despite being a massive star, could actually fit over 1 million Earths within its volume. " +
                      "This showcases the immense scale of celestial objects.",
                      
                      "The twinkling of stars we see at night is not due to the stars themselves, but rather the Earth's atmosphere " +
                      "causing distortions in the starlight as it travels through it. In space, stars would appear to shine steadily.",
                      
                      "When you look at distant stars and galaxies, you're essentially seeing them in the past. Since light travels " + 
                      "at a finite speed, the farther an object is, the longer it takes its light to reach us, offering a glimpse into the " +
                      "universe's vast history."
                      ]
        
        random_aboutspace = random.choice(aboutspace)
            
        print(random_aboutspace)
        speak(random_aboutspace)
        
        


        
        

