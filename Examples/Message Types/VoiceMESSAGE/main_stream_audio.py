import  framework, secret
from framework import discord


some_audio_file = framework.AUDIO("VoiceMessage.mp3")

guilds = [
    framework.GUILD(
        snowflake=123456789,                                    # ID of server (guild) or a discord.Guild object or a discord.Guild object
        messages=[                                      # List MESSAGE objects 
            framework.VoiceMESSAGE(
                              start_period=None,                # If None, messages will be send on a fixed period (end period)
                              end_period=15,                    # If start_period is None, it dictates the fixed sending period,
                                                                # If start period is defined, it dictates the maximum limit of randomized period
                              data=some_audio_file,             # Data parameter
                              channels=[123456789],             # List of channel ids or discord.VoiceChannel objects
                              volume=50,                        # The volume (0-100%) at which to play the audio
                              start_now=True                    # Start sending now (True) or wait until period
                              ),  
        ],
        logging=True           ## Generate file log of sent messages (and failed attempts) for this server 
    )
]

############################################################################################

if __name__ == "__main__":
    framework.run(  token=secret.C_TOKEN,               # MANDATORY
                    intents=discord.Intents.default(),  # OPTIONAL (see https://docs.pycord.dev/en/master/intents.html)
                    server_list=guilds,                 # MANDATORY
                    is_user=False,                      # OPTIONAL
                    user_callback=None,                 # OPTIONAL
                    server_log_output="History",        # OPTIONAL
                    debug=True)                         # OPTIONAL