import  framework, secret
from framework import discord



############################################################################################
#                               GUILD MESSAGES DEFINITION                                  #
############################################################################################

# File object representing file that will be sent
l_file = framework.FILE("./Examples/main_send_file.py")

guilds = [
    framework.USER(
        user_id=123456789,                                 # ID of server (guild) or a discord.Guild object
        messages=[                                  # List MESSAGE objects
            framework.DirectMESSAGE(
                              start_period=None,            # If None, messages will be send on a fixed period (end period)
                              end_period=15,                # If start_period is None, it dictates the fixed sending period,
                                                            # If start period is defined, it dictates the maximum limit of randomized period
                              data=l_file,                  # Data you want to sent to the function (Can be of types : str, embed, file, list of types to the left
                                                            # or function that returns any of above types(or returns None if you don't have any data to send yet), 
                                                            # where if you pass a function you need to use the framework.FUNCTION decorator on top of it ).
                              mode="send",                  # "send" will send a new message every time, "edit" will edit the previous message, "clear-send" will delete
                                                            # the previous message and then send a new one
                              start_now=True                # Start sending now (True) or wait until period
                              ),  
        ],
        logging=True                                   ## Generate file log of sent messages (and failed attempts) for this user
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
    