
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
