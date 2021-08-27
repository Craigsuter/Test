import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordpy-replit-heroku",
    version="0.4.0",
    author="cool story bob",
    description="Hosting a bot on Discord.py",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[
        "discord.py",
        "flask",
        "python-dotenv",
        "PyNaCl",
        "dnspython",
    ],
    python_requires='>=3.6',
)
