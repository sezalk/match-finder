import streamlit as st
from difflib import get_close_matches

def find_closest_match(user_input, items):
    closest_match = get_close_matches(user_input, items)
    if closest_match:
        return closest_match[0]
    else:
        return None

def main():
    st.title("Closest Match Finder")
    items = ["US", "UK", "Canada", "Germany", "France", "Italy", "Spain", "China", "Japan", "India", "Australia"]
    user_input = st.text_input("Type an item:")
    if user_input:
        closest_item = find_closest_match(user_input, items)
        if closest_item:
            st.success(f"Closest match: {closest_item}")
        else:
            st.warning("No match found")

if __name__ == "__main__":
    main()
