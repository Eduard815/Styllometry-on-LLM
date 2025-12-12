import pandas as pd



def process_informative():
    df = pd.read_csv("data/raw/informative.csv", sep = ",", engine = "python", on_bad_lines = "skip")
    df["word_count"] = df["Text"].astype(str).str.split().str.len()

    # selectam textele cu cel putin 200 si cel mult 500 de cuvinte
    df_min = df["word_count"] >= 200
    df_max = df["word_count"] <= 500
    filtered_df = df[df_min & df_max].copy().reset_index(drop = True)

    # 100 de sample-uri random din cele filtrate
    sample = filtered_df.sample(n = 100, random_state = 42).copy().reset_index(drop = True)

    # cream doua coloane noi in sample_wiki, singurele pe care le vom folosi
    # sample["title"] = sample["Title"]
    sample["content"] = sample["Text"]

    sample[["content"]].to_csv("data/human/human_informative.csv", index = False)
    

    
    

def process_news():
    #dataframe df, adaugam coloana word_count la df-ul ce contine deja news.csv
    df = pd.read_csv("data/raw/news.csv", sep = "\t", engine = "python", on_bad_lines = "skip")
    df["word_count"] = df["content"].astype(str).str.split().str.len()

    #doar paragrafe intre 150 si 300 de cuv
    df_min = df["word_count"] >= 150
    df_max = df["word_count"] <= 300
    filtered_df = df[df_min & df_max].copy().reset_index(drop = True)

    #sample-ul ce va contine 100 de paragrafe
    sample = filtered_df.sample(n = 100, random_state = 42).copy()
    sample = sample.reset_index(drop = True)

    sample[["content"]].to_csv("data/human/human_news.csv", index = False)
    #print(f"A fost creat fisierul")
    
    
    
    
def process_reviews():
    #dataframe df, adaugam coloana word_count la df-ul ce contine deja news.csv
    df = pd.read_csv("data/raw/IMDB_dataset_320.000_reviews.csv", sep = ",", engine = "python", on_bad_lines = "skip")
    df["word_count"] = df["review"].astype(str).str.split().str.len()

    #doar paragrafe intre 100 si 200 de cuv
    df_min = df["word_count"] >= 100
    df_max = df["word_count"] <= 200
    filtered_df = df[df_min & df_max].copy().reset_index(drop = True)

    #sample-ul ce va contine 100 de paragrafe
    sample = filtered_df.sample(n = 100, random_state = 42).copy()
    sample = sample.reset_index(drop = True)
    
    sample["content"] = sample["review"]

    sample[["content"]].to_csv("data/human/human_reviews.csv", index = False)
    #print(f"A fost creat fisierul")
    
    
    
    

    
    
    
def main():
    process_informative()
    process_news()
    process_reviews()
    
if __name__ == "__main__":
    main()






"""    
def process_fiction():
    df = pd.read_csv("data/raw/fiction.csv", sep = ",", engine = "python", on_bad_lines = "skip")
    final_paragraphs = [] # cele initial 100 de paragrafe ales random din toate cartile
    
    print("Columns:", df.columns)
    print("Example text snippet:")
    print(df.iloc[0]["text"][:500])

    
    # parcurgem fiecare carte pe indexul ei
    for index, row in df.iterrows():
        book_text = row["text"] # toata cartea
        book_author = row["target"]
        raw_paragraphs = book_text.split("\n") # toate paragrafele din carte
        
        for parag in raw_paragraphs:
            aux = parag.strip().replace("\n", " ")
            word_count = len(aux.split())
            
            # paragrafele pe care le vom adauga in human_fiction.csv
            if 200 <= word_count:
                final_paragraphs.append({"text":aux})

    sample = pd.DataFrame(final_paragraphs)
    sample[["text"]].to_csv("data/human/human_fiction.csv", index = False)
"""
    