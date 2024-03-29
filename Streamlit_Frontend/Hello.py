import streamlit as st

# Customizing page configuration
st.set_page_config(
    page_title="Healthy Diet Recommender",
    page_icon="🍏",
    layout="wide",  # Setting layout to wide
    initial_sidebar_state="collapsed",  # Sidebar initially collapsed
)

# Custom CSS for hover effects
hover_css = """
    <style>
        .hover:hover {
            background-color: #238c69;
            transition: background-color 0.3s ease;
            border-radius: 10px;
        }
    </style>
"""

# Adding custom CSS to the page
st.markdown(hover_css, unsafe_allow_html=True)

# Customizing main title
st.title("Healthy Diet Recommender 🥗")

# Adding a cool banner
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 10px; border-radius: 10px;'>
        <h2 style='text-align: center; color: #4CAF50;'>Discover Nutritious and Delicious Recipes!</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Adding sidebar options
option = st.sidebar.selectbox(
    "About",
    ("Home", "Diet Recommender", "My Favorites")
)

# Home Page Content
if option == "Home":
    st.markdown(
        """
        Welcome to the Healthy Recipes Recommender! Choose the "Recipe Recommendation" option 
        from the sidebar to find personalized recipes, or explore your customized recipes under "My Favorites".
        """
    )

# Recipe Recommender Page Content
elif option == "Diet Recommender":
    st.markdown(
        """
        ## Diet Recommender
        Discover healthy recipes tailored to your preferences! 
        Let's help you make nutritious and delicious meals.
        You just have to select the Diet Recommendation section!

        """
    )
    # Placeholder for recommendation system
    # Add your recommendation system here
    
# My Favorites Page Content
elif option == "My Favorites":
    st.markdown(
        """
        ## My Favorites
        
        Explore your customized recipes in Custom Food Recommendation section!
        """
    )

