# LIST OPEN SOURCE PROJECTS

This project leverages the power of the GitHub REST API to gather a curated list of highly popular and actively maintained open-source repositories that are written in Python. By utilizing the GitHub API, the project searches for repositories based on specific criteria such as the number of stars, ensuring that only well-established and widely recognized repositories are included in the results. These repositories are then organized and stored in a text file (open-source.txt), which serves as an easily accessible reference for anyone looking to explore top Python projects.

This project not only serves as a practical tool for gathering valuable open-source resources but also acts as a hands-on demonstration of how to interact with the GitHub API in an efficient and automated manner. Through this, you can learn how to make HTTP requests, handle JSON data, and write output to files—all in Python. Additionally, the project showcases how to schedule and automate such tasks using GitHub Actions, making it an excellent starting point for anyone interested in automating data collection processes or exploring Python-based solutions for API integrations.

In essence, this project provides both practical utility and a learning opportunity, helping developers and enthusiasts stay up-to-date with the latest and greatest Python-based open-source repositories, all while showcasing how to build automated workflows with Python.

- Collects a list of repositories written in Python with more than 1 star.
- Saves the repository details, including the repository URL and owner URL, in a open-source.txt file.
- Uses GitHub Actions for automated scheduling and logging.
- Python: The main programming language used for making API calls, processing data, and interacting with files.
- GitHub API: To fetch open-source repositories.
- GitHub Actions: To automate the script execution on a scheduled basis (e.g., every Monday at 00:00).
- Logging: To log the output and results
