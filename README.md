# Among_us_discord_bot
 Auto mute bot discord members based on the rules of amongUs

2 bits of information are needed
1) developer token
2) guild ID
Only one user per game is required to run the program.
The bot works by changing the users role to a role that does not have permission to speak in the current server (no direct route to muting members with a bot in discord api)
The game side of the application utilizes the pyauto gui in combination with opencv to use template matching to recognize when a player had been killed(can no longer speak to protect the identity of the imposter).

Commands = 'start', 'stop', 'help', 'bind'.

To Start:
first type bind to link users with character in the game, so that we know who is who,
then typing start start will begin the program.

help will provide usage syntax
stop will terminate the program
