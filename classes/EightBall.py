import random


class EightBall:
    def get_response(self, entropy: str):
        random.seed(entropy)
        answer = random.randint(0, 2)
        answer_variation_max = len(self.__responses[answer]) - 1
        answer_variation_key = random.randint(0, answer_variation_max)

        return self.__responses[answer][answer_variation_key]

    __responses = [
        [
            # No
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ],
        [
            # Maybe
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
        ],
        [
            # Yes
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
        ],
    ]