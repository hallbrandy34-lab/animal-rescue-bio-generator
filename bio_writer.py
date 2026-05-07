# AI Adoption Bio Generator
# Simple starter project for animal rescue work

def generate_bio(name, species, traits):
    traits_text = ", ".join(traits)
    bio = (
        f"Meet {name}! This sweet {species} is {traits_text}. "
        f"{name} is looking for a loving home where they can feel safe, cared for, "
        f"and finally get the happy ending they deserve."
    )
    return bio

# Example usage:
pet_name = "Daisy"
pet_species = "dog"
pet_traits = ["gentle", "playful", "great with kids"]

print(generate_bio(pet_name, pet_species, pet_traits))
