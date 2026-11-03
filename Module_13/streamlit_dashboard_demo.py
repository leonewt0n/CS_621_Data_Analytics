# Disclaimer: this example was modified from Chatgpt's suggestions.
import streamlit as st
import nltk
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")

# For NLTK 3.8.2+
try:
    nltk.download("averaged_perceptron_tagger_eng")
except:
    pass

st.set_page_config(page_title="Text Analysis Dashboard", layout="wide")

st.title("Text Analysis Dashboard")
st.write("Enter a piece of text or upload a text file to generate a word cloud, word frequency chart, and parts-of-speech distribution.")

# 1. Keep the input widgets assigned to distinct variables
text_input = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Type or paste your text here..."
)

file_input = st.file_uploader(label="Or upload a text file (.txt)")

# Initialize an empty string for processing
text = ""

# 2. Determine which source to extract text from
if file_input is not None:
    # Read and decode raw bytes from the uploaded file into a string
    text = file_input.getvalue().decode("utf-8")
elif text_input:
    text = text_input

if st.button("Generate Analysis"):

    # 3. Check if the consolidated text string is completely empty
    if not text.strip():
        st.warning("Please enter some text or upload a valid text file.")
    else:
        # Tokenize text
        tokens = word_tokenize(text.lower())
	
	# Keep alphabetic words only
        words = [word for word in tokens if word.isalpha()]
	
	# ----------------------------------
	# For bar chart (includes stop words)
	# ----------------------------------
        all_word_freq = Counter(words)
	
	# ----------------------------------
	# For word cloud and POS analysis
	# ----------------------------------
        stop_words = set(stopwords.words("english"))
        filtered_words = [word for word in words if word not in stop_words]
	
        filtered_word_freq = Counter(filtered_words)
        
        if len(filtered_words) == 0:
            st.error("No valid words found after removing stopwords.")
        else:
            # ----------------------------------
            # Word Frequency
            # ----------------------------------
            word_freq = filtered_word_freq

            # ----------------------------------
            # POS Tagging
            # ----------------------------------
            tagged_words = nltk.pos_tag(filtered_words)

            noun_count = 0
            adjective_count = 0
            adverb_count = 0

            for word, tag in tagged_words:
                if tag.startswith("NN"):      # Nouns
                    noun_count += 1
                elif tag.startswith("JJ"):    # Adjectives
                    adjective_count += 1
                elif tag.startswith("RB"):    # Adverbs
                    adverb_count += 1

            # Display three charts
            col1, col2, col3 = st.columns(3)

            # ----------------------------------
            # Word Cloud
            # ----------------------------------
            with col1:
                st.subheader("Word Cloud")

                wc = WordCloud(
                    width=800,
                    height=400,
                    background_color="black",
                    colormap="viridis",
                    max_words=20
                ).generate_from_frequencies(word_freq)

                fig, ax = plt.subplots(figsize=(6, 5))
                ax.imshow(wc, interpolation="bilinear")
                ax.axis("off")
                st.pyplot(fig)

            # ----------------------------------
            # Top 10 Word Frequency
            # ----------------------------------
            with col2:
                st.subheader("Top 10 Most Frequent Words")

                top_words = all_word_freq.most_common(10)

                labels = [item[0] for item in top_words]
                counts = [item[1] for item in top_words]

                fig, ax = plt.subplots(figsize=(6, 5))
                ax.bar(labels, counts, color="steelblue")
                ax.set_xlabel("Words")
                ax.set_ylabel("Frequency")
                ax.set_title("Top 10 Words")
                plt.xticks(rotation=45)
                st.pyplot(fig)

            # ----------------------------------
            # Parts of Speech Pie Chart
            # ----------------------------------
            with col3:
                st.subheader("Parts of Speech")

                pos_labels = []
                pos_counts = []

                if noun_count > 0:
                    pos_labels.append("Nouns")
                    pos_counts.append(noun_count)

                if adjective_count > 0:
                    pos_labels.append("Adjectives")
                    pos_counts.append(adjective_count)

                if adverb_count > 0:
                    pos_labels.append("Adverbs")
                    pos_counts.append(adverb_count)

                fig, ax = plt.subplots(figsize=(6, 5))

                if pos_counts:
                    ax.pie(
                        pos_counts,
                        labels=pos_labels,
                        autopct="%1.1f%%",
                        startangle=90,
                        colors=["#66b3ff", "#99ff99", "#ff9999"]
                    )
                    ax.set_title("Distribution of Parts of Speech")
                    ax.axis("equal")
                    st.pyplot(fig)
                else:
                    st.info("No nouns, adjectives, or adverbs detected.")

            # ----------------------------------
            # Summary Statistics
            # ----------------------------------
            st.markdown("---")
            st.subheader("Summary Statistics")

            colA, colB, colC, colD = st.columns(4)

            colA.metric("Total Words", len(words))
            colB.metric("Unique Words", len(word_freq))
            colC.metric("Most Frequent Word", word_freq.most_common(1)[0][0])
            colD.metric("Frequency", word_freq.most_common(1)[0][1])
