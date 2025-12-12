import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #reprezentare date prin grafice foarte interesante
from wordcloud import WordCloud

#luam un dataframe ce contine tot ce e in combined.csv
df = pd.read_csv("combined_data/combined.csv")


#plt graph pentru class distribution (human vs ai)
def class_distribution():
    plt.figure(figsize = (9, 6))
    labels = ["Human", "AI"]
    new_palette = ["Cyan", "Purple"]
    sns.countplot(x = "label", data = df, palette = new_palette)
    plt.title("Class Distribution")
    plt.ylabel("Number of paragraphs")
    plt.xlabel("Class")
    plt.savefig("eda_images/class_distribution.png")
    plt.show()

#plt graph pentru style distribution (informative, news, reviews)
def style_distribution():
    plt.figure(figsize = (9, 6))
    new_palette = ["Cyan", "Purple"]
    sns.countplot(x = "style", data = df, hue = "label", palette = new_palette)
    plt.title("Styles Distribution")
    plt.xlabel("Style")
    plt.ylabel("Number of paragraphs")
    plt.savefig("eda_images/style_distribution.png")
    plt.show()

#plt graph pentru lungimea paragrafelor
def length_distribution():
    df["word_count"] = df["text"].apply(lambda x: len(str(x).split()))
    plt.figure(figsize = (9, 6))
    #histograme, una pentru AI, alta pentru Human
    plt.hist(df[df["label"] == "human"]["word_count"], bins = 30, alpha = 0.3, label = "Human", color = "Cyan")
    plt.hist(df[df["label"] == "ai"]["word_count"], bins = 30, alpha = 0.3, label = "AI", color = "Purple")
    plt.title("Paragraph Length Distribution")
    plt.xlabel("Word Count")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("eda_images/word_count_distribution.png")
    plt.show()


#wordclouds
#doua df-uri mai mici, unu pentru toate textele human, altul pentru toate textele ai
df_human = " ".join(df[df["label"] == "human"]["text"])
df_ai = " ".join(df[df["label"] == "ai"]["text"])

def wordcloud_distribution(df_type, title):
    wordcloud = WordCloud(width = 800, height = 400, background_color = "black").generate(df_type)
    plt.figure(figsize = (9, 6))
    plt.imshow(wordcloud)
    plt.title(f"Wordcloud for {title} generated text")
    plt.savefig(f"eda_images/wordcloud_{title}.png")
    plt.show()


def main():
    print("Total number of paragraphs:", len(df))
    print("Number of paragraphs per label:")
    print(df["label"].value_counts())   
    
    
    class_distribution()
    style_distribution()
    length_distribution()

    wordcloud_distribution(df_human, "Human")
    wordcloud_distribution(df_ai, "AI")
    
if __name__ == "__main__":
    main()
