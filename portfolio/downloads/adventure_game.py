"""
Author: Branson Hall
W05-06 Prove

Purpose: Write a text-based adventure game using 'if' and 'else' statements
"""

character = input("\nChoose your character: CRIMINAL or CIVILIAN\n")
is_criminal = False
is_civilian = False

if character.lower() == "criminal":
    is_criminal = True
    is_civilian = False
elif character.lower() == "civilian":
    is_criminal = False
    is_civilian = True
else:
    print("Invalid response: Please start over and try again.")

if is_civilian: # Civilian character
    print("\nYou're innocent. Don't get arrested.")
    choice1 = input("\nYou wake up in the middle of the night groggy and tired but you hear a strange, faint noise coming from somewhere outside your bedroom. \nDo you want to INVESTIGATE the noise or go back to SLEEP? ")
    if choice1.lower() == "investigate":
        choice2 = input("\nAs you quietly exit your bedroom and tiptoe down the hallway, the noise gets progressively louder. It sounds like someone is rummaging through your home. \n\
As you peek around the corner, your suspicion is confirmed. You find two men in FBI attire destroying the place. Most likely dirty agents. You were warned they were \n\
coming for you. But why? You're just another nobody trying to catch up on bills. You've noticed their tinted, black SUV's stalking you from a distance the last few days. \n\
It's time for this end. \nDo you want to RUN from the agents, HIDE, or CONFRONT them? ")
        if choice2.lower() == "run":
            choice3 = input("\nYou sneak back to your bedroom and very quietly shut the door so they won't hear you when you crawl out the window. As you make your way through the window, \n\
your foot catches on something causing you to trip and loudly fall into the brush. You immediately hear distant yelling and running as the FBI agents come after you. \n\
Climbing back to your feet, you run away as fast as you can. With their specialized training, you know the agents will eventually catch up to you unless you do \n\
something fast. Then you notice someone climbing out of their car with a bag of clothes. \nDo you want to HIJACK the car or DISGUISE yourself with the clothes? ")
            if choice3.lower() == "hijack":
                print("\nVeins pumping with adrenaline, you forcefully steal the keys and climb into the driver's seat of the car. Fumbling to start the car, you notice the FBI agents \n\
sprinting toward you, getting closer with every passing second. You throw the car into gear and quickly accelerate but it's not long until you see the red and blue \n\
lights of several poice cars and one dark SUV with tinted windows shining in the rearview mirror. As you rack your mind for a way out of this mess, you barely notice \n\
when a police car performs a pit manuever on your car. There's nothing you can do as the swarm of officers arrest you. \nGAME OVER")
            elif choice3.lower() == "disguise":
                print("\nVeins pumping with adrenaline, you steal the bag of clothes and ignore the yelling that ensues as your victim directs the agents in your direction. You quickly \n\
sneak into a port-a-john outside a small gas station, change into the clothes from the bag, and shove the bag and your old clothes down the port-a-john's dark abyss. \n\
You can hear the agents devising a search plan outside the plastic walls. The agents fail to recognize you as you slip outside and make for a brisk walk out of sight \n\
of the two men searching for you. \nWELL DONE, YOU ESCAPED")
            else:
                print("\nInvalid response: Please start over and try again.")
        elif choice2.lower() == "hide":
            choice3 = input("\nYou quietly sneak back into your room, grab your baseball bat, and hide in your closet. It isn't long before the agents begin searching your bedroom. You \n\
hear them quietly conversing but you can't make out what they're saying through the closet door. You put your ear to the door to hear them better but just at that moment, \n\
the agents throw it open with guns drawn. They command you to drop the bat and lay on the ground. \nDo you want to RESIST or COMPLY with their orders? ")
            if choice3.lower() == "resist":
                print("\nThere's no way you're going to jail. You swing your bat at the agent nearest to you, striking him in the shoulder. He instantly drops his gun and falls to the \n\
floor clutching his shoulder in agony. You make to grab the gun on the floor but the second agent rapidly fires three rounds. One tears into your thigh, another through \n\
the hand that was reaching for the gun, and third round missed you altogether. You drop to floor in pain as the uninjured agent secures all weapons. He places you under \n\
arrest before tending to his injured partner. \nGAME OVER")
            elif choice3.lower() == "comply":
                print("\nYou place down your bat and lay on ground following all instructions given to you as the agents place you under arrest. \nGAME OVER")
            else:
                print("\nInvalid response: Please start over and try again.")
        elif choice2.lower() == "confront":
            choice3 = input("\nWho do they think they are to pick on an innocent person? What did you ever do to them? You are a law-abiding citizen. What right do they have to be in \n\
your home? In a rage you stomp around the corner yelling as you give the agents a piece of your mind. The agents jump in surprise but are quick to pull out their weapons \n\
and order you to get on the ground. \nDo you want to IGNORE their commands or COMPLY? ")
            if choice3.lower() == "ignore":
                print("\nYou continue yelling at them but it isn't long before the agents wrestle you to the ground and force you into handcuffs. \nGAME OVER")
            elif choice3.lower() == "comply":
                print("\nYou follow their orders to get on the ground and the agents are quick to place you in handcuffs. \nGAME OVER")
            else:
                print("\nInvalid response: Please start over and try again.")
        else:
            print("\nInvalid response: Please start over and try again.")
    elif choice1.lower() == "sleep":
        choice2 = input("\nIt's probably just a breeze or something else not to be worried about. You lay down again and let yourself fall back to sleep. It isn't long before you \n\
wake to a man's voice outside your room ordering you by name to open your door with your hands raised. \nDo you want to FOLLOW these orders, or ESCAPE through your window? ")
        if choice2.lower() == "follow":
            choice3 = input("\nConfused, you open the door and raise your hands above your head. Standing outside your door you see two men in FBI uniforms with their guns drawn. You \n\
immediately remember the letter you received in the mail. You thought it was a sick joke. Whoever sent that letter tried to warn you that corrupt agents were coming for you. \n\
It doesn't make any sense. What would they gain from you? You're nobody to them. The dirty agents order you to lie on the ground. \nDo you want to RESIST or COMPLY? ")
            if choice3.lower() == "resist":
                print("\nAs one of the agents steps toward you, you swing your fist, connecting with his jaw. He immediately buckles and falls but before he can hit the ground, the \n\
other agent is on top of you, locking your wrists into handcuffs. \nGAME OVER")
            elif choice3.lower() == "comply":
                print("\nYou follow the orders from the agents as they lock you into handcuffs. \nGAME OVER")
            else:
                print("\nInvalid response: Please start over and try again.")
        elif choice2.lower() == "escape":
            choice3 = input("\nYou rush through your window and run for your life as you hear the agents some distance behind you. You eventually break out of their line of sight and \n\
sneak through an unlocked door into soomeone's home. When you turn around to face the interior of the home, you find it's attractive owner standing there, threatening to \n\
call the police. \nDo you want to BRIBE them or FLIRT? ")
            if choice3.lower() == "bribe":
                print("\nYou try explaining your situation but the stranger isn't sympathetic so you dig through your pockets for anything of any value. You find a single twenty \n\
dollar bill and bribe the owner with it. Taking the money into their hands, the stranger scoffs, pockets the money and screams. The agents are quick to rush through the \n\
door and arrest you. \nGAME OVER")
            elif choice3.lower() == "flirt":
                print("\nYou stand confidently and to your surprise, your pickup line actually worked! The owner invites you to stay for a brunch date which you gladly accept. \nWELL DONE, YOU ESCAPED")
            else:
                print("\nInvalid response: Please start over and try again.")
        else:
            print("\nInvalid response: Please start over and try again.")
    else:
        print("\nInvalid response: Please start over and try again.")
elif is_criminal: # Criminal character
    print("\nYou're on the most wanted list. Don't get caught.")
    choice1 = input("\nYou wake up in the middle of the night groggy and tired but you hear a strange, faint noise coming from somewhere outside your bedroom. \nDo you want to INVESTIGATE the noise or go back to SLEEP? ")
    if choice1.lower() == "investigate":
        choice2 = input("\nAs you quietly exit your bedroom and tiptoe down the hallway, the noise gets progressively louder. It sounds like someone is rummaging through the home. \n\
As you peek around the corner, your suspicion is confirmed. You find two men in FBI attire destroying the place. How did they find you? This is the first night you've \n\
spent in this home. You've been hiding perfectly. You never leave any evidence of your whereabouts. It's time for this end. \nDo you want to RUN from the agents or ATTACK them? ")
        if choice2.lower() == "run":
            choice3 = input("\nYou sneak back to the bedroom and very quietly shut the door so they won't hear you when you crawl out the window. As you make your way through the window, \n\
your foot catches on something causing you to trip and loudly fall into the brush. You immediately hear distant yelling and running as the FBI agents come after you. \n\
Climbing back to your feet, you run away as fast as you can. With their specialized training, you know the agents will eventually catch up to you unless you do \n\
something fast. Then you notice someone climbing out of their car with a bag of clothes. \nDo you want to HIJACK the car or DISGUISE yourself with the clothes? ")
            if choice3.lower() == "hijack":
                print("\nVeins pumping with adrenaline, you forcefully steal the keys and climb into the driver's seat of the car. Fumbling to start the car, you notice the FBI agents \n\
sprinting toward you, getting closer with every passing second. You throw the car into gear and quickly accelerate but it's not long until you see the red and blue lights \n\
of a police car in the distance through the rearview mirror. This isn't your first pursuit. After a short pursuit, you lose the cop before more can join in and cruise to \n\
freedom. \nWELL DONE, YOU ESCAPED")
            elif choice3.lower() == "disguise":
                print("\nVeins pumping with adrenaline, you steal the bag of clothes and ignore the yelling that ensues as your victim directs the agents in your direction. You quickly \n\
sneak into a port-a-john outside a small gas station, change into the clothes from the bag, and shove the bag and your old clothes down the port-a-john's dark abyss. \n\
You can hear the agents devising a search plan outside the plastic walls. The agents immediately recognize you as you slip out of your hiding place and arrest you. \nGAME OVER")
            else:
                print("\nInvalid response: Please start over and try again.")
        elif choice2.lower() == "attack":
            choice3 = input("\nYou quietly sneak back into the bedroom, grab a baseball bat, and charge the agents. They don't stand a chance against you. It's a short fight before \n\
you're standing over their unconscious bodies. \nDo you want to FLEE or SLEEP? ")
            if choice3.lower() == "flee":
                print("\nYou quickly flee the home to find a new place to hide far away from here. \nWELL DONE, YOU ESCAPED")
            elif choice3.lower() == "sleep":
                print("\nYou handcuff the agent's wrists to the pipe underneath the kitchen sink and lay down on a couch to sleep some more. Before you wake up, the agents escape their \n\
trap and arrest you. \nGAME OVER")
            else:
                print("\nInvalid response: Please start over and try again.")
        else:
            print("\nInvalid response: Please start over and try again.")
    elif choice1.lower() == "sleep":
        choice2 = input("\nIt's probably just the wind. Nothing to be worried about. You lay down again and let yourself fall back to sleep. It isn't long before you wake to a man's \n\
voice outside your room ordering you by name to open your door with your hands raised. \nDo you want to INVESTIGATE, or ESCAPE through your window? ")
        if choice2.lower() == "investigate":
            choice3 = input("\nConfused, you open the door and standing outside your door are two men in FBI uniforms with their guns drawn. They order you to get on the ground. \nDo you want to RESIST or COMPLY? ")
            if choice3.lower() == "resist":
                print("\nAs one of the agents steps toward you, you swing your fist, connecting with his jaw. He immediately buckles and falls but before he can hit the ground, the \n\
other agent is on top of you, locking your wrists into handcuffs. \nGAME OVER")
            elif choice3.lower() == "comply":
                print("\nYou follow the orders from the agents as they arrest you. \nGAME OVER")
            else:
                print("\nInvalid response: Please start over and try again.")
        elif choice2.lower() == "escape":
            choice3 = input("\nYou rush through your window and run for your life as you hear the agents some distance behind you. You eventually break out of their line of sight \n\
and sneak through an unlocked door into soomeone's home. When you turn around to face the interior of the home, you find it's attractive owner standing there, threatening \n\
to call the police. \nDo you want to BRIBE them or FLIRT? ")
            if choice3.lower() == "bribe":
                print("\nYou try telling some fake story but the stranger isn't sympathetic so you dig through your pockets for anything of any value. You find a single twenty dollar bill \n\
and bribe the owner with it. Taking the money into their hands, the stranger scoffs, pockets the money and screams. Afraid the agents will hear the screaming, you \n\
tackle them to the ground and clamp their mouth shut but the agents are quick to rush through the door and arrest you. \nGAME OVER")
            elif choice3.lower() == "flirt":
                print("\nYou stand confidently and to your surprise, your pickup line actually worked! The owner invites you to stay for a brunch date which you gladly accept. \nWELL DONE, YOU ESCAPED")
            else:
                print("\nInvalid response: Please start over and try again.")
        else:
            print("\nInvalid response: Please start over and try again.")
    else:
        print("\nInvalid response: Please start over and try again.")
else:
    print("\nCharacter unknown. Please start over and try again.")