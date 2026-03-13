
import random

subjects=[
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Ricksaw Driver from Delhi"
]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"

]

places_or_things=[
    "at red Fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

#start headline generation

while True :
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline=f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n"+headline)

    user_input=input("\n Do you want another headline ? (yes/no)").strip().lower()
    if user_input=="no":
        break

print("\nThanks for using the fake news headline generator. Have a fun day")

