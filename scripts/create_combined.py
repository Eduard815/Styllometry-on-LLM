import pandas as pd

def load_file(path, label, style):
    df = pd.read_csv(path)
    
    ret = pd.DataFrame()
    ret["text"] = df["content"]
    ret["label"] = label
    ret["style"] = style
    
    return ret




def main():
    final = []
    final.append(load_file("data/human/human_informative.csv", "human", "informative"))
    final.append(load_file("data/human/human_news.csv", "human", "news"))
    final.append(load_file("data/human/human_reviews.csv", "human", "reviews"))
    final.append(load_file("data/ai/ai_informative.csv", "ai", "informative"))
    final.append(load_file("data/ai/ai_news.csv", "ai", "news"))
    final.append(load_file("data/ai/ai_reviews.csv", "ai", "reviews"))
    
    combined = pd.concat(final)
    combined[["text", "label", "style"]].to_csv("combined_data/combined.csv", index = False)
    
    print("Fisierul combined creat")
    

if __name__ == "__main__":
    main()