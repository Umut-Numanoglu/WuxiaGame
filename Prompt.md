> Hi ChatGPT, 
    we are going to write an API multiplayer based game written in Python, about chinese cultivation novels. 
    Can you describe all the steps that will be required to go from an empty project to a working game? Functionality should include:

- Players can reqister and create an account over API per POST request
- Player gets a bearer token by logging in that they can use for other commands
- The game characters have attributes like Cultivation Level, Qi Cultivation, alchemy level, artificier level, health, inspiration 
- Players can use /metitade endpoint to increase their Qi Cultivation
- Cultivation Levels are split in Steps
- First  step have substeps named in Order: Qi Condensation, Foundation Establishment,  Core Formation, Nascent Soul,  Spirit Severing, Dao Seeking
- Second Step have substeps named in order: True Immortal, Immortal Emperor, Allheaven Emperor Immortal, Allheaven Dao Immortal, Ancient Realm
- Third Step only has one substep called Dao Realm
- Fourth Step has two steps in order: Daosource and Ancestor Realm
- Players have an inventory where they can store items. An endpoint /inventory should be available to players to see the content of their inventory
- Items have different categories: weapons, cultivation tools, pills, and plants
- Players can use /delve endpoint to journey to old ruins. This endpoint will add a timer where where the player can not take other action, after the end of the timer, they have a chance to get items added to their inventory but also a chance to take a decrease in health or Qi cultivation
- Players can use /plant endpoint together with the name of an item in their inventory to remove that item from their inventory and get multiple copies of this item after a period of time
- Every action have a chance to increase inspiration stat
- When Inspiration stat gets to 100 players can use /breakthrough endpoint to get to the next level in their Cultivation Level

> Sure, I can give you a general idea of the steps that you will need to take to create your API multiplayer game in Python. Here is an overview of the steps you will need to take:
    
> Set up your development environment: First, you will need to set up your development environment by installing the necessary tools and libraries. You will need to have Python and a web framework like Flask or Django installed on your computer. You may also need to install additional libraries for handling database connections, authentication, and other features.

> Design your database schema: You will need to design a database schema to store all the necessary data for your game. This will include tables for storing player information, character attributes, inventory items, and other game data.

> Create API endpoints for player registration and authentication: You will need to create API endpoints for players to register and create an account, as well as to log in and obtain a bearer token that they can use for other commands. You may also want to create endpoints for password reset, account deletion, and other features.

> Create API endpoints for managing characters and attributes: You will need to create API endpoints for managing characters and their attributes, such as Cultivation Level, Qi Cultivation, alchemy level, artificer level, health, and inspiration. You may also need to create endpoints for leveling up and increasing character attributes, such as /metitade for increasing Qi Cultivation.

> Create API endpoints for managing inventory: You will need to create an API endpoint for managing player inventories, such as /inventory, where players can view the content of their inventory. You will also need to create endpoints for adding and removing items from the inventory, such as /plant for planting items and /delve for journeying to old ruins and potentially gaining new items.

> Implement a chance system: You will need to implement a chance system to determine the outcome of certain actions, such as the success rate of gaining items from delving in old ruins or the chance of increasing inspiration stat from taking certain actions.

> Create API endpoints for advancing to higher cultivation levels: You will need to create an API endpoint for players to advance to higher cultivation levels, such as /breakthrough, which will be available once their Inspiration stat reaches 100.

> Test your game: You will need to thoroughly test your game to make sure that all the features are working as intended and that there are no bugs or glitches.

> Deploy your game: Finally, you will need to deploy your game to a production environment so that other players can access it. You may want to use a cloud hosting service like AWS or Google Cloud to deploy your game.

> These are the general steps that you will need to take to create your API multiplayer game in Python. Good luck!