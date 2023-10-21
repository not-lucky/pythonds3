from discord import SyncWebhook
import multiprocessing

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"

# S = """
# When it comes to writing content, two factors are crucial, "perplexity" and "burstiness." Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness.
# """

# U = '\nMake the following extremely precise and shorter (I am trying to make short notes):\n'
try:
    U += ''
except NameError:
    U = ''

U += """
If you have to develop a yen large project for at least 8 to 10 years and
there is the requirement of risk analysis in every phase, which
development model is best suitable. Explain the selected model with its
advantages and disadvantages.
"""

U = U.strip() + "\n"


def discord_message(content: str) -> None:
    # to send content to my discord channel
    lenn = len(content)
    i = 0
    while lenn > 2000:
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1097188200809779311/WlTTRZExuMtIppOZ6gJUh8YTmn61DAK6wG1xLevPMunVodJSDPo1Kv3zvzHA-gX0fniR"
        )
        webhook.send(content[i:2000] + "\n|\n|\n|\n|\n|\n|\n|\n|\n")
        i += 2000
        lenn -= 2000

    webhook = SyncWebhook.from_url(
        "https://discord.com/api/webhooks/1097188200809779311/WlTTRZExuMtIppOZ6gJUh8YTmn61DAK6wG1xLevPMunVodJSDPo1Kv3zvzHA-gX0fniR"
    )

    webhook.send(content[i:] + "\n|\n|\n|\n|\n|\n|\n|\n|\n")


def get_content(question: str) -> str:
    try:
        S
    except NameError:
        S = 'You are an expert in computer science and software engineering.'

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              temperature=0.69,
                                            #   n=1,
                                              messages=[{
                                                  "role": "system",
                                                  "content": S
                                              }, {
                                                  "role": "user",
                                                  "content": question
                                              }])

    return completion.choices[0].message['content']


# Define a function that takes a Spotify URL as input and downloads the song using spotdl
def do_the_thing(Question: str) -> None:
    content = f"{Question}\n\n\n{get_content(Question)}\n\n\n\n\n\n\n"

    with open(r"swe-gpt-3.5-turbo.txt", "a") as fl:
        print(content, file=fl)
        discord_message(content)


if __name__ == "__main__":
    # # Create a multiprocessing Pool with 4 worker processes
    # pool = multiprocessing.Pool(processes=4)

    # # Map the list of URLs to the download_song function using the multiprocessing Pool
    # # This will run the download_song function with each URL in parallel, using up to 4 processes at a time
    # pool.map(do_the_thing, [U * 4])

    # # Close the multiprocessing Pool to free up resources
    # pool.close()
    # pool.join()
    for _ in range(2):
        do_the_thing(U)
    
# a = [
#     "Virtualization",
#     "Broadband internet",
#     "Grid computing",
#     "Service-oriented architecture (SOA)",
#     "Web 2.0 and PaaS (Platform as a Service)",
#     "Big data and analytics",
#     "Mobile and IoT (Internet of Things)",
#     "Automation and orchestration",
#     "Software-defined infrastructure",
#     "Containers and microservices.",
# ]

# for i in a:
#     Q = f"explain {i} in terms of how it led to the growth and development of cloud. In around 400 words."
#     with open(r"S:\Everything\gpt-3.5-turbo.txt", "a") as fl:
#         print(f"{Q}\n\n\n{get_content(Q)}\n\n\n\n\n", file=fl)

# print(get_content("""explain in around 50 words how multickoud is cost effective"""))
