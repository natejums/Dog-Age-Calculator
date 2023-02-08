# Dictionary to store breed and their life expectancy
breeds_life_expectancy = {
    "Chihuahua": 15,
    "Yorkshire Terrier": 17,
    "Poodle": 18,
    "German Shepherd": 13,
    "Golden Retriever": 12,
    "Labrador Retriever": 12,
    "Beagle": 14,
    "Bulldog": 10,
    "Dachshund": 15,
    "Shih Tzu": 16,
    "Rottweiler": 9,
    "Siberian Husky": 13,
    "Boxer": 10,
    "Doberman Pinscher": 10,
    "Bichon Frise": 14,
    "Shetland Sheepdog": 14,
    "English Springer Spaniel": 12,
    "Cocker Spaniel": 14,
    "Great Dane": 8,
    "Saint Bernard": 8,
    "Pomeranian": 16,
    "American Staffordshire Terrier": 14,
    "Bull Terrier": 13,
    "Boston Terrier": 15,
    "Lhasa Apso": 14,
    "Maltese": 14,
    "Irish Setter": 12,
    "Cavalier King Charles Spaniel": 10,
    "Weimaraner": 11,
    "Alaskan Malamute": 12,
    "Afghan Hound": 12,
    "Samoyed": 12,
    "Bernese Mountain Dog": 7,
    "Australian Shepherd": 13,
    "Dalmatian": 11,
    "Schnauzer": 14,
    "Shar Pei": 10,
    "Collie": 12,
    "Chow Chow": 8,
    "Akita": 10,
    "Basset Hound": 12,
    "English Bulldog": 9,
    "Greyhound": 10,
    "Jack Russell Terrier": 15,
    "Pug": 14,
    "Shiba Inu": 14,
    "West Highland White Terrier": 15,
    "Scottish Terrier": 14,
    "Miniature Schnauzer": 14,
    "Standard Schnauzer": 14,
    "Welsh Corgi": 12
}

# Function to calculate dog's age to human years
def dog_age_to_human_years(dog_age, breed):
    # Conversion factor
    conversion_factor = 7
    # Human age
    human_age = dog_age * conversion_factor
    # Life expectancy
    life_expectancy = breeds_life_expectancy.get(breed)

    if life_expectancy:
        print("The dog's age in human years is:", human_age)
        print("The dog's breed is:", breed)
        print("The dog's life expectancy is:", life_expectancy, "years")
    else:
        print("Breed not found in our database")

# Input from user
dog_age = int(input("Enter the dog's age in dog years: "))
breed = input("Enter the dog's breed: ")

# Call the function
dog_age_to_human_years(dog_age, breed)
