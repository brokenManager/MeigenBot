import discord

from IroIroBot.Command.CommandParameters import CommandParameters
from IroIroBot.Command.Meigen.MeigenSubcommandBase import MeigenSubcommandBase
from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class PrintSubcommand(MeigenSubcommandBase):
    DEFAULT_NUM = 5

    COMMAND = "print"
    TEMPLATE = f"{{prefix}}{{command}} {COMMAND} [表示数={DEFAULT_NUM}]"
    HELP = f"{TEMPLATE}\n" +\
            "   MEIGENを表示するよ！\n"


    async def run(self, params: CommandParameters):
        words = params.args.split()
        if len(words) < 1:
            await params.send(
                MeigenHolder().print(PrintSubcommand.DEFAULT_NUM)
            )
            return

        if not words[0].isdecimal():
            await params.send(
                "```\n" +\
                "†キレた†\n" +\
                "   まともな数字入力しろよカス\n" +\
                "```"
            )
            return

        await params.send(
            MeigenHolder().print(int(words[0]))
        )