**Sharmili's Discord Bot**

This Discord bot, named "Sharmili's Discord Bot", is designed to enhance your Discord server experience by integrating a generative AI model provided by Google's GenerativeAI package. The bot allows users to interact with the AI model by invoking commands prefixed with "@".

**Features:**

1. **Welcome Message:** When a new member joins the server, the bot sends a welcoming message to the designated welcome channel.

2. **Greeting Response:** The bot responds to common greetings like "hello" and "hi" with a personalized welcome message and prompts users to use the `@HeyBot` command to engage with the AI.

3. **AI Interaction:** Users can invoke the `@HeyBot` command followed by a prompt to interact with the generative AI model. The model generates content based on the provided prompt and responds within the Discord channel.

**Dependencies:**

- `discord.py`: A Python library for interacting with the Discord API.
- `google.generativeai`: A package provided by Google for accessing generative AI models.

**Setup:**

1. Clone or download the repository containing the bot code.
2. Ensure you have Python installed on your system.
3. Install the required dependencies (`discord.py` and `google.generativeai`).
4. Set up a Discord bot application through the Discord Developer Portal and obtain the bot token.
5. Set up a Google API key for accessing the generative AI model.
6. Set environment variables for `SECRET_KEY` (Discord bot token) and `GOOGLE_API_KEY` (Google API key).
7. Customize the bot's behavior and settings as needed.
8. Run the bot script (`sharmilis_discord_bot.py`).

**Screenshots:**


**Usage:**

- Invite the bot to your Discord server using the [invite link](https://discord.gg/EpQ6Zz6H) generated from the Discord Developer Portal.
- Interact with the bot by sending messages prefixed with `@`.
- Use the `@HeyBot` command followed by a prompt to engage with the AI model.

**Contributing:**

Contributions to this Discord bot project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

**License:**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for more details.

**Author:**

This Discord bot was created by Sharmili. You can reach out to Sharmili for any inquiries or support regarding this bot.
