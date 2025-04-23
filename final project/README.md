# Currency Converter

## Video URL
[https://youtu.be/rq31jycV1Sc](https://youtu.be/rq31jycV1Sc)

## Description

Currency Converter is a Python-based application that enables users to convert monetary amounts between different international currencies in real time. It utilizes the [Frankfurter.app](https://www.frankfurter.app) API to fetch the latest official exchange rates directly from the European Central Bank.

The core functionality is implemented with a clean and modular structure that follows best programming practices. The application consists of a `main()` function for user interaction and at least three additional utility functions responsible for fetching exchange rates, validating user input, and performing the conversion calculation. Each of these functions is covered by unit tests written with `pytest`, ensuring correctness and robustness of the logic.


This project meets all the final project requirements for CS50P:
- Implemented entirely in Python with a command-line interface.
- Organized with a `main()` function inside `project.py` and additional non-nested custom functions at the same level.
- Fully tested with `pytest` via a separate `test_project.py` file.
- Real-time data integration via external HTTP requests using the `requests` library.
- Dependency list managed through a `requirements.txt` file.
- Code is readable, maintainable, and well-documented with comments and structured flow.

The user experience is simple and intuitive: the user is prompted to enter a base currency code (e.g., EUR), a target currency code (e.g., USD), and the amount to be converted. The result is printed out showing the final converted value after applying the exchange rate and fee.

This tool can be useful for educational purposes, quick manual currency conversions, or as a base for more advanced financial applications involving currency data.

