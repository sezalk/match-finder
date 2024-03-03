# Closest Match Finder App

This is a simple Streamlit web application that allows users to find the closest match to a given input from a predefined array of items. The app uses the `difflib` library to find the closest match based on the user's input.

## Getting Started

To run this Streamlit app on your local machine, follow these steps:

1. **Install Python**: Make sure you have Python installed on your computer. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open a terminal or command prompt and install the required libraries using pip:

   ```bash
   pip install streamlit
   ```

3. **Run the Application**: Open a terminal or command prompt, navigate to the directory where you saved `closest_match_app.py`, and run the following command:

   ```bash
   streamlit run closest_match_app.py
   ```

4. **Access the App**: After running the command, Streamlit will start a local server, and it will provide a URL (usually starting with `http://localhost`). Open a web browser and go to that URL to access the Closest Match Finder app.

## Usage

Once you access the app in your web browser, follow these steps:

1. **Type an Item**: Type an item in the text box provided.

2. **Find Closest Match**: The app will find the closest match from the predefined array of items based on the input provided.

3. **View Closest Match**: The closest match will be displayed on the screen.
